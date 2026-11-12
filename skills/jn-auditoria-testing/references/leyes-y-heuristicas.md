# Leyes y heurísticas de testing

Consúltalo en los **pasos 2, 3, 4 y 7** de la skill (evaluar pirámide, auditar calidad, mocks/asincronía, TDD).

- **Pirámide de Testing**: Unit 60-70% (base), Integración 20-30% (medio), E2E 5-10% (cúspide). Más tests unitarios, menos E2E.
- **Las 3 Leyes de TDD**: (1) No escribas código de producción hasta tener un test que falle; (2) No escribas más test del necesario para fallar; (3) No escribas más código del necesario para pasar el test.
- **Ciclo Rojo-Verde-Refactor (RED-GREEN-REFACTOR)**: escribe un test que falle, implementa lo mínimo para que pase, y luego mejora el código manteniendo la barra verde.
- **Objetivos de Coverage (Vitest)**: Funciones 100%, Líneas 80%, Branches 80%, Statements 80%. "100% funciones, 80% líneas" es lo realista.
- **Coverage por tipo (Integración)**: User Flows 90%, State Management 95%, Component Interaction 85%, API Integration 80%, Form Validation 100%.
- **Jerarquía de Queries (Testing Library)**: getByRole > getByLabelText > getByText > getByTestId (último recurso). Busca elementos como un usuario real.
- **Filosofía user-centric**: "Cuanto más se parezcan tus tests a la forma en que se usa tu software, más confianza te darán." Testa comportamiento, no implementación.
- **Características de cada nivel**: Unit < 10ms (rápida, aislada, determinística); Integración 100-500ms (conectada, DOM real); E2E 1-10s (real, costosa, crítica).
- **Patrón AAA (Arrange-Act-Assert)**: estructura todo test en tres bloques claros con comentarios.
- **Fake It 'Til You Make It**: implementa primero la solución más simple (incluso hardcoded) para validar el contrato.
- **Triangulation (Triangulación)**: añade varios casos de prueba para forzar la lógica real y generalista (un solo test permite hardcodear; dos o más obligan a generalizar).
- **Green Bar Pattern**: durante el refactoring, todos los tests deben permanecer siempre en verde.
- **Inmutabilidad (regla de oro)**: los tests deben validar que el estado original de los datos no se altera accidentalmente.
- **Selectores estables en E2E**: getByRole > getByLabelText > getByTestId; nunca selectores CSS volátiles.
- **Esperas inteligentes**: usa auto-wait / waitFor, nunca setTimeout. Gestiona la asincronía con await.
- **Tests independientes y aislados**: cada test debe poder correr solo; resetea la base de datos/estado entre tests (beforeEach).
- **forbidOnly en CI**: la CI debe fallar si encuentra un test.only olvidado (evita falsa sensación de seguridad).
- **E2E solo para flujos críticos**: enfócate exclusivamente en flujos que generan ingresos o son vitales para la operación.
