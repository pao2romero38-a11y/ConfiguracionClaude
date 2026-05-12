---
episodio: 4
titulo: "/prompt — afinar lo que TÚ preguntas"
duracion_objetivo_min: 6-7
concepto_central: "La calidad del input determina la calidad del output"
analogia_principal: "Pregunta clara al especialista vs pregunta vaga"
bloom: 5 — Evaluar
prerequisitos: Episodios 0, 1, 2, 3
artefacto_producido: "Una pregunta propia del espectador refinada con /prompt, lado a lado con la original"
---

# Episodio 4 — `/prompt`: afinar lo que TÚ preguntas

> **Función en la serie:** primer encuentro con una **meta-skill**.
> Hasta aquí, las técnicas mejoran lo que Claude entrega. Hoy se
> mejora lo que el usuario *manda*. Es la palanca de mayor impacto que
> aún no se había tocado.

---

## [PANORAMA]

Has aprendido a pedir auto-revisión, a exigir estructura y a activar
modos expertos. Toda esa mejora está del lado de la respuesta.

Lo que no se discute aún es esto: **la calidad del input determina la
calidad del output**. Un prompt vago al especialista correcto sigue
produciendo respuestas vagas. La asimetría está clara — el prompt es
la palanca con más impacto en lo que recibes — y aun así, casi nadie
la afina conscientemente.

Hoy aprendes a usar la meta-skill `/prompt`: una herramienta que toma
tu prompt crudo y lo refina contra una rúbrica de diez dimensiones,
exponiendo qué te falta en cada consulta. Es modo entrenamiento; el
objetivo final es que dejes de necesitarla.

---

## [ACTIVACIÓN]

> *"Piensa en las últimas tres consultas profesionales que le hiciste
> a Claude. ¿Cuántas líneas tenía cada prompt? Probablemente entre 1
> y 4. Ahora piensa: si un colega humano te preguntara lo mismo en 1-4
> líneas, ¿podrías responderle bien? Lo más probable es que tuvieras
> que pedirle aclaraciones primero."*

[Pausa 3s]

Lo que harías con un colega — pedirle contexto, restricciones, formato
esperado — es exactamente lo que Claude no puede hacer por su cuenta.
Por eso responde con su mejor adivinanza. Y por eso la respuesta nunca
es totalmente lo que querías.

---

## [CONCEPTO CENTRAL]

`/prompt` evalúa cada prompt crudo contra **10 dimensiones**:

```
 1. Modo y composición          — ¿qué modo o /lider +apoyo activar?
 2. Sistema o contexto anfitrión — ¿en qué proyecto vive la tarea?
 3. Alcance funcional           — ¿qué entra y qué queda fuera?
 4. Restricciones técnicas      — stack, herramientas, integraciones
 5. Estándares aplicables       — NIF, IFRS, ISO, NIST, APA 7, ...
 6. Entregable esperado         — análisis, código, informe, plan
 7. Fase del método             — ¿análisis, diseño, implementación?
 8. Convenciones del proyecto   — branch, mensajes, memoria técnica
 9. Riesgos técnicos conocidos  — patrones documentados aplicables
10. Datos / preguntas bloqueantes — ¿qué necesito ANTES de responder?
```

Para cada dimensión, la skill marca con tres estados:

- **✓** la dimensión ya está en el prompt original
- **⚠** mencionada pero sin detalle suficiente
- **✗** ausente

Lo que `/prompt` devuelve es:

1. **Diagnóstico** — modo sugerido + ambigüedades detectadas
2. **Prompt refinado** — listo para ejecutar
3. **Qué añadí** — 1-4 viñetas explicando los cambios
4. **Rúbrica visible** — comparando original vs refinado
5. **Alternativas** — solo si la intención original admitía varias lecturas
6. **¿Ejecutar ahora?** — menú interactivo: ejecutar tal cual, ejecutar alternativa, empezar de nuevo, o cerrar

---

## [ANALOGÍA / ANCLA]

**Analogía:** *Pregunta clara a un especialista vs pregunta vaga.*

Comparar dos visitas al médico:

- **Vaga:** *"Doctor, me duele."*
  → El médico hace 15 preguntas y media hora después tiene contexto suficiente para diagnosticar.

