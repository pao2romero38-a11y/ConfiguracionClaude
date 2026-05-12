---
name: gestor-de-capacidades
description: >
  Activar AUTOMÁTICAMENTE cuando se detecte que la petición del usuario
  requiere una capacidad que NO está disponible en las herramientas
  actuales — por ejemplo: generación de video, audio, imágenes; OCR
  avanzado; scraping con renderizado de JavaScript; ejecución de modelos
  ML específicos; síntesis de voz; transcripción; conversión de formatos
  no soportados; integración con APIs no instaladas. También activar
  cuando el usuario invoca /capacidad explícitamente para expandir el
  conjunto de herramientas sin estar a mitad de una tarea. NO activar
  cuando la herramienta SÍ existe pero la respuesta sería difícil — solo
  cuando hay una BRECHA real entre lo que se pide y lo que se puede
  hacer con los tools disponibles. El protocolo investiga opciones
  ordenadas por costo creciente (Scripts → CLIs → MCP → APIs), presenta
  un menú multi-opción con comparación de 4 dimensiones (costo · setup ·
  calidad · latencia), instala lo que el usuario apruebe, valida con una
  prueba mínima y registra el resultado en la memoria del usuario para
  evitar re-investigar lo ya resuelto.
  Comandos de activación: /capacidad · [MODO: GESTOR DE CAPACIDADES]
---

# SKILL — Gestor de Capacidades

## 1. Propósito

Cuando Claude detecta que una petición requiere una capacidad fuera de las
herramientas disponibles, **antes de declarar imposibilidad o fallar**, este
protocolo:

1. Diagnostica la brecha con honestidad epistémica
2. Investiga opciones actuales (no fiarse del corte enero 2026 para herramientas)
3. Presenta opciones ordenadas por costo creciente — Scripts → CLIs → MCP → APIs
4. Implementa la opción elegida por el usuario
5. Valida que la nueva capacidad funcione
6. Registra el resultado en la memoria del usuario

Es el cumplimiento operativo de la regla obligatoria de `CLAUDE.md` §9:
*"Antes de declarar que no puedes cumplir una petición, evaluar si el
bloqueo es por falta de herramienta. Si lo es, invocar /capacidad antes
de fallar."*

---

## 2. Cuándo se activa

```
AUTO-ACTIVACIÓN (caso principal):
  Disparador: Claude detecta que la petición requiere una capacidad
              que NO puede cubrir con los tools actuales
              (Bash, Read, Edit, Write, WebSearch, WebFetch, ...)
  Momento:    ANTES de empezar la tarea principal (no después de fallar)
  Acción:     Pausar la tarea principal, ejecutar /capacidad, retornar

INVOCACIÓN MANUAL:
  Disparador: El usuario teclea /capacidad <descripción de la capacidad>
  Momento:    Cuando el usuario quiere expandir capacidades de antemano
              sin estar a mitad de una tarea
  Acción:     Ejecutar el protocolo completo desde el paso 1

CUÁNDO NO ACTIVAR:
  ✗ La capacidad SÍ existe pero la tarea es difícil o larga
  ✗ El usuario solo pregunta "¿podrías hacer X?" sin pedir hacerlo
  ✗ El bloqueo es por permisos o información faltante, no por herramientas
  ✗ La capacidad ya está habilitada (revisar memoria primero)
```

---

## 3. Verificaciones obligatorias ANTES de investigar

- [ ] **¿Cuál es exactamente la capacidad faltante?** Describirla en una frase concreta (no "video" sino "generar video corto narrado a partir de texto").
- [ ] **¿Está ya habilitada y no me di cuenta?** Revisar `MEMORY.md` por entradas `capacidad-*` previas.
- [ ] **¿Confirmé el modelo o tools disponibles?** No asumir; consultar la lista de tools del turno.
- [ ] **¿La brecha es real o es percepción?** Algunas tareas se resuelven combinando tools existentes (ej. `ffmpeg` ya instalado vía Bash).
- [ ] **¿El usuario aprobó el costo de investigar?** Si la tarea original era trivial, preguntar antes de invertir tiempo en `/capacidad`.

---

## 4. Investigación — 4 niveles ordenados por costo creciente

