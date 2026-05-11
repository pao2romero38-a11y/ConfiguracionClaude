# Skills de Claude Code — Índice completo

Este directorio contiene los **20 skills** que extienden el comportamiento definido
en `CLAUDE.md`. Cada skill activa comportamientos especializados para su dominio.

## Cómo activar un skill

**Opción 1 — Automática:** Claude detecta la situación y carga el skill por su `description`.

**Opción 2 — Explícita en el prompt:**
```
Lee .claude/skills/fin/SKILL.md y analiza este estado de resultados.
```

**Opción 3 — Con comando de modo** (definido en CLAUDE.md):
```
/fin Analiza la rentabilidad de esta empresa manufacturera.
```

---

## Directorio de skills

### Skills de programación (8)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/dev` | `skills/dev/` | Programador / Diseñador de sistemas — arquitectura, concurrencia, performance |
| `/dev-modes` | `skills/dev-modes/` | Modos globales — DEBUG, PERFORMANCE, MAINTENANCE (skill maestro) |
| `/dev-test` | `skills/dev-test/` | Pruebas unitarias e integración — pytest, Jest, JUnit, TDD, mocking |
| `/dev-api` | `skills/dev-api/` | Diseño de APIs REST y GraphQL — OpenAPI, versionado, seguridad |
| `/dev-db` | `skills/dev-db/` | Bases de datos — SQL-92, modelado, índices, N+1, transacciones |
| `/dev-git` | `skills/dev-git/` | Flujo Git — branching, Conventional Commits, PR, hooks |
| `/dev-docker` | `skills/dev-docker/` | Contenedores — Dockerfile, multi-stage, Compose, secrets |
| `/dev-clean` | `skills/dev-clean/` | Código limpio — SOLID, code smells, refactorización, complejidad |

### Skills de dominio (13)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/edu` | `skills/edu/` | Capacitador — Aprendizaje Significativo y Competencias |
| `/inv` | `skills/inv/` | Investigador riguroso |
| `/fin` | `skills/fin/` | Experto en Finanzas |
| `/mkt` | `skills/mkt/` | Experto en Marketing |
| `/tec` | `skills/tec/` | Experto en Tecnología |
| `/proy` | `skills/proy/` | Evaluador de Proyectos |
| `/seg` | `skills/seg/` | Experto en Seguridad |
| `/rsk` | `skills/rsk/` | Evaluador de Riesgos |
| `/ci` | `skills/ci/` | Control Interno |
| `/aud` | `skills/aud/` | Auditor profesional |
| `/dis` | `skills/dis/` | Diseñador estratégico |
| `/cost` | `skills/cost/` | Experto en Costos |
| `/tra` | `skills/tra/` | Traductor profesional |

---

## Estructura de cada SKILL.md

```
---
name:         identificador único del skill
description:  cuándo activarlo — Claude lo lee para decidir automáticamente
---

1. Verificaciones antes de responder   ← checklist de contexto requerido
2. Protocolo / marcos de referencia    ← cómo trabajar en este dominio
3. Formato de entrega obligatorio      ← estructura exacta de la respuesta
4. Restricciones                       ← qué nunca hacer en este modo
5. Señales de alerta                   ← cuándo aplicar precaución adicional
6. Advertencias obligatorias           ← textos legales o de responsabilidad
7. Referencias del dominio (APA 7)     ← fuentes base del skill
```

---

## Principios que aplican a todos los skills

Heredados del `CLAUDE.md` — no se repiten en cada skill pero siempre aplican:

- **APA 7ª edición** en todas las referencias y citas
- **Más reciente → más antigua** en el orden de las referencias
- **General → particular** en la estructura de toda respuesta
- **Protocolo de calidad de 4 pasos** antes de cada respuesta
- **Marcadores de certeza** `[DOCUMENTADO]` `[ESTIMADO]` `[VERIFICAR]` cuando corresponda

---

*Skills v3.0 — 21 skills (8 de programación + 13 de dominio)*
*Proyecto: Curso Claude Code · Aprendizaje Significativo*
*Mayo 2026*
