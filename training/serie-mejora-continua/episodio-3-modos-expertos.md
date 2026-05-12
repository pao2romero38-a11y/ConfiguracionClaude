---
episodio: 3
titulo: "Modos expertos — un especialista por tema"
duracion_objetivo_min: 7-8
concepto_central: "Encapsular reglas de dominio profesional en un comando reutilizable"
analogia_principal: "Ir al cardiólogo en vez del médico general"
bloom: 6 — Crear (básico: esqueleto de modo personalizado)
prerequisitos: Episodios 0, 1, 2
artefacto_producido: "Esqueleto de un modo experto personalizado para el dominio profesional del espectador"
---

# Episodio 3 — Modos expertos: un especialista por tema

> **Función en la serie:** primer salto cualitativo. Los Ep 1-2
> enseñaron técnicas genéricas. Este episodio introduce la idea de que
> Claude puede operar bajo **paquetes de reglas específicos de un
> dominio profesional**. Es donde la configuración se vuelve realmente
> propia.

---

## [PANORAMA]

Hasta ahora, todo lo que has aprendido aplica a cualquier consulta a
Claude. Hoy entras en territorio personalizado: **modos expertos**.

Un modo experto es un paquete de reglas profesionales que Claude
aplica al responder en un dominio específico. Cuando activas el modo
finanzas, Claude usa terminología NIF mexicanas o IFRS. Cuando activas
el modo seguridad, encuadra todo bajo NIST o ISO 27001. Cuando activas
el modo investigación, etiqueta cada afirmación con marcadores
epistémicos.

Esta configuración base trae **17 modos pre-construidos** y la
posibilidad de **componerlos** y de **crear modos propios** para tu
dominio profesional.

---

## [ACTIVACIÓN]

> *"¿Cuándo fue la última vez que le preguntaste algo a Claude
> relacionado con tu profesión y notaste que la respuesta era
> técnicamente correcta pero culturalmente fuera de lugar? Te habló
> en términos de US GAAP cuando trabajas con NIF mexicanas. Te citó
> NIST cuando tu organización usa ISO. Te recomendó un framework de
> proyectos que no encaja con cómo trabajas. ¿De quién fue la culpa?"*

[Pausa 3s]

Nadie tuvo la culpa. Le hablaste a un médico general cuando necesitabas
un cardiólogo. Hoy aprendes a llamar al cardiólogo.

---

## [CONCEPTO CENTRAL]

### Parte A — Qué es un modo

Un modo de operación es un comando que se escribe al inicio del
prompt para activar reglas específicas del dominio.

```
EJEMPLO:

/fin   Analiza la viabilidad financiera de un proyecto de
       50 millones con período de payback de 3 años.

       → Claude responde aplicando:
         · Marcos financieros (NIF/IFRS según contexto)
         · Métricas correctas (VPN, TIR, WACC, payback)
         · Advertencia obligatoria de no constituir asesoría de inversión
         · Referencias APA 7 del dominio financiero
```

Los **17 modos pre-construidos** se agrupan en:

```
CORE          /dev · /edu · /inv

EXPERTOS      /fin · /mkt · /tec · /proy · /seg · /rsk
              /ci · /aud · /dis · /cost · /tra

IA            /ai · /ai-llm · /ai-ml
```

### Parte B — Composición de modos

Cuando una tarea cruza dominios, los modos se combinan con la regla
**líder + apoyo**:

```
/proy +fin +rsk
  ↑     ↑    ↑
  │     │    └── apoyo: aporta criterios de riesgos
  │     └────── apoyo: aporta criterios financieros
  └────────── líder: define la estructura de la respuesta

REGLA: máximo 1 líder + 2 apoyos (3 skills totales).
```

El líder define **cómo se estructura** la respuesta. Los apoyos
aportan **criterios** dentro de las secciones del líder. No es
"hacer tres análisis paralelos" — es una respuesta única enriquecida
por tres marcos de criterios.

---

## [ANALOGÍA / ANCLA]

**Analogía:** *Ir al cardiólogo en vez del médico general.*

El médico general sabe mucho de todo. Para un dolor de cabeza, te
sirve. Para un problema cardíaco serio, quieres al cardiólogo: alguien
que tiene en la cabeza **300 referencias específicas, 50 medicamentos
de su especialidad, 20 protocolos de emergencia y la sensibilidad para
notar lo que un general pasaría por alto**.

