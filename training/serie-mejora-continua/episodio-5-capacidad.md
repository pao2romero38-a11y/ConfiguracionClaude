---
episodio: 5
titulo: "/capacidad — expandir lo que Claude PUEDE hacer"
duracion_objetivo_min: 6-7
concepto_central: "El sistema no es fijo; las herramientas se pueden expandir en 4 niveles ordenados por costo"
analogia_principal: "Añadir aplicaciones a tu smartphone"
bloom: 6 — Crear
prerequisitos: Episodios 0, 1, 2, 3, 4
artefacto_producido: "Solicitud documentada de una capacidad nueva, con propuesta de nivel de implementación"
---

# Episodio 5 — `/capacidad`: expandir lo que Claude PUEDE hacer

> **Función en la serie:** la segunda meta-skill, dual a `/prompt`.
> Si `/prompt` mejora lo que el usuario pide, `/capacidad` mejora lo
> que Claude puede ejecutar. Es la mirada al techo de capacidades —
> y a cómo se rompe ese techo de forma controlada y barata.

---

## [PANORAMA]

Hasta aquí has aprendido a mejorar **cómo se piensa** la consulta y
**cómo se entrega** la respuesta. Pero hay un límite que no se cruza
con técnica conversacional: **lo que Claude puede materialmente
ejecutar** — qué archivos puede leer, qué comandos puede correr, qué
servicios puede llamar.

Por defecto Claude tiene un conjunto de herramientas — leer y escribir
archivos, ejecutar comandos de terminal, buscar en la web. Cuando una
petición requiere algo fuera de esto — generar un video, sintetizar
audio en español, transcribir, generar imágenes, ejecutar un modelo
especializado — Claude no puede simplemente "intentarlo".

La meta-skill `/capacidad` formaliza qué hacer en ese momento: en
lugar de declarar imposibilidad, **investiga, propone, instala y
registra** una nueva herramienta, escogiendo la opción **menos
costosa que cumpla**.

---

## [ACTIVACIÓN]

> *"Piensa en algo que te gustaría poder pedirle a Claude que hiciera
> y que sospechas que aún no puede. Generar un video corto para un
> curso. Transcribir una reunión grabada. Convertir un PDF complejo
> a un formato editable. Crear una imagen para una propuesta. ¿Qué
> haces hoy cuando llegas a ese límite?"*

[Pausa 3s]

La respuesta de la mayoría: *"asumo que no se puede y busco otra
forma."* Eso te cuesta tiempo y, peor, te enseña a no pedirle a
Claude las cosas valiosas. **`/capacidad` invierte ese hábito.**

---

## [CONCEPTO CENTRAL]

`/capacidad` se activa de dos maneras:

- **Automáticamente**, cuando Claude detecta que tu petición requiere algo fuera de sus tools actuales.
- **Manualmente**, escribiendo `/capacidad <descripción>` cuando tú quieres expandir capacidades sin estar a mitad de una tarea.

Cuando se activa, investiga en **4 niveles ordenados por costo
creciente**:

```
NIVEL 1 — SCRIPTS HELPER (costo recurrente: cero)
  Combinaciones de herramientas que YA están en el sistema,
  orquestadas en un script.
  Ejemplo: ffmpeg + texto → video con narración generada localmente.

NIVEL 2 — CLIs LOCALES (costo: solo cómputo local)
  Herramientas instalables vía brew, npm, pip, cargo.
  Ejemplo: piper-tts para síntesis de voz en español, cero costo
           recurrente.

NIVEL 3 — MCP SERVERS (config en settings; costo variable)
  Servidores que se registran en la configuración de Claude Code.
  Ejemplo: servidor MCP de filesystem ampliado, de imagen, etc.

NIVEL 4 — APIs EXTERNAS (costo recurrente garantizado)
  Servicios pagos accesibles vía script wrapper.
  Ejemplo: ElevenLabs para voz humana clonable, HeyGen para video
           con avatar.
```

Para cada opción, evalúa **4 ejes**:

```
1. Costo recurrente  (USD/mes o cero)
2. Costo de setup    (minutos para dejarlo funcionando)
3. Calidad esperada  (alta / media / baja, justificada)
4. Latencia          (segundos por unidad de trabajo)
```

