# Serie de capacitación — Mejora continua de tu Claude

> Diseño pedagógico maestro de la serie. Cada episodio vive en su propio
> archivo (`episodio-N-<slug>.md`) con el script de narración y la
> estructura de slides. La producción de audio se hace al final con
> el protocolo `/capacidad` y un TTS local cero costo.

---

## [PANORAMA DE LA SERIE]

**Pregunta central:** *¿Cómo se convierte Claude en una herramienta cada
vez más útil para mi trabajo, sin depender de un equipo externo que la
configure?*

Esta serie enseña al usuario el **proceso operativo** para configurar y
mejorar progresivamente su propio Claude: afinar respuestas, estructurar
resultados, especializar por dominio, refinar prompts y expandir
herramientas. El objetivo no es memorizar comandos, sino interiorizar el
**meta-proceso** según el cual el propio Claude ayuda a su usuario a
configurar mejor a Claude — un ciclo de mejora continua sin techo.

Es la primera serie del proyecto **ConfiguracionClaude** orientada al
usuario final que parte de cero.

---

## [AUDIENCIA Y NIVEL PREVIO]

| Dimensión | Especificación |
|---|---|
| Audiencia primaria | Profesional que usa Claude como asistente y quiere obtener resultados de calidad defendible |
| Nivel previo asumido | **Cero** sobre configuración de Claude. Se asume que sabe usar un chat (escribir prompts) y nada más. |
| Conocimientos transferibles | Cualquier disciplina profesional con estándares de calidad documental (consultoría, auditoría, investigación, ingeniería, finanzas, derecho, educación) |
| Lo que NO se asume | Programación, conocimiento de CLIs, conceptos de IA, terminología de prompt engineering |

---

## [OBJETIVOS DE APRENDIZAJE — verbos Bloom observables]

Al terminar la serie, el participante será capaz de:

1. **Identificar** las diferencias entre una respuesta de Claude por defecto y una respuesta producida bajo un protocolo de calidad (Nivel 1 — Recordar).
2. **Aplicar** el protocolo de 4 pasos de auto-revisión a sus propias consultas (Nivel 3 — Aplicar).
3. **Analizar** cuándo una respuesta cumple con estructura general → particular y citación APA 7 (Nivel 4 — Analizar).
4. **Evaluar** un prompt propio según las 10 dimensiones de la rúbrica `/prompt` y refinarlo (Nivel 5 — Evaluar).
5. **Crear** un modo experto personalizado para su dominio profesional (Nivel 6 — Crear).
6. **Crear** una solicitud de nueva herramienta vía el protocolo `/capacidad`, distinguiendo los 4 niveles de costo (Nivel 6 — Crear).
7. **Diseñar** su propio plan de mejora continua de su configuración (Nivel 6 — Crear, auto-evaluación).

---

## [4 PILARES PEDAGÓGICOS — verificación de la serie]

Estrategia de **aprendizaje significativo** (Ausubel, 1963) aplicada a la serie completa:

| Pilar | Cómo se aplica en la serie |
|---|---|
| **Activación** | Cada episodio abre con una situación profesional que el espectador reconoce: "te pidieron X, le preguntaste a Claude, obtuviste Y. Ahora notas que Y tiene un problema." |
| **Anclaje** | Una analogía visual por episodio, marcada explícitamente como *Analogía:* — por ejemplo, los modos expertos como "contratar un especialista por tema". |
| **Organización** | Cada episodio depende solo de conceptos ya enseñados. Episodio N + 1 nunca exige saber algo no cubierto en episodios 0…N. |
| **Aplicación** | Cada episodio termina con una **actividad integradora** que produce un artefacto que no existía antes (un prompt refinado, una propuesta de modo, etc.). |

---

## [ESTRATEGIA DE APRENDIZAJE SIGNIFICATIVO — diseño macro]

Estructura del recorrido cognitivo (Ausubel, 1963; Anderson & Krathwohl, 2001):