La investigación produce una lista de opciones distribuidas en 4 niveles. Presentar todos los niveles, **incluso si solo hay 1-2 opciones por nivel**, para que el usuario decida según el contexto del proyecto.

```
NIVEL 1 — SCRIPTS HELPER (costo recurrente: cero)
  Combinaciones de tools que YA están en el sistema, orquestadas en un
  script bash/python. Ejemplos:
    · ffmpeg + audios concatenados → video con narración
    · whisper local + texto → transcripción
    · pandoc → conversión entre formatos de documento
  Pros: cero costo, totalmente local, transparente.
  Cons: calidad limitada a herramientas open-source disponibles.

NIVEL 2 — CLIs LOCALES (costo: solo cómputo local)
  Herramientas instalables vía brew / npm / pip / cargo. Ejemplos:
    · whisper.cpp (transcripción)
    · piper-tts (síntesis de voz local)
    · ollama + llama.cpp (LLMs locales)
  Pros: una sola instalación, sin claves, sin recurrencia.
  Cons: consume recursos locales; calidad variable según modelo.

NIVEL 3 — MCP SERVERS (config en settings.json; costo: variable)
  Servidores MCP registrados en .claude/settings.json. Ejemplos:
    · @modelcontextprotocol/server-filesystem (acceso ampliado)
    · Servidores MCP comunitarios para imágenes, audio, etc.
  Pros: integración nativa con Claude Code; tools aparecen automáticamente.
  Cons: depende de mantenimiento del servidor; algunos requieren API key.

NIVEL 4 — APIs EXTERNAS (costo recurrente garantizado)
  APIs comerciales accesibles vía script wrapper. Ejemplos:
    · ElevenLabs (TTS de alta calidad)
    · HeyGen / Synthesia (video sintético con avatar)
    · OpenAI Whisper API / TTS / DALL-E
    · Anthropic API directa para tareas especiales
  Pros: calidad estado del arte; latencia baja.
  Cons: costo por uso; requiere clave; vendor lock-in.
```

**Para cada opción investigada, recopilar:**

| Campo | Detalle |
|---|---|
| Nombre y nivel | Ej. `ffmpeg + whisper.cpp` (Script — combinación de CLIs) |
| Costo recurrente | USD/mes o "cero" |
| Costo por uso | USD/unidad o N/A |
| Costo de setup | Tiempo estimado en minutos |
| Calidad esperada | Alta / media / baja, justificada |
| Latencia | Estimación en segundos por unidad de trabajo |
| Dependencias | Qué hay que instalar antes |
| Riesgos | Vendor lock-in, breaking changes, privacidad |
| Etiqueta de certeza | `[DOCUMENTADO / INFERIDO / ESTIMADO]` per `/inv` |

**Usar `/inv` como apoyo transversal** durante la investigación: las
afirmaciones sobre precios y disponibilidad deben llevar etiqueta de
certeza, especialmente cuando el corte de conocimiento puede estar
desactualizado (`WebSearch` para confirmar precios actuales).

---

## 5. Formato de entrega del análisis

```
## [DIAGNÓSTICO DE BRECHA]
- Capacidad requerida: [frase concreta]
- Tools disponibles relevantes: [lista corta]
- Brecha confirmada: SÍ / probable / NO (en cuyo caso terminar aquí)
- Tarea original pausada: [recordatorio de qué se estaba haciendo]

## [OPCIONES INVESTIGADAS]
Tabla con 1-2 candidatos por nivel (4 niveles), comparando:
| Opción | Nivel | Costo recurrente | Costo setup | Calidad | Latencia | Riesgos |

## [RECOMENDACIÓN]
- Recomendación principal: [opción + nivel + por qué]
- Plan B: [segunda opción si la primera no es viable]
- Justificación contra los 4 ejes: costo · setup · calidad · latencia

## [¿QUÉ INSTALAMOS?]
Pregunta interactiva (AskUserQuestion) con hasta 4 opciones:
  · Instalar recomendación (Opción X — nivel Y)
  · Instalar plan B (Opción Z — nivel W)
  · Mostrar más opciones del nivel preferido por el usuario
  · No instalar nada ahora (cancelar /capacidad y volver a la tarea)
```

---

## 6. Implementación por nivel

Una vez aprobada la opción, ejecutar según su nivel:

