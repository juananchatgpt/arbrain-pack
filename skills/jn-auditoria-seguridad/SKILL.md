---
name: jn-auditoria-seguridad
description: "Audita o implementa la seguridad de un proyecto: secretos y .env, autenticación y permisos, OWASP Top 10, XSS/CSRF/SQLi, cabeceras, rate limiting, dependencias y logs; hallazgos por severidad con su arreglo. Stack ALZAT (Next.js, pg, auth propia, Zod). Triggers: seguridad, OWASP, secretos, autenticación, vulnerabilidades, npm audit, antes de desplegar revisa seguridad."
---

# Skill: Seguridad + ENV + OWASP Top 10

> **Adaptado al stack ALZAT:** Next.js 16 + Postgres directo (`pg`) + auth propia (`users`+`sessions`,
> bcryptjs, cookie httpOnly) + Zod + SMTP. Auditar dependencias con **`npm audit`** (no pnpm).
> En Next.js solo las variables con prefijo **`NEXT_PUBLIC_`** se exponen al navegador: nunca metas
> secretos ahí (equivalente al `VITE_` de proyectos Vite).

Audita la seguridad de software existente o implementa controles alineados con OWASP Top 10,
gestión de secretos y AuthN/AuthZ.

## Procedimiento

1. **Inventariar superficie de ataque:** identifica entradas de usuario, endpoints, dependencias, almacenamiento de secretos y flujos de autenticación.
2. **Auditar gestión de secretos:** busca hardcoded secrets en código e historial Git, verifica `.gitignore`, `.env.example` y validación con esquema al arranque. → `references/secretos-authn-web.md`
3. **Revisar AuthN/AuthZ:** confirma que cada endpoint valida identidad y permisos en backend; verifica códigos 401/403, almacenamiento de tokens (HttpOnly/Secure/SameSite) y expiración corta. → `references/secretos-authn-web.md`
4. **Recorrer OWASP Top 10:** para A01-A10, comprueba la presencia del riesgo y aplica/recomienda la defensa correspondiente. → `references/owasp-top10.md`
5. **Verificar web security:** escapado/sanitización XSS, tokens y SameSite contra CSRF, consultas parametrizadas, HTTPS/HSTS, CSP y cabeceras (Helmet). → `references/secretos-authn-web.md`
6. **Auditar dependencias:** ejecuta `npm audit`/Snyk y reporta/parcha vulnerabilidades.
7. **Validar logging y monitoreo:** asegura registro de eventos críticos y alertas, sin exponer contraseñas, tokens ni datos sensibles.
8. **Implementar o recomendar:** aplica los controles faltantes con código mínimo y verifica con pruebas (inyección, rate limit 429, token alterado/expirado, headers en DevTools).
9. **Reportar:** entrega hallazgos priorizados por severidad con remediación concreta. → `references/checklist-y-principios.md`

## Referencias

| Fichero | Cuándo abrirlo |
|---|---|
| `references/owasp-top10.md` | Paso 4: recorrer A01–A10 con la defensa de cada riesgo. |
| `references/secretos-authn-web.md` | Pasos 2, 3 y 5: env/secretos, AuthN vs AuthZ, XSS/CSRF/CSP/headers. |
| `references/checklist-y-principios.md` | Paso 9 y proyectos nuevos: checklist de 14 puntos + principios de diseño seguro. |