```
ORGANIZADOR AVANZADO (Episodio 0)
   "Hoy le preguntas a Claude y te responde. Mañana puedes hacer
    que esa respuesta sea de mucha mayor calidad — sin tocar
    código, sin equipo técnico, sin presupuesto."
   → Anclaje a la experiencia previa del usuario con cualquier chatbot.

DIFERENCIACIÓN PROGRESIVA (Episodios 1 → 5)
   De simple a complejo:
   · Ep 1 → calidad de la respuesta (uno mismo, sin modos)
   · Ep 2 → forma de la respuesta (estructura + APA 7)
   · Ep 3 → especialización (modos expertos)
   · Ep 4 → calidad del input (/prompt)
   · Ep 5 → expansión de capacidades (/capacidad)

RECONCILIACIÓN INTEGRADORA (Episodio 6)
   "Todo lo anterior se conecta: Claude no solo responde mejor,
    sino que te ayuda a configurar mejor el sistema con el que
    le preguntas. Es un ciclo sin techo."
   → Activación de la metacognición.
```

---

## [TABLA DETALLADA DE EPISODIOS]

| # | Título | Min | Concepto central | Analogía | Actividad integradora | Bloom |
|---|---|---|---|---|---|---|
| 0 | Por qué configurar a Claude | 5-6 | Claude por defecto vs configurado | Como recibir un asistente nuevo vs uno que ya conoce tu estilo | Comparar dos respuestas a la misma pregunta | 1 — Identificar |
| 1 | Tu primer reflejo de calidad: protocolo de 4 pasos | 6-7 | Auto-revisión sistemática antes de entregar | Como un editor profesional revisa antes de publicar | Pedirle a Claude que aplique el protocolo a una respuesta anterior | 3 — Aplicar |
| 2 | Estructura, fuentes y APA 7 | 5-6 | La forma importa tanto como el contenido | Como leer un paper científico vs un blog | Reformatear una respuesta a estructura general → particular + APA 7 | 4 — Analizar |
| 3 | Modos expertos: un especialista por tema | 7-8 | Encapsular reglas de dominio en un comando | Como ir al cardiólogo en vez del médico general | Identificar qué modo le falta a tu trabajo y diseñar su esqueleto | 6 — Crear |
| 4 | `/prompt`: afinar lo que TÚ preguntas | 6-7 | La calidad del input determina la del output | Como hacer una pregunta clara a un especialista vs una vaga | Tomar tu última pregunta a Claude y refinarla con `/prompt` | 5 — Evaluar |
| 5 | `/capacidad`: expandir lo que Claude PUEDE hacer | 6-7 | El sistema no es fijo, es extensible | Como añadir aplicaciones a tu smartphone | Identificar una capacidad faltante y proponer cómo habilitarla | 6 — Crear |
| 6 | El meta-proceso: Claude configura a Claude | 5-6 | Mejora continua autosostenida | Como un gimnasio donde tú mismo diseñas tus ejercicios | Diseñar tu próxima mejora a la configuración | 6 — Crear + auto-evaluación |

**Total estimado:** 41-47 minutos · **Densidad:** un concepto nuevo por bloque, ≤3 conceptos nuevos por episodio · **Repetición espaciada:** los conceptos de Ep N reaparecen en Ep N+1 y Ep N+2 como anclas.

---

## [PLAN DE EVALUACIÓN — Modelo Kirkpatrick]

Cuatro niveles de evidencia de aprendizaje (Kirkpatrick & Kirkpatrick, 2016):

| Nivel | Qué se evalúa | Instrumento | Cuándo |
|---|---|---|---|
| **1 — Reacción** | ¿El espectador percibió valor? | Mini-encuesta de 3 preguntas al final de cada episodio | Inmediato post-episodio |
| **2 — Aprendizaje** | ¿Puede aplicar lo enseñado? | Actividad integradora de cada episodio (entregable visible) | Final de cada episodio |
| **3 — Comportamiento** | ¿Lo aplica en su trabajo real? | Auto-reporte una semana después: "¿qué cambió en tus consultas a Claude?" | 7 días post-serie |
| **4 — Resultados** | ¿Mejoraron las decisiones que toma con apoyo de Claude? | Auto-evaluación libre a 30 días: ejemplos concretos donde la nueva forma de usar Claude generó un mejor resultado profesional | 30 días post-serie |

**Rúbrica de competencia integral** (al final del Ep 6):

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Diagnóstico de calidad de respuestas | Detecta cuando una respuesta es genérica | Identifica qué dimensión falta (estructura / fuentes / dominio) | Predice antes de preguntar qué dimensiones debe especificar |
| Uso de modos | Activa el modo correcto en cada consulta | Combina líder + apoyo según el cruce de dominios | Diseña modos propios para su dominio profesional |
| Refinamiento de prompts | Reescribe sus prompts cuando el output es pobre | Anticipa las dimensiones que necesita aclarar antes de enviar | Internaliza la rúbrica y deja de invocar `/prompt` explícitamente |
| Expansión de capacidades | Pide a `/capacidad` cuando algo no es posible | Distingue niveles de costo (Scripts → APIs) y elige conscientemente | Mantiene su `MEMORY.md` de capacidades como activo personal |

