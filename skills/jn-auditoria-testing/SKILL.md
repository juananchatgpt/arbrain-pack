---
name: jn-auditoria-testing
description: "Audita o implementa una estrategia de tests (unitarios, integración y E2E) con TDD, Vitest, Testing Library y Playwright; reporta brechas de cobertura, tests frágiles y plan. Triggers: tests, testing, TDD, E2E, Playwright, Vitest, cobertura, ¿está bien testeado?, añade tests."
---

# Skill: Testing con IA

> **Adaptado al stack ALZAT:** Next.js 16 + React 19, gestor de paquetes **npm** (no pnpm), CI en
> GitHub Actions (deploy GitHub→VPS Easypanel). Sigue exigiendo `npm run build`/`typecheck` verdes
> antes de dar algo por terminado.

Audita o implementa una estrategia de testing completa (unit, integración y E2E) centrada en el usuario, con TDD, mocks y CI, usando Vitest, Testing Library y Playwright.

## Procedimiento

1. **Reconocimiento del proyecto**: Identifica el stack (framework de UI, runner de tests, herramienta E2E) y localiza los archivos de test existentes (`*.test.ts(x)`, `*.spec.ts`, carpeta `e2e/`). Revisa la configuración de coverage.

2. **Evaluar la pirámide**: Cuenta tests por tipo. Confirma que predominan los unitarios (60-70%), con integración (20-30%) y E2E mínimos (5-10%). Si está invertida (demasiados E2E), señálalo como riesgo.

3. **Auditar calidad de los tests**:
   - Que busquen por rol/label/texto, no por CSS/testid salvo último recurso.
   - Que validen comportamiento visible, no implementación interna.
   - Que sigan el patrón AAA.
   - Que sean rápidos, aislados y determinísticos.

4. **Revisar mocks y asincronía**: Verifica que las APIs estén mockeadas (mock global + overrides para error/vacío), que se use `await`/`waitFor`/auto-wait y que el estado se resetee con `beforeEach`.

5. **Revisar coverage**: Comprueba umbrales (functions 100%, lines/branches 80%). Reporta funciones de negocio sin cubrir.

6. **Revisar E2E y CI**: Confirma tests E2E para flujos críticos con Page Object Model y selectores estables, `forbidOnly` activado en CI, reintentos configurados y ejecución en cada push/PR.

7. **Implementar (si aplica) con TDD**: Para nueva funcionalidad sigue Rojo-Verde-Refactor: escribe primero un test que falle, implementa lo mínimo (Fake It), añade más casos (Triangulation) para forzar la lógica real, y refactoriza manteniendo la barra verde. Usa funciones puras e inmutabilidad.

8. **Entregar reporte**: Lista hallazgos priorizados, brechas de cobertura, tests frágiles y un plan accionable. Aprovecha la IA para generar tests de casos límite.

## Referencias

| Fichero | Cuándo abrirlo |
|---|---|
| `references/leyes-y-heuristicas.md` | Pasos 2, 3, 4 y 7: pirámide, 3 leyes de TDD, umbrales de coverage, jerarquía de queries, AAA, triangulación, selectores E2E. |
| `references/checklist-y-principios.md` | Paso 8 y proyectos nuevos: checklist de 12 puntos + principios para montar el testing desde cero. |
