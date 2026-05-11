# Changelog

Todos los cambios relevantes a este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/es/1.1.0/)
y este proyecto adhiere a [Semantic Versioning 2.0.0](https://semver.org/lang/es/).

---

## [Unreleased]

Cambios en preparación que aún no se han publicado en una versión.

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
