# OWASP Top 10 (2021) aplicado al stack ALZAT

Consúltalo en el **paso 4** de la skill: recorrer A01–A10 comprobando si el riesgo está presente
y aplicando la defensa correspondiente.

- **A01 - Broken Access Control (Control de acceso roto):** un usuario accede a recursos o acciones que no le corresponden; valida permisos y propiedad del recurso siempre en el backend.
- **A02 - Cryptographic Failures (Fallas criptográficas):** contraseñas en texto plano, datos sin cifrar o algoritmos débiles (MD5, SHA1); usa bcrypt/Argon2 con 12+ rounds y HTTPS en todo.
- **A03 - Injection (Inyección):** SQL, NoSQL, LDAP o comandos OS; nunca concatenes input de usuario en consultas, usa consultas parametrizadas/ORM y valida con Zod.
- **A04 - Insecure Design (Diseño inseguro):** falta de modelado de amenazas; añade rate limiting, expiración de tokens y mensajes de error genéricos por diseño.
- **A05 - Security Misconfiguration (Configuración incorrecta):** credenciales por defecto, CORS abierto (`origin: '*'`), stack traces o modo debug en producción; configura restrictivo por defecto y usa Helmet.
- **A06 - Vulnerable Components (Componentes vulnerables):** dependencias desactualizadas; audita con `npm audit`, Snyk o Dependabot de forma recurrente.
- **A07 - Authentication Failures (Fallas de autenticación):** contraseñas débiles, sin MFA, session fixation, credential stuffing; exige contraseñas fuertes, sesiones cortas y bloqueo de cuenta tras intentos fallidos.
- **A08 - Software and Data Integrity Failures (Fallas de integridad):** supply chain attacks y despliegues sin firmar; verifica la integridad del software y su cadena de suministro.
- **A09 - Logging & Monitoring Failures (Fallas de logging y monitoreo):** sin registro de eventos críticos ni alertas; loguea logins (sin contraseñas) y configura alertas automáticas.
- **A10 - SSRF (Server-Side Request Forgery):** el servidor hace peticiones a URLs controladas por el atacante; valida y restringe los destinos de las peticiones salientes.
