---
name: jn-auditoria-funcional
description: "Audita si las funciones de una app funcionan de verdad para el usuario (botones, formularios, CRUD, persistencia, filtros, integraciones): detecta mocks, éxitos falsos y datos que desaparecen, con Playwright y el código; informe con evidencia y prioridades. NO: implementar, seguridad (jn-auditoria-seguridad) ni estrategia de tests (jn-auditoria-testing)."
metadata:
  author: agent
  version: "1.0"
---

# Auditoría funcional real

Determina qué puede hacer realmente un usuario y qué sólo aparenta funcionar. El resultado es un
diagnóstico reproducible, no una revisión superficial del código ni una promesa de que la aplicación
está terminada.

## Límite de la skill

- Audita; no implementa correcciones, no edita tests para ocultar fallos y no cambia configuración,
  esquema, datos de aplicación ni código del proyecto auditado.
- Puede crear el informe y las evidencias de la auditoría en `QA/` de la raíz del BOS. No dejes
  capturas, logs ni temporales en la raíz ni dentro del proyecto si no es necesario.
- No audites producción con operaciones de escritura ni uses datos reales. En producción sólo observa
  de forma no destructiva si el usuario lo ha autorizado; marca los flujos de escritura como no
  verificados.
- Si la expectativa de una funcionalidad no está documentada, distingue el requisito inferido de un
  error demostrado. No presentes una suposición como hecho.
- No confundas una funcionalidad deliberadamente simulada de una demo con un error. Sí es un hallazgo
  si se presenta como funcionalidad real sin estar indicado.

## Antes de tocar un proyecto

1. Identifica proyecto, cliente, entorno (local, staging o producción), URL, comando de arranque,
   cuenta de prueba, rol y alcance autorizado.
2. Abre lo que tu memoria tenga de ese cliente o proyecto (en `.claude/memory/`, si existe). Lee también su `CLAUDE.md` o `AGENTS.md` si existe. No mezcles
   datos, credenciales, decisiones ni evidencias entre clientes.
3. Comprueba que el entorno no sea producción o, si lo es, que el plan sea sólo lectura. Si no existe
   un entorno seguro para probar escrituras, no inventes una prueba: marca el flujo como `NO VERIFICADA`
   y explica el bloqueo.
4. Define el alcance. Empieza por los recorridos críticos del producto, normalmente entre 3 y 8, en
   vez de pulsar botones sin criterio. Si el usuario pide una auditoría completa, amplía después del
   primer inventario.

## Método

### 1. Reconocimiento

Inventa primero un mapa, no conclusiones. Localiza:

- pantallas, rutas, roles y navegación;
- formularios, botones, menús, filtros, búsquedas y estados vacíos;
- operaciones de creación, lectura, edición, eliminación e importación/exportación;
- endpoints, server actions, servicios, tablas, ficheros o almacenamiento que deberían persistir datos;
- integraciones externas, webhooks, correo, pagos y tareas asíncronas;
- mocks, fixtures, datos hardcodeados, `setTimeout`, respuestas de demo y feature flags;
- tests existentes y scripts disponibles para ejecutar la aplicación.

Para cada elemento registra qué debería hacer, de dónde sale esa expectativa y si está confirmada o
inferida. En esta fase se puede inspeccionar código, pero el código por sí solo no demuestra que el
recorrido funcione.

### 2. Selección de recorridos críticos

Escribe los recorridos como acciones observables, por ejemplo:

```text
Crear registro → verlo en el listado → recargar → editarlo → comprobar una pantalla relacionada → eliminarlo
```

Incluye, cuando aplique:

- estado inicial y datos de prueba aislados;
- permisos y rol del usuario;
- resultado visible esperado;
- persistencia después de recargar o volver a entrar;
- efecto en otras pantallas, contadores, informes o exportaciones;
- datos vacíos, duplicados, inválidos o incompletos;
- fallo de red, respuesta no válida, timeout y recuperación;
- navegación atrás/adelante y acceso directo a la ruta;
- declaración de que el interlocutor es una IA si hay chatbot, y etiquetado si hay contenido sintético;
- confirmación y control de borrados o acciones irreversibles.

No marques como funcional un recorrido sólo porque termina en un toast, un modal cerrado o un HTTP
200. Comprueba el efecto que el usuario esperaba.

### 3. Verificación en código

Traza cada recorrido desde la interacción hasta el almacenamiento o integración:

```text
control UI → handler/server action → API/servicio → persistencia o proveedor externo → respuesta UI
```

Busca rutas muertas, handlers vacíos, `TODO`, mocks, valores fijos, respuestas siempre exitosas,
errores tragados y diferencias entre el tipo declarado y el dato guardado. Esta inspección sólo da
evidencia `VERIFICADO EN CÓDIGO`; no eleva por sí sola la clasificación a `FUNCIONAL`.

Si es seguro y relevante, ejecuta `npm run typecheck`, `npm run build` o el script existente de
tests como señal técnica. Registra el comando, resultado y limitaciones. Un build verde no prueba la
persistencia ni la experiencia de usuario.

