# Implementación estándar del driver `pg`

Instala: `npm install pg` (+ `npm install -D @types/pg` en TypeScript).

Crea `src/lib/db.ts` (o `src/shared/lib/db.ts` según la estructura del proyecto):

```ts
import { Pool, QueryResultRow } from 'pg'

let pool: Pool | null = null

// Lazy singleton: nunca crear el Pool a nivel de módulo con new Pool()
// directamente exportado — rompe el build de Next.js cuando DATABASE_URL
// aún no existe, y en serverless multiplica conexiones.
function getPool(): Pool {
  if (!pool) {
    pool = new Pool({
      connectionString: process.env.DATABASE_URL,
      max: 10,                      // baja a 1-3 en serverless sin pooler externo
      idleTimeoutMillis: 30_000,
      connectionTimeoutMillis: 10_000,
    })
  }
  return pool
}

// Query parametrizada — ÚNICA forma permitida de pasar valores
export async function query<T extends QueryResultRow>(
  sql: string,
  params: unknown[] = []
): Promise<T[]> {
  const { rows } = await getPool().query<T>(sql, params)
  return rows
}

// Transacciones
export async function withTransaction<T>(
  fn: (q: typeof query) => Promise<T>
): Promise<T> {
  const client = await getPool().connect()
  try {
    await client.query('BEGIN')
    const txQuery = async <R extends QueryResultRow>(sql: string, params: unknown[] = []) =>
      (await client.query<R>(sql, params)).rows
    const result = await fn(txQuery as typeof query)
    await client.query('COMMIT')
    return result
  } catch (e) {
    await client.query('ROLLBACK')
    throw e
  } finally {
    client.release()
  }
}
```

Uso en servicios:

```ts
const users = await query<User>('SELECT * FROM users WHERE email = $1', [email])
await query('INSERT INTO tasks (title, status) VALUES ($1, $2)', [title, 'inbox'])
```

**Regla innegociable:** parámetros siempre con `$1, $2...`. Nunca interpoles valores en el string SQL (inyección SQL).

## Verificación obligatoria tras configurar

Con la cadena real configurada, verifica ANTES de dar nada por terminado:

```ts
// scripts/test-db.ts — npx tsx scripts/test-db.ts
import 'dotenv/config'
import { Pool } from 'pg'

const pool = new Pool({ connectionString: process.env.DATABASE_URL })
const { rows } = await pool.query('SELECT now() AS server_time, current_database() AS db')
console.log('✓ Conexión OK:', rows[0])
await pool.end()
```

Reporta el resultado real al usuario (hora del servidor y nombre de la BBDD, o el error literal).

## Migraciones (sin ORM, SQL plano)

Mantén las migraciones como archivos SQL numerados en `db/migrations/`:

```
db/migrations/001_initial_schema.sql
db/migrations/002_add_invoices.sql
```

Aplícalas con un script simple que registre las ya ejecutadas en una tabla `_migrations` (créalo en `scripts/migrate.ts` la primera vez que el proyecto lo necesite). Si el usuario prefiere un ORM (Drizzle, Prisma), pregúntaselo antes de introducirlo — por defecto, SQL plano.
