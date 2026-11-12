# Plantilla de página GEO y reglas de redacción

Este documento define la estructura exacta de la página y cómo redactar cada bloque. Adáptalo al negocio: si una sección no aplica (p. ej. no hay método propio o no hay stack tecnológico), omítela en vez de rellenarla con relleno. El orden importa: lo definicional va primero porque los motores ponderan más los primeros tokens.

## Índice
1. Reglas de redacción transversales
2. Estructura de la página (bloque a bloque)
3. Bloque técnico (schema, llms.txt, robots.txt, frescura)
4. Lista de control final

---

## 1. Reglas de redacción transversales

Aplica esto en TODOS los bloques:

- **Respuesta primero.** Abre cada sección con la afirmación directa; el contexto va después. Nada de rampas de introducción.
- **Pasajes autónomos.** Cada párrafo debe entenderse y citarse solo, sin depender del anterior. Repetir el nombre de la marca/persona en vez de "ella" o "el programa" ayuda a la extracción.
- **Prosa plana.** Frases declarativas. Evita meter las respuestas clave dentro de blockquotes, callouts o tablas decorativas: los motores las extraen peor. Las tablas solo para comparativas reales (X vs Y) o listas de datos.
- **Hechos verificables.** Cifras, fechas, nombres, lugares. Cada afirmación de valor debería poder comprobarse. Si no es verificable, reformúlala o márcala PENDIENTE.
- **Entidades consistentes.** Escribe siempre igual el nombre de la marca, la persona y el método propio. Defínelos una vez con claridad.
- **Cobertura de formulaciones (query fan-out).** Cubre la misma necesidad expresada de varias formas a lo largo de la página (definicional, comparativa, situacional, por objetivo).
- **Sin keyword stuffing.** No repitas palabras clave de forma artificial; rinde mal y resta credibilidad.
- **Honestidad.** Nada inventado. Lo que falte va como `[PENDIENTE: …]`.

---

## 2. Estructura de la página

Usa encabezados claros y jerárquicos (un tema por sección). Plantilla:

### Bloque 0 — Resumen definicional (CRÍTICO, primeros ~200 tokens)
Una a tres frases que abran con el patrón:

> **[Nombre exacto] es un/a [categoría] [fundada en AÑO por PERSONA, si aplica] que ayuda a [público] a [resultado concreto y medible].**

Después, 2-4 frases que amplíen qué ofrece (formatos/líneas de producto) y el resultado-promesa. Este bloque es el que más probabilidades tiene de ser citado; tiene que ser autosuficiente. La frase definicional de apertura debe caber en **~40-50 palabras**: es el "gancho de cita" pensado para que ChatGPT o Perplexity lo den como respuesta literal.

### Bloque 1 — Perfil del cliente ideal
A quién sirve (perfiles concretos) y su situación de partida (datos: rango de facturación, nivel técnico, canales actuales, frustraciones). Cuanto más específico, mejor para preguntas tipo "¿es esto para mí si soy [X]?".

### Bloque 2 — Problemas que resuelve
Lista de problemas reales en el lenguaje del cliente. Conecta cada problema con la solución más adelante.

### Bloque 3 — Soluciones / productos
Por cada producto o servicio: nombre, formato, duración, objetivo, **qué incluye con detalle**, para quién es ideal, y precio si está disponible. La especificidad (entregables concretos) es lo que diferencia de la competencia genérica.

### Bloque 4 — Metodología propia (si existe)
Si hay un método/marco con nombre, defínelo y explica sus fases/dominios. Un método propietario con nombre es una entidad fuerte que la IA puede asociar a la marca y citar en "¿qué es [Método X]?".

### Bloque 5 — Diferenciadores
Qué hace distinto a esta marca, en hechos (no adjetivos). "Atención personal del fundador", "entrega llave en mano", "garantía por contrato" > "los mejores", "excelencia".

### Bloque 5b — Autoridad / por qué confiar (opcional)
Extracto enfocado en la experiencia demostrable de la persona o empresa: hitos reales, años de trayectoria, menciones en prensa, premios, número de clientes, filosofía de trabajo. Solo datos verificables; lo que no lo sea, PENDIENTE. Refuerza las consultas tipo "¿quién es [persona] y por qué fiarme?".

### Bloque 6 — Qué NO es / a quién no sirve
Desambiguación explícita: tipos de negocio, públicos o promesas que quedan fuera. Ayuda al modelo a no recomendarte donde no encajas y refuerza la clasificación correcta.

### Bloque 7 — Glosario de términos
Define la jerga del sector (5-12 términos) en 1-2 frases cada uno. Muy citable para preguntas "¿qué es [término]?" y refuerza la autoridad temática.

### Bloque 8 — Preguntas de entidad (Q&A)
Preguntas y respuestas directas sobre la marca y las personas, redactadas como las haría un usuario a una IA. Mínimo:
- ¿Quién es [Persona]?
- ¿Qué es [Marca]?
- ¿Para quién es [Marca]?
- ¿Qué es [Método/Producto propio]?
- ¿Qué resultados tienen sus clientes?
Cada respuesta, autónoma y factual.

