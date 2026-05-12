# `training/` — Materiales de capacitación complementarios

Esta carpeta contiene **materiales de capacitación** sobre cómo usar la
configuración base de Claude de este repositorio.

Es complementaria a la configuración del repo: la documentación bajo
`.claude/skills/` y `CLAUDE.md` **define** las técnicas; los materiales
aquí **enseñan a usarlas**.

---

## Series disponibles

### `serie-mejora-continua/`

Mini-serie de 7 episodios sobre cómo usar Claude para configurar y mejorar
progresivamente la propia configuración de Claude.

| Dimensión | Especificación |
|---|---|
| Audiencia | Profesional que parte de cero en configuración de Claude |
| Duración | ~38 min total (7 episodios de 4-7 min) |
| Pedagogía | Aprendizaje significativo (Ausubel), Bloom, Kirkpatrick |
| Idioma | Español (México), términos técnicos en inglés |
| Estado | v1 — producida y validada |

Cada episodio contiene:

- 10 secciones del formato `/edu` (panorama, activación, concepto central, analogía, ejemplo real, competencia en acción, actividad integradora, evaluación, transferencia, referencias)
- Script de narración cronometrado en bloques (130-140 wpm en español)
- Estructura de slides con duraciones
- Notas de producción + checklist de 4 pilares pedagógicos

---

## Producción de audio

Los archivos `.wav` no están versionados (`.gitignore`). Se regeneran a
partir de los markdown con el wrapper `narrar.py` del repo:

```bash
# 1) Habilitar capacidad TTS local (una sola vez)
#    Ver: .claude/skills/capacidad/SKILL.md §9 bis.1
pip install --user piper-tts
brew install ffmpeg espeak-ng

# 2) Descargar modelo de voz es_MX-claude-high (60 MB) en
#    ~/.local/share/piper/voices/  — ver la receta estándar para URL exacta.

# 3) Parchar bug del JSON si aplica (phoneme_type: "PhonemeType.ESPEAK" → "espeak")

# 4) Producir un episodio
python3 .claude/scripts/narrar.py training/serie-mejora-continua/episodio-0-por-que-configurar.md
```

`narrar.py` lee la sección `# === SCRIPT DE NARRACIÓN ===` del markdown,
respeta los marcadores `[PAUSA Ns]`, aplica el diccionario de pronunciación
inglesa (Claude → Clod, ROI → ar óu ai, etc.) y produce dos entregables:

- `audio/<episodio>/bloque-NN.wav` — un wav por bloque (iteración granular)
- `audio/<episodio>-completo.wav` — episodio concatenado, listo para publicar

---

## Roadmap de producción

Lo que ya está validado: **audio narrado**. Lo que sigue como complementos
naturales:

### Slides renderizados (próxima ronda de `/capacidad`)

Cada episodio markdown ya trae la sección `# === ESTRUCTURA DE SLIDES ===`
con una tabla de slides, duración y notas. Falta el paso de render visual.

Niveles posibles (siguiendo el patrón Scripts → CLIs → MCP → APIs):

| Nivel | Opción | Costo | Esfuerzo |
|---|---|---|---|
| 1 — Script | Generar slides en Markdown puro y exportar con `marp` o `reveal.js` | cero | bajo |
| 2 — CLI | `pandoc` con plantilla Beamer → PDF imprimible / proyectable | cero | bajo |
| 3 — MCP | Servidor MCP de generación de imágenes para diagramas y analogías | variable | medio |
| 4 — API | Herramientas comerciales de slides automatizados (Tome, Beautiful.ai) | recurrente | bajo |

Cuando se quiera producir slides, invocar `/capacidad` con la descripción de la
brecha y la skill propondrá la receta. Si se acuerda una receta estándar (como
se hizo con TTS), se documenta en `.claude/skills/capacidad/SKILL.md` §9 bis.

### Composición final video mp4 (con slides sincronizados al audio)

Una vez con audio + slides, el último paso es la composición. ffmpeg ya está
instalado tras la receta de TTS. El script de composición es un nuevo wrapper
en `.claude/scripts/` (por hacer) que toma:

