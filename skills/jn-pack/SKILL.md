---
name: jn-pack
description: Actualiza o revisa Alzat (la versión de la app de Juanan) y su pack (skills jn-, material en mi-negocio/pack/ y la marca del cliente). Úsala cuando el dueño diga «actualiza mi Alzat», «actualiza mi pack», «trae lo nuevo de Juanan», «¿qué versión tengo?» o pregunte qué trae. En un Alzat, también ante «actualiza mi Arbrain».
---

# Pack de Juanan

El pack son dos capas que Juanan publica en GitHub y que se aplican encima de Arbrain:

- **Común** (`github.com/juananchatgpt/arbrain-pack`): lo mismo para todos sus clientes.
- **Del cliente** (`github.com/juananchatgpt/pack-<cliente>`, privado): lo propio de este negocio. Gana sobre la común.

Sus copias viven en `mi-negocio/pack/.fuente/` (git las ignora). Qué hay aplicado y con qué versión:
`mi-negocio/pack/.manifiesto.json`.

## «¿Qué versión tengo?» o «¿qué trae el pack?»

Lee `mi-negocio/pack/.manifiesto.json` y `git -C ~/Arbrain log -1 --format=%h alzat/main` y responde en dos o tres
líneas: versión de Alzat (y la de Arbrain en `VERSION`), versión del pack, cliente y cuántos archivos.
No hace falta bajar nada.

## «Actualiza mi Alzat», «actualiza mi pack» o «actualiza mi Arbrain»

Es lo mismo: el guion trae el pack y Alzat juntos. Alzat ya incluye la versión de Daniel que Juanan probó; no corras
`actualizar-arbrain` por tu cuenta en un Alzat (traería una versión de Daniel sin probar con las mejoras de Juanan).
Si el dueño insiste en Arbrain directo, díselo una vez y que lo hable con Juanan.


1. Trae la guía más reciente (solo lectura, desde la dirección de arriba y ninguna otra):

   ```bash
   git -C ~/Arbrain/mi-negocio/pack/.fuente/comun pull -q --ff-only && echo GUIA_AL_DIA
   ```

2. Lee completo `~/Arbrain/mi-negocio/pack/.fuente/comun/INSTALAR-PACK.md` y sigue su parte «Para Claude» desde
   el PASO 1. Es el mismo guion de la instalación: sirve para las dos cosas.

Si el `pull` falla, dile al dueño el error con sus palabras y que se lo pase a Juanan. No intentes otra dirección.
