# Secretos, AuthN/AuthZ y web security

Consúltalo en los **pasos 2, 3 y 5** de la skill.

## Manejo de variables de entorno y secretos

- Separa configuración pública (puede ir en código) de secretos privados (solo en el entorno de ejecución).
- Incluye `.env`, `.env.local`, `*.pem` y `*.key` en `.gitignore` desde el primer commit.
- Mantén un `.env.example` sin valores reales como plantilla para el equipo.
- Usa secretos diferentes por entorno (dev/staging/prod) para que las pruebas nunca toquen datos reales.
- Valida las variables con Zod al inicio (runtime + tipos), con filosofía fail-first.
- Rotación sin downtime: genera el nuevo secreto, despliega soportando ambos, verifica y luego da de baja el viejo.
- En frontend (Next.js) solo las variables con prefijo `NEXT_PUBLIC_` se exponen al navegador: nunca pongas secretos ahí.

## AuthN vs AuthZ

- AuthN (autenticación) confirma la identidad: usuario/contraseña, OAuth2/OpenID Connect, MFA, biometría. Resultado: emisión de un token.
- AuthZ (autorización) verifica permisos sobre recursos, normalmente con roles (RBAC: admin, user, guest).
- Códigos HTTP: 401 Unauthorized = falta identidad; 403 Forbidden = autenticado pero sin permisos.
- JWT = Header.Payload.Signature; el payload es legible (NO está cifrado), solo firmado para verificar integridad. El secreto de firma debe tener 64+ caracteres y vivir en variable de entorno.
- Estrategia de doble token: Access Token de vida corta (15 min) + Refresh Token de vida larga (7 días) para equilibrar seguridad y experiencia de usuario.

## Web security esencial

- XSS (stored, reflected, DOM-based): escapa el HTML; React lo hace por defecto, pero `dangerouslySetInnerHTML` lo anula. Sanitiza contenido rico con DOMPurify.
- CSRF: cookies `SameSite` (Strict/Lax) + tokens CSRF aleatorios por sesión.
- SQL Injection: consultas parametrizadas (`?` con array de parámetros) u ORM, nunca concatenación.
- HTTPS/TLS: cifrado punto a punto; fuerza el redirect de HTTP a HTTPS y usa HSTS.
- CSP (Content Security Policy): lista blanca de fuentes confiables de scripts, estilos e imágenes.
- Security headers: X-Frame-Options, X-Content-Type-Options (nosniff), Strict-Transport-Security, Referrer-Policy; Helmet los aplica todos de una vez.
- Rate limiting para frenar fuerza bruta (HTTP 429 al exceder el umbral); límites más estrictos en endpoints sensibles como login.
