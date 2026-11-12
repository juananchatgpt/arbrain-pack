# Checklist de auditoría y principios de construcción

Consúltalo en el **paso 9** (reportar) y al construir un proyecto desde cero.

## Checklist de auditoría

- [ ] ¿Hay secretos hardcodeados en el código o el historial de Git? (revisar también claves filtradas en repos públicos).
- [ ] ¿Están `.env`, `.env.local`, `*.pem` y `*.key` en `.gitignore` y nunca commiteados?
- [ ] ¿Se validan las variables de entorno al arranque y la app falla si falta alguna?
- [ ] ¿El backend valida autenticación Y autorización en cada endpoint sensible (no solo el frontend)?
- [ ] ¿Las contraseñas se almacenan hasheadas (bcrypt/Argon2) y nunca en texto plano?
- [ ] ¿Toda la comunicación usa HTTPS/TLS con redirect forzado y HSTS activo?
- [ ] ¿Las consultas a base de datos están parametrizadas o usan ORM (sin concatenación de input)?
- [ ] ¿El input de usuario se sanitiza/escapa antes de renderizarse (protección XSS)?
- [ ] ¿Las cookies de sesión/token usan HttpOnly, Secure y SameSite? ¿Los tokens tienen expiración corta?
- [ ] ¿Existe rate limiting en endpoints sensibles (login, reseteo de password)?
- [ ] ¿Están configuradas las cabeceras de seguridad (Helmet/CSP/X-Frame-Options/nosniff)?
- [ ] ¿CORS está restringido a dominios concretos y no a `origin: '*'`?
- [ ] ¿Los mensajes de error son genéricos en producción (sin stack traces ni "user not found")?
- [ ] ¿Se loguean los eventos críticos (logins fallidos, cambios de permisos) sin exponer secretos, y hay alertas? ¿`npm audit` está limpio?

## Principios al construir desde cero

- Asume que el entorno es hostil: diseña con modelado de amenazas desde la concepción del producto.
- Defensa en profundidad: nunca dependas de una sola barrera; superpón capas redundantes.
- Mínimo privilegio: otorga a cada usuario, servicio y conexión solo lo estrictamente necesario (ej. DB de solo lectura cuando no se escribe).
- Fail securely y fail-fast: ante un error o config inválida, la app debe denegar acceso y/o no arrancar, nunca degradar a un estado inseguro.
- Separa configuración pública, configuración por entorno y secretos desde el primer día (12-Factor App).
- Valida y sanitiza todo input en el borde del sistema, con esquemas estrictos (Zod) y parametrización.
- Cifra por defecto: HTTPS en todo, hashing fuerte de contraseñas y cifrado de datos sensibles en reposo.
- Diseña la gestión del ciclo de vida de tokens y secretos (expiración corta, refresh, rotación sin downtime, blacklist en logout).
- Construye observabilidad de seguridad desde el inicio: logging de eventos críticos + alertas, sin filtrar datos sensibles.