**Regla rectora del protocolo:** *bajar al nivel más barato que cumpla
calidad aceptable.* No saltar al Nivel 4 cuando una solución Nivel 1
hace el trabajo.

Tras presentar las opciones, el usuario aprueba una vía menú
interactivo, Claude implementa, hace un **smoke test** mínimo, y
**registra el resultado en la memoria del proyecto** para no
re-investigar la misma capacidad en sesiones futuras.

---

## [ANALOGÍA / ANCLA]

**Analogía:** *Añadir aplicaciones a tu smartphone.*

Cuando compras un smartphone trae 20 apps preinstaladas. Algunas las
usas, otras no. Cuando descubres que necesitas algo que ninguna app
preinstalada hace — escanear documentos, medir ritmo cardíaco, editar
audio — vas a la tienda y eliges entre opciones.

En la tienda hay tres tipos de apps:

- **Gratuitas con buen funcionamiento** (= Nivel 1 y 2 de `/capacidad`)
- **Apps premium one-time** (= Nivel 3 con MCP gratuito)
- **Apps con suscripción mensual** (= Nivel 4 — APIs pagas)

Casi nadie compra la app premium cuando la gratuita hace el trabajo.
Y nadie se suscribe mensualmente cuando una compra única ya resuelve.
Esa misma sensatez aplica a `/capacidad`.

---

## [EJEMPLO REAL]

**Sector:** capacitación corporativa · **Rol:** diseñador instruccional · **Tarea:** producir audio narrado en español para una serie de videos de capacitación interna.

> *(Este ejemplo es real: es lo que vamos a hacer al final de ESTA
> serie de videos. Es el caso meta-recursivo más cercano que se puede
> dar.)*

### Diagnóstico de brecha

```
Capacidad requerida: narración de audio en español a partir de texto,
                     cero costo recurrente, calidad media-alta suficiente
                     para capacitación interna.

Tools disponibles:   Read, Write, Edit, Bash, WebSearch.
                     ffmpeg disponible vía Bash si está instalado.

Faltante:            motor de síntesis de voz (TTS) en español.
```

### Las 4 opciones investigadas

```
NIVEL 1 — SCRIPT con `say` de macOS
  Costo:       cero
  Setup:       cero (ya viene en macOS)
  Calidad:     baja-media (voz robótica clásica)
  Latencia:    < 1s por frase
  Veredicto:   plan B — funciona pero suena dated

NIVEL 2 — piper-tts con modelo en español
  Costo:       cero recurrente, ~50 MB de descarga única
  Setup:       ~5 min (brew install piper, descargar modelo es-MX)
  Calidad:     media-alta (voces neuronales modernas)
  Latencia:    ~3s por minuto de audio
  Veredicto:   RECOMENDADO — cumple con el requisito de cero costo

NIVEL 3 — MCP server de TTS
  Costo:       depende del servidor; mayoría gratuitos pero
               experimentales
  Setup:       configuración en settings.json
  Calidad:     variable
  Veredicto:   descartado por inmadurez relativa para producción

NIVEL 4 — OpenAI TTS API
  Costo:       ~0.015 USD por 1000 caracteres
  Setup:       API key + script wrapper, ~10 min
  Calidad:     muy alta
  Veredicto:   descartado por requisito de cero costo
```

### Implementación de la opción aprobada (Nivel 2)

```
1. brew install piper                       # CLI
2. descargar voz es-MX-claude (≈ 50 MB)     # modelo
3. crear .claude/scripts/narrar.sh          # wrapper
4. smoke test: narrar 30 palabras           # validación
5. registrar en MEMORY.md como
   capacidad-tts-local-es                   # memoria persistente
```

**Tiempo total de implementación: ~12 minutos. Costo: cero. Calidad
suficiente para los videos de capacitación.**

A partir de este momento, cualquier futura petición de narración en
español usa el mismo wrapper, sin re-investigar.

---

## [COMPETENCIA EN ACCIÓN]

El profesional competente:

- **No asume "no se puede"** cuando topa con un límite de Claude. Pide `/capacidad`.
- **Lee las 4 opciones** antes de aprobar una — entiende qué está aprobando.
- **Privilegia el nivel más bajo** que cumpla calidad aceptable. No salta al Nivel 4 por reflejo.
- **Verifica el smoke test** antes de declarar exitosa la capacidad.

Indicador conductual:

