---
episodio: 1
titulo: "Tu primer reflejo de calidad — el protocolo de 4 pasos"
duracion_objetivo_min: 6-7
concepto_central: "Auto-revisión sistemática antes de entregar la respuesta"
analogia_principal: "Un editor profesional revisa antes de publicar"
bloom: 3 — Aplicar
prerequisitos: Episodio 0
artefacto_producido: "Una respuesta propia de Claude pasada por el protocolo, con las grietas marcadas"
---

# Episodio 1 — Tu primer reflejo de calidad: el protocolo de 4 pasos

> **Función en la serie:** primera intervención operativa. Tras el
> diagnóstico del Ep 0, el espectador necesita una acción concreta de
> alto impacto y bajo esfuerzo. El protocolo de 4 pasos es exactamente
> eso: no instala nada, no aprende código, solo le pide a Claude que
> aplique una rutina de auto-revisión.

---

## [PANORAMA]

En el episodio anterior detectaste que las respuestas de Claude por
defecto tienen lagunas: datos sin verificar, fuentes ausentes,
estructura genérica. Hoy aprendes la primera técnica para tapar esas
lagunas sin tocar configuración técnica.

La técnica se llama **protocolo de calidad de 4 pasos** y es la
intervención de mayor impacto y menor esfuerzo de toda la serie. Una
vez interiorizada, cada respuesta de Claude pasa por una auto-revisión
que tú decides cuándo activar.

---

## [ACTIVACIÓN] — pregunta de diagnóstico

> *"Cuando entregas un informe importante en tu trabajo, ¿cuánto tardas
> en releerlo antes de mandarlo? Treinta segundos. Un minuto. Cinco.
> ¿Sabías que Claude puede hacer ese mismo paso de auto-revisión, pero
> a velocidad de máquina, en menos de un segundo, si le dices que lo
> haga?"*

La mayoría de los usuarios no le pide a Claude que se auto-revise
porque **no sabe que se puede pedir**. Eso termina hoy.

---

## [CONCEPTO CENTRAL]

El protocolo de calidad es una rutina de cuatro preguntas que Claude
se hace a sí mismo antes de entregar una respuesta:

```
PASO 1 — VERIFICACIÓN DE HECHOS
  ¿Cada afirmación que voy a decir es correcta?
  ¿Tengo certeza o debo marcarla como estimación?
  Si hay duda → marcar con [⚠ verificar].

PASO 2 — REVISIÓN DE COHERENCIA
  ¿La respuesta es consistente internamente?
  ¿No me contradigo entre párrafos?
  ¿El nivel de profundidad es apropiado para la pregunta?

PASO 3 — COMPROBACIÓN DE FUENTES
  ¿Cité fuentes donde corresponde?
  ¿Distinguí entre hecho documentado, inferencia y opinión?
  ¿Hay alguna fuente más actual que la que estoy citando?

PASO 4 — REVISIÓN DE PRESENTACIÓN
  ¿La estructura va de lo general a lo particular?
  ¿Incluí al menos un dato de ejemplo concreto cuando corresponde?
  ¿La longitud es proporcional a la complejidad de la pregunta?
```

**Si algún paso falla → Claude corrige antes de entregar, nunca después.**

---

## [ANALOGÍA / ANCLA]

**Analogía:** *Un editor profesional revisa antes de publicar.*

Un escritor brillante puede producir un texto en treinta minutos. Un
editor profesional lo revisa en otros treinta y le quita exactamente las
tres cosas que el lector iba a notar: el dato sin fuente, la
contradicción entre el párrafo 2 y el párrafo 5, y la frase que asume
contexto que el lector no tiene.

El editor no es más inteligente que el escritor. Tiene una **rutina de
revisión**. Esa rutina, aplicada con disciplina, hace que cualquier
texto pase de bueno a defendible.

**El protocolo de 4 pasos es esa rutina, ejecutada por Claude sobre sí
mismo.**

---

## [EJEMPLO REAL]

**Sector:** ciberseguridad · **Rol:** consultor en gestión de riesgos · **Tarea:** explicar la diferencia entre ISO/IEC 27001 e ISO/IEC 27002 para un cliente que está iniciando su programa de cumplimiento.

### Respuesta sin protocolo

> *"ISO 27001 e ISO 27002 son normas relacionadas con la seguridad de
> la información. ISO 27001 establece los requisitos para un sistema
> de gestión de seguridad de la información, mientras que ISO 27002
> proporciona controles específicos que pueden implementarse. Ambas
> son ampliamente utilizadas para fortalecer la postura de seguridad."*

