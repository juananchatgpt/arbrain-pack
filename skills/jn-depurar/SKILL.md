---
name: jn-depurar
description: "Depuración sistemática con causa raíz primero, antes de proponer ningún arreglo: bug, test en rojo, error 500, pantalla en blanco, funciona en local y no en prod, fallo intermitente. Cierra guardando el aprendizaje en memoria. Triggers: bug, no funciona, falla, error, flaky, llevo 3 intentos, depurar, causa raíz."
---

# Skill: Depuración sistemática (causa raíz primero)

> **Adaptado al stack ALZAT:** Next.js 16 + React 19, **Postgres directo** (`pg`,
> `DATABASE_URL`), deploy **GitHub→VPS Easypanel** (Node corre en **UTC**, ojo a
> fechas), ficheros con **CRLF**, un Postgres por proyecto. Antes de considerar
> nada resuelto: `npm run build`/`typecheck` en verde. Muchos bugs ya vividos
> están en la memoria del BOS → sección **"Gotchas técnicos"** de `MEMORY.md`;
> míralos antes de trazar desde cero.

**Regla que no se rompe: NINGÚN fix sin causa raíz.** Un arreglo del síntoma no es
un arreglo, es un fallo aplazado. Ver el síntoma ≠ entender la causa.

## Procedimiento

1. **Fase 1 — Causa raíz (antes de tocar nada).**
   - Lee el error **entero** (stack trace incluido), no la primera línea.
   - **Reprodúcelo de forma fiable**: pasos exactos, mismo entorno. Si es "a veces", es una condición de carrera o un dato sucio, no magia.
   - Revisa los **cambios recientes** (`git log --oneline -20`, `git diff`): ¿qué se movió?
   - **Instrumenta las capas** para ver *QUÉ capa* falla antes de *por qué*: loguea el dato que **entra** y el que **sale** en cada frontera (navegador → Server Action → `pg` → Postgres). En Next, ten claro si el código corre en server o cliente. Traza hacia arriba por la cadena de llamadas hasta el **origen** del dato malo, no te quedes donde revienta. Detalle → [references/metodo-4-fases.md](references/metodo-4-fases.md).

2. **Fase 2 — Comparar con lo que SÍ funciona.** Busca un caso equivalente que funcione (otra ruta, otro proyecto del BOS, un commit anterior) y compáralo **entero**. Prohibido "eso no puede importar": las diferencias pequeñas son las que importan.

3. **Fase 3 — Hipótesis y prueba.** Formula una hipótesis concreta y falsable ("falla porque X"). Cambia **una variable cada vez**, mínima, y verifica antes de seguir. Nada de "toco tres cosas y corro". Sin hipótesis clara, no toques código.

4. **Fase 4 — Arreglo.** Escribe primero un **test que falle** por la causa raíz, aplica **un** fix, y verifica que pasa (y que no rompe el resto ni el build). Un fix sin test no se sostiene.

5. **STOP a los 3 intentos.** Si llevas 3 fixes fallidos, **para**: no es un bug de línea, es la arquitectura. Cuestiona el patrón/diseño en vez de parchear una cuarta vez (Fase 4.5 en la referencia).

6. **Cierra a memoria.** Si la causa raíz no era obvia, vuelca el gotcha: al **silo del cliente** si es específico de ese proyecto, a la **global** (`Gotchas técnicos`) si es transversal (el *cómo*, nunca datos del cliente).

## Red flags (cázate pensando esto → vuelve a Fase 1)

- "Un fix rápido por ahora, ya investigo luego."
- "Pruebo a cambiar X a ver si va."
- "Meto varios cambios y corro los tests."
- "Me salto el test, lo verifico a mano."
- "Seguramente es X, lo arreglo."
- "No lo entiendo del todo pero esto quizá funciona."
- "El patrón dice X pero yo lo adapto distinto."
- Proponer soluciones antes de trazar el flujo del dato.
- "Un intento más" (cuando ya van 2+).

Tabla completa de racionalizaciones y sus contras → [references/metodo-4-fases.md](references/metodo-4-fases.md).
Bug de timing / `sleep()` / test flaky / esperar a un deploy → [references/esperar-por-condicion.md](references/esperar-por-condicion.md).

---
*Adaptado de [`obra/superpowers`](https://github.com/obra/superpowers) (skill `systematic-debugging`, licencia MIT) al método de 3 capas y al stack del BOS. Sin hooks ni auto-activación: se invoca a mano.*