---

## [TRANSFERENCIA AL PUESTO]

**Indicadores observables a los 30 días** (Kirkpatrick Nivel 3):

- [ ] El profesional **abre** sus consultas a Claude con el modo apropiado en al menos 70 % de los casos
- [ ] El profesional **revisa** la rúbrica mental de 10 dimensiones antes de mandar un prompt no trivial
- [ ] El profesional **registra** en `MEMORY.md` al menos una capacidad habilitada vía `/capacidad`
- [ ] El profesional **identifica** al menos una nueva mejora a su configuración y la implementa con apoyo de Claude

Si el profesional cumple 3 de 4, la transferencia se considera exitosa.

---

## [PLAN DE PRODUCCIÓN — protocolo `/capacidad` deferido]

La fase de producción se ejecutará tras aprobar los scripts (Ep 0-6). En ese momento se invoca `/capacidad` con el siguiente diagnóstico de brecha pre-cargado:

```
Capacidad requerida: narración de audio profesional a partir de texto
                     en español, cero costo recurrente, calidad media-alta
                     suficiente para capacitación interna.

Tools disponibles: Read, Write, Edit, Bash (con acceso a ffmpeg si está
                   instalado), WebSearch para verificar opciones actuales.

Faltante: motor TTS (text-to-speech) en español.

Niveles de solución a investigar:
  · Nivel 1 (Scripts): ¿se puede combinar say + ffmpeg en macOS para algo
                       aceptable? (cero costo, calidad básica)
  · Nivel 2 (CLIs):    piper-tts con modelo en español, instalable vía brew
                       o pip; cero costo recurrente, calidad media-alta
                       (recomendado a priori dado el requisito de cero costo)
  · Nivel 3 (MCP):     buscar servidores MCP de TTS si emergieron en 2026
  · Nivel 4 (APIs):    descartado a priori por requisito de cero costo

Plan B si Nivel 2 falla: TTS de macOS (`say` command) que ya está disponible
sin instalar nada.

Composición de audio: ffmpeg para unir narración + slides exportados a
imagen + transiciones simples.
```

La instalación se documenta en `MEMORY.md` como `capacidad-tts-local-es`.

---

## [PRINCIPIO DE NO-MEMORIZACIÓN]

Cada episodio termina con una **invitación a la práctica**, no con un
resumen de "qué aprendimos". El principio es:

> **No se aprende a usar Claude memorizando comandos. Se aprende
> usándolo bajo el protocolo, fallando, corrigiendo y notando lo que
> mejora.**

Por eso la actividad integradora de cada episodio produce un artefacto
tangible (un prompt, una propuesta de modo, una nueva capacidad
habilitada) que el participante puede revisar la semana siguiente.

---

## [ESTRUCTURA DE LOS ARCHIVOS DE EPISODIO]

Cada `episodio-N-<slug>.md` contiene:

```
1. Frontmatter con metadata (duración, concepto, prerequisitos)
2. Las 10 secciones del formato /edu
3. Script de narración línea por línea (timing en segundos)
4. Estructura de slides con título y bullets clave
5. Notas de producción (transiciones, énfasis, pausas)
```

Esto permite que un editor humano (o el flujo automatizado de `/capacidad`)
tome el archivo y genere directamente:

- Slides en PDF/HTML vía pandoc o reveal.js
- Audio narrado vía el TTS elegido en `/capacidad`
- Composición final vía ffmpeg

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Kirkpatrick, J. D., & Kirkpatrick, W. K. (2016). *Kirkpatrick's four
    levels of training evaluation*. ATD Press.

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for
    learning, teaching, and assessing: A revision of Bloom's
    educational objectives*. Longman.

Merrill, M. D. (2002). First principles of instruction. *Educational
    Technology Research and Development, 50*(3), 43–59.
    https://doi.org/10.1007/BF02505024

Ausubel, D. P. (1963). *The psychology of meaningful verbal learning*.
    Grune & Stratton.

Bloom, B. S. (1956). *Taxonomy of educational objectives*. David McKay.