- **Clara:** *"Doctor, tengo dolor punzante en el pecho izquierdo desde hace 2 horas, sin antecedentes cardíacos, irradiando al brazo, intensidad 7/10."*
  → El médico llama a emergencias en 20 segundos.

Misma persona, mismo médico, misma capacidad de diagnóstico. **Lo que cambia es el ancho de banda del prompt.** Y como con el médico, Claude no puede leerte la mente — necesita las dimensiones explícitas.

`/prompt` es el entrenador que te ayuda a aprender a hacer la
"pregunta clara" sin tener que pensar en las 10 dimensiones una por
una. Con el tiempo, internalizas el patrón y dejas de necesitar la
skill.

---

## [EJEMPLO REAL]

**Sector:** ingeniería de software · **Rol:** desarrollador senior · **Tarea:** pedirle a Claude que diseñe un sistema de inventario para un negocio en crecimiento.

### Prompt crudo del desarrollador

> *"crea un sistema de inventario para una pyme"*

### Resultado de `/prompt`

```
[DIAGNÓSTICO]
- Modo sugerido: /dev +dev-db +cost
- Razón: sistema de inventario = código + diseño de BD + costos
- Ambigüedades: alcance funcional (mínimo viable vs ERP completo);
                stack tecnológico; presupuesto; usuario objetivo

[PROMPT REFINADO]
/dev +dev-db +cost

CONTEXTO
Pyme mexicana en crecimiento. Sin sistema actual. Equipo técnico
limitado (1-2 desarrolladores).

OBJETIVO
Diseñar Inventario General mínimo viable, escalable a futuro.

FASE 1 — ANÁLISIS PREVIO
  · Inventario de entidades: producto, almacén, lote, movimiento, ...
  · Reglas básicas: kardex, costo promedio o PEPS
  · Puntos de integración futura (ventas, compras)
  · Riesgos: consistencia transaccional en alta concurrencia

DATOS QUE NECESITO QUE ME DES
1. Volumen estimado: SKUs, movimientos/día
2. Plataforma objetivo: web, móvil, escritorio
3. Marco contable: NIF mexicanas / IFRS / ninguno
4. Stack preferido o restricciones existentes
5. Presupuesto y plazo

ALCANCE FUERA DE ESTA ITERACIÓN
  · Reportes financieros
  · Integración con sistemas existentes
  · Multi-empresa o multi-moneda

[QUÉ AÑADÍ]
1. Modo apropiado: /dev +dev-db +cost
2. Acoté entregable a FASE 1 (análisis) — no saltar a código
3. 5 preguntas bloqueantes que hacen la diferencia
4. Alcance fuera explícito para evitar scope creep

[RÚBRICA] — original vs refinado
1. Modo            ✗  →  ✓
2. Contexto        ⚠  →  ✓
3. Alcance         ✗  →  ✓
4. Restricciones   ✗  →  ⚠ (pendiente del usuario)
5. Estándares      ✗  →  ⚠
6. Entregable      ✗  →  ✓
7. Fase            ✗  →  ✓
8. Convenciones    ✗  →  N/A
9. Riesgos         ✗  →  ✓
10. Bloqueantes    ✗  →  ✓

Original: 0 ✓ / 1 ⚠ / 9 ✗
Refinado: 7 ✓ / 2 ⚠ / 0 ✗

[¿EJECUTAR AHORA?]
○ Sí, ejecutar refinado tal cual
○ Empezar de nuevo (reescribir el prompt crudo)
○ No, solo quería ver el refinamiento
```

**Diagnóstico del ejemplo:** el prompt original tenía 7 palabras. El
refinado tiene 25 líneas. Y lo más importante: **5 preguntas que el
desarrollador no había pensado** (volumen, plataforma, marco contable,
stack, presupuesto). Si hubiera ejecutado el prompt crudo, habría
recibido una respuesta genérica y habría tenido que iterar 3-4 veces.
Con `/prompt`, el desarrollador termina con una conversación de mucho
mayor calidad desde el primer turno.

---

## [COMPETENCIA EN ACCIÓN]

El profesional competente:

- **Usa `/prompt`** en cada consulta no trivial durante la fase de entrenamiento.
- **Lee la rúbrica** para identificar qué dimensiones suele omitir (patrón personal).
- **Internaliza el patrón** y, eventualmente, escribe prompts ya "refinados" sin invocar `/prompt`.

Indicador conductual:

> *"El profesional competente, antes de mandar un prompt no trivial,
> repasa mentalmente: ¿modo? ¿alcance? ¿estándares? ¿entregable?
> ¿bloqueantes? — aunque no escriba todas las dimensiones, las
> considera."*

---

## [ACTIVIDAD INTEGRADORA]

**Nombre del reto:** *Refinar mi último prompt de verdad*

**Descripción:**

1. Abre tu historial de Claude. Encuentra una consulta reciente donde la primera respuesta no fue lo que esperabas y tuviste que iterar.
2. Copia el prompt original que mandaste.
3. Inicia un nuevo prompt con `/prompt ` y pega tu prompt original a continuación.
4. Lee el refinado, la rúbrica y las alternativas que aparezcan.
5. **No ejecutes todavía** — primero, **identifica las 2-3 dimensiones que más sueles omitir**.

**Entregable:** una nota personal con:
- Tu prompt original
- El refinado de `/prompt`
- La lista de las 2-3 dimensiones que tú sueles omitir consistentemente

Ese patrón es **tu sesgo personal de prompts**. Identificarlo es el primer paso a internalizarlo.

**Nivel de Bloom:** 5 — Evaluar
**Nivel de competencia:** Intermedio

---

## [EVALUACIÓN]

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Invocación | Usa `/prompt` cuando se acuerda | Lo usa rutinariamente en consultas profesionales | Internaliza la rúbrica y deja de invocarlo explícitamente |
| Lectura de la rúbrica | La ignora | Identifica dimensiones ⚠ y ✗ del prompt original | Detecta su patrón personal de omisiones |
| Acción sobre el refinado | Ejecuta sin leer | Compara original vs refinado antes de ejecutar | Selecciona alternativas conscientemente cuando se ofrecen |

---

## [TRANSFERENCIA AL PUESTO]

Indicador a 7 días: *"El profesional ha invocado `/prompt` en al menos 5 consultas reales, ha identificado 2-3 dimensiones que suele omitir, y ha empezado a incluirlas en sus prompts sin invocar la skill."*

---

## [INVITACIÓN AL EPISODIO 5]

> *"Ya tienes cómo afinar lo que TÚ pides. Pero todavía hay un techo:
> Claude solo puede hacer lo que sus herramientas le permiten hacer.
> Generar un video, sintetizar audio, generar imágenes, ejecutar
> modelos especializados — son cosas fuera de sus tools por defecto.
> En el siguiente episodio aprendes la segunda meta-skill: `/capacidad`
> — cómo expandir lo que Claude PUEDE hacer."*

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Anthropic. (2024). *Prompt engineering best practices*. Anthropic.
    https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering

Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G.
    (2023). Pre-train, prompt, and predict: A systematic survey of
    prompting methods in natural language processing. *ACM Computing
    Surveys, 55*(9), 1–35. https://doi.org/10.1145/3560815

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F.,
    Chi, E., Le, Q. V., & Zhou, D. (2022). Chain-of-thought prompting
    elicits reasoning in large language models. *Advances in Neural
    Information Processing Systems, 35*, 24824–24837.

---

# === SCRIPT DE NARRACIÓN ===

> Tiempo objetivo: 6:00 — 7:00 min · Cadencia: 130-140 wpm

## Bloque 1 — Hook (0:00 — 0:30)

```
[Slide 1 — texto: "Toda la mejora hasta aquí fue de Claude. Hoy mejoras tú"]

[NARRACIÓN]

Hasta hoy todas las mejoras han sido del lado de Claude — su
auto-revisión, su estructura, su especialización.

[PAUSA 1s]

Hoy cambia el foco. La palanca con más impacto en lo que recibes no
está en Claude. Está en cómo TÚ formulas la pregunta.
```

## Bloque 2 — Activación (0:30 — 1:15)

