---
name: jn-landing-forge
description: Crea o rehace landings comerciales con dirección de arte propia, datos de negocio separados, medios con procedencia y verificación reproducible. Úsala cuando el usuario pida una landing, página de venta, página de captación, scrollytelling o una web que parezca genérica. No la uses para redactar una página GEO sin entregar una experiencia visual ni para publicar automáticamente.
metadata:
  author: ALZAT
  version: "1.1.0"
---

# Landing Forge — ALZAT

Convierte una oferta real en una experiencia web distintiva, legible y verificable. La skill
separa tres decisiones: qué es la página (estructura), de qué está hecha (materia) y qué puede
hacer el visitante (instrumento). No impone un layout universal.

## Antes de escribir HTML

Lee [brief.md](references/brief.md). Captura en una sola pasada:

- público, oferta y una sola acción principal;
- evidencia comercial disponible de verdad;
- materiales existentes y referencias de atmósfera;
- lo que el visitante debe poder hacer aquí;
- restricciones de marca, sector y regulación.

Separa siempre `Hechos`, `Supuestos` y `Desconocidos`. Un precio, resultado, cliente, testimonio,
certificación o cifra que no esté respaldado permanece desconocido y se muestra como pendiente o
se elimina. No se rellenan huecos con copy de marketing.

## Aprendizajes operativos incorporados

### La entrega no es solo la home

Si el objetivo es enseñar un rediseño a un cliente, planifica desde el brief el recorrido completo:

- home con propuesta de valor, prueba social y una acción principal;
- páginas intermedias de servicio con intención de búsqueda propia;
- páginas legales enlazadas desde el pie cuando haya formulario, almacenamiento local, cookies o
  terceros;
- propuesta comercial separada si el usuario necesita vender el rediseño.

Una landing de servicio no debe ser una tarjeta ampliada. Como mínimo debe tener un `h1` específico,
introducción útil, bloques de información escaneables, imágenes reales del servicio, FAQ y CTA
contextualizado. El texto debe poder vivir como página SEO independiente y no debe hablar de “la web
actual”, “esta propuesta”, “la demo” o “antes de publicar”. Sustituye ese lenguaje interno por una
frase útil para el cliente final: “Cuéntanos tu proyecto”, “Consúltanos” o equivalente.

### Marca y medios consistentes

Usa una única fuente para el logotipo y el wordmark. La cabecera de la home, las páginas de servicio
y las páginas legales deben parecer la misma marca; no inventes una variante del logo para cada
plantilla.

Cuando exista una web original con material aprovechable, reutiliza sus imágenes si el encargo lo
permite y registra la procedencia y el uso en `ASSET-MANIFEST.json`. No sustituyas fotografías reales
de trabajos por imágenes generadas o stock solo para llenar espacio. Si una imagen es mala, cambia
solo esa pieza y deja constancia de la decisión. Los `alt` deben describir el trabajo o el contexto,
no repetir palabras clave de forma artificial.

### Conversión y responsive desde el principio

Mantén una navegación visible al desplazarse: `fixed` en la home o `sticky` en plantillas donde
respete mejor el flujo, siempre también en móvil. Añade `scroll-padding-top` para que los anclajes no
queden tapados por la cabecera y comprueba el menú abierto/cerrado con teclado.

Para rejillas de muchos servicios, parte de tres fichas por fila en escritorio, una por fila en
móvil y dos en un ancho intermedio, salvo que el brief justifique otra densidad. No des por validado
un breakpoint porque el CSS compile: inspecciona visualmente al menos 1440×900 y 390×844.

### Legal, cookies y prueba social

Si la web recoge datos, prepara las páginas de aviso legal, privacidad/protección de datos y cookies,
con enlaces visibles desde el pie y consentimiento asociado al formulario cuando corresponda. No
presentes el texto como asesoramiento jurídico definitivo: parte de la identidad y hechos verificados
del negocio y deja marcada la revisión legal pendiente cuando no exista validación profesional.

Las reseñas solo se muestran si tienen una fuente verificable. Conserva cita, autor tal como aparece,
origen y fecha o contexto disponible; enlaza a la ficha original cuando sea posible. Nunca inventes
valoraciones, nombres, puntuaciones o volumen de reseñas para mejorar la conversión.

## Contrato de datos

Guarda los hechos comerciales en `marca.json` (o el módulo equivalente del stack) y la decisión
visual en CSS/componentes. El copy repetido debe tener una única fuente. Si se usa un build estático,
una referencia a un dato inexistente debe romper el build en lugar de dejar un hueco silencioso.

La entrega mínima de una landing incluye:

```text
BRIEF.md             hechos, supuestos, desconocidos y decisiones
marca.json           datos de la oferta y mensajes del formulario
pagina.html          o componentes fuente; no editar el generado
index.html           solo si existe un paso de generación
ASSET-MANIFEST.json  procedencia, licencia, modelo y decisión de cada medio
LIMITACIONES.md      qué se probó y qué no
ACCEPTANCE.json      criterios pass/fail/not-run con evidencia
```

## Dirección de arte

Elige una gramática antes de maquetar y define qué prohíbe. Cambiar colores o tipografías no crea
una página distinta. La interacción principal debe explicar la oferta o dejar algo útil al
visitante; no añadas scroll por espectáculo.

- Mantén el texto como HTML seleccionable y entendible sin animación.
- No dibujes héroes, logos, fondos o ilustraciones principales con SVG propio ni uses CSS/canvas
  para fingir una fotografía.
- Usa fotografías, vídeo o imágenes generadas con procedencia local y manifiesto. Si el contenido
  sintético puede confundirse con material real, etiquétalo según las reglas del BOS.
- El CTA, la oferta y la navegación no pueden depender de la animación.
- Un formulario de demostración local puede usar almacenamiento del navegador, pero debe decirlo.
  En una landing real del BOS, conecta el proyecto a su API o a `jn-smtp-email`; nunca digas “enviado”
  si solo se guardó localmente.

## Verificación

Lee [verification.md](references/verification.md) antes de cerrar. Ejecuta como mínimo:

```bash
node .claude/skills/jn-landing-forge/scripts/validate-landing.mjs <sitio>
```

Si hay navegador disponible, recorre el resultado en escritorio, móvil, teclado, reduced motion,
zoom 200 %, medio principal fallido y recarga en una posición intermedia. Revisa las capturas a ojo:
el automatismo no detecta todos los solapes ni decide si la dirección de arte funciona.

La validación verde demuestra la compilación y los invariantes comprobados; no demuestra conversión,
compatibilidad con todos los navegadores ni pruebas en un teléfono físico.

## Límites de alcance

Esta skill construye y verifica una landing dentro del proyecto autorizado. No publica, no envía
leads, no compra servicios, no conecta cuentas de Meta y no inventa datos. Para una página GEO
documental usa `jn-geo-page-builder` y, si también hace falta una experiencia visual, combina ambas
capas sin mezclar sus fuentes de verdad.

Para decisiones de procedencia y atribución, lee [third-party.md](references/third-party.md).
