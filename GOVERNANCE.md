# GOVERNANCE — Modelo de decisión y versionado

Este documento describe **quién decide qué** sobre los cambios al repo
y **cómo se versiona** cada aprobación.

---

## 1. Roles

### Mantenedor
- Una persona (autor original del repo) o el equipo designado.
- Aprueba o rechaza todo PR.
- Conduce la revisión usando una sesión de Claude Code como espacio
  estructurado de evaluación.
- Tiene última palabra sobre cambios al `CLAUDE.md` raíz.

### Contribuidor
- Especialista en al menos uno de los 14 dominios cubiertos.
- Propone mejoras al `SKILL.md` de su área via PR.
- Documenta justificación profesional y fuentes APA 7.
- No autoriza merges propios.

### Revisor por dominio (rol futuro)
- Si un dominio acumula contribuciones frecuentes, el mantenedor puede
  delegar la revisión técnica a un especialista de confianza en ese dominio.
- El mantenedor conserva la autorización final del merge.

---

## 2. Proceso de decisión

```
┌──────────────────────────────────────────────────────────────────┐
│  Contribuidor abre PR                                            │
│         ↓                                                        │
│  Mantenedor abre sesión de Claude Code para revisar              │
│         ↓                                                        │
│  Verificación contra criterios de CONTRIBUTING.md §2             │
│         ↓                                                        │
│  Decisión documentada como comentario en el PR:                  │
│    a) Aceptado          → merge + versión + CHANGELOG            │
│    b) Aceptado c/cambios → comentarios → contribuidor itera      │
│    c) Rechazado         → justificación contra criterios         │
│         ↓                                                        │
│  Si aceptado: ejecución de release (ver §3)                      │
└──────────────────────────────────────────────────────────────────┘
```

### Criterios de decisión (resumen — ver CONTRIBUTING §2 para detalle)

1. ¿El cambio mejora demostrablemente el SKILL del modo correspondiente?
2. ¿Las fuentes citadas son verificables y vigentes?
3. ¿Está alineado con los principios del CLAUDE.md (estructura, APA 7,
   marcadores de certeza)?
4. ¿No introduce ceremonia para casos triviales?
5. ¿No genera inconsistencia con otros skills del mismo dominio?

Si los 5 son sí: aceptar.
Si alguno requiere ajuste menor: aceptado con cambios.
Si alguno falla en lo fundamental: rechazar con justificación.

---

## 3. Versionado — SemVer

Se usa **Semantic Versioning 2.0.0** (https://semver.org).

```
MAYOR . MENOR . PATCH

MAYOR (X.0.0)  — Cambios incompatibles:
  · Eliminación o renombrado de un modo existente
  · Cambio estructural al frontmatter de los SKILL.md
  · Modificación de las reglas globales del CLAUDE.md raíz
  · Cambio al modelo de gobierno

MENOR (1.X.0)  — Funcionalidad nueva compatible:
  · Nuevo skill agregado
  · Nueva sección o capacidad en un skill existente
  · Nuevas combinaciones de modos documentadas

PATCH (1.0.X)  — Correcciones sin cambio funcional:
  · Corrección de referencias APA 7 desactualizadas
  · Typos
  · Aclaraciones a ejemplos existentes
  · Actualización del año de una norma sin cambio en su contenido aplicado
```

### Bump de versión

Al aceptar un PR, el mantenedor:

1. Decide el tipo de bump (mayor / menor / patch).
2. Actualiza el archivo `VERSION` (formato `X.Y.Z\n`).
3. Mueve la entrada del PR de `## [Unreleased]` a `## [X.Y.Z] — YYYY-MM-DD`
   en `CHANGELOG.md`.
4. Crea un tag anotado: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
5. Push del merge + tag.

---

## 4. Cadencia de releases

- **No hay calendario fijo.** Cada PR aprobado genera una nueva versión.
- **Agrupación de PRs:** si varios PRs se aprueban en la misma sesión,
  pueden agruparse en una sola versión menor (X.Y.0) en vez de generar
  varios bumps de patch consecutivos.
- **Hotfix:** correcciones críticas (ej. una referencia legal incorrecta
  con implicaciones) se publican inmediatamente como patch.

---

## 5. Historial de versiones

Mantenido íntegramente en `CHANGELOG.md` con formato
**Keep a Changelog** (https://keepachangelog.com/es/1.1.0/).

Cada entrada incluye:
- Versión y fecha
- Cambios agrupados por tipo: `Added` / `Changed` / `Fixed` / `Removed`
- Autor del PR cuando aplique
- Referencia al PR/commit cuando esté disponible

---

## 6. Resolución de conflictos

Si dos PRs compiten por el mismo cambio:

1. El mantenedor revisa ambos en la misma sesión.
2. Decide cuál cumple mejor los criterios.
3. El rechazado recibe justificación; el autor puede enviar una versión
   revisada que tome elementos del aceptado si aplica.

Si un contribuidor disiente de un rechazo: puede abrir un issue de
discusión. El mantenedor responde en la siguiente sesión de revisión.
La decisión final del mantenedor no es apelable dentro del repo —
si el desacuerdo es estructural, el contribuidor puede hacer su propio
fork.

---

## 7. Cambios a este documento

Modificaciones a `GOVERNANCE.md`:
- Requieren bump mayor de versión (afectan reglas del juego).
- Pasan por PR como cualquier otro cambio.
- Solo el mantenedor puede autorizarlas.

---

*Las reglas pueden evolucionar. Esta versión refleja el modelo al
momento del release v1.0.0.*