- `audio/<episodio>-completo.wav`
- `slides-render/<episodio>/*.png` (o pdf convertido a png)
- Tabla de slides del markdown con duraciones

Y produce `video/<episodio>.mp4`.

**Requisito obligatorio: sincronización slide ↔ audio.**

Los slides deben aparecer EN ORDEN y al mismo tiempo que se va explicando
el contenido en el audio — no antes, no después. La sincronización se
deriva automáticamente del markdown porque ambos componentes comparten el
mismo eje temporal:

```
Sección del markdown                Datos de sincronización
─────────────────────────────────   ────────────────────────────────
## Bloque N — Título (0:30 — 1:15)  ← timing del audio narrado
| Slide M | ... | 0:30 — 1:15 |     ← timing del slide visible
```

El script de composición:

1. Lee la tabla de slides del markdown (`# === ESTRUCTURA DE SLIDES ===`).
2. Para cada slide, calcula `inicio` y `fin` en segundos.
3. Genera segmentos de video por slide con duración = `fin − inicio`.
4. Concatena los segmentos en orden estricto.
5. Mezcla con el audio del episodio.
6. Valida que `duración_total_slides ≈ duración_total_audio` (±2 % de tolerancia). Si no coinciden, error explícito en consola — no producir un video desincronizado.

La invariante de diseño es: **un solo eje temporal por episodio, derivado
del markdown**. No hay "ajuste manual de tiempos" en el flujo — si los
slides y el audio no calzan, se corrige el markdown, no el render.

### Subtítulos automáticos

Los scripts de narración son el ground truth. Generar `.srt` por bloque
a partir del markdown es un script de ~30 líneas. Pendiente.

---

## Contribuir nuevas series

Si quieres aportar una serie de capacitación nueva, propuesta general:

1. Crear carpeta `training/<nombre-serie>/`
2. Diseño maestro `00-DISEÑO-SERIE.md` con audiencia, objetivos Bloom, estructura de episodios, plan Kirkpatrick.
3. Un archivo por episodio siguiendo el formato del skill `/edu` (10 secciones obligatorias).
4. Validar con la rúbrica de 4 pilares (activación, anclaje, organización, aplicación) — está en cada archivo de episodio como sección final.
5. Smoke test produciendo el audio del Ep 0 antes de seguir con los demás.
6. PR a este repo describiendo el caso de uso y la audiencia objetivo.

### Series complementarias propuestas (huecos detectados)

- **`serie-onboarding-equipo`** — cómo equipos compartidos adoptan esta configuración (governance, conventions, branch namespace)
- **`serie-modos-por-dominio`** — un módulo por modo experto (`/fin`, `/seg`, `/edu`, ...) profundizando en el dominio respectivo
- **`serie-modo-personalizado`** — recorrido paso a paso para diseñar un modo experto propio desde cero
- **`serie-otra-configuracion`** — cómo derivar este repo para construir una configuración de Claude con otro propósito (ej. consultoría legal, investigación científica, salud) preservando las invariantes (APA 7, protocolo de calidad, 4 pilares pedagógicos)

Cada serie nueva amplía el valor de la configuración base sin acoplarse a
ella — la base puede evolucionar y las series se actualizan en su propio
ritmo. Ese es el modelo de complementos del repo.

---

## Cómo este material se relaciona con el resto del repo

| Archivo / carpeta | Rol |
|---|---|
| `CLAUDE.md` | Configuración base: reglas, modos, presentación, citación |
| `.claude/skills/<modo>/SKILL.md` | Definición operativa de cada modo |
| `.claude/scripts/narrar.py` | Wrapper que ESTA carpeta usa para producir audio |
| `training/<serie>/*.md` | Material que ENSEÑA a usar lo anterior |
| `templates/` | Plantillas de proyecto que CONSUMEN la configuración |

Los cuatro niveles son distintos y no deben confundirse:
**configuración → operativa → enseñanza → consumo en proyectos nuevos**.