```
NIVEL 1 — SCRIPT HELPER
  1. Crear el script en .claude/scripts/<nombre>.sh o .py
  2. Hacer chmod +x si es shell
  3. Documentar uso en cabecera del script
  4. Probar invocación con un input mínimo
  5. (sin cambios en settings.json)

NIVEL 2 — CLI LOCAL
  1. Ejecutar el comando de instalación (brew/npm/pip/cargo)
  2. Verificar instalación con --version
  3. Configurar PATH si es necesario
  4. Probar comando mínimo
  5. (sin cambios en settings.json normalmente)

NIVEL 3 — MCP SERVER
  1. Editar .claude/settings.json (NO settings.local.json salvo para credenciales)
  2. Añadir entrada en "mcpServers"
  3. Si requiere API key, guardarla en variable de entorno o
     .claude/settings.local.json (que está en .gitignore)
  4. Recargar Claude Code o reiniciar para que el servidor cargue
  5. Confirmar que los tools nuevos aparecen

NIVEL 4 — API EXTERNA
  1. Crear cuenta y obtener API key (instrucción al usuario; NO automatizable)
  2. Guardar la key en variable de entorno o .claude/settings.local.json
     (NUNCA en archivos versionados — riesgo de leak)
  3. Crear script wrapper en .claude/scripts/<api>.sh que use la key
  4. Probar con una llamada de costo mínimo
  5. Documentar el costo por llamada para que Claude pueda estimar antes de invocar
```

**Reglas duras de implementación:**

```
✗ NUNCA guardar API keys en archivos versionados en git
✗ NUNCA editar settings.json sin que el usuario haya aprobado la opción específica
✗ NUNCA instalar globalmente cuando una instalación local en el proyecto es suficiente
✗ NUNCA omitir el paso de validación post-instalación
✗ NUNCA implementar más de una opción por ejecución de /capacidad

✓ Privilegiar instalaciones reversibles (no afectar el sistema base si se puede evitar)
✓ Documentar el comando exacto de desinstalación al instalar
✓ Probar con el input más pequeño posible antes de declarar éxito
```

---

## 7. Validación post-instalación

```
PASO 7.1 — Smoke test
  Invocar la nueva capacidad con un input mínimo conocido.
  Ejemplo: si se instaló whisper.cpp, transcribir un audio de 5 segundos.

PASO 7.2 — Comparar con resultado esperado
  ¿La salida tiene el formato y la calidad esperada?
  Si no → reportar al usuario y proponer NIVEL alternativo.

PASO 7.3 — Estimar costo real de uso
  Si la opción es de pago (Nivel 4), calcular costo de un uso típico
  basado en el smoke test y documentarlo.

PASO 7.4 — Reportar al usuario
  "✓ Capacidad <X> habilitada vía <opción>.
   Smoke test: <resultado>.
   Costo estimado por uso típico: <USD>.
   Comando de desinstalación: <cmd>."
```

---

## 8. Registro en memoria del usuario

Después de validar la instalación, **crear una entrada de tipo `reference`** en la auto-memoria del usuario. Esto evita re-investigar la misma capacidad en sesiones futuras.

**Archivo a crear:**

```
/Users/<user>/.claude/projects/<project-slug>/memory/capacidad-<slug>.md

---
name: capacidad-<slug>
description: <una línea: qué capacidad cubre, qué opción se instaló>
metadata:
  type: reference
---

## Capacidad
<frase concreta de qué resuelve>

## Opción instalada
- Nombre: <X>
- Nivel: Script / CLI / MCP / API
- Fecha de instalación: <YYYY-MM-DD>
- Costo recurrente: <USD/mes o "cero">
- Costo por uso: <USD/unidad o N/A>

## Cómo invocar
<comando o snippet de código mínimo>

## Cómo desinstalar
<comando exacto>

## Resultado del smoke test
<una línea: input → output observado>

## Alternativas descartadas
<lista breve de las otras opciones evaluadas, con razón del descarte>
```

**Después de crear el archivo:**

Añadir una línea en `MEMORY.md` bajo una nueva sección si no existe:

```markdown
## Capacidades habilitadas (instaladas vía /capacidad)

- [Capacidad <X>](capacidad-<slug>.md) — <una línea>
```

