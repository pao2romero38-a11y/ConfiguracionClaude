# Skills de Claude Code — Índice completo

Este directorio contiene los **44 skills** que extienden el comportamiento definido
en `CLAUDE.md`. Cada skill activa comportamientos especializados para su dominio.

Distribución:
- **Familia `dev-*`** (10): núcleo de programación.
- **Ciclo de vida del proyecto** (10): de carpeta vacía a módulo CRUD funcional.
- **Operación multi-agente** (3): `/status`, `/handoff`, `/inbox`.
- **Dominio profesional** (13): finanzas, marketing, tec, proy, seg, rsk, ci,
  aud, dis, cost, tra, edu, inv.
- **Inteligencia Artificial** (3): `/ai`, `/ai-llm`, `/ai-ml`.
- **Medicina** (2): `/medicina` (padre) · `/audiologia` — Audiología, Foniatría, Otoneurología, Patología del lenguaje.
- **Meta-skills** (3): `/prompt`, `/capacidad`, `/commit` — operan sobre el prompt, el conjunto de herramientas o la continuidad de contexto, no sobre un dominio.

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

### Familia `dev-*` — núcleo de programación (10)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/dev` | `skills/dev/` | Programador / Diseñador de sistemas — arquitectura, concurrencia, performance, DoD compartida (§11) |
| `/dev-modes` | `skills/dev-modes/` | Modos globales — DEBUG, PERFORMANCE, MAINTENANCE |
| `/dev-test` | `skills/dev-test/` | Pruebas unitarias e integración — pytest, Jest, JUnit, TDD, mocking |
| `/dev-api` | `skills/dev-api/` | Diseño de APIs REST y GraphQL — contrato canónico (§15) |
| `/dev-db` | `skills/dev-db/` | Bases de datos — SQL-92, modelado, índices, N+1, transacciones |
| `/dev-git` | `skills/dev-git/` | Flujo Git — branching, Conventional Commits, PR, hooks |
| `/dev-docker` | `skills/dev-docker/` | Contenedores — Dockerfile, multi-stage, Compose, secrets |
| `/dev-clean` | `skills/dev-clean/` | Código limpio — SOLID, code smells, refactorización, complejidad |
| `/dev-meta` | `skills/dev-meta/` | Metadata-driven SSOT y 9 niveles progresivos |
| `/dev-multiagent` | `skills/dev-multiagent/` | Convivencia multi-agente (opcional, con bus obligatorio si activo) |

### Ciclo de vida del proyecto (10)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/init-proyecto` | `skills/init-proyecto/` | Inicializar proyecto nuevo desde cero |
| `/stack-pick` | `skills/stack-pick/` | Fase 3: seleccionar stack tecnológico |
| `/install-from-stack` | `skills/install-from-stack/` | Fase 4: bootstrap del entorno desde el stack |
| `/back-scaffold-from-meta` | `skills/back-scaffold-from-meta/` | Fase 5: scaffold backend desde metadata |
| `/front-scaffold-from-meta` | `skills/front-scaffold-from-meta/` | Fase 5: scaffold frontend desde metadata |
| `/meta-add-tabla` | `skills/meta-add-tabla/` | Wizard para agregar tabla nueva con metadata completa |
| `/meta-bump` | `skills/meta-bump/` | Versionado SemVer de la metadata |
| `/meta-validate` | `skills/meta-validate/` | Gate pre-Fase 5: 17 checks de consistencia |
| `/diff-meta` | `skills/diff-meta/` | Diff legible de cambios en metadata desde último commit |
| `/arq-derive` | `skills/arq-derive/` | Fase 2: propuesta de arquitectura derivada de la metadata |

### Operación multi-agente (3)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/status` | `skills/status/` | Vista única: PRs, mensajes, pendientes, CI |
| `/handoff` | `skills/handoff/` | Fin de sesión: pasa contexto al siguiente agente |
| `/inbox` | `skills/inbox/` | Re-check de mensajes nuevos durante sesión larga |

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

### Skills de IA (3)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/ai` | `skills/ai/` | Experto en IA — estrategia y gobierno (NIST AI RMF, EU AI Act, ISO/IEC 42001) |
| `/ai-llm` | `skills/ai-llm/` | Aplicaciones de LLMs — prompt engineering, RAG, agentes, evals |
| `/ai-ml` | `skills/ai-ml/` | ML / MLOps — ciclo de vida del modelo, drift, monitoring, retraining |

### Medicina (2)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/medicina` | `skills/medicina/` | Médico Clínico — razonamiento clínico general, diagnóstico diferencial, terapéutica |
| `/audiologia` | `skills/audiologia/` | Audiólogo Clínico (hijo de `/medicina`) — Audiología, Foniatría, Otoneurología, Patología del lenguaje |

### Meta-skills (3)

| Comando | Carpeta | Dominio |
|---------|---------|---------|
| `/prompt` | `skills/prompt/` | Refinador de prompts — detecta modo, refina y expone rúbrica visible |
| `/capacidad` | `skills/capacidad/` | Gestor de capacidades — investiga, instala y registra herramientas faltantes |
| `/commit` | `skills/commit/` | Protocolo COMMIT — continuidad de contexto ante compactación (snapshot versionado) |

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

*Skills — 44 skills (10 familia dev-* + 10 ciclo de vida + 3 multi-agente + 13 dominio + 3 IA + 2 medicina + 3 meta-skills)*
*Más 4 agentes especializados en `.claude/agents/`: be-reviewer, ui-reviewer, code-reviewer, message-bus*
*Proyecto: ConfiguracionClaude · Configuración base de Claude Code*
*Versión vigente en VERSION en la raíz del repo*