```
[Slide 2 — pregunta: "¿Cuántas líneas tenía tu último prompt profesional?"]

[NARRACIÓN]

Pregunta.

Las últimas tres consultas profesionales que le hiciste a Claude.
¿Cuántas líneas tenía cada prompt?

[PAUSA 2s]

Probablemente entre una y cuatro líneas. Ahora piensa: si un colega
humano te preguntara lo mismo en una a cuatro líneas, ¿podrías
responderle bien? Lo más probable es que tuvieras que pedirle
aclaraciones antes.

[ÉNFASIS] Lo que harías con un colega — pedirle contexto, restricciones,
formato esperado — es exactamente lo que Claude no puede hacer por su
cuenta. Por eso responde con su mejor adivinanza. Y por eso nunca
es totalmente lo que querías. [/ÉNFASIS]
```

## Bloque 3 — Concepto: las 10 dimensiones (1:15 — 2:45)

```
[Slide 3 — las 10 dimensiones en una tabla compacta]

[NARRACIÓN]

La meta-skill /prompt evalúa tu prompt contra diez dimensiones.

Modo y composición. ¿Qué especialista activar?
Sistema anfitrión. ¿En qué proyecto vive esto?
Alcance. ¿Qué entra y qué queda fuera?
Restricciones técnicas. Stack, herramientas, integraciones.
Estándares aplicables. NIF, IFRS, ISO, NIST.
Entregable esperado. ¿Análisis, código, informe?
Fase del método. ¿Análisis o implementación?
Convenciones del proyecto. Branches, memoria técnica.
Riesgos técnicos conocidos. Patrones documentados aplicables.
Y por último: datos bloqueantes. ¿Qué necesito antes de poder
responder?

[PAUSA 2s]

[ÉNFASIS] Diez dimensiones. /prompt te muestra cuáles ya están en tu
prompt original y cuáles tuvo que añadir el refinado. [/ÉNFASIS]
```

## Bloque 4 — Analogía (2:45 — 3:30)

```
[Slide 4 — ilustración: paciente vago vs paciente claro]

[NARRACIÓN]

Una analogía.

Visita al médico, dos versiones.

Versión vaga: "Doctor, me duele". El médico tarda media hora haciendo
quince preguntas hasta tener contexto para diagnosticar.

Versión clara: "Doctor, tengo dolor punzante en el pecho izquierdo
desde hace dos horas, sin antecedentes cardíacos, irradiando al brazo,
intensidad siete sobre diez". El médico llama a emergencias en veinte
segundos.

[PAUSA 2s]

Misma persona. Mismo médico. Misma capacidad de diagnóstico.

[ÉNFASIS] Lo que cambia es el ancho de banda del prompt. /prompt es
el entrenador que te enseña a hacer la pregunta clara sin tener que
pensar en las diez dimensiones una por una. [/ÉNFASIS]
```

## Bloque 5 — Ejemplo real (3:30 — 5:00)

```
[Slide 5 — prompt crudo del desarrollador: "crea un sistema de inventario para una pyme"]

[NARRACIÓN]

Un caso. Un desarrollador escribe a Claude el prompt: "crea un sistema
de inventario para una pyme". Siete palabras.

Sin /prompt, recibirá una respuesta genérica y tendrá que iterar tres
o cuatro veces.

[Slide 6 — diagnóstico de /prompt]

Con /prompt, el diagnóstico le sugiere modo /dev más /dev-db más /cost.
Razón: sistema de inventario es código más diseño de base de datos
más dominio de costos.

[Slide 7 — prompt refinado en bloques]

El prompt refinado añade cinco bloques: contexto del negocio, objetivo
concreto, fase uno como entregable, cinco preguntas bloqueantes que el
desarrollador no había pensado — volumen, plataforma, marco contable,
stack, presupuesto — y un alcance explícito fuera de esta iteración.

[Slide 8 — rúbrica antes/después]

La rúbrica muestra el original con cero dimensiones cubiertas; el
refinado con siete cubiertas y dos pendientes del usuario.

[ÉNFASIS] El prompt original tenía siete palabras. El refinado tiene
veinticinco líneas. Y lo más importante: cinco preguntas que el
desarrollador no había pensado. /prompt no inventa; expone lo que
faltaba. [/ÉNFASIS]
```

## Bloque 6 — Actividad (5:00 — 6:00)

