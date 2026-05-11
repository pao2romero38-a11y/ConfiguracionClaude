# Changelog

Todos los cambios relevantes a este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/es/1.1.0/)
y este proyecto adhiere a [Semantic Versioning 2.0.0](https://semver.org/lang/es/).

---

## [Unreleased]

Cambios en preparación que aún no se han publicado en una versión.

---

## [2.0.0] — 2026-05-11

Primera ronda de refactor sobre la configuración heredada. Cambios
estructurales en `CLAUDE.md` y correcciones transversales en skills.

### Added

- **CLAUDE.md §1.1 — Principio de no-trivialidad.** Regla explícita que
  documenta el alcance del proyecto: configuración para trabajo profesional
  especializado, no para consultas triviales. Para preguntas casuales,
  Claude debe sugerir abrir una sesión sin esta configuración.
- **CLAUDE.md §4 bis — Composición de modos.** Nuevas reglas para combinar
  varios modos en un mismo prompt usando el patrón "líder + apoyo".
  Define sintaxis (`/lider +apoyo1 +apoyo2`), 6 reglas de composición
  (verificaciones unificadas, referencias fundidas, advertencias
  concatenadas, máximo 3 skills), y 7 combinaciones recomendadas.
  Resuelve comportamiento previamente indefinido al invocar modos múltiples.

### Changed

- **CLAUDE.md §5 — De especificación duplicada a índice delgado.** La
  versión anterior duplicaba literalmente el contenido de cada SKILL.md
  (~690 líneas, ~40 KB). Ahora §5 es un índice que apunta a
  `.claude/skills/<modo>/SKILL.md` como única fuente de verdad. Reduce
  `CLAUDE.md` de 1273 a 724 líneas (-43%), libera ~30 KB de contexto en
  cada sesión, y elimina riesgo de desincronización entre las dos copias.
- **CLAUDE.md — Marcador de versión.** Eliminada la referencia "v2.1"
  del encabezado y el pie. La versión vigente ahora se gobierna desde
  el archivo `VERSION` en la raíz del repo (SemVer).
- **CLAUDE.md §10 — Contexto del proyecto.** Yaml actualizado para
  reflejar la identidad nueva del repo (`ConfiguracionClaude`), audiencia
  profesional, gobierno y referencia a `GOVERNANCE.md` y `VERSION`.
- **CLAUDE.md §11 — Mensaje de inicio de sesión.** Reemplazado para
  referenciar `VERSION` en vez de marca interna estática, y mencionar
  la disponibilidad de §4 bis (composición).

### Fixed

- **Corte temporal de conocimiento — `ago 2025` → `enero 2026`.**
  Actualizadas 8 ocurrencias en 3 archivos: `CLAUDE.md` (4 lugares),
  `.claude/skills/inv/SKILL.md` (3 lugares),
  `.claude/skills/dev-test/SKILL.md` (1 lugar). El modelo activo de
  Claude tiene corte enero 2026; la marca anterior estaba desfasada
  5 meses respecto al modelo en uso.
- **`.claude/skills/README.md` — Conteo de skills.** Corregido el
  encabezado de "20 skills" a "21 skills" (8 dev-* + 13 dominio), que
  ya era correcto en el pie de página y coincide con los directorios
  reales en `.claude/skills/`.

### Criterios de las decisiones

Los cambios siguen los criterios formalizados en la sesión de revisión
previa al refactor:

1. **Eliminar duplicación** entre `CLAUDE.md` y los `SKILL.md` (deuda
   técnica identificada como la principal en la evaluación inicial).
2. **Documentar reglas implícitas** (principio de no-trivialidad,
   composición de modos) que hasta ahora vivían solo en la cabeza del
   mantenedor.
3. **Alinear con el modelo activo** (corte temporal correcto).
4. **No tocar los SKILL.md** salvo para correcciones puntuales: el
   contenido especializado se respeta y queda como única fuente de verdad
   de cada dominio.

### Beneficios medibles

- Tamaño de contexto cargado en cada sesión: **-43%** en `CLAUDE.md`.
- Fuentes de verdad para cada modo: **2 → 1** (elimina riesgo de divergencia).
- Reglas para combinar modos: **indefinido → 6 reglas + 7 ejemplos**.
- Coherencia temporal: **5 meses de desfase → 0**.
- Conteo de skills: **inconsistente (20 vs 21) → 21 en todos lados**.

---

## [1.0.0] — 2026-05-11

### Added

- **Documentación inicial del proyecto:**
  - `README.md` con origen, audiencia, quick start y estructura.
  - `USAGE.md` con tres opciones de instalación (clon como base, copia a
    proyecto existente, instalación global) y verificación de configuración.
  - `CONTRIBUTING.md` con alcance, criterios de aceptación, flujo Git y
    plantilla de PR.
  - `GOVERNANCE.md` con roles, proceso de decisión, política SemVer y
    cadencia de releases.
  - `CHANGELOG.md` (este archivo).
  - `VERSION` con la versión vigente en formato SemVer.
  - `.gitignore` para excluir ruido de macOS y archivos de editores.

### Notes

Esta versión establece la base documental del proyecto sobre la
configuración importada en `v1.0.0-baseline`. No modifica la configuración
en sí (CLAUDE.md ni SKILL.md). La primera ronda de refactor se publica
en v2.0.0.

---

## [1.0.0-baseline] — 2026-05-11

### Added

- **Configuración importada desde ConfiguracionAI:**
  - `CLAUDE.md` v2.1 con 14 modos de operación (4 core + 10 dominio).
  - 21 skills bajo `.claude/skills/`:
    - **Programación (8):** `/dev` `/dev-api` `/dev-clean` `/dev-db`
      `/dev-docker` `/dev-git` `/dev-modes` `/dev-test`.
    - **Dominio (13):** `/edu` `/inv` `/fin` `/mkt` `/tec` `/proy`
      `/seg` `/rsk` `/ci` `/aud` `/dis` `/cost` `/tra`.
  - `.claude/skills/README.md` con índice de skills.

### Notes

Punto de partida del repositorio. Copia literal de `ConfiguracionAI/`
sin modificaciones. Este tag se preserva como referencia histórica del
estado inicial.

---

## Criterios de versionado (resumen)

```
MAYOR (X.0.0) — Cambios incompatibles
MENOR (1.X.0) — Funcionalidad nueva compatible
PATCH (1.0.X) — Correcciones sin cambio funcional
```

Detalle completo en [`GOVERNANCE.md`](GOVERNANCE.md) §3.

---

*Mantenido por el mantenedor del repo. Todo cambio publicado pasa por el
proceso descrito en `GOVERNANCE.md`.*
