# arbrain-pack

Pack de Juanan para [Arbrain](https://github.com/arbrain-ai/arbrain): skills, material de trabajo y marca que se
aplican encima del Arbrain oficial de cada cliente, sin tocar el núcleo ni lo que el cliente crea.

- **Este repo** es la capa común: llega a todos los clientes.
- **`pack-<cliente>`** (uno por cliente, privado) es la capa de cada cliente. Gana sobre la común.
- Arbrain se sigue actualizando solo desde el autor, con su firma. El pack se actualiza con «actualiza mi pack».

Guion de instalación (para Claude): [`INSTALAR-PACK.md`](INSTALAR-PACK.md).

**Alzat (desde la 0.3.0).** El guion también trae **Alzat**, la versión de la app de Juanan (Arbrain de Daniel Carreón
con sus mejoras, su nombre y su logo), desde el repo privado `juananchatgpt/alzat-arbrain`, y la mezcla en la rama
`mi-arbrain` del cliente con una rama de respaldo antes. Cada cliente necesita acceso de lectura a ese repo
(Settings › Collaborators). Para actualizar todo, el cliente dice «actualiza mi Alzat».

## Qué hay aquí y adónde va

| En el repo | En el Arbrain del cliente | Notas |
|---|---|---|
| `skills/jn-*/` | `.claude/skills/jn-*/` | Toda skill empieza por `jn-` (el `prefijo` de `pack.json`). Las demás se ignoran. |
| `negocio/` | `mi-negocio/pack/` | Metodología, plantillas, material de consulta. |
| `marca/` | `mi-marca/` | `tema.css`, `logo.png` o `logo.svg`, `marca.json`. Opcional. |
| `MEMORIA.md` | bloque marcado en `.claude/memory/MEMORY.md` | Lo esencial que Levy debe saber siempre. Corto: se carga en cada conversación. |
| `pack.json` | — | Nombre, prefijo y versión. |
| `plantilla-cliente/` | — | Punto de partida para cada `pack-<cliente>` (no se aplica). |

¿Por qué `MEMORY.md` y no `CLAUDE.local.md`? Porque el chat de la app Arbrain no lee `CLAUDE.local.md`; `MEMORY.md` se
carga en la app y en Claude Code. ¿Y por qué no `.claude/knowledge/`? Porque Arbrain lo regenera solo.

## Reglas del pack

1. **Nunca pisa lo del cliente.** Cada archivo que escribe queda anotado con su huella en
   `mi-negocio/pack/.manifiesto.json`. Si el cliente lo cambia, el pack lo respeta en las siguientes
   actualizaciones (`PACK_RESPETA`).
2. **Gana el cliente sobre lo común.** Mismo archivo en las dos capas → se queda el de `pack-<cliente>`.
3. **Nada se borra.** Lo que quitas del pack se mueve en su máquina a `~/Arbrain-respaldos/pack-<fecha>/`.
4. **No toca su memoria, su plan, su diario ni sus skills propias.** Solo el bloque marcado de `MEMORY.md`.
5. **Cada aplicación es un commit** en la rama `mi-arbrain` del cliente, solo con los archivos del pack.

## Dar de alta un cliente

1. En GitHub crea un repo **privado** `pack-<cliente>` (minúsculas y guiones, por ejemplo `pack-acme`).
2. Copia dentro el contenido de `plantilla-cliente/` y rellénalo (`MEMORIA.md`, `negocio/empresa.md`, `marca/`).
3. En ese repo, Settings › Collaborators › invita la cuenta de GitHub del cliente con permiso **Read**.
4. Pásale el prompt de la parte «Para la persona» de `INSTALAR-PACK.md` con `Cliente: acme`.

Si un cliente no necesita nada propio, no crees su repo: el prompt sin línea `Cliente:` instala solo la capa común.

## Publicar una mejora

1. Cambia lo que quieras aquí (o en un `pack-<cliente>`).
2. En `pack.json`, sube `version` si cambiaste la capa común.
3. Sube los cambios a GitHub (`git push`). Nunca reescribas la historia (`push --force`): los clientes actualizan con
   `pull --ff-only` y dejaría de funcionarles.
4. Los clientes lo reciben cuando dicen «actualiza mi pack».

Prueba los cambios en tu propio Arbrain antes de publicarlos: lo que subes aquí les llega a todos.

## Qué no poner nunca

- Llaves, contraseñas o tokens. El repo común es visible para todos tus clientes (y para cualquiera si es público).
- Datos de un cliente en la capa común ni en el repo de otro cliente.
- Archivos del autor de Arbrain modificados: el pack extiende, no edita. Si algo exige cambiar el código de
  Arbrain, ya no es un pack (ver `docs/PERSONALIZAR.md` de Arbrain).