> *"El profesional competente, al recibir 'no puedo hacer X' de
> Claude, escribe '/capacidad <X>' antes de buscar otra solución."*

---

## [ACTIVIDAD INTEGRADORA]

**Nombre del reto:** *Detectar una capacidad faltante y proponerla*

**Descripción:**

1. Identifica **una capacidad** que te gustaría que Claude tuviera y sospechas que aún no tiene. Ejemplos:
   - Transcribir audios grabados en reuniones
   - Resumir PDFs con imágenes
   - Generar diagramas técnicos
   - Editar imágenes con instrucciones de texto
2. Intenta clasificarla en uno de los 4 niveles:
   - **Nivel 1** — ¿se podría resolver combinando tools existentes?
   - **Nivel 2** — ¿hay un CLI conocido que lo hace?
   - **Nivel 3** — ¿hay un MCP server?
   - **Nivel 4** — ¿solo APIs externas, con costo recurrente?
3. **Sin invocar `/capacidad` todavía**, escribe en una nota personal:
   - La capacidad faltante
   - Tu nivel sospechado
   - El costo aceptable que estarías dispuesto a pagar
4. La próxima vez que necesites esa capacidad, invoca `/capacidad` y compara tu sospecha con la propuesta real.

**Entregable:** una nota personal con la capacidad faltante, el nivel sospechado, y el costo aceptable.

**Nivel de Bloom:** 6 — Crear (análisis de necesidad + diseño de propuesta)
**Nivel de competencia:** Avanzado

---

## [EVALUACIÓN]

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Reflejo ante "no puedo" | Acepta y busca otra solución | Pide `/capacidad` cuando se acuerda | Pide `/capacidad` como primer reflejo |
| Lectura de opciones | Aprueba la primera recomendada | Compara los 4 ejes (costo/setup/calidad/latencia) | Detecta cuándo el nivel propuesto es sobre-dimensionado |
| Costo consciente | Aprueba sin verificar costo | Verifica costo recurrente antes de aprobar | Negocia hacia nivel más bajo si calidad aceptable |
| Validación post-instalación | Asume que funciona | Ejecuta el smoke test | Verifica el costo real vs estimado tras primer uso |

---

## [TRANSFERENCIA AL PUESTO]

Indicador a 30 días: *"El profesional ha habilitado al menos una capacidad nueva vía `/capacidad` y la usa rutinariamente. La entrada correspondiente está en su `MEMORY.md`."*

---

## [INVITACIÓN AL EPISODIO 6]

> *"Ya tienes el conjunto completo. Auto-revisión, estructura, modos,
> /prompt, /capacidad. Cinco técnicas que cubren desde la forma de la
> respuesta hasta la expansión de las herramientas. En el episodio
> final no aprendes una técnica más — aprendes el **meta-proceso** que
> conecta todas ellas en un ciclo de mejora continua. Vas a entender
> cómo este mismo video se hizo... usando exactamente lo que estás
> aprendiendo."*

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Anthropic. (2024). *Model Context Protocol specification*. Anthropic.
    https://modelcontextprotocol.io/

Anthropic. (2024). *Claude Code documentation — MCP integration*.
    Anthropic. https://docs.anthropic.com/en/docs/claude-code/mcp

Hunt, A., & Thomas, D. (1999). *The pragmatic programmer: From
    journeyman to master*. Addison-Wesley.

---

# === SCRIPT DE NARRACIÓN ===

> Tiempo objetivo: 6:00 — 7:00 min · Cadencia: 130-140 wpm

## Bloque 1 — Hook (0:00 — 0:30)

```
[Slide 1 — texto: "Lo que Claude NO puede hacer... aún"]

[NARRACIÓN]

Hay cosas que Claude no puede hacer.

[PAUSA 1s]

Por ahora.

[PAUSA 1s]

Hoy aprendes a cambiar ese "por ahora" en "ya puede" — sin tocar
código, sin presupuesto, y de manera controlada.
```

## Bloque 2 — Activación (0:30 — 1:15)

