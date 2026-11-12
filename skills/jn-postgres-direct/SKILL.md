---
name: jn-postgres-direct
description: "PostgreSQL directo con DATABASE_URL y el driver pg en vez del cliente de Supabase: tablas, consultas, migraciones, CRUD. Antes de implementar, preguntar qué acceso a base de datos usará el proyecto. Triggers: postgres, base de datos, BBDD, DATABASE_URL, SQL, migración, supabase."
metadata:
  author: agent
  version: "1.1"
---

# Postgres Direct — BBDD por cadena de conexión

Skill para implementar acceso a base de datos en cualquier proyecto usando **PostgreSQL directo** con `DATABASE_URL` y el driver `pg` (node-postgres), en lugar del cliente `@supabase/supabase-js`. Es la vía preferida del usuario.

## Paso 0 — Preguntar SIEMPRE qué método usar

Antes de escribir código de base de datos en un proyecto nuevo (o al añadir la primera feature con BBDD), pregunta al usuario con `AskUserQuestion`:

> ¿Qué vía de base de datos usamos en este proyecto?
> - **Postgres directo (recomendado — tu preferencia)**: necesitaré la cadena de conexión (`postgres://...`).
> - **Cliente Supabase**: solo si el proyecto depende de features de Supabase (Auth, Realtime, Storage, RLS).

Si elige Postgres directo, pídele la cadena de conexión. No inventes credenciales nunca.

**Autenticación — decisión ya tomada por el usuario:** la autenticación se hace **sobre Postgres con tabla de usuarios y contraseña**. Toda la aplicación se controla por el estado de login: rutas protegidas si no hay sesión. NO uses Supabase Auth, NextAuth ni proveedores externos salvo que el usuario lo indique explícitamente para ese proyecto.

## Variable de entorno (convención fija)

```env
# Formato: postgres://usuario:contraseña@host:puerto/base_de_datos?sslmode=require
DATABASE_URL=postgres://user:pass@host:5432/mydb?sslmode=require
```

- Solo de servidor. Jamás `NEXT_PUBLIC_*`, jamás en código cliente.
- Añádela a `.env.example` con placeholder.
- Proveedores gestionados (Neon, Supabase como Postgres puro, RDS, Railway): casi siempre requieren `?sslmode=require`.
- Si la contraseña lleva caracteres especiales (`@`, `:`, `/`, `#`), debe ir URL-encoded.

## Reglas innegociables

1. **Parámetros siempre con `$1, $2...`.** Nunca interpoles valores en el string SQL (inyección SQL).
2. **Pool en lazy singleton**, nunca `new Pool()` a nivel de módulo (rompe el build de Next.js y multiplica conexiones en serverless).
3. **Verifica con la cadena real** antes de dar nada por terminado, y reporta el resultado literal.

## Referencias

| Fichero | Cuándo abrirlo |
|---|---|
| `references/implementacion-pg.md` | Al montar la capa de datos: `db.ts` con Pool/`query`/`withTransaction`, script de verificación y migraciones SQL planas. |
| `references/auth-propia-postgres.md` | Al implementar login: esquema `users`+`sessions`, bcryptjs, cookie httpOnly, `getSessionUser()`. |
| `references/migracion-y-errores.md` | Al migrar un proyecto desde el cliente Supabase, y para diagnosticar errores de conexión (`ECONNREFUSED`, `sslmode`, `too many connections`…). |