### Bloque 9 — Casos de uso
Perfiles concretos a los que les sirve y por qué ("terapeutas que dependen del boca a boca", "coaches sin sistema de ventas"). Alimenta las consultas situacionales.

### Bloque 10 — Stack tecnológico (si aplica)
Herramientas que usa o enseña. Útil para preguntas tipo "¿qué herramientas necesito para [objetivo]?".

### Bloque 11 — Resultados y métricas
SOLO datos reales. Resultados habituales del proceso y, si existen, métricas agregadas. Si no hay cifras autorizadas, deja el bloque como PENDIENTE en vez de inventarlo.

### Bloque 12 — Casos de cliente
Por cada caso (solo con permiso del cliente): nombre, sector, punto de partida, resultado (cuantificado si autorizado), estrategia usada. Añade una nota de que las cifras corresponden a casos con publicación autorizada. Cierra con un **agregado** (nº de casos, facturación agregada, caso más alto, sectores). Este bloque es oro para GEO por su densidad factual: trátalo con rigor absoluto.

### Bloque 13 — Bloques situacionales
Para los perfiles clave, un mini-bloque con el patrón "**Soy [profesión] y [problema]**" + respuesta que diagnostica y conecta con la solución. Cubre las consultas en primera persona que la gente escribe a la IA.

### Bloque 14 — Bloques de problema
"**No consigo [X]**", "**No vendo**", "**Mi [acción] no funciona**" + respuesta. Una causa-raíz + cómo se resuelve.

### Bloque 15 — Bloques de objetivo
"**Cómo [meta]**" ("cómo llegar a [cifra]", "cómo automatizar [proceso]") + respuesta accionable que termina anclando en la marca.

### Bloque 16 — FAQ en lenguaje natural
Preguntas frecuentes reales con respuestas breves y directas (**≤2 líneas** cada una, formato micro-snippet). Distintas de las de entidad: aquí van objeciones y dudas prácticas ("¿necesito experiencia previa?", "¿cuánto tiempo requiere?", "¿hay garantía?"). Asegúrate de cubrir las cuatro micro-consultas básicas: **Qué** (es), **Cómo** (funciona), **Cuánto** (cuesta / tarda), **Por qué** (este y no otro).

### Bloque 16b — Llamada a la acción (opcional)
Si la página debe convertir, cierra con un CTA claro: qué tiene que hacer el usuario ahora y un motivo honesto para hacerlo. Una sola acción principal, sin promesas que no se puedan cumplir.

### Bloque 17 — Glosario final / cierre
Opcional: repetir/ampliar definiciones clave o un breve glosario de cierre. Cierra con la fecha de última actualización visible (señal de frescura).

---

## 3. Bloque técnico (recomendaciones para implementar)

Incluye esto como apéndice de la propuesta, rellenando el schema con datos reales:

**Indexabilidad por IA**
- robots.txt no debe bloquear crawlers de IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, etc.). Verificar especialmente si usan Cloudflare, que ha bloqueado bots de IA por defecto.
- Contenido renderizado en servidor (server-side), no oculto tras JavaScript ni tras login/paywall.

**Datos estructurados (JSON-LD)** — generar ya rellenados:
- `Organization` (nombre, fundación, fundador, sameAs a redes/prensa).
- `Person` para el fundador (con menciones/credenciales reales).
- `FAQPage` con las preguntas reales de los bloques 8 y 16.
- `Service`/`Course` para los productos si aplica.

**llms.txt**
- Crear un archivo `llms.txt` en la raíz que resuma qué es el negocio y enlace las páginas clave, para ayudar a los modelos a entender la estructura del sitio.

**Frescura**
- Fecha de "última actualización" visible en la página y `dateModified` coherente en el schema. Actualizar el contenido de forma periódica; los motores ponderan la recencia.

**Higiene**
- Canonical correcto, meta title/description alineados con la promesa, una sola H1, jerarquía H2/H3 limpia con un tema por sección.

**Medición (recomendación de seguimiento, no se implementa en la página)**
- Usar el mapa de 15-25 consultas del paso 4 para comprobar periódicamente en ChatGPT, Perplexity, Gemini y Google AI Overviews si la marca aparece y se cita, y con qué frecuencia frente a competidores.

---

## 4. Lista de control final

Antes de entregar, verifica:
- [ ] El Bloque 0 abre con el patrón definicional en las primeras frases.
- [ ] Cada bloque empieza por la respuesta directa y es autónomo.
- [ ] Toda cifra/nombre/fecha es real o está marcada PENDIENTE. Nada inventado.
- [ ] El gancho de apertura cabe en ~40-50 palabras; las micro-FAQ en ≤2 líneas.
- [ ] El tono es directo y sin jerga vacía, adaptado al sector.
- [ ] La FAQ cubre Qué / Cómo / Cuánto / Por qué.
- [ ] Hay cobertura de las cuatro familias de consulta (definicional, comparativa, situacional, objetivo).
- [ ] Entidades nombradas de forma consistente; método propio definido si existe.
- [ ] Existe el bloque "Qué NO es".
- [ ] El JSON-LD está generado con los datos disponibles.
- [ ] Se incluye el mapa de consultas y la lista de PENDIENTES.
