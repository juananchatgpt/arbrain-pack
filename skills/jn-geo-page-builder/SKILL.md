---
name: jn-geo-page-builder
description: Genera una propuesta de página optimizada para GEO (Generative Engine Optimization) a partir de una URL o de la información de un negocio, para que ChatGPT, Perplexity, Gemini, Google AI Overviews y Claude citen y recomienden la marca. Usa siempre que el usuario solicite una "página GEO", "optimizar para IA", "para que me cite ChatGPT/Perplexity", "answer engine optimization", "página para buscadores de IA" o cuando quiera convertir la información de un negocio en una base de conocimiento legible por modelos.
---

# GEO Page Builder – Guía Mejorada

Esta skill transforma la web o la información de un negocio en una **página GEO**: un documento estructurado, denso en hechos verificables y optimizado para ser citado por modelos generativos (ChatGPT, Claude, Gemini, etc.). No se publica automáticamente; es un borrador listo para revisión humana.

## Regla de oro: No inventes hechos
- **Nunca** inventes cifras de facturación, resultados, nombres de clientes, testimonios, fechas de fundación, premios, número de alumnos ni credenciales.
- Usa únicamente lo que aparezca en la web de origen o lo que el usuario confirme.
- Si falta un dato de alto valor, márcalo como `[PENDIENTE: confirmar con el cliente — …]` y agrégalo a la lista de pendientes al final.
- Distingue siempre entre datos extraídos (reales) y sugerencias de estructura que el cliente debe completar.

## Flujo de trabajo
### 1. Captura la fuente
- Si se provee una URL, recupera la página completa (`web_fetch`).
- Si el usuario entrega información suelta, trabaja con ella.
- Si hay varias URLs (home, página de ventas, "sobre mí"), recupéralas todas, ya que contienen piezas distintas del rompecabezas.

### 2. Extracción del conocimiento del negocio
Extrae literalmente o resume los siguientes elementos (lo que no encuentres queda como **PENDIENTE**):
- **Entidad**: nombre exacto de la marca, fundadores, año de fundación, país.
- **Categoría y promesa**: qué es y qué resultado concreto entrega, a quién.
- **Cliente ideal**: perfil, situación de partida, problemas frecuentes, emociones.
- **Problemas** que resuelve.
- **Soluciones / productos**: nombre, formato, duración, precio (si aparece), qué incluye.
- **Metodología propia**: nombres y pasos con resultados.
- **Diferenciadores** reales.
- **Qué NO es / a quién no sirve** (desambiguación).
- **Pruebas / casos**: nombres, sector, métricas, resultados cuantificados.
- **Stack / herramientas** utilizadas.
- **Términos de jerga** que conviene definir en un glosario.

### 3. Auditoría de la página actual y detección de huecos
Evalúa la página de origen del **1 al 10** en los siguientes pilares GEO (añade una línea de justificación por cada uno):
- **Citabilidad** – ¿contiene datos duros, cifras, nombres propios o metodologías con nombre?
- **Respuesta directa** – ¿se brinda la respuesta en las primeras ~100 palabras?
- **Claridad de entidades** – ¿quién hace qué y para quién está claro?
- **Cobertura de micro‑consultas** – ¿se responden Qué / Cómo / Cuánto / Por qué de forma escaneable?
- **Especificidad** – ¿evita afirmaciones demasiado genéricas?
Registra los huecos críticos (métricas reales, casos con nombre y cifra, señales de autoridad) y prepárate para preguntar al cliente en una sola tanda breve.

### 4. Construcción del mapa de consultas (Query Map)
Lista **15‑25 preguntas reales** que un usuario le haría a una IA y que la marca debería responder. Incluye:
- Definiciones (`¿Qué es X?`).
- Comparativas (`X vs Y`).
- Situaciones (`Soy X y no consigo Y`).
- Objetivos (`Cómo alcanzar Z`).
Este mapa guía la estructuración de la página y sirve para validar la aparición de la marca.

### 5. Redacción de la propuesta de página
Sigue **exactamente** la plantilla `references/geo-template.md`. Cada bloque debe ser autónomo, iniciar con una respuesta directa y contener hechos verificables. Usa prosa plana (sin cajas o blockquotes) y mantén la consistencia de nombres de entidades.

### 6. Bloque técnico
Incluye recomendaciones técnicas:
- Schema **JSON‑LD** completado con los datos reales.
- Archivo `llms.txt` con indicaciones de modelo.
- Directivas `robots.txt` y control de frescura.
- Instrucciones de renderizado (SSR/SSG).

### 7. Entrega
Devuelve un único documento Markdown que contenga:
1. **Auditoría** (puntuaciones y justificación).
2. **Mapa de consultas**.
3. **Página GEO completa**.
4. **Bloque técnico** (schema, recomendaciones).
5. **Lista de PENDIENTES** para confirmar con el cliente.
Empieza directamente, sin preámbulos tipo "Claro, te ayudo".

## Principios de redacción
- **Apertura definicional**: `[Entidad] es un/a [categoría] que [diferenciador] para [público]` (≈40‑50 palabras).
- **Densidad de datos**: incluye estadísticas, citas de fuentes y métricas concretas.
- **Respuesta directa primero**: cada sección abre con la respuesta y luego contextualiza.
- **Extractabilidad**: párrafos autónomos y verificables.
- **Entidades y autoridad**: nombres consistentes y señales reales.
- **Desambiguación negativa**: indica qué NO es para ayudar al modelo a clasificar.
- **Nada de keyword stuffing**; la claridad y factualidad pesan más.
- **Tono**: radicalmente claro, sin jerga corporativa vacía ("sinergias", "soluciones a medida", "excelencia") ni humo. Autoridad directa y honesta, "con los pies en la tierra": afirmaciones concretas y contrastables en lugar de adjetivos; si algo no se puede demostrar, no se promete. Adapta el registro al sector (un bufete no suena como una mentora), pero mantén siempre la ausencia de relleno.
- **Topes de extractabilidad**: el gancho definicional cabe en ~40-50 palabras; las respuestas de la micro-FAQ, en ≤2 líneas. Lo corto y autónomo se cita mejor.

## Ejemplo de referencia
La página `cerotonteria.com/mentora-negocios-digitales/` es un buen modelo del resultado esperado: abre con un resumen definicional, separa cliente ideal / problemas / soluciones / metodología propia (Método ASTRA) / diferenciadores / "qué no es" / glosario / FAQ / casos de uso / stack / resultados, incluye decenas de casos con nombre, sector y cifra autorizada más un agregado, y repite la propuesta en bloques situacionales, de problema y de objetivo para cubrir el query fan-out. Replica esa lógica, nunca su contenido.