Activar `/fin` es ir al especialista financiero. Activar `/seg +rsk` es
pedir el especialista de seguridad acompañado por el especialista de
riesgos. Y `/proy +fin +rsk` es el equipo completo para evaluar una
inversión: el PMO lidera, el financiero aporta números, el de riesgos
aporta su matriz.

**Sin activar modo, le estás hablando al médico general.**

---

## [EJEMPLO REAL]

**Sector:** financiero · **Rol:** asociado de M&A en banca de inversión · **Tarea:** evaluar la viabilidad de adquirir una pequeña empresa de software de gestión por 80 millones de pesos, con riesgos regulatorios pendientes.

### Sin modo activado

> *"La adquisición de una empresa de software por 80 millones de pesos
> requiere un análisis cuidadoso de su valor presente, los flujos
> futuros esperados, las sinergias con la compradora y los riesgos
> regulatorios. Es recomendable hacer un due diligence completo."*

**Diagnóstico:** correcto pero superficial. No aplica métricas
específicas, no menciona regulación mexicana (PROFECO, INAI, COFECE),
no estructura como evaluación PMI.

### Con `/proy +fin +rsk`

> *"**Estructura de evaluación (PMO).** Decisión GO/NO-GO basada en
> análisis multi-criterio: financiero, riesgos, integración operativa.
>
> **Análisis financiero (`/fin`).** VPN proyectado a 5 años a tasa de
> descuento WACC del comprador (estimar 12-14 %), TIR comparada contra
> hurdle rate del comité de inversión, payback ajustado por riesgo de
> ejecución. Considerar valor terminal con múltiplo EV/EBITDA del
> sector (mediana 8-12x para SaaS B2B mexicano según información
> pública 2023-2024 [⚠ verificar fecha]).
>
> **Análisis de riesgos (`/rsk`).** Matriz P×I de los riesgos
> identificados, con foco en:
> · Riesgo regulatorio: pendientes con PROFECO/INAI (probabilidad
>   alta dada la naturaleza del software).
> · Riesgo de retención del equipo clave (probabilidad media en
>   adquisiciones de software).
> · Riesgo de integración tecnológica (probabilidad media-baja).
> KRIs sugeridos: NPS de clientes existentes, % rotación de devs
> clave a 90 / 180 días post-cierre.
>
> **Recomendación condicional.** GO si VPN > 0 a WACC + prima de
> riesgo de 200 bps. NO-GO si los pendientes regulatorios implican
> contingencia > 15 % del precio.
>
> ⚠ Esta respuesta es informativa y no constituye asesoría de
> inversión. Para decisiones reales: consultar al comité de
> inversión y a asesoría legal externa especializada en M&A en
> México."*

**Diagnóstico:** estructura del modo líder (PMO), criterios del modo
apoyo financiero (VPN/TIR/WACC), criterios del modo apoyo de riesgos
(matriz P×I, KRIs), datos verificables, advertencia legal obligatoria.
**Un asociado podría llevar esta respuesta al primer borrador del
memo del comité.**

---

## [COMPETENCIA EN ACCIÓN]

El profesional competente:

- **Activa el modo correcto** al inicio de la consulta, no después.
- **Compone modos** cuando la tarea cruza dominios (no fuerza un modo a hacer todo).
- **Identifica el modo líder** primero (¿qué estructura espero?) y luego añade apoyos (¿qué criterios necesito que se apliquen?).

Indicador conductual:

> *"El profesional competente, al iniciar una sesión con Claude para
> una tarea profesional, escribe el modo apropiado antes de la primera
> pregunta — no después de recibir una primera respuesta
> insatisfactoria."*

---

## [ACTIVIDAD INTEGRADORA]

**Nombre del reto:** *Diseñar el esqueleto de mi modo personalizado*

**Descripción:**

Vas a diseñar el **esqueleto** de un modo experto propio. Aún no lo
vas a implementar — solo dibujar su contenido.

1. Identifica un dominio profesional **propio tuyo** que no esté en los
   17 modos pre-construidos. Ejemplos: notaría pública, compliance
   farmacéutico, ciencia de datos en retail, consultoría de turismo
   sustentable, peritaje agronómico, ...