Esto permite que en futuras sesiones, antes de invocar /capacidad para una
capacidad similar, Claude revise primero si ya está habilitada.

---

## 9. Regreso a la tarea original

Si `/capacidad` se activó AUTOMÁTICAMENTE (no manualmente), después de
validar y registrar:

1. Confirmar al usuario: *"Capacidad habilitada. Retomo la tarea original."*
2. Re-leer la petición original del turno previo
3. Ejecutarla usando la nueva capacidad
4. NO repetir el flujo de `/capacidad` ni la pregunta interactiva

Si `/capacidad` fue invocado MANUALMENTE, terminar después del paso 8 y
esperar a que el usuario haga su próxima petición.

---

## 9 bis. Recetas estándar pre-validadas

Cuando la capacidad solicitada coincide con una **receta estándar**
documentada en esta sección, **omitir los pasos 4 (investigación) y 5
(análisis comparativo)** y ofrecer directamente la receta para
aprobación del usuario. Se preserva la regla dura *"nunca instalar sin
aprobación"* — solo se acelera el camino cuando la solución óptima ya
está validada.

Una receta solo entra a esta sección cuando:

- Ha sido instalada al menos una vez con éxito
- El smoke test pasó
- El usuario expresó conformidad con el resultado
- Los parámetros configurables fueron afinados en uso real

### 9 bis.1 — TTS local en español mexicano (cero costo)

**Disparador:** el usuario pide narración / síntesis de voz en español
mexicano, con cero costo recurrente, calidad media-alta suficiente para
capacitación interna o uso personal.

**Receta validada (mayo 2026):**

```
Nivel:        2 — CLI local
Motor:        piper-tts 1.4.2 (pip install --user piper-tts)
Voz:          es_MX-claude-high (modelo neural, ~60 MB)
Dependencias: ffmpeg (brew install ffmpeg)
              espeak-ng (brew install espeak-ng)  ← requerido por piper
Wrapper:      .claude/scripts/narrar.py (en este repo)

Parámetros estándar:
  LENGTH_SCALE        = 1.08    (ritmo pedagógico)
  SENTENCE_SILENCE    = 0.35    (silencio entre frases, segundos)
  INTER_BLOCK_SILENCE = 1.5     (silencio entre bloques narrativos)

Diccionario de pronunciación inglesa incluido en narrar.py:
  Claude → Clod · ROI → ar óu ai · WACC → uak · DCF → di si ef
  IFRS → ai ef ar es · PMBOK → pimbok · GAAP → gap
  retail · online · software · hardware · prompt · feedback · stack
  Bloom · Kirkpatrick · Ausubel · Anderson · Krathwohl · Merrill
```

**Bug conocido a parchar durante install:**

Algunos `.onnx.json` traen `phoneme_type: "PhonemeType.ESPEAK"` literal.
piper-tts espera `"espeak"` (lowercase string). Parchar antes de invocar:

```python
import json
p = '/Users/<user>/.local/share/piper/voices/<voz>.onnx.json'
with open(p) as f: d = json.load(f)
if d.get('phoneme_type', '').startswith('PhonemeType.'):
    d['phoneme_type'] = 'espeak'
    with open(p, 'w') as f: json.dump(d, f)
```

**Smoke test estándar:**

```bash
echo "Hoy aprendes una técnica nueva. Sin instalar nada, sin programar." | \
  ~/Library/Python/3.9/bin/piper \
  -m ~/.local/share/piper/voices/es_MX-claude-high.onnx \
  --length-scale 1.08 --sentence-silence 0.35 \
  -f /tmp/smoke.wav
afplay /tmp/smoke.wav
```

**Cuándo aplica esta receta:**

- ✓ macOS con Homebrew disponible
- ✓ Usuario quiere español (México) o español-neutro
- ✓ Calidad media-alta es suficiente
- ✗ Linux/Windows → comandos cambian (investigar)
- ✗ Idioma distinto al español → cambiar voz (investigar)
- ✗ Calidad estado del arte requerida → ir a Nivel 4 (APIs comerciales)
- ✗ Volumen muy alto (> 1 hora de audio por día) → reconsiderar costo de cómputo local

**Validación de la receta:**

