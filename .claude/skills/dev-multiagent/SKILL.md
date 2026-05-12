---
name: programador-multiagente
description: >
  Activar SOLO cuando un proyecto tiene división backend + frontend (+ infra)
  y se va a trabajar con varios agentes en paralelo (humanos o IA). Documenta
  el protocolo de convivencia: mensajes append-only, pendientes split por
  scope, bus de comunicación obligatorio, identidad de agente en commits.
  No activar en proyectos unipersonales — agrega complejidad sin beneficio.
  Comandos de activación: /dev-multiagent · [MODO: MULTI-AGENTE]
---

# SKILL — Convivencia multi-agente (opcional, con bus obligatorio)

## 1. Cuándo activar este skill

```
ACTIVAR cuando:
  □ El proyecto declara explícitamente división backend + frontend (+ infra)
  □ Habrá ≥2 agentes (humanos, IA o mixtos) trabajando en paralelo
  □ Se busca que cada agente pueda ejecutar trabajos largos sin bloquear al otro

NO activar cuando:
  ✗ Hay un solo desarrollador (incluso si usa Claude para code review)
  ✗ El sistema no tiene división backend/frontend (usar /dev directamente
    sin multi-agente, con code-reviewer en lugar de be/ui-reviewer)
  ✗ El proyecto es prototipo / experimental
```

> **Regla inamovible** (ver `CRITERIOS-EVALUACION-DEV.md` §3.1): si se
> activa multi-agente, el **bus de comunicación es obligatorio**. No
> existe la configuración "multi-agente sin bus".

---

## 2. Tres pilares del protocolo

```
PILAR 1 — MENSAJES APPEND-ONLY (docs/messages/)
  Comunicación inter-agente. Inmutable después de creación. Sin estado
  mutable → cero merge conflicts.

PILAR 2 — PENDIENTES SPLIT POR SCOPE (docs/pendientes/)
  Cada agente edita SOLO su archivo (backend.md, frontend.md, infra.md,
  roadmap.md). Sin conflicto de edición concurrente.

PILAR 3 — IDENTIDAD DE AGENTE EN GIT
  Cada commit lleva Authored-Agent: trailer identificando al agente
  que lo produjo. Permite git log --author=<agente> y revisión por agente.
```

---

## 3. Mensajes append-only — protocolo

### 3.1 Estructura de archivos

```
docs/messages/
├── open/                    ← mensajes vivos (pendientes de respuesta o cierre)
│   ├── 2026-05-11-be-to-fe-001-contrato-usuarios.md
│   ├── 2026-05-12-fe-to-be-002-respuesta-contrato.md
│   └── ...
├── archived/                ← threads cerrados (state=closed)
│   ├── 2026-05-10-be-to-infra-001-cluster-staging.md
│   └── ...
└── README.md                ← este protocolo
```

### 3.2 Formato de cada mensaje (frontmatter YAML + cuerpo)

```markdown
---
from: backend
to: frontend
created: 2026-05-11T14:30:00Z
subject: Contrato del recurso usuarios v2
labels: [contract, breaking]
in_reply_to: ""            # si responde a otro mensaje, ID del original
closes: ""                 # si cierra otro mensaje, ID del cerrado
---

Contenido en markdown. Plantea pregunta, propuesta, decisión, hallazgo,
o handoff. Una vez creado, NO se modifica — solo se responde con otro
mensaje que tenga in_reply_to apuntando a este.

Si la respuesta resuelve el tema, el respondedor puede agregar closes:
con el ID del thread completo (todos los mensajes con el mismo prefijo
de fecha-emisor-destino-N).
```

### 3.3 Reglas de derivación de estado

```
Sin campo "state" mutable. El estado se deriva:

  open      ← mensaje sin respuestas (no hay otro mensaje con
               in_reply_to apuntando a él)
  replied   ← tiene ≥1 respuesta pero ninguna con closes:
  closed    ← tiene una respuesta con closes:
  archived  ← el thread completo se movió a archived/
              (solo permitido si todos están closed)
```

### 3.4 Inmutabilidad

```
✗ NUNCA editar un mensaje existente
✗ NUNCA borrar un mensaje (mover a archived/, sí)
✗ NUNCA cambiar la fecha o el subject de un mensaje creado
✓ SÍ agregar nuevos mensajes que respondan, complementen o cierren

Razón: la inmutabilidad elimina merge conflicts cuando dos agentes
trabajan en paralelo. Si A escribe un mensaje y B escribe otro, ambos
existen como archivos distintos. Si A respondiera modificando el
mensaje de B, habría conflicto. El append-only lo evita por diseño.
```

---

## 4. Pendientes SSOT split por scope

### 4.1 Estructura

```
docs/pendientes/
├── backend.md       ← solo el agente backend edita este archivo
├── frontend.md      ← solo el agente frontend edita este archivo
├── infra.md         ← solo el agente infra edita este archivo
└── roadmap.md       ← editado por todos, requiere revisión cruzada
```

### 4.2 Formato

```markdown
# Pendientes — Backend

## Activos

- [ ] be-127: Migrar query de usuarios a paginación con cursor
- [ ] be-128: Agregar idempotencia a POST /v1/transferencias
- [ ] be-129: Resolver N+1 en service de productos.list()

## Recientes (cerrados últimos 30 días, archivar después)

- [x] be-125: Bump versión OpenAPI a 1.3.0 — cerrado 2026-05-08
- [x] be-126: Crear endpoint /v1/usuarios/me — cerrado 2026-05-09
```