```
[Slide 2 — pregunta: "¿Qué te gustaría poder pedirle a Claude que aún no puede hacer?"]

[NARRACIÓN]

Piensa en algo que te gustaría poder pedirle a Claude y que sospechas
que aún no puede. Generar un video corto para un curso. Transcribir
una reunión. Convertir un PDF complejo a un formato editable. Crear
una imagen para una propuesta.

[PAUSA 3s]

¿Qué haces hoy cuando llegas a ese límite?

La respuesta de la mayoría: asumo que no se puede y busco otra forma.

[ÉNFASIS] Eso te cuesta tiempo y, peor, te enseña a no pedirle a
Claude las cosas valiosas. /capacidad invierte ese hábito. [/ÉNFASIS]
```

## Bloque 3 — Concepto: 4 niveles de costo (1:15 — 3:00)

```
[Slide 3 — los 4 niveles en columnas]

[NARRACIÓN]

/capacidad investiga en cuatro niveles ordenados por costo creciente.

Nivel uno: scripts helper. Combinar herramientas que YA están en el
sistema. Ejemplo: ffmpeg con un texto puede producir un video con
narración. Costo recurrente: cero.

Nivel dos: CLIs locales. Herramientas que se instalan con brew, npm o
pip. Ejemplo: piper-tts para síntesis de voz en español. Costo
recurrente: cero. Cuesta solo el cómputo de tu laptop.

Nivel tres: servidores MCP. Componentes que se registran en la
configuración de Claude Code. Algunos gratuitos, otros con API key.

Nivel cuatro: APIs externas. Servicios pagos como ElevenLabs para voz
humana clonable o HeyGen para avatar de video. Costo recurrente
garantizado.

[Slide 4 — los 4 ejes de evaluación]

Cada opción se evalúa en cuatro ejes: costo recurrente, costo de
setup, calidad esperada, y latencia.

[ÉNFASIS] Regla rectora: bajar al nivel más barato que cumpla calidad
aceptable. No saltar al Nivel cuatro cuando una solución Nivel uno
hace el trabajo. [/ÉNFASIS]
```

## Bloque 4 — Analogía (3:00 — 3:45)

```
[Slide 5 — smartphone con apps siendo añadidas]

[NARRACIÓN]

Una analogía.

Tu smartphone trae veinte apps preinstaladas. Cuando descubres que
necesitas escanear documentos, medir ritmo cardíaco, editar audio, vas
a la tienda y eliges.

En la tienda hay tres tipos de apps: gratuitas que funcionan bien,
apps premium de pago único, y apps con suscripción mensual.

[PAUSA 2s]

Casi nadie compra la app premium cuando la gratuita hace el trabajo.
Y nadie se suscribe mensualmente cuando una compra única resuelve.

[ÉNFASIS] Esa misma sensatez aplica a /capacidad. [/ÉNFASIS]
```

## Bloque 5 — Ejemplo real (META) (3:45 — 5:15)

```
[Slide 6 — meta-reference: "Este video se hizo así"]

[NARRACIÓN]

Y ahora un ejemplo muy especial.

Esta misma serie de videos que estás viendo se produjo usando
/capacidad.

La brecha: necesitábamos audio narrado en español, cero costo
recurrente, calidad suficiente para capacitación.

[Slide 7 — las 4 opciones evaluadas]

/capacidad investigó cuatro opciones.

Nivel uno: el comando "say" de macOS. Funciona, pero suena robótico.
Plan B.

Nivel dos: piper-tts con modelo de voz en español de México. Cero
costo recurrente, calidad neuronal moderna, cinco minutos de setup.
Recomendado.

Nivel tres: servidores MCP de TTS. Descartado por inmadurez relativa.

Nivel cuatro: OpenAI TTS API. Calidad muy alta pero descartado por el
requisito de cero costo.

[Slide 8 — opción seleccionada y resultado]

Se aprobó Nivel dos. Tiempo total de implementación: doce minutos.
Costo: cero. La voz que estás escuchando AHORA fue generada con esa
capacidad recién habilitada.

[ÉNFASIS] Si hubiéramos saltado al Nivel cuatro por reflejo, habríamos
gastado dinero innecesario. /capacidad nos ayudó a bajar al nivel más
barato que cumplía. [/ÉNFASIS]
```

## Bloque 6 — Actividad (5:15 — 6:15)

