# Esperar por una condición, no por el reloj

Aplica a: tests flaky, bugs intermitentes ("a veces falla"), esperar a que un
proceso async termine, esperar a que un deploy/endpoint responda, colas, crons.

## Por qué `sleep(n)` está mal

`await new Promise(r => setTimeout(r, 50))` es una **suposición**: asumes que la
operación acaba en 50 ms. Pasa en tu máquina y falla en CI o bajo carga. Eso ES la
condición de carrera, no su solución. (Encaja con el gotcha del BOS de Node en
Docker/UTC y con los crons: nunca dependas del reloj para coordinar.)

### Anti-patrones

- **Adivinar el timing:** dormir X ms y dar por hecho que ya está.
- **Sin timeout:** un `while` que sondea sin límite se cuelga para siempre si la condición nunca llega.
- **Dato rancio:** cachear el estado ANTES del bucle y comprobar la foto vieja en vez del valor actual.

## Patrón correcto: sondea la condición real

```ts
async function waitFor<T>(
  condition: () => T | false | undefined | null,
  description: string,
  timeoutMs = 5000,
): Promise<T> {
  const start = Date.now();
  while (true) {
    const result = condition();                 // reevalúa cada vuelta (no dato rancio)
    if (result) return result;
    if (Date.now() - start > timeoutMs) {        // timeout obligatorio
      throw new Error(`Timeout esperando: ${description}`);
    }
    await new Promise((r) => setTimeout(r, 10)); // sondea cada 10 ms, no cada 1 ms
  }
}
```

Uso:

- `await waitFor(() => estado === 'listo', 'estado listo')`
- `await waitFor(() => filas.length >= 5, '5 filas insertadas')`
- `await waitFor(async () => (await fetch(url)).ok, 'endpoint arriba', 30000)`

Compruebas el **comportamiento real**, no el reloj: la condición se reevalúa en cada
vuelta, el timeout evita el cuelgue, y sondear cada 10 ms responde rápido sin quemar CPU.

---
*Adaptado de `obra/superpowers` (`systematic-debugging/condition-based-waiting.md`, MIT).*