**Diagnóstico:** correcta en esencia, pero genérica. Sin año de versión
(ambas se actualizaron en 2022). Sin distinguir entre norma certificable
y norma de guía. Sin contexto de uso. Un cliente exigente lo notaría.

### Respuesta con protocolo aplicado

> *"ISO/IEC 27001:2022 es la norma **certificable**: establece los
> requisitos del Sistema de Gestión de Seguridad de la Información
> (SGSI) y es contra la que una organización se audita formalmente
> (Organización Internacional de Normalización, 2022a).
>
> ISO/IEC 27002:2022 es una norma **de guía complementaria**: no es
> certificable; proporciona el catálogo de 93 controles (en la versión
> 2022, frente a 114 controles en la versión 2013) con orientación
> de implementación (Organización Internacional de Normalización,
> 2022b).
>
> Para un programa que arranca: 27001 define **qué** debes tener;
> 27002 sugiere **cómo** implementarlo. La certificación se obtiene
> contra 27001; 27002 facilita la preparación pero no se audita."*

**Diagnóstico:** años explícitos, distinción certificable vs guía,
datos numéricos verificables (93 vs 114 controles), respuesta práctica
para el caso del cliente. **El paso 1 (verificación) descartó la
imprecisión de "ambas son ampliamente utilizadas".** El paso 4
(presentación) impuso la estructura *qué vs cómo*.

---

## [COMPETENCIA EN ACCIÓN]

El profesional competente:

- **Pide explícitamente** a Claude que aplique el protocolo de 4 pasos en respuestas con consecuencias profesionales.
- **Identifica** cuándo una respuesta tiene `[⚠ verificar]` y trata esa marca como una obligación, no como decoración.
- **No confunde** "respuesta extensa" con "respuesta revisada" — el protocolo evalúa rigor, no longitud.

Indicador conductual:

> *"El profesional competente, al pedir algo no trivial, escribe al
> menos una vez por sesión la frase 'aplica el protocolo de 4 pasos a
> tu respuesta' antes de usar el resultado en un entregable."*

---

## [ACTIVIDAD INTEGRADORA]

**Nombre del reto:** *Mi primera auto-revisión asistida*

**Descripción:**

1. Abre una conversación reciente con Claude donde la respuesta haya tenido un uso profesional.
2. Copia tu pregunta original al inicio de un nuevo prompt.
3. Pega la respuesta original que recibiste.
4. Añade: *"Aplica el protocolo de calidad de 4 pasos a esta respuesta. Dime explícitamente qué paso falló y qué corregirías."*
5. Observa el diagnóstico.

**Entregable:** una lista de 3-5 dudas marcadas con `[⚠ verificar]` que el protocolo levantó sobre tu respuesta original.

**Nivel de Bloom:** 3 — Aplicar
**Nivel de competencia:** Básico

---

## [EVALUACIÓN]

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Invocación del protocolo | Lo pide cuando se acuerda | Lo pide para respuestas con consecuencias profesionales | Internaliza el protocolo y lo aplica al leer cualquier respuesta |
| Tratamiento de `[⚠ verificar]` | Lo ignora | Lo investiga antes de usar | Lo trata como bloqueador hasta confirmar la fuente |
| Distinción rigor vs longitud | Cree que respuesta larga = revisada | Distingue pero a veces se deja llevar | Pide brevedad explícita y aún así exige protocolo |

---

## [TRANSFERENCIA AL PUESTO]

Indicador a 7 días: *"El profesional ha pedido el protocolo al menos tres veces en consultas reales y ha modificado al menos una decisión de trabajo basado en un `[⚠ verificar]` que el protocolo levantó."*

---

## [INVITACIÓN AL EPISODIO 2]

> *"Ya tienes la primera técnica: pedirle a Claude que se revise. Pero
> al revisar, ¿bajo qué estándar? ¿Cómo se estructura una respuesta
> profesional? ¿Cómo se citan fuentes en serio? En el próximo episodio
> vemos la forma — la estructura general → particular y la citación
> APA 7 — que convierten una respuesta correcta en una respuesta
> defendible."*

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Organización Internacional de Normalización. (2022a). *ISO/IEC
    27001:2022 — Information security, cybersecurity and privacy
    protection — Information security management systems —
    Requirements*. ISO.

Organización Internacional de Normalización. (2022b). *ISO/IEC
    27002:2022 — Information security, cybersecurity and privacy
    protection — Information security controls*. ISO.