```
[Slide 9 — actividad: 4 pasos]

[NARRACIÓN]

Tu turno.

Uno: identifica UNA capacidad que te gustaría que Claude tuviera y
sospechas que no tiene. Una capacidad real que uses en tu trabajo.

Dos: intenta clasificarla mentalmente en uno de los cuatro niveles.
¿Combinable con tools existentes? ¿Hay un CLI? ¿Hay un MCP? ¿Solo
APIs?

Tres: anota en una nota personal: la capacidad faltante, el nivel
sospechado, y el costo aceptable que estarías dispuesto a pagar.

Cuatro: la próxima vez que necesites esa capacidad, invoca /capacidad
y compara tu sospecha con la propuesta real.

[PAUSA 1s]

[ÉNFASIS] El propósito no es habilitar la capacidad hoy. Es que la
próxima vez que choques con un límite, tu reflejo sea pedir /capacidad
en vez de buscar otra solución. [/ÉNFASIS]
```

## Bloque 7 — Cierre (6:15 — 6:45)

```
[Slide 10 — invitación a Ep 6]

[NARRACIÓN]

Ya tienes el conjunto completo.

Auto-revisión. Estructura. Modos. /prompt. /capacidad.

Cinco técnicas que cubren desde la forma de la respuesta hasta la
expansión de las herramientas.

En el episodio final no aprendes una técnica más. Aprendes el
**meta-proceso** que conecta todas ellas en un ciclo de mejora
continua.

[PAUSA 1s]

Y vas a entender cómo este mismo video se hizo... usando exactamente
lo que estás aprendiendo.

[Slide final]
```

---

# === ESTRUCTURA DE SLIDES ===

| # | Título / Texto en pantalla | Visual | Duración |
|---|---|---|---|
| 1 | "Lo que Claude NO puede hacer... aún" | Texto con elipsis | 0:00 — 0:30 |
| 2 | "¿Qué te gustaría poder pedirle a Claude?" | Pregunta abierta | 0:30 — 1:15 |
| 3 | Los 4 niveles en columnas | Diagrama con costos | 1:15 — 2:30 |
| 4 | Los 4 ejes de evaluación | Tabla compacta | 2:30 — 3:00 |
| 5 | Smartphone con apps siendo añadidas | Ilustración | 3:00 — 3:45 |
| 6 | "Este video se hizo así" | Texto + flecha | 3:45 — 4:00 |
| 7 | Las 4 opciones evaluadas (meta) | Tabla con veredictos | 4:00 — 4:45 |
| 8 | Opción seleccionada + resultado | Caja destacada | 4:45 — 5:15 |
| 9 | Actividad: 4 pasos | Lista | 5:15 — 6:15 |
| 10 | Próximo: meta-proceso | Cierre | 6:15 — 6:45 |

---

# === NOTAS DE PRODUCCIÓN ===

- **Momento meta del bloque 5:** este es el momento más memorable de la serie. Cuando se diga "la voz que estás escuchando ahora fue generada con esa capacidad recién habilitada", la voz debería **hacer un cambio sutil de entonación** para que el espectador note la auto-referencia. Si el TTS lo permite, énfasis adicional en esa frase.
- **Slide 8 (resultado):** poner en grande "12 minutos · 0 USD" como números destacados. Es el indicador de éxito del protocolo.
- **Importante para v2 del propio script:** una vez producido el primer episodio en audio, regenerar el bloque 5 con métricas reales del setup que se haya hecho (no las estimadas en este texto). Es honestidad epistémica del protocolo.

---

# === CHECKLIST DE 4 PILARES ===

```
PILAR 1 — ACTIVACIÓN  ✓
  La pregunta sobre capacidades faltantes activa la frustración previa
  del espectador con límites del sistema.

PILAR 2 — ANCLAJE  ✓
  Analogía explícita "tienda de apps del smartphone" en bloque 4 — usa
  un dominio donde todos hemos hecho decisiones de costo/beneficio.

PILAR 3 — ORGANIZACIÓN  ✓
  Depende solo del concepto general de "herramientas de Claude"
  introducido implícitamente desde Ep 0. El concepto de niveles es
  intuitivo (todos entendemos gratis vs pago).

PILAR 4 — APLICACIÓN  ✓
  Actividad produce un artefacto: clasificación de una capacidad
  faltante en uno de los 4 niveles, con costo aceptable estimado.

PILAR EXTRA — META-RECURSIÓN  ✓
  El ejemplo es el propio proceso de producción del video, lo cual
  produce el "momento aha" más memorable de la serie.
```