2. Lista 5-8 **reglas profesionales** que un experto en ese dominio
   siempre aplica. Ejemplos:
   - "Toda recomendación cita el artículo legal aplicable"
   - "Las cantidades en USD/MXN se convierten a la fecha de la consulta"
   - "Cualquier diagnóstico médico se acompaña de la advertencia de
     consultar profesional certificado"
3. Identifica el **marco normativo o de referencia** del dominio.
4. Define la **estructura de entrega** que un experto del dominio espera ver.

**Entregable:** un documento de 1-2 páginas con: nombre del modo,
verbo de activación (ej. `/notario` o `/farma`), reglas profesionales
listadas, marco normativo, estructura de entrega. **No es código —
es el esqueleto pedagógico.**

**Nivel de Bloom:** 6 — Crear (básico)
**Nivel de competencia:** Intermedio

> **Próximo paso natural** (fuera del alcance de la serie): este
> esqueleto puede convertirse en un archivo `SKILL.md` que se añade a
> la configuración. La serie no te enseña la implementación técnica,
> pero te enseña qué pedirle a Claude (o a un colaborador técnico) para
> que el modo quede instalado.

---

## [EVALUACIÓN]

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Selección de modo | Usa un modo cuando alguien le sugiere | Identifica solo el modo apropiado por consulta | Compone líder + apoyo sin titubear |
| Diseño de modo propio | Lista reglas pero sin marco normativo | Lista reglas + marco normativo + estructura | Diseña modo con advertencias obligatorias y referencias del dominio |
| Composición | Solo usa un modo a la vez | Compone con un apoyo cuando aplica | Compone con 2 apoyos respetando regla 1+2 |

---

## [TRANSFERENCIA AL PUESTO]

Indicador a 7 días: *"El profesional ha activado modos pre-construidos en al menos 5 consultas reales y ha presentado el esqueleto de su modo personalizado a alguien de su equipo para validar la lista de reglas."*

---

## [INVITACIÓN AL EPISODIO 4]

> *"Tienes la forma (Ep 2) y el especialista (Ep 3). Sigue faltando lo
> más invisible: **cómo formulas TÚ la pregunta**. Una pregunta vaga
> al especialista correcto sigue produciendo respuestas vagas. En el
> siguiente episodio aprendes la meta-skill `/prompt` — la herramienta
> para afinar lo que TÚ preguntas antes de mandarlo."*

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Institute of Internal Auditors. (2024). *Global internal audit
    standards*. IIA.

Project Management Institute. (2021). *A guide to the project
    management body of knowledge (PMBOK guide)* (7th ed.). PMI.

International Organization for Standardization. (2018). *ISO 31000:2018
    — Risk management — Guidelines*. ISO.

---

# === SCRIPT DE NARRACIÓN ===

> Tiempo objetivo: 7:00 — 8:00 min · Cadencia: 130-140 wpm

## Bloque 1 — Hook (0:00 — 0:30)

```
[Slide 1 — texto: "Dejaste de hablarle al médico general"]

[NARRACIÓN]

Hoy dejas de hablarle al médico general.

[PAUSA 2s]

Hasta ahora todo lo que has aprendido aplica a cualquier consulta. Hoy
entras en territorio personalizado: modos expertos.
```

## Bloque 2 — Activación (0:30 — 1:30)

```
[Slide 2 — pregunta: "¿Te habló en US GAAP cuando trabajas con NIF?"]

[NARRACIÓN]

Pregunta.

La última vez que le preguntaste algo a Claude relacionado con tu
profesión, ¿notaste que la respuesta era técnicamente correcta pero
culturalmente fuera de lugar? Te habló en US GAAP cuando trabajas con
NIF mexicanas. Te citó NIST cuando tu organización usa ISO. Te
recomendó un framework de proyectos que no encaja con cómo trabajas.

¿De quién fue la culpa?

[PAUSA 3s]

[ÉNFASIS] De nadie. Le hablaste a un médico general cuando necesitabas
un cardiólogo. Hoy aprendes a llamar al cardiólogo. [/ÉNFASIS]
```

## Bloque 3 — Concepto: qué es un modo (1:30 — 3:00)