Merrill, M. D. (2002). First principles of instruction. *Educational
    Technology Research and Development, 50*(3), 43–59.
    https://doi.org/10.1007/BF02505024

---

# === SCRIPT DE NARRACIÓN ===

> Tiempo objetivo: 6:00 — 7:00 min · Cadencia: 130-140 wpm

## Bloque 1 — Hook (0:00 — 0:30)

```
[Slide 1 — texto grande: "30 segundos para una mejora del 80%"]

[NARRACIÓN]

Si te dijera que existe una mejora a tu uso de Claude que toma treinta
segundos por consulta y eleva la calidad de las respuestas en un orden
de magnitud, ¿la probarías?

[PAUSA 2s]

Eso es lo que vamos a hacer hoy. No vas a instalar nada. No vas a
aprender a programar. Solo le vas a enseñar a Claude un reflejo: el
reflejo de revisar antes de entregar.
```

## Bloque 2 — Activación (0:30 — 1:15)

```
[Slide 2 — pregunta: "¿Cuánto tardas en releer un informe antes de mandarlo?"]

[NARRACIÓN]

Pregunta rápida.

Cuando entregas un informe importante en tu trabajo, ¿cuánto tardas
en releerlo antes de mandarlo? Treinta segundos. Un minuto. Cinco.

[PAUSA 2s]

Lo haces porque sabes que tu primer borrador tiene errores. Datos sin
verificar. Frases que se contradicen. Una conclusión que no se sigue
del análisis.

[ÉNFASIS] Claude tiene exactamente el mismo problema con su primer
borrador. Y tiene exactamente la misma solución: una rutina de
revisión que tú le pides aplicar. [/ÉNFASIS]
```

## Bloque 3 — Concepto central (1:15 — 2:45)

```
[Slide 3 — los 4 pasos numerados]

[NARRACIÓN]

El protocolo de calidad son cuatro preguntas que Claude se hace antes
de entregar.

Paso uno: verificación de hechos. ¿Cada afirmación es correcta? Si hay
duda, se marca explícitamente con el símbolo "verificar". No se borra,
no se ignora — se marca para que tú decidas.

Paso dos: coherencia. ¿No me contradigo entre el inicio y el final?
¿El nivel de detalle es proporcional a la pregunta?

Paso tres: fuentes. ¿Cité de dónde viene cada dato? ¿Distinguí entre
hecho documentado, inferencia razonada y opinión?

Paso cuatro: presentación. ¿La estructura va de lo general a lo
particular? ¿Hay al menos un ejemplo concreto? ¿La longitud es
proporcional a la complejidad?

[ÉNFASIS] Si algún paso falla, Claude corrige antes de entregar.
Nunca después. [/ÉNFASIS]
```

## Bloque 4 — Analogía (2:45 — 3:30)

```
[Slide 4 — ilustración: escritor + editor sobre la misma mesa]

[NARRACIÓN]

Una analogía.

Un escritor brillante puede producir un texto en treinta minutos. Un
editor profesional lo revisa en otros treinta y le quita exactamente
las tres cosas que el lector iba a notar: el dato sin fuente, la
contradicción entre el párrafo dos y el párrafo cinco, y la frase que
asume contexto que el lector no tiene.

[PAUSA 1s]

El editor no es más inteligente que el escritor. Tiene una rutina de
revisión.

[ÉNFASIS] El protocolo de cuatro pasos es esa rutina, ejecutada por
Claude sobre sí mismo. [/ÉNFASIS]
```

## Bloque 5 — Ejemplo real (3:30 — 5:00)

```
[Slide 5 — caso: consultor de ciberseguridad, ISO 27001 vs 27002]

[NARRACIÓN]

Un caso real. Un consultor de gestión de riesgos tiene que explicar a
un cliente la diferencia entre ISO 27001 e ISO 27002.

Sin protocolo, Claude responde algo así:

[Slide 6 — texto de la respuesta sin protocolo]

"ISO 27001 e ISO 27002 son normas relacionadas con la seguridad de la
información. La primera establece requisitos del sistema de gestión; la
segunda proporciona controles específicos."

[PAUSA 1s]

Correcto en esencia. Pero sin año de versión. Sin distinguir si una es
certificable y la otra no. Sin números concretos. Un cliente exigente
lo notaría.

[Slide 7 — texto de la respuesta CON protocolo]

Ahora con protocolo aplicado:

"ISO 27001 versión 2022 es la norma certificable. ISO 27002 versión
2022 es de guía complementaria, con 93 controles, frente a 114 que
tenía la versión de 2013. Para un programa que arranca: 27001 define
qué debes tener; 27002 sugiere cómo implementarlo."

[ÉNFASIS] El paso uno descartó la imprecisión de 'ambas son
ampliamente utilizadas'. El paso cuatro impuso la estructura 'qué vs
cómo'. Mismo modelo. Misma pregunta. Distinta respuesta. [/ÉNFASIS]
```