### 4.3 Convención de IDs

```
Formato:  <scope>-<n>
Ejemplos: be-127, fe-205, infra-42, roadmap-12

n incremental por scope. Sin colisiones porque cada agente solo edita
su archivo. Para items roadmap.md, requiere coordinación cruzada
(generar ID via /handoff que centraliza).
```

---

## 5. Identidad de agente en git

### 5.1 agents-config.json

Vive en `.claude/agents-config.json`. Define los agentes del proyecto:

```json
{
  "agents": {
    "backend":  { "email": "backend-agent@<dominio>",  "trailer": "Authored-Agent: backend"  },
    "frontend": { "email": "frontend-agent@<dominio>", "trailer": "Authored-Agent: frontend" },
    "infra":    { "email": "infra-agent@<dominio>",    "trailer": "Authored-Agent: infra"    }
  }
}
```

### 5.2 apply-agent-identity.js

`.claude/apply-agent-identity.js <backend|frontend|infra>` configura
`git config user.email` para la sesión actual e inyecta el trailer
`Authored-Agent:` en los commits.

```bash
node .claude/apply-agent-identity.js backend
# Las siguientes commits del shell llevan:
#   Author: ... (email global del usuario humano)
#   Authored-Agent: backend       ← trailer en el cuerpo del commit
```

**No altera git config global**. Solo modifica la sesión local actual
del shell.

### 5.3 Branch namespace

```
feat/be-<descripcion>         ← rama de feature backend
fix/be-<descripcion>          ← rama de bugfix backend
feat/fe-<descripcion>         ← rama de feature frontend
fix/fe-<descripcion>          ← rama de bugfix frontend
chore/infra-<descripcion>     ← rama de infraestructura
chore/docs-<descripcion>      ← rama de documentación
```

Convención: el prefijo identifica al agente dueño del trabajo. Cada
agente solo abre PRs desde ramas con su prefijo.

---

## 6. Agente message-bus

Sub-agente especializado (`.claude/agents/message-bus.md`). Su trabajo:

1. Leer `docs/messages/{open,archived}/`
2. Construir grafo de threads (in_reply_to)
3. Derivar estado (open / replied / closed)
4. Computar prioridad (labels: blocker → alta; security → alta;
   contract → media; nice-to-have → baja)
5. Filtrar por target del agente activo (`to: <backend|frontend|infra|all>`)
6. Retornar tabla priorizada

**Output esperado** (menos de 30 segundos):

```
| Mensaje | Estado | Prio | Edad | From | Subject |
|---|---|---|---|---|---|
| 2026-05-11-be-to-fe-001 | open | alta | 0d | backend | Contrato usuarios v2 |
| 2026-05-09-fe-to-be-003 | replied | media | 2d | frontend | Pregunta sobre validación |
```

Se invoca al inicio de cada sesión y bajo demanda con `/inbox`.

---

## 7. Skills relacionados

| Skill | Propósito |
|---|---|
| `/status` | Vista única: PRs, mensajes, pendientes, CI |
| `/handoff` | Fin de sesión: genera mensaje en docs/messages/open/ con rama, SHA, archivos, tests, pendientes que deja |
| `/inbox` | Re-check de mensajes nuevos durante sesión larga |

---

## 8. Validación CI

Script `templates/scripts/message-bus-validate.js` corre en CI con
`--strict`:

```
Checks:
  □ Cada mensaje tiene frontmatter completo (from, to, created, subject)
  □ in_reply_to apunta a un archivo existente
  □ closes apunta a archivos existentes
  □ Mensajes en archived/ tienen estado closed derivable
  □ No hay loops en in_reply_to
  □ Fechas en formato ISO 8601

Exit:
  0 → todo correcto
  1 → anomalía detectada (--strict bloquea CI)
```

---

## 9. Cuándo desactivar este skill

Si el proyecto pasa de multi-agente a single-dev (porque se redujo el
equipo o cambió la metodología), desactivar requiere:

1. Cerrar todos los threads en `docs/messages/open/`
2. Mover `docs/messages/` entero a archived/ (preservar historial)
3. Consolidar pendientes split en un solo archivo o eliminar
4. Quitar el llamado a `apply-agent-identity.js` del onboarding
5. Documentar en CHANGELOG que multi-agente queda en standby

**No eliminar los archivos** — preservan trazabilidad histórica.

---

## 10. Restricciones

```
✗ Multi-agente sin bus de comunicación (mensajes + pendientes + agente
  message-bus + script de validación)
✗ Editar mensajes existentes (siempre append-only)
✗ Borrar mensajes (siempre mover a archived/)
✗ Agentes editando archivos de pendientes ajenos (be solo edita backend.md)
✗ Identidad de agente que altere git config global
✗ Multi-agente en proyectos unipersonales (agrega complejidad sin valor)
```

---

## 11. Referencias del dominio (APA 7)

Newman, S. (2019). *Monolith to microservices: Evolutionary patterns to
   transform your monolith*. O'Reilly Media.

Conway, M. E. (1968). How do committees invent? *Datamation, 14*(4), 28–31.
   [Ley de Conway: la arquitectura de un sistema refleja la estructura
   de comunicación de la organización que lo construye.]
