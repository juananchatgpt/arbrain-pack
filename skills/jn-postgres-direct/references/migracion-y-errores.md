# Migrar desde Supabase y catálogo de errores

## Migrar un proyecto desde el cliente Supabase

1. Localiza todos los usos: `grep -r "supabase" src/` y `createClient(`.
2. Sustituye cada `supabase.from('tabla').select/insert/update/delete` por la query SQL equivalente vía `query()`.
3. **Auth**: sustituye `supabase.auth.*` por el patrón de `references/auth-propia-postgres.md` (tabla `users` + `sessions` + cookie httpOnly).
4. **RLS ya no protege nada**: las policies de Supabase actúan en su API. Con conexión directa, toda autorización debe estar en el código del servidor. Revisa cada endpoint.
5. Elimina `@supabase/supabase-js` del package.json y las variables `NEXT_PUBLIC_SUPABASE_*` cuando ya no queden usos.
6. `npm run build` antes de dar por terminada la migración.

## Errores comunes y su causa real

- `ECONNREFUSED`: host/puerto mal, o la BBDD no acepta conexiones externas (whitelist de IPs).
- `no pg_hba.conf entry... no encryption`: falta `?sslmode=require` en la cadena.
- `password authentication failed`: credenciales mal o contraseña sin URL-encodear.
- `too many connections` (serverless/Vercel): cada lambda crea su pool. Usa el **pooler** del proveedor (PgBouncer; en Neon/Supabase es otra URL con puerto 6543) y `max: 1`.
- Build de Next.js falla con env placeholder: el Pool se está creando a nivel de módulo — usa el patrón lazy singleton de `references/implementacion-pg.md`.
- `self signed certificate in certificate chain`: añade `ssl: { rejectUnauthorized: false }` solo si el proveedor lo documenta así (común en algunos gestionados).
