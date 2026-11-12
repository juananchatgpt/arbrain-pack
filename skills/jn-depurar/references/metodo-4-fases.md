# Método de 4 fases — detalle

Fundamento: **encuentra SIEMPRE la causa raíz antes de intentar un arreglo. Un fix
del síntoma es un fallo.** Violar la letra de la regla es violar el espíritu: si te
descubres justificando por qué *esta vez* no hace falta el proceso, esa
justificación es exactamente el síntoma que debe hacerte parar.

## Fase 1 — Investigación de la causa raíz

Objetivo: entender **qué** falla y **en qué capa** antes de tocar el **por qué**.

1. **Lee el mensaje completo.** Stack trace entero. La línea que importa rara vez es la primera.
2. **Reproduce de forma consistente.** Pasos exactos + mismo entorno. Un fallo intermitente es una señal (carrera, dato sucio, caché, zona horaria), no ruido.
3. **Revisa lo que cambió.** `git log --oneline -20`, `git diff`. La causa suele estar en el último movimiento.
4. **Instrumenta las fronteras** (multi-capa). Loguea el dato que ENTRA y el que SALE en cada límite para aislar la capa culpable:
   - navegador → Server Action / route handler
   - Server Action → capa de datos (`pg`)
   - `pg` → Postgres (mira la query y los parámetros **reales**, no los que crees)

   En Next.js 16, ten claro si el código corre en server o cliente (un `console.log` puede acabar en sitios distintos).

### Trazado a la causa raíz (root-cause tracing)

No arregles donde revienta; **traza hacia arriba** por la cadena de llamadas hasta el origen del dato malo.

1. Observa el síntoma (dónde peta).
2. Localiza la causa inmediata (la línea exacta).
3. Pregunta "¿quién llamó a esto?" y sube nivel a nivel, mirando **qué valor** se pasó en cada salto.
4. Sigue subiendo hasta el **disparador original** (p. ej. un path vacío, una fecha rota por `toISOString()`, un env con nombre distinto, un `LIMIT 1` sin `ORDER BY`).
5. Arregla **en el origen** y añade validación en los puntos intermedios para que no vuelva.

Cuando el trazado manual no llega, instrumenta con el stack:

```ts
function algo(dir: string) {
  console.error('DEBUG algo:', { dir, cwd: process.cwd(), stack: new Error().stack });
  // ...
}
```

y filtra la salida (`... 2>&1 | grep 'DEBUG algo'`). Si un test "contamina" a otros, aíslalo por bisección: corre los tests en secuencia hasta dar con el culpable.

## Fase 2 — Análisis de patrón

- Encuentra un ejemplo que **sí** funciona (otra ruta, otro proyecto del BOS, un commit anterior).
- Compáralo **completo** con el roto. Prohibido "eso no puede importar".
- Entiende dependencias y orden (¿se ejecuta antes de que exista el dato?).

## Fase 3 — Hipótesis y prueba

- Escribe la hipótesis en una frase falsable: "Falla porque X".
- Prueba con el **cambio mínimo** y **una variable cada vez**.
- Verifica el resultado **antes** de seguir. Guess-and-check está prohibido.

## Fase 4 — Implementación

1. Escribe un **test que falle** reproduciendo la causa raíz.
2. Aplica **un solo** fix.
3. Verifica: el test pasa, el resto sigue verde, `npm run build`/`typecheck` en verde.

## Fase 4.5 — Si llevas 3+ fixes fallidos: PARA

3 intentos fallidos = problema de arquitectura, no de línea. Deja de parchear:

- Nombra en voz alta el supuesto de diseño que puede estar mal.
- Cuestiona el patrón entero antes de un 4º intento.
- Si cada fix mueve el fallo a otro sitio, el diseño **es** el bug.

## Tabla de racionalizaciones (excusa → realidad)

| Te dices… | Realidad |
|---|---|
| "Es simple, no necesito proceso." | Los bugs simples también tienen causa raíz. El proceso es rápido con ellos. |
| "Es una emergencia, no hay tiempo." | La depuración sistemática es MÁS rápida que el thrashing de prueba y error. |
| "Pruebo esto primero y luego investigo." | El primer fix marca el patrón. Hazlo bien desde el principio. |
| "Escribo el test después de confirmar el fix." | Los fixes sin test no se sostienen. El test primero prueba que es la causa. |
| "Varios fixes a la vez ahorran tiempo." | No puedes aislar qué funcionó y creas bugs nuevos. |
| "La referencia es larga, adapto el patrón." | Entender a medias garantiza bugs. Léela entera. |
| "Veo el problema, lo arreglo." | Ver el síntoma ≠ entender la causa raíz. |
| "Un intento más" (tras 2+ fallos). | 3+ fallos = problema de arquitectura. Cuestiona el patrón, no lo parchees otra vez. |

## Red flags (lista completa)

- "Un fix rápido por ahora, ya investigo luego."
- "Pruebo a cambiar X a ver si va."
- "Meto varios cambios y corro los tests."
- "Me salto el test, lo verifico a mano."
- "Seguramente es X, lo arreglo."
- "No lo entiendo del todo pero esto quizá funciona."
- "El patrón dice X pero yo lo adapto distinto."
- "Aquí están los problemas: [lista fixes sin haber investigado]."
- Proponer soluciones antes de trazar el flujo del dato.
- "Un intento más" (cuando ya van 2+).
- Cada fix descubre un problema nuevo en otro sitio.