```
[Slide 9 — actividad: 5 pasos]

[NARRACIÓN]

Tu turno.

Uno: abre tu historial de Claude. Encuentra una consulta reciente
donde la primera respuesta no fue lo que esperabas y tuviste que
iterar.

Dos: copia el prompt original que mandaste.

Tres: inicia un nuevo prompt con /prompt y pega tu prompt original a
continuación.

Cuatro: lee el refinado, la rúbrica y las alternativas que aparezcan.

Cinco: NO ejecutes todavía. Primero identifica las dos o tres
dimensiones que tú sueles omitir consistentemente.

[PAUSA 2s]

[ÉNFASIS] Ese patrón es TU sesgo personal de prompts. Identificarlo es
el primer paso a internalizarlo. /prompt es modo entrenamiento. El
objetivo final es que dejes de necesitarla porque ya las llevas en la
cabeza. [/ÉNFASIS]
```

## Bloque 7 — Cierre (6:00 — 6:45)

```
[Slide 10 — invitación a Ep 5]

[NARRACIÓN]

Tienes cómo afinar lo que TÚ pides.

Pero todavía hay un techo. Claude solo puede hacer lo que sus
herramientas le permiten. Generar un video. Sintetizar audio. Generar
imágenes. Ejecutar modelos especializados. Cosas fuera de sus tools
por defecto.

[PAUSA 1s]

En el siguiente episodio, la segunda meta-skill: /capacidad. Cómo
expandir lo que Claude PUEDE hacer.

[Slide final]
```

---

# === ESTRUCTURA DE SLIDES ===

| # | Título / Texto en pantalla | Visual | Duración |
|---|---|---|---|
| 1 | "Toda la mejora hasta aquí fue de Claude. Hoy mejoras tú" | Texto | 0:00 — 0:30 |
| 2 | "¿Cuántas líneas tenía tu último prompt profesional?" | Pregunta | 0:30 — 1:15 |
| 3 | Las 10 dimensiones (tabla compacta) | Lista numerada | 1:15 — 2:45 |
| 4 | Paciente vago vs paciente claro | Ilustración dual | 2:45 — 3:30 |
| 5 | Prompt crudo: "crea un sistema de inventario" | Texto pequeño | 3:30 — 3:50 |
| 6 | Diagnóstico de /prompt | Texto + flechas | 3:50 — 4:15 |
| 7 | Prompt refinado en bloques | Estructura visible | 4:15 — 4:45 |
| 8 | Rúbrica antes/después | Tabla con ✓/⚠/✗ | 4:45 — 5:00 |
| 9 | Actividad: 5 pasos | Lista | 5:00 — 6:00 |
| 10 | Próximo: /capacidad | Cierre | 6:00 — 6:45 |

---

# === NOTAS DE PRODUCCIÓN ===

- **Slide 3 (las 10 dimensiones):** denso. Mostrar la lista con números 1-10 grandes a la izquierda y descripciones breves a la derecha. Si la lectura en voz alta dura más de 1:15 min, dividir en dos slides (1-5 y 6-10).
- **Slide 7 (prompt refinado):** mostrar la estructura como bloques apilados con bordes redondeados, no como bloque de código corrido. Da sensación de "respuesta estructurada" que es el punto.
- **Slide 8 (rúbrica antes/después):** usar verde para ✓, amarillo para ⚠, rojo para ✗. Es la metáfora visual del "diagnóstico médico" del prompt.
- **Frase exacta del bloque 6:** mostrar literal "/prompt " seguido del prompt original para que el espectador vea el formato exacto.

---

# === CHECKLIST DE 4 PILARES ===

```
PILAR 1 — ACTIVACIÓN  ✓
  La pregunta sobre las últimas 3 consultas conecta directo con
  comportamiento reciente del espectador.

PILAR 2 — ANCLAJE  ✓
  Analogía explícita "paciente vago vs paciente claro" en bloque 4 —
  es la analogía más concreta de la serie.

PILAR 3 — ORGANIZACIÓN  ✓
  Depende de Ep 3 (modos) que es referenciado en el ejemplo. No exige
  conocer la implementación técnica de /prompt.

PILAR 4 — APLICACIÓN  ✓
  Actividad produce un artefacto: refinado de un prompt propio + lista
  de las 2-3 dimensiones que el espectador omite habitualmente.
```
