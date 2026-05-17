---
name: protocolo-commit-continuidad
description: >
  Activar cuando: la conversación fue resumida/compactada y hay que
  reconstruir contexto antes de actuar; o se alcanzó un hito/decisión
  importante y hay que dejar checkpoint. Gestiona el snapshot versionado
  docs/commits/COMMIT-V{n}.md de cada proyecto. Aditivo: no altera modos,
  skills ni el estándar APA. Comandos de activación: /commit · [MODO: COMMIT]
---

# SKILL — Protocolo COMMIT (continuidad ante compactación)

## Alcance
Se SUMA a, no reemplaza, el CLAUDE.md global ni ningún modo. Solo añade
continuidad de contexto por proyecto.

## Ubicación del COMMIT
`docs/commits/COMMIT-V{n}.md` en el repo del proyecto, monotónico por
hito. El "más reciente" = mayor n. Inmutable una vez superado.

## Contenido mínimo de cada COMMIT
1. Conclusiones importantes
2. Criterios construidos (anti-errores)
3. Estado / reconstrucción de avances
4. Próximos pasos
5. Puntero al anterior

## REGLA MÁXIMA — recuperación tras compactación
Si hubo resumen/compactación, ANTES de actuar: abrir docs/commits/, leer
el COMMIT de mayor versión y reconstruir criterios y estado desde ahí.

## REGLA DE ORO — checkpoint por cadencia (no por predicción)
Actualizar/crear el COMMIT en cada hito o decisión importante, de forma
incondicional (no depende de predecir la compactación). Best-effort
adicional: si el contexto se percibe muy largo, checkpoint inmediato.

## Frontera (evitar duplicación)
- Auto-memoria = criterios duraderos transversales (siempre cargada).
- COMMIT V{n} = snapshot de reconstrucción del workstream activo.
- git = código. Conviven; ninguna sustituye a otra.

## Referencias (APA 7)
Preston-Werner, T. (2013). Semantic versioning 2.0.0. https://semver.org
International Organization for Standardization. (2017). ISO/IEC/IEEE
    12207:2017 — Software life cycle processes. ISO.