Producida la serie "serie-mejora-continua" (7 episodios, ~38 min total,
50 bloques individuales, ~97 MB de audio). Tiempo de setup completo:
~25 min (incluye debug del bug del JSON y descarga del modelo).

**Memoria asociada:**

Tras instalar, registrar en `MEMORY.md` como `capacidad-tts-local-es`
siguiendo la plantilla del §8 (Registro en memoria del usuario).

### 9 bis.3 — Sincronización de biblioteca local con documentos en dominio público (cero costo)

**Disparador:** el usuario quiere tener acceso offline a las leyes,
normas y guías oficiales del catálogo `library/CATALOG.yaml` que están
en dominio público (LFPDPPP, NIST CSF, NOMs SSA, OECD, UN SDGs, etc.).

**Receta validada (mayo 2026):**

```
Nivel:        1 — Script helper (sin instalación adicional; usa stdlib)
Wrapper:      .claude/scripts/descargar-publicos.py
Dependencias: pyyaml (ya instalado por receta §8 — biblioteca-sync.py)

Filtro:       Solo entradas con license == "public_domain" Y url_oficial
              que apunta a recurso descargable directamente. NUNCA descarga
              copyrighted (ISO, AICPA, libros de editores, NIF MX, etc.).

Destino:      library/local/<id>.<ext>
              · library/local/ está en .gitignore — copia personal del usuario
              · No se sube al repo
```

**Tres modos del script:**

```bash
# 1) Listar qué se descargaría (default, no toca disco)
python3 .claude/scripts/descargar-publicos.py --dry-run

# 2) Descargar
python3 .claude/scripts/descargar-publicos.py --download

# 3) Reporte de cobertura local (qué hay en disco vs en catálogo)
python3 .claude/scripts/descargar-publicos.py --report
```

**Cuándo aplica esta receta:**

- ✓ Usuario quiere acceso offline a marcos legales mexicanos vigentes
- ✓ Usuario consulta frecuentemente normas NIST / OECD / UN
- ✓ Usuario trabaja en zonas con conectividad inestable
- ✗ Para documentos copyrighted (ISO, libros, NIF) — adquirir
  legalmente por separado y configurar mapeo manual en
  `~/.config/biblioteca-local.yaml` (ver receta §8 — biblioteca-sync.py)

**Validación de la receta (al corte mayo 2026):**

- 46 entradas marcadas como descargables en el catálogo (de ~108 totales).
- Concentradas en: regulacion-mx (todas las leyes federales + NOMs +
  sectoriales), seguridad-cumplimiento (NIST CSF, NIST SP 800-30/53),
  ia-gobernanza (NIST AI RMF, OECD, UNESCO, EU AI Act, UN SDGs).
- Los sitios oficiales mexicanos (diputados.gob.mx, dof.gob.mx, sat.gob.mx)
  responden a User-Agent estándar; los URLs de listado (sin .pdf en
  el path) requieren navegación manual y se reportan como fallidos.

**Memoria asociada:**

Tras el primer `--download` exitoso, registrar en `MEMORY.md` como
`capacidad-biblioteca-local` siguiendo la plantilla del §8.

### 9 bis.2 — Render de slides + composición video sincronizado con audio (cero costo)

**Disparador:** el usuario tiene una serie de capacitación con audio
narrado producido y quiere generar el video final con slides
sincronizados al audio. La sincronización slide ↔ audio es obligatoria.

**Receta validada (mayo 2026):**

```
Nivel:              2 — CLI local
Motor de slides:    marp-cli 4.4.0  (npm install -g @marp-team/marp-cli)
Composición video:  ffmpeg (ya instalado por la receta §9 bis.1)
Dependencias adic:  Google Chrome o Chromium (Marp lo usa para render)
                    Node.js + npm (verificar disponibilidad antes)

Wrappers:           .claude/scripts/slides.py     (render PNG por slide)
                    .claude/scripts/componer.py   (audio + slides → mp4)

Parámetros estándar (en componer.py):
  WIDTH                 = 1280
  HEIGHT                = 720
  FPS                   = 30
  TOLERANCE_HARD        = 0.30  (audio vs declarado)

Sincronización:
  Todos los slides de contenido se ESCALAN PROPORCIONALMENTE para que
  la suma de sus duraciones iguale exactamente la duración real del audio.
  El slide de Conclusiones (opcional) se añade DESPUÉS del audio con
  duración fija de 8 segundos.
```

