# Checklist de auditoría y principios de construcción

Consúltalo en el **paso 8** (entregar reporte) y al montar el testing de un proyecto desde cero.

## Checklist de auditoría

- [ ] ¿Existe una pirámide de testing equilibrada (muchos unit, algunos integración, pocos E2E) o está invertida?
- [ ] ¿La cobertura cumple objetivos razonables (funciones ~100%, líneas/branches ~80%) y está vinculada a casos de calidad?
- [ ] ¿Los tests buscan elementos como un usuario (getByRole/getByLabelText/getByText) y no por clases CSS o IDs internos?
- [ ] ¿Los tests validan comportamiento visible y no detalles de implementación o estado interno?
- [ ] ¿Las funciones de lógica de negocio son puras (sin efectos secundarios) y por tanto fáciles de testear?
- [ ] ¿Los tests unitarios son rápidos (<10ms), aislados y determinísticos?
- [ ] ¿Las llamadas a APIs/servicios están mockeadas para probar también errores de red y listas vacías?
- [ ] ¿Se usa await/waitFor/auto-wait para la asincronía en lugar de setTimeout?
- [ ] ¿Cada test es independiente y el estado/base de datos se resetea entre tests (beforeEach)?
- [ ] ¿Existen tests E2E para los flujos críticos de negocio (pago, registro, checkout) con selectores estables?
- [ ] ¿La CI ejecuta los tests en cada push/PR y bloquea merges con tests rojos o con test.only (forbidOnly)?
- [ ] ¿Hay visual regression testing para detectar regresiones de CSS/layout/responsive?

## Principios al construir desde cero

- Configura el stack moderno desde el inicio: Vitest + Testing Library (unit/integration) y Playwright (E2E).
- Define umbrales de coverage en la configuración (functions 100%, lines/branches/statements 80%) y vincúlalos a la calidad de casos.
- Adopta TDD: escribe el test antes que el código siguiendo Rojo-Verde-Refactor y las tres leyes.
- Diseña con funciones puras e inmutabilidad para que el código sea testeable por construcción.
- Escribe tests centrados en el usuario desde el día uno, priorizando getByRole y la accesibilidad (ARIA roles, labels).
- Estructura cada test con el patrón AAA (Arrange-Act-Assert) para máxima claridad.
- Mockea el service layer/API con un mock global por defecto (happy path) y overrides por test (errores, vacíos).
- Reserva los E2E para flujos críticos (5-10%) y úsalos con Page Object Model para mantenibilidad y escalabilidad.
- Integra los tests en CI/CD (GitHub Actions) con forbidOnly, reintentos y subida de artefactos en fallo.
- Apoya la generación de tests con IA para cubrir casos límite y acelerar, sin caer en sobreingeniería de tests.