### 4. Verificación en interfaz

Si la aplicación puede ejecutarse y Playwright ya está disponible, úsalo sin instalarlo
automáticamente. Comprueba los recorridos críticos desde la interfaz real. Por cada caso registra:

1. precondiciones y datos creados;
2. acción exacta del usuario;
3. resultado esperado y resultado observado;
4. persistencia tras recargar o cerrar/abrir la pantalla;
5. impacto en pantallas relacionadas;
6. casos inválidos, vacíos y estados de error;
7. captura, trace, URL, selector o log que permita reproducirlo.

Para pruebas de escritura usa datos claramente sintéticos y aislados, por ejemplo un prefijo
`QA-FUNC-<fecha>`, sólo en local o staging. Limpia esos datos al terminar si la aplicación y el
alcance lo permiten; si no puedes limpiarlos, deja constancia. Nunca alteres datos reales para
conseguir evidencia.

Si Playwright no está disponible, si la app no arranca o falta una cuenta segura, no lo disimules:
continúa con la inspección posible y clasifica la interfaz como `NO VERIFICADA`, explicando qué faltó.

### 5. Clasificación

Aplica estas definiciones de forma conservadora:

| Estado | Regla |
|---|---|
| `FUNCIONAL` | Hace lo esperado y hay evidencia suficiente; si implica datos, se comprobó su persistencia y sus efectos relevantes. |
| `SIMULADA` | La respuesta o los datos son intencionadamente de demostración, mock o hardcodeados. Indica si está documentado. |
| `INCOMPLETA` | Una parte funciona, pero falta un paso, caso, integración, permiso, persistencia o estado de error relevante. |
| `NO FUNCIONAL` | La acción falla, guarda mal, pierde datos o produce un resultado distinto del esperado. |
| `NO VERIFICADA` | No hay evidencia suficiente por falta de entorno, acceso, datos, especificación o prueba ejecutable. |

Asigna también el nivel de evidencia:

- `VERIFICADO EN INTERFAZ`: recorrido ejecutado realmente, preferentemente con Playwright, con
  resultado y evidencia reproducible.
- `VERIFICADO EN CÓDIGO`: implementación trazada, sin prueba completa en interfaz.
- `NO VERIFICADO`: no se pudo comprobar de forma suficiente.

Un caso con evidencia contradictoria no es funcional por defecto: explica la contradicción y conserva
la clasificación más prudente.

### 6. Informe

Guarda, salvo que el usuario indique otra cosa, en:

```text
QA/_qa_<proyecto>_<AAAAMMDD-HHmm>/
├── AUDITORIA-FUNCIONAL.md
├── AUDITORIA-FUNCIONAL.json
└── evidence/
```

Usa la plantilla [formato-informe.md](references/formato-informe.md). El informe debe incluir:

- resumen ejecutivo, alcance, entorno, fecha y limitaciones;
- inventario de funcionalidades y recorridos críticos;
- tabla de estado, evidencia, impacto, prioridad y referencias técnicas;
- qué se verificó con interfaz/Playwright, qué se verificó sólo en código y qué no se pudo verificar;
- simulaciones, incompletudes, operaciones no funcionales, problemas de persistencia e inconsistencias;
- acciones que parecen funcionar pero no completan la operación;
- hallazgos ordenados por `P0` bloqueante, `P1` alta, `P2` media y `P3` baja;
- propuesta de corrección accionable sin modificar el código durante esta skill.

En `AUDITORIA-FUNCIONAL.json`, conserva un registro por funcionalidad con al menos: `id`, `nombre`,
`recorrido`, `expectativa`, `expectativaFuente`, `resultado`, `estado`, `evidencia`, `nivelEvidencia`,
`persistencia`, `referencias`, `prioridad`, `limitaciones` y `siguientePaso`. Redacta o elimina secretos,
tokens, contraseñas, datos personales y contenido de clientes de las evidencias.

## Recibo final

Termina con una conclusión clara: `FUNCIONALIDAD SUFICIENTEMENTE VERIFICADA`, `NO LISTA PARA DARLA
POR FUNCIONAL` o `AUDITORÍA PARCIAL`. Indica exactamente qué se ejecutó, qué no, qué evidencia queda
guardada y cuál es el siguiente paso. No conviertas `NO VERIFICADA` en `FUNCIONAL` por intuición.

## Relación con otras skills

- Una revisión contra la Definition of Done: comprueba una Definition of Done o `ACCEPTANCE.json`; esta skill descubre el estado
  funcional real y aporta evidencia de recorridos.
- `jn-auditoria-testing`: revisa estrategia, calidad y cobertura de tests; esta skill comprueba el
  producto aunque no existan tests.
- `jn-auditoria-seguridad`: revisa OWASP, secretos y autenticación/autorización; deriva allí los
  hallazgos de seguridad que excedan el comportamiento funcional.
