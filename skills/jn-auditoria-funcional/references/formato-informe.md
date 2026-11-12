# Plantilla de informe de auditoría funcional

Usa esta estructura para `AUDITORIA-FUNCIONAL.md`. Sustituye los corchetes y elimina las secciones
que no apliquen; no rellenes huecos con suposiciones.

```markdown
# Auditoría funcional — [proyecto]

## 1. Resumen ejecutivo

- Fecha: [AAAAMMDD]
- Entorno: [local/staging/producción/otro]
- Alcance: [pantallas, roles y recorridos incluidos]
- Veredicto: [FUNCIONALIDAD SUFICIENTEMENTE VERIFICADA / NO LISTA PARA DARLA POR FUNCIONAL / AUDITORÍA PARCIAL]
- Limitaciones: [acceso, entorno, datos, Playwright, especificación]

## 2. Inventario y estado

| ID | Funcionalidad/recorrido | Estado | Evidencia | Prioridad | Referencias |
|---|---|---|---|---|---|
| F-001 | [nombre] | [FUNCIONAL/SIMULADA/INCOMPLETA/NO FUNCIONAL/NO VERIFICADA] | [interfaz/código/no verificado] | [P0-P3] | [ruta, archivo, endpoint] |

## 3. Evidencia de recorridos

### F-001 — [nombre]

- Expectativa: [qué debería hacer]
- Fuente de la expectativa: [PRP, documentación, UI, requisito inferido]
- Precondiciones y datos de prueba: [sin secretos ni datos reales]
- Pasos ejecutados: [lista breve]
- Resultado observado: [hecho comprobable]
- Persistencia: [sí/no/no aplica/no verificada; cómo se comprobó]
- Efectos relacionados: [pantallas, contadores, informes, exportaciones]
- Casos de error: [vacío, inválido, red, permisos]
- Estado: [clasificación]
- Nivel de evidencia: [VERIFICADO EN INTERFAZ/VERIFICADO EN CÓDIGO/NO VERIFICADO]
- Evidencia: [captura, trace, URL, log o referencia]
- Siguiente paso: [corrección o prueba que falta]

## 4. Simulaciones y falsos positivos

| Hallazgo | Por qué parece funcional | Qué demuestra que no lo es | ¿Está documentado? |
|---|---|---|---|
| [F-xxx] | [toast, mock, dato fijo...] | [prueba concreta] | [sí/no] |

## 5. Persistencia e inconsistencias

- [qué se pierde al recargar y evidencia]
- [qué pantalla no refleja el cambio y evidencia]
- [qué datos sólo existen en memoria/localStorage/mock]

## 6. Hallazgos priorizados

| Prioridad | Hallazgo | Impacto | Reproducción | Corrección propuesta |
|---|---|---|---|---|
| P0 | [bloquea operación principal] | [impacto] | [pasos] | [acción] |

## 7. No verificado

| Funcionalidad | Motivo | Qué hace falta para verificarla |
|---|---|---|
| [nombre] | [entorno/acceso/datos/especificación] | [siguiente condición] |

## 8. Señales técnicas ejecutadas

| Comando | Resultado | Qué demuestra | Qué no demuestra |
|---|---|---|---|
| `npm run ...` | [salida] | [hecho] | [límite] |

## 9. Conclusión

[Veredicto honesto y siguiente paso. No declarar funcional lo que no tenga evidencia suficiente.]
```

## Convención de referencias

Usa referencias que permitan volver al origen: `ruta:línea`, URL y rol, endpoint/método, tabla o
captura/trace. Para una conclusión basada en código indica el archivo concreto. Para una prueba de
interfaz indica el recorrido, el dato de prueba y la evidencia. No incluyas credenciales, tokens,
cookies ni datos personales.