## Bloque 6 — Actividad (5:00 — 6:00)

```
[Slide 8 — actividad: 5 pasos]

[NARRACIÓN]

Tu turno.

Uno: abre una conversación reciente con Claude donde la respuesta haya
tenido un uso profesional.

Dos: copia tu pregunta original al inicio de un nuevo prompt.

Tres: pega la respuesta original que recibiste.

Cuatro: añade la siguiente frase, palabra por palabra: "Aplica el
protocolo de calidad de cuatro pasos a esta respuesta. Dime
explícitamente qué paso falló y qué corregirías".

Cinco: observa el diagnóstico.

[PAUSA 2s]

[ÉNFASIS] Lo que vas a ver es a Claude levantando, sobre su propia
respuesta, las dudas que tú habrías levantado al releerla — pero a
velocidad de máquina, sin que tú tuvieras que cazar cada error. [/ÉNFASIS]
```

## Bloque 7 — Cierre (6:00 — 6:45)

```
[Slide 9 — invitación a Ep 2]

[NARRACIÓN]

Ya tienes la primera técnica: pedirle a Claude que se revise.

Pero al revisar, bajo qué estándar. Cómo se estructura una respuesta
profesional. Cómo se citan fuentes en serio.

[PAUSA 1s]

En el próximo episodio vemos la forma — la estructura general a
particular y la citación APA 7ª edición — que convierten una respuesta
correcta en una respuesta defendible.

Nos vemos.

[Slide final 2s]
```

---

# === ESTRUCTURA DE SLIDES ===

| # | Título / Texto en pantalla | Visual | Duración |
|---|---|---|---|
| 1 | "30 segundos para una mejora del 80 %" | Texto grande, fondo limpio | 0:00 — 0:30 |
| 2 | "¿Cuánto tardas en releer un informe antes de mandarlo?" | Pregunta centrada | 0:30 — 1:15 |
| 3 | Los 4 pasos numerados | Lista con iconos simples | 1:15 — 2:45 |
| 4 | Escritor + editor (ilustración) | Minimal | 2:45 — 3:30 |
| 5 | Caso: ISO 27001 vs 27002 | Contexto del caso | 3:30 — 3:50 |
| 6 | Respuesta sin protocolo | Texto + crítica | 3:50 — 4:20 |
| 7 | Respuesta con protocolo | Texto destacado, números visibles | 4:20 — 5:00 |
| 8 | Actividad: 5 pasos | Lista numerada | 5:00 — 6:00 |
| 9 | Próximo: estructura + APA 7 | Cierre | 6:00 — 6:45 |

---

# === NOTAS DE PRODUCCIÓN ===

- **Frase exacta de invocación:** en el slide 8, mostrar literal el texto *"Aplica el protocolo de calidad de cuatro pasos a esta respuesta. Dime explícitamente qué paso falló y qué corregirías"* en una caja destacada, **para que el espectador pueda pegarla directamente**. Es el artefacto reutilizable de este episodio.
- **Pausa larga en slide 7:** el espectador necesita comparar visualmente respuesta sin protocolo vs con protocolo. Dar 3-4 segundos extra antes de continuar la narración.
- **No leer las referencias en voz alta:** las referencias APA 7 quedan en el documento, no en la narración. El audio se concentra en lo accionable.

---

# === CHECKLIST DE 4 PILARES ===

```
PILAR 1 — ACTIVACIÓN  ✓
  La pregunta sobre el tiempo de releer informes conecta con experiencia universal.

PILAR 2 — ANCLAJE  ✓
  Analogía del escritor + editor en bloque 4.

PILAR 3 — ORGANIZACIÓN  ✓
  Solo depende del Ep 0 (concepto "respuesta tiene lagunas"). No introduce
  modos ni configuración técnica.

PILAR 4 — APLICACIÓN  ✓
  Actividad produce un artefacto: la lista de [⚠ verificar] sobre una
  respuesta real del espectador.
```
