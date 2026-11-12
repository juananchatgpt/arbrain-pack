---
name: jn-smtp-email
description: "Enviar correos por SMTP con nodemailer y credenciales explícitas: transaccionales, formularios de contacto, avisos, informes. Antes de implementar, preguntar qué método de correo usará el proyecto. Triggers: email, correo, enviar correo, SMTP, nodemailer, formulario de contacto."
metadata:
  author: agent
  version: "1.0"
---

# SMTP Email — Envío de correos con credenciales SMTP

Skill para implementar envío de emails en cualquier proyecto usando **SMTP directo** (host, puerto, usuario y contraseña) con `nodemailer`. Es la vía preferida del usuario.

## Paso 0 — Preguntar SIEMPRE qué método usar

Antes de escribir código de email en un proyecto nuevo (o al añadir la primera funcionalidad de email a un proyecto existente), pregunta al usuario con `AskUserQuestion`:

> ¿Qué método de envío de email usamos en este proyecto?
> - **SMTP (recomendado — tu preferencia)**: necesitarás pasarme host, puerto, usuario y contraseña.
> - **Otro proveedor por API** (Resend, SendGrid, etc.): solo si este proyecto lo requiere.

Si elige SMTP, pídele las credenciales (o dile exactamente qué variables debe rellenar en el `.env`). No inventes credenciales nunca.

## Variables de entorno (convención fija)

Usa siempre estos nombres en `.env` / `.env.local` (y en Vercel si se despliega):

```env
SMTP_HOST=smtp.tuproveedor.com
SMTP_PORT=587            # 587 = STARTTLS (lo más común) | 465 = SSL directo
SMTP_SECURE=false        # true SOLO si el puerto es 465
SMTP_USER=usuario@dominio.com
SMTP_PASS=contraseña-o-app-password
SMTP_FROM="Nombre Visible <usuario@dominio.com>"
SMTP_REPLY_TO=           # opcional
```

Reglas:
- Las credenciales SMTP son **solo de servidor**. En Next.js: route handlers (`app/api/.../route.ts`) o Server Actions. Jamás en componentes cliente ni variables `NEXT_PUBLIC_*`.
- Añade las variables también a `.env.example` con placeholders (sin valores reales).

## Implementación estándar (nodemailer)

Instala: `npm install nodemailer` (+ `npm install -D @types/nodemailer` en TypeScript).

Crea `src/lib/mailer.ts` (o `src/shared/lib/mailer.ts` según la estructura del proyecto):

```ts
import nodemailer, { Transporter } from 'nodemailer'

let transporter: Transporter | null = null

// Lazy singleton: no crear el transporter a nivel de módulo.
// Si se crea al cargar el módulo, el build de Next.js falla cuando
// las variables de entorno aún no existen (placeholders, CI, etc.).
function getTransporter(): Transporter {
  if (!transporter) {
    transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: Number(process.env.SMTP_PORT ?? 587),
      secure: process.env.SMTP_SECURE === 'true',
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
      },
    })
  }
  return transporter
}

export interface SendEmailOptions {
  to: string | string[]
  subject: string
  html: string
  text?: string          // siempre que puedas, incluye versión texto plano
  replyTo?: string
  attachments?: { filename: string; content: Buffer | string }[]
}

export async function sendEmail(options: SendEmailOptions): Promise<void> {
  await getTransporter().sendMail({
    from: process.env.SMTP_FROM,
    replyTo: options.replyTo ?? process.env.SMTP_REPLY_TO || undefined,
    ...options,
  })
}
```

## Verificación obligatoria tras configurar

Después de configurar credenciales reales, verifica la conexión ANTES de dar la feature por terminada. Crea un script temporal o ejecútalo inline:

```ts
// scripts/test-smtp.ts — npx tsx scripts/test-smtp.ts
import 'dotenv/config'
import nodemailer from 'nodemailer'

const t = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT ?? 587),
  secure: process.env.SMTP_SECURE === 'true',
  auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
})

await t.verify()                       // valida credenciales y conexión
console.log('✓ Conexión SMTP OK')

const info = await t.sendMail({        // email real de prueba al propio usuario
  from: process.env.SMTP_FROM,
  to: process.env.SMTP_USER,
  subject: 'Test SMTP — configuración correcta',
  text: 'Si lees esto, el SMTP funciona.',
})
console.log('✓ Email enviado:', info.messageId)
```

Reporta al usuario el resultado real (messageId o el error literal). Nunca digas que el email "debería funcionar" sin haber ejecutado `verify()`.

## Configuraciones típicas por proveedor

| Proveedor | Host | Puerto | Nota |
|---|---|---|---|
| Gmail / Google Workspace | smtp.gmail.com | 587 | Requiere **App Password** (no la contraseña normal; activar 2FA primero) |
| Outlook / Office 365 | smtp.office365.com | 587 | SMTP AUTH debe estar habilitado en el tenant |
| IONOS | smtp.ionos.es | 587 | |
| OVH | ssl0.ovh.net | 587 o 465 | |
| Hostinger | smtp.hostinger.com | 587 o 465 | |
| Brevo (SMTP relay) | smtp-relay.brevo.com | 587 | El SMTP_USER es el login de Brevo, la pass es la SMTP key |

## Errores comunes y su causa real

- `EAUTH 535`: credenciales mal. En Gmail casi siempre es que falta el App Password.
- `ETIMEDOUT` / `ECONNECTION`: puerto bloqueado (algunos hosting/VPN bloquean el 25 y a veces el 587 — prueba 465 con `SMTP_SECURE=true`) o host mal escrito.
- `self signed certificate`: servidor con TLS no estándar; como último recurso `tls: { rejectUnauthorized: false }` SOLO en desarrollo, nunca en producción.
- Emails que llegan a spam: no es un bug del código — el dominio necesita SPF/DKIM/DMARC. Avisa al usuario, no intentes "arreglarlo" en código.
- En serverless (Vercel): cada invocación puede crear conexión nueva; mantén el patrón singleton y usa `await` en `sendMail` (no fire-and-forget, la lambda muere antes de enviar).
