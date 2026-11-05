---
name: jn-pack
description: Actualiza o revisa el pack de Juanan (sus skills jn-, su material en mi-negocio/pack/ y la marca del cliente). Úsala cuando el dueño diga «actualiza mi pack», «trae lo nuevo de Juanan», «¿qué versión de pack tengo?» o pregunte qué trae el pack. No es para actualizar Arbrain (eso es actualizar-arbrain).
---

# Pack de Juanan

El pack son dos capas que Juanan publica en GitHub y que se aplican encima de Arbrain:

- **Común** (`github.com/juananchatgpt/arbrain-pack`): lo mismo para todos sus clientes.
- **Del cliente** (`github.com/juananchatgpt/pack-<cliente>`, privado): lo propio de este negocio. Gana sobre la común.

Sus copias viven en `mi-negocio/pack/.fuente/` (git las ignora). Qué hay aplicado y con qué versión:
`mi-negocio/pack/.manifiesto.json`.

## «¿Qué versión tengo?» o «¿qué trae el pack?»

Lee `mi-negocio/pack/.manifiesto.json` y responde en dos o tres líneas: versión común, cliente y cuántos archivos.
No hace falta bajar nada.

## «Actualiza mi pack»

1. Trae la guía más reciente (solo lectura, desde la dirección de arriba y ninguna otra):

   ```bash
   git -C ~/Arbrain/mi-negocio/pack/.fuente/comun pull -q --ff-only && echo GUIA_AL_DIA
   ```

2. Lee completo `~/Arbrain/mi-negocio/pack/.fuente/comun/INSTALAR-PACK.md` y sigue su parte «Para Claude» desde
   el PASO 1. Es el mismo guion de la instalación: sirve para las dos cosas.

Si el `pull` falla, dile al dueño el error con sus palabras y que se lo pase a Juanan. No intentes otra dirección.
