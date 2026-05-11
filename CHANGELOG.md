# Changelog

Todos los cambios relevantes a este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/es/1.1.0/)
y este proyecto adhiere a [Semantic Versioning 2.0.0](https://semver.org/lang/es/).

---

## [Unreleased]

Cambios en preparación que aún no se han publicado en una versión.

---

## [2.1.0] — 2026-05-11

Primera adición de una nueva familia de skills al repo. Bump MINOR
(funcionalidad nueva compatible con la versión anterior).

### Added

- **Familia `/ai` con 3 skills.** Cubre los tres perfiles profesionales
  reales del campo de IA, siguiendo el patrón de la familia `/dev`
  (un skill principal + sub-skills por sub-dominio):

  - **`/ai` — Experto en IA (estrategia y gobierno).**
    Casos de uso, ROI/TCO, vendor selection, build vs. buy vs. partner,
    marcos regulatorios (EU AI Act 2024, NIST AI RMF 1.0 + GenAI Profile
    2024, ISO/IEC 42001:2023), AI literacy, hoja de ruta de adopción.
    Audiencia: AI lead, director, consultor, PM, arquitecto.

  - **`/ai-llm` — Aplicaciones de LLMs.**
    Prompt engineering, RAG, agentes, selección de modelo
    (Claude/GPT/Gemini/open source), evaluación (golden datasets,
    LLM-as-judge, benchmarks), mitigación de prompt injection y jailbreaks.
    Incluye jerarquía de técnicas (prompting → few-shot → CoT → RAG →
    agents → fine-tuning) con regla de escalamiento solo ante fallo.
    Audiencia: ML engineer con LLMs, prompt engineer, agent builder.

  - **`/ai-ml` — ML / MLOps.**
    Ciclo de vida del modelo, detección de drift (datos y concepto),
    monitoring en producción, feature stores, A/B testing, retraining.
    Define los **8 componentes obligatorios** de un sistema ML productivo
    (heurística: si faltan componentes, no está en producción, está en
    "demo permanente con tráfico real"). Referencia Sculley et al.
    (2015) sobre deuda técnica oculta en ML.
    Audiencia: ML engineer tradicional, MLOps engineer, data scientist
    productivo.

- **Combinaciones de modos recomendadas con IA** (en CLAUDE.md §4 bis):
  - `/ai +tec` — Estrategia de adopción de IA en una organización
  - `/ai +seg +rsk` — Evaluación de riesgo de un sistema de IA en producción
  - `/ai +ci` — Controles internos para uso de IA generativa
  - `/ai-llm +dev` — Implementación técnica de aplicación con LLMs
  - `/ai-ml +dev-test` — ML con cobertura de pruebas y eval suite

### Changed

- **`CLAUDE.md` §4 (tabla de modos):** 3 filas nuevas para `/ai`,
  `/ai-llm`, `/ai-ml`.
- **`CLAUDE.md` §5 (índice de skills):** 3 filas nuevas y total
  actualizado a 24 skills.
- **`CLAUDE.md` §10 (yaml):** `modos_disponibles` 14 → 17,
  `skills_total` 21 → 24, nueva sub-categoría `ia: [ai, ai-llm, ai-ml]`.
- **`CLAUDE.md` §11 (mensaje de inicio):** nueva fila "IA:" en la lista
  de modos disponibles.
- **`CLAUDE.md` §12 (comandos rápidos):** 3 filas nuevas.
- **`CLAUDE.md` pie de página:** "14 modos · 21 skills" → "17 modos · 24 skills".
- **`.claude/skills/README.md`:** nueva sección "Skills de IA (3)",
  conteo 21 → 24, footer actualizado a la identidad del proyecto.
- **`README.md` raíz:** familia "Inteligencia Artificial" agregada
  a la tabla de modos, conteo "21 skills" → "24 skills", "14 dominios"
  → "17 dominios".
- **`GOVERNANCE.md`:** "14 dominios" → "17 dominios" en el rol Contribuidor.

### Criterios de las decisiones

1. **Tres skills, no uno.** Cubrir los tres perfiles profesionales reales
   (estratega / LLM engineer / MLOps) en archivos separados respeta el
   patrón de la familia `/dev` y permite que cada usuario active solo el
   skill relevante a su trabajo del día.
2. **Audiencia profesional confirmada.** Lenguaje técnico, terminología
   sin simplificar, sin disclaimers patronizantes — solo advertencia de
   evolución rápida del campo.
3. **Sin implicaciones legales especiales** (a diferencia de `/med` y
   `/psi`), por lo que no se introducen protocolos de seguridad
   adicionales. Sí se mantienen advertencias estándar de no-asesoría
   legal/regulatoria.
4. **Marcos de referencia vigentes:** EU AI Act 2024, NIST AI RMF 1.0
   + GenAI Profile 2024, ISO/IEC 42001:2023, OWASP Top 10 for LLM
   Applications 2025.

### Beneficios medibles

- Cobertura de dominio: **14 → 17 dominios** (+21%).
- Skills totales: **21 → 24** (+14%).
- Profesionales de IA atendidos: **0 → 3 perfiles claros** (estratega,
  LLM engineer, MLOps engineer).

### Pendiente

- `/med` y `/psi` postergados — requieren cierre de alcance y validación
  de protocolos de derivación. Se agregarán en una iteración futura.
- `LICENSE` sigue pendiente; el repo es público bajo "all rights reserved"
  implícito hasta que se agregue.

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
