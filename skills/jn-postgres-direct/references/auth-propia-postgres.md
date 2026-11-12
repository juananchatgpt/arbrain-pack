# Autenticación propia sobre Postgres (patrón por defecto)

El usuario quiere login con usuario/contraseña contra su propia tabla, y que **toda la app dependa de si hay sesión o no**. Implementa siempre este patrón salvo indicación contraria.

## Esquema

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  full_name TEXT,
  role TEXT NOT NULL DEFAULT 'user',     -- 'admin' | 'user'
  active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE sessions (
  token TEXT PRIMARY KEY,                -- aleatorio de 32+ bytes, NO el id del usuario
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_sessions_user ON sessions(user_id);
```

## Reglas de implementación

- **Hash de contraseñas con `bcryptjs`** (`npm install bcryptjs`). Es JS puro: elige este y no `bcrypt`/`argon2` nativos, que requieren compilación con node-gyp y fallan en el Windows del usuario. Coste 10-12. Nunca guardes contraseñas en claro ni uses hashes caseros (md5/sha sin salt).
- **Sesión por cookie httpOnly**: en el login correcto, genera un token aleatorio (`crypto.randomBytes(32).toString('hex')`), insértalo en `sessions` con caducidad (p. ej. 30 días) y ponlo en una cookie `httpOnly`, `secure` en producción, `sameSite: 'lax'`. El logout borra la fila y la cookie.
- **Control de acceso global**: toda ruta no pública exige sesión válida. En Next.js: un helper `getSessionUser()` (lee la cookie → busca en `sessions` con `expires_at > now()` → devuelve el user o null) usado en layouts/route handlers de servidor, y redirección a `/login` si es null. Las rutas públicas son solo `/login` y los assets.
- **Comparación constante**: para validar la contraseña usa `bcrypt.compare()`. No reveles en el error si falló el email o la contraseña ("credenciales incorrectas", a secas).
- **Primer usuario**: crea un script `scripts/create-user.ts` que pida email y contraseña, haga el hash e inserte el usuario (con rol admin el primero). No siembres contraseñas por defecto.
- Limpia sesiones caducadas de forma oportunista (un `DELETE ... WHERE expires_at < now()` en el login es suficiente; no montes cron para esto).