**Diseño visual de slides** (editorial cream + acento cálido, embebido en
`slides.py`):

- Fondo: gradiente cream `#f7f3ed → #ede4d3`
- Texto principal: serif `Georgia` para títulos, sans para cuerpo
- Acento: `#c8553d` (terracota cálido)
- Cita de remate `[ÉNFASIS]`: italic en serif con borde izquierdo terracota
- Número de slide: esquina inferior derecha, solo el número (sin "Nº" ni total)
- Nombre del episodio: esquina superior izquierda, solo el título
- Slide de conclusiones: mismo tema con borde superior terracota +
  bullets numerados en círculos
- Comparativa lado a lado: dos paneles con colores diferenciados

**Pipeline completo para producir un video desde el markdown del episodio:**

```bash
# 1) Audio (receta §9 bis.1)
python3 .claude/scripts/narrar.py training/<serie>/<episodio>.md

# 2) Slides (esta receta)
python3 .claude/scripts/slides.py training/<serie>/<episodio>.md

# 3) Composición video
python3 .claude/scripts/componer.py training/<serie>/<episodio>.md
```

Produce:

- `training/<serie>/audio/<episodio>-completo.wav`
- `training/<serie>/slides-render/<episodio>/slide-NN.png` + `timing.json`
- `training/<serie>/video/<episodio>.mp4` (~5-6 MB por episodio de 5-6 min)

**Sincronización obligatoria:**

El composer valida que la diferencia entre audio real y duración
declarada de slides no supere `TOLERANCE_HARD` (30 %). Por encima,
error explícito: corregir las duraciones del markdown. Por debajo, el
escalado proporcional absorbe la diferencia sin que el usuario lo note.

**Cuándo aplica esta receta:**

- ✓ macOS / Linux con Node.js + npm + Google Chrome (o Chromium)
- ✓ Episodios con tabla `# === ESTRUCTURA DE SLIDES ===` y duraciones declaradas
- ✓ Tema cream editorial encaja con capacitación profesional
- ✗ Si se requiere video con avatares humanos → Nivel 4 (HeyGen/Synthesia)
- ✗ Si se requiere animaciones complejas (no slides estáticos) → otro tooling

**Validación de la receta:**

Producidos los 7 videos de la serie "serie-mejora-continua":

- 74 slides totales · ~3.3 MB
- 7 videos mp4 · ~37 MB · ~38 min total
- Sincronización slide ↔ audio con escalado proporcional (factor 0.77–0.96 según episodio)
- Tiempo de setup completo: ~5 min (npm install marp-cli)

---

## 10. Restricciones no negociables

```
✗ NUNCA implementar sin que el usuario haya aprobado la opción específica
✗ NUNCA omitir la validación post-instalación
✗ NUNCA omitir el registro en MEMORY.md
✗ NUNCA guardar API keys en archivos versionados
✗ NUNCA recomendar Nivel 4 (API externa) cuando una opción de nivel 1-3
  cubre el caso de uso con calidad aceptable
✗ NUNCA inventar precios o disponibilidad — usar WebSearch para confirmar
✗ NUNCA modificar settings.json sin mostrar el diff al usuario primero

✓ Privilegiar siempre el nivel más bajo que cumpla el requisito de calidad
✓ Documentar TODO: comando de instalación, desinstalación, uso, costo
✓ Si la investigación toma más de 3 búsquedas web, pausar y preguntar al
  usuario si quiere seguir invirtiendo tiempo
```

---

## 11. Referencias del dominio (APA 7)

Anthropic. (2024). *Model Context Protocol specification*. Anthropic.
    https://modelcontextprotocol.io/

Anthropic. (2024). *Claude Code documentation — MCP integration*. Anthropic.
    https://docs.anthropic.com/en/docs/claude-code/mcp

OpenAI. (2024). *OpenAI API pricing*. OpenAI.
    https://openai.com/api/pricing/

Hunt, A., & Thomas, D. (1999). *The pragmatic programmer: From journeyman
    to master*. Addison-Wesley. [capítulos sobre "tool building" como
    inversión incremental en productividad]
