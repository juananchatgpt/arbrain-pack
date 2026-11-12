# Verificación de una landing

## Contenido y datos

- Cada precio, cifra, testimonio, nombre de cliente, resultado y certificación aparece en el
  brief o está marcado como pendiente.
- Cambiar un dato de `marca.json` cambia todas sus apariciones y no altera otros sitios.
- No hay medios locales rotos, texto incrustado como imagen ni alt ausente en imágenes informativas.
- Un medio principal fallido conserva la oferta, el texto y el CTA.
- La home y cada servicio prioritario tienen un `h1` propio, copy orientado a la consulta y no
  contienen lenguaje interno como “la web actual”, “esta propuesta” o “la demo”.
- Las páginas de servicio incluyen una imagen o galería coherente con el servicio, FAQ y CTA; sus
  imágenes proceden del manifiesto y no son relleno genérico sin atribución.
- El logotipo, wordmark, navegación y enlaces legales son coherentes entre home, servicios y legales.
- Si aplica protección de datos o cookies, existen las tres páginas legales previstas, están
  enlazadas desde el pie y el formulario no simula un envío que no se ha producido.
- Las reseñas tienen fuente verificable y no hay cifras, nombres o testimonios inventados.

## Interacción y formulario

- Entrada inválida no se guarda.
- Entrada válida confirma el guardado real y sobrevive a recarga.
- Doble envío rápido no duplica.
- Un fallo de almacenamiento o API se muestra como error, nunca como éxito.
- La acción funciona con teclado y tiene foco visible.

## Matriz visual mínima

Captura e inspecciona el recorrido completo a 1440×900 y 390×844. Añade 360×640 si la composición
usa columnas o imágenes con proporciones sensibles. Repite, si aplica, en reduced motion, zoom
200 %, sin el medio principal, con recarga en mitad del recorrido y en sentido inverso.

Comprueba específicamente que la cabecera sigue visible tras desplazar la home y una página de
servicio, también en móvil, y que los anclajes no quedan ocultos bajo ella. Revisa la densidad real
de las fichas de servicio (por defecto 3 en escritorio, 2 intermedio y 1 en móvil).

Mide en un build servido, indicando navegador, hardware, viewport, red y concurrencia. Reporta
bytes iniciales, LCP y CLS si se dispone de navegador; no conviertas esos objetivos de laboratorio
en una promesa de conversión.

## Evidencia

Conserva los fallos y la corrida que los sustituye. `ACCEPTANCE.json` debe distinguir `pass`, `fail`
y `not-run`; una prueba antigua no respalda código posterior. La revisión humana de las capturas es
obligatoria cuando hay scroll, sticky, vídeo o composición superpuesta.