```
[Slide 3 — los 17 modos agrupados]

[NARRACIÓN]

Un modo es un comando que se escribe al inicio del prompt para activar
reglas específicas del dominio.

Cuando activas /fin, Claude usa NIF mexicanas o IFRS según contexto,
métricas como VPN, TIR, WACC, y siempre añade la advertencia de no
constituir asesoría de inversión.

Cuando activas /seg, encuadra bajo NIST o ISO 27001 y diferencia
controles preventivos de detectivos.

La configuración trae diecisiete modos pre-construidos.

[Slide 4 — grupos: CORE / EXPERTOS / IA]

Se agrupan en tres familias.

Core: /dev para programación, /edu para capacitación, /inv para
investigación rigurosa.

Expertos: /fin, /mkt, /tec, /proy, /seg, /rsk, /ci, /aud, /dis, /cost,
/tra. Once dominios profesionales.

IA: /ai para estrategia organizacional, /ai-llm para aplicaciones con
modelos de lenguaje, /ai-ml para MLOps.
```

## Bloque 4 — Composición (3:00 — 4:00)

```
[Slide 5 — sintaxis /lider +apoyo +apoyo]

[NARRACIÓN]

Cuando una tarea cruza dominios, los modos se combinan con la regla
"líder más apoyo".

Por ejemplo: /proy más /fin más /rsk para evaluar viabilidad de una
inversión. El modo /proy lidera la estructura. El modo /fin aporta
criterios financieros — VPN, TIR. El modo /rsk aporta la matriz de
probabilidad por impacto.

Regla dura: máximo un líder más dos apoyos. Tres skills totales.

[PAUSA 1s]

[ÉNFASIS] No es hacer tres análisis paralelos. Es una sola respuesta,
con la estructura del líder, enriquecida por los criterios de los
apoyos. [/ÉNFASIS]
```

## Bloque 5 — Analogía (4:00 — 4:45)

```
[Slide 6 — ilustración: médico general vs equipo de especialistas]

[NARRACIÓN]

La analogía.

El médico general sabe mucho de todo. Para un dolor de cabeza, te
sirve. Para un problema cardíaco serio, quieres al cardiólogo —
alguien que tiene en la cabeza trescientas referencias específicas,
cincuenta medicamentos de su especialidad, veinte protocolos de
emergencia.

Activar /fin es ir al especialista financiero. Activar /seg más /rsk
es pedir el especialista de seguridad acompañado por el de riesgos.

[ÉNFASIS] Sin activar modo, le estás hablando al médico general.
Todo el tiempo. [/ÉNFASIS]
```

## Bloque 6 — Ejemplo real (4:45 — 6:00)

```
[Slide 7 — caso: asociado de M&A, adquisición de empresa de software]

[NARRACIÓN]

Un caso. Un asociado de M&A en banca de inversión tiene que evaluar la
adquisición de una empresa de software por ochenta millones de pesos,
con riesgos regulatorios pendientes.

[Slide 8 — respuesta sin modo: genérica]

Sin modo, Claude le dice algo así: "La adquisición requiere análisis
cuidadoso de su valor presente y los flujos futuros. Es recomendable
hacer un due diligence completo".

Correcto pero superficial. Sin métricas específicas. Sin regulación
mexicana. Sin estructura PMI.

[Slide 9 — con /proy +fin +rsk: estructurada]

Con /proy más /fin más /rsk, la respuesta se estructura así:

Decisión GO/NO-GO, modo PMO.
Análisis financiero con VPN, TIR, WACC del comprador estimado en doce
a catorce por ciento.
Análisis de riesgos con matriz probabilidad por impacto, foco en
PROFECO, INAI, retención del equipo clave.
Recomendación condicional con umbral cuantificable.
Advertencia obligatoria de no constituir asesoría de inversión.

[ÉNFASIS] Un asociado podría llevar esa respuesta al primer borrador
del memo del comité de inversión. [/ÉNFASIS]
```

## Bloque 7 — Actividad (6:00 — 7:00)

```
[Slide 10 — actividad: diseñar tu modo]

[NARRACIÓN]

Tu turno. Hoy haces algo más ambicioso que en episodios anteriores.

Vas a diseñar el esqueleto de un modo experto **propio tuyo**.

Uno: identifica un dominio profesional tuyo que no esté en los
diecisiete modos pre-construidos. Notaría. Compliance farmacéutico.
Peritaje agronómico. Lo que sea tu especialidad.

Dos: lista cinco a ocho reglas profesionales que un experto en ese
dominio siempre aplica.

Tres: identifica el marco normativo del dominio.

Cuatro: define la estructura de entrega que un experto del dominio
espera ver.

[PAUSA 2s]

[ÉNFASIS] No es código. Es el esqueleto pedagógico. Si después decides
implementarlo técnicamente, ya tienes el contenido. Eso lo cubrimos en
la cadencia normal de configuración del proyecto. [/ÉNFASIS]
```

## Bloque 8 — Cierre (7:00 — 7:30)

```
[Slide 11 — invitación a Ep 4]

[NARRACIÓN]

Tienes la forma del Ep 2. Tienes el especialista del Ep 3.

Sigue faltando lo más invisible: cómo formulas tú la pregunta. Una
pregunta vaga al especialista correcto sigue produciendo respuestas
vagas.

En el siguiente episodio: la meta-skill /prompt — la herramienta para
afinar lo que tú preguntas antes de mandarlo.

[Slide final]
```

---

# === ESTRUCTURA DE SLIDES ===

| # | Título / Texto en pantalla | Visual | Duración |
|---|---|---|---|
| 1 | "Dejaste de hablarle al médico general" | Texto centrado | 0:00 — 0:30 |
| 2 | "¿Te habló en US GAAP cuando trabajas con NIF?" | Pregunta | 0:30 — 1:30 |
| 3 | Ejemplo de /fin | Diagrama prompt → reglas activadas | 1:30 — 2:15 |
| 4 | 17 modos en 3 grupos | CORE / EXPERTOS / IA | 2:15 — 3:00 |
| 5 | Sintaxis /lider +apoyo +apoyo | Diagrama de composición | 3:00 — 4:00 |
| 6 | Médico general vs equipo de especialistas | Ilustración | 4:00 — 4:45 |
| 7 | Caso M&A: contexto | Slide de tarea | 4:45 — 5:00 |
| 8 | Respuesta sin modo | Texto + crítica | 5:00 — 5:20 |
| 9 | Respuesta con /proy +fin +rsk | Texto estructurado en 4 bloques | 5:20 — 6:00 |
| 10 | Actividad: diseñar tu modo | 4 pasos | 6:00 — 7:00 |
| 11 | Próximo: /prompt | Cierre | 7:00 — 7:30 |

---

# === NOTAS DE PRODUCCIÓN ===

- **Slide 4 (los 17 modos):** muy denso visualmente. Usar 3 cajas claramente diferenciadas con color para cada grupo. No leer los 17 nombres en voz alta — solo los grupos.
- **Slide 9 (respuesta con composición):** mostrar los 4 bloques (PMO / financiero / riesgos / recomendación) con bordes de colores distintos que correspondan a cada modo activo. Es la metáfora visual del episodio.
- **Pausa larga al final del bloque 4 (composición):** el concepto de "líder + apoyo" es nuevo y necesita asentarse. 2-3 segundos antes de seguir.
- **Cuidado con la advertencia legal del ejemplo:** la frase "no constituye asesoría de inversión" debe leerse en voz alta para subrayar que es una de las reglas profesionales del modo /fin.

---

# === CHECKLIST DE 4 PILARES ===

```
PILAR 1 — ACTIVACIÓN  ✓
  La pregunta sobre "respuesta culturalmente fuera de lugar" conecta con
  la experiencia profesional propia del espectador.

PILAR 2 — ANCLAJE  ✓
  Analogía explícita "médico general vs cardiólogo / equipo de
  especialistas" en bloque 5.

PILAR 3 — ORGANIZACIÓN  ✓
  Depende de Ep 0 (notar lagunas) y Ep 2 (estructura visible). No exige
  programación ni conocimiento de YAML.

PILAR 4 — APLICACIÓN  ✓
  La actividad produce un artefacto: esqueleto del modo personalizado del
  espectador. Por primera vez en la serie, el espectador CREA contenido
  para la configuración.
```
