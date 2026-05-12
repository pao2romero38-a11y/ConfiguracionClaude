---
episodio: 2
titulo: "Estructura, fuentes y APA 7ª edición"
duracion_objetivo_min: 5-6
concepto_central: "La forma de la respuesta importa tanto como el contenido"
analogia_principal: "Leer un paper científico vs leer un blog"
bloom: 4 — Analizar
prerequisitos: Episodios 0, 1
artefacto_producido: "Una respuesta de Claude reformateada por el espectador a estructura general → particular + APA 7"
---

# Episodio 2 — Estructura, fuentes y APA 7ª edición

> **Función en la serie:** segundo nivel de calidad. El Ep 1 enseñó la
> rutina de auto-revisión; este episodio enseña el **estándar** contra
> el cual revisar. Sin un estándar visible, el protocolo del Ep 1 no
> sabe qué corregir.

---

## [PANORAMA]

Una respuesta profesional no se reconoce por lo que dice — se reconoce
por **cómo lo dice**. Un paper científico y una nota de blog pueden
cubrir el mismo tema; uno se cita en una tesis, el otro no. La
diferencia no está en la inteligencia del autor; está en la
**estructura** y en las **fuentes**.

Hoy aprendes los dos estándares visibles que convierten una respuesta
correcta en una respuesta defendible:

1. **Estructura general → particular**, en 5 niveles.
2. **Citación APA 7ª edición**, ordenada de más reciente a más antigua.

Ambos son estándares de la comunidad científica; ambos se pueden
pedir a Claude como rutina.

---

## [ACTIVACIÓN]

> *"Piensa en la última vez que leíste un texto profesional largo —
> un informe de auditoría, un white paper, una tesis. ¿Qué fue lo
> primero que leíste antes de meterte en los detalles? Casi seguro
> fue un resumen ejecutivo o un panorama general. ¿Por qué los textos
> serios siempre empiezan así, y un blog rara vez lo hace?"*

[Pausa 4s]

La respuesta es que el lector profesional necesita **decidir si seguir
leyendo** antes de invertir 20 minutos. El panorama general le da esa
decisión. Y la lista de referencias al final le da el segundo dato
crítico: **¿con quién está discutiendo este texto?**

---

## [CONCEPTO CENTRAL]

### Parte A — Estructura general → particular (5 niveles)

Toda respuesta profesional sigue esta jerarquía:

```
NIVEL 1 — PANORAMA
  ¿Qué es esto en términos amplios? ¿Cuál es su relevancia hoy?

NIVEL 2 — CATEGORÍAS O DIMENSIONES
  ¿Cuáles son las grandes divisiones del tema?

NIVEL 3 — DETALLE ESPECÍFICO
  ¿Cómo funciona en la práctica? Mecanismos concretos.

NIVEL 4 — EJEMPLO O CASO PARTICULAR
  Caso real con datos concretos: quién, cuándo, dónde, resultado.

NIVEL 5 — FUENTES
  Lista de referencias en APA 7, más reciente → más antigua.
```

El lector que solo lee el Nivel 1 sale con la idea principal. El que
lee hasta el Nivel 4 sale con la idea aplicada. El que necesita
auditarlo va al Nivel 5.

### Parte B — APA 7ª edición — reglas mínimas

```
□ Ordenar referencias de MÁS RECIENTE a MÁS ANTIGUA
  (regla de actualidad: la fuente nueva supera a la vieja
   si ambas son válidas)

□ Sangría francesa: primera línea al margen, resto indentadas

□ Año visible siempre: (Autor, 2024) — APA 7 lo exige

□ DOI obligatorio cuando existe; URL cuando no hay DOI

□ Dos autores en el texto: (García & López, 2024)

□ Tres o más autores: (García et al., 2024)

□ Si no tienes acceso al original: declarar cita de cita explícitamente
```

---

## [ANALOGÍA / ANCLA]

**Analogía:** *Leer un paper científico vs leer un blog.*

Un blog y un paper pueden cubrir el mismo tema con la misma idea
correcta. Pero:

- El blog te lo cuenta linealmente: dato, dato, opinión, dato.
- El paper te da contexto, luego categorías, luego mecanismo, luego un caso, y al final una lista de quién más ha dicho esto.

Cuando le pides a Claude algo profesional, **estás pidiendo el paper,
no el blog**. Pero por defecto te da el blog. Configurarlo es decirle:
*"a partir de ahora, dame papers."*

---

## [EJEMPLO REAL]

**Sector:** auditoría interna · **Rol:** gerente de auditoría · **Tarea:** redactar un punto del informe trimestral sobre el estado del control interno en una empresa.

### Respuesta sin estructura ni APA 7

> *"El control interno de la empresa ha mejorado en los últimos meses.
> Se han implementado nuevos controles en el área financiera y se han
> reducido las desviaciones. Sin embargo, persisten áreas de oportunidad
> en la segregación de funciones del proceso de compras. Se recomienda
> reforzar la supervisión."*

**Diagnóstico:** sin niveles, sin datos, sin fuentes, sin marco
normativo. Un comité de auditoría externo lo devolvería pidiendo
respaldo.

### Respuesta con estructura general → particular + APA 7

> *"**Panorama (Nivel 1).** El sistema de control interno opera bajo
> el marco COSO 2013, con un avance estimado del 72 % de madurez en
> los componentes de ambiente, evaluación de riesgos y actividades de
> control (Committee of Sponsoring Organizations of the Treadway
> Commission, 2013).
>
> **Dimensiones (Nivel 2).** Tres áreas se evaluaron en este
> trimestre: tesorería, compras y cierre contable.
>
> **Detalle (Nivel 3).** En compras, el proceso muestra deficiencia
> material en segregación de funciones: el mismo rol crea proveedor,
> autoriza orden de compra y registra la recepción de mercancía.
>
> **Caso (Nivel 4).** En la muestra del trimestre se detectaron 14
> órdenes en las que el mismo usuario completó las tres fases en menos
> de 5 minutos.
>
> **Recomendación.** Implementar dual control sobre la creación de
> proveedores, conforme a los Estándares Globales de Auditoría Interna
> (Institute of Internal Auditors, 2024).
>
> **Referencias.**
> Institute of Internal Auditors. (2024). *Global internal audit
>     standards*. IIA.
> Committee of Sponsoring Organizations of the Treadway Commission.
>     (2013). *Internal control — integrated framework*. COSO."*

**Diagnóstico:** los 5 niveles visibles, dato concreto (14 órdenes en
< 5 min), marco normativo citado, referencias en APA 7 más reciente →
más antigua. Defendible ante el comité de auditoría.

---

## [COMPETENCIA EN ACCIÓN]

El profesional competente:

- **Detecta a primera vista** si una respuesta sigue la estructura general → particular.
- **Identifica** referencias mal formateadas (sin año visible, ordenadas de antigua a reciente, sin DOI cuando existe).
- **Pide la estructura explícitamente** cuando la respuesta va a un entregable formal.

Indicador conductual:

> *"El profesional competente, al leer una respuesta de Claude, ubica
> primero el Nivel 1 (panorama) antes de evaluar el resto. Si no lo
> encuentra, devuelve la respuesta a reformatear."*

---

## [ACTIVIDAD INTEGRADORA]

**Nombre del reto:** *Reformatear a estándar profesional*

**Descripción:**

1. Toma una respuesta de Claude reciente sobre un tema profesional.
2. Inicia un nuevo prompt con: *"Reformatea la siguiente respuesta a estructura general → particular en 5 niveles, y añade una sección final de referencias en APA 7ª edición ordenadas de más reciente a más antigua. Si necesitas afirmar algo sin fuente, márcalo con la etiqueta [estimado]."*
3. Compara las dos versiones lado a lado.

**Entregable:** las dos versiones (antes / después) en un solo documento, con notas tuyas sobre **qué dimensión nueva apareció** en la versión reformateada.

**Nivel de Bloom:** 4 — Analizar
**Nivel de competencia:** Básico → Intermedio

---

## [EVALUACIÓN]

| Criterio | Básico | Intermedio | Avanzado |
|---|---|---|---|
| Detección de niveles | Distingue introducción y conclusión | Identifica los 5 niveles general → particular | Nota cuándo un nivel está vacío o desproporcionado |
| Lectura de referencias | Las ignora | Verifica que estén en APA 7 | Detecta cuando el orden no es más reciente → más antigua |
| Aplicación a entregables | Lo pide cuando se acuerda | Lo pide rutinariamente para entregables externos | Pide la estructura ANTES de preguntar, no después |

---

## [TRANSFERENCIA AL PUESTO]

Indicador a 7 días: *"El profesional ha pedido al menos una vez la estructura general → particular para un entregable real, y ha verificado al menos una lista de referencias contra las reglas APA 7."*

---

## [INVITACIÓN AL EPISODIO 3]

> *"Tienes el protocolo de revisión y tienes el estándar de
> presentación. Lo que aún te falta es lo más interesante: **reglas
> propias de tu dominio profesional**. Las NIF mexicanas para finanzas,
> el ISO 27001 para seguridad, el marco COSO para control interno. Esas
> reglas no caben en cuatro pasos genéricos — necesitan un modo experto.
> En el siguiente episodio aprendes qué son los modos y cómo se
> componen."*

---

## [REFERENCIAS] — APA 7, más reciente → más antigua

Institute of Internal Auditors. (2024). *Global internal audit
    standards*. IIA.

American Psychological Association. (2020). *Publication manual of
    the American Psychological Association* (7th ed.).
    https://doi.org/10.1037/0000165-000

Committee of Sponsoring Organizations of the Treadway Commission.
    (2013). *Internal control — integrated framework*. COSO.

---

# === SCRIPT DE NARRACIÓN ===

> Tiempo objetivo: 5:00 — 6:00 min · Cadencia: 130-140 wpm

## Bloque 1 — Hook (0:00 — 0:30)

```
[Slide 1 — texto: "Una respuesta correcta puede no ser defendible"]

[NARRACIÓN]

Una respuesta puede ser correcta y aún así no ser defendible.

[PAUSA 2s]

¿Cómo? Cuando le falta la **forma** que el lector profesional espera.
Hoy vemos la forma.
```

## Bloque 2 — Activación (0:30 — 1:15)

```
[Slide 2 — pregunta: "¿Cuándo fue la última vez que leíste un paper
                      vs un blog sobre el mismo tema?"]

[NARRACIÓN]

Piensa en algún tema donde hayas leído un texto profesional largo
—un informe, un white paper, una tesis—. ¿Qué fue lo primero que
leíste antes de meterte en los detalles?

[PAUSA 3s]

Casi seguro fue un resumen ejecutivo, un panorama. ¿Por qué los textos
serios siempre empiezan así, y un blog rara vez lo hace?

[ÉNFASIS] Porque el lector profesional necesita decidir si seguir
leyendo antes de invertir veinte minutos. El panorama le da esa
decisión. Las referencias al final le dan la otra decisión: con quién
está discutiendo este texto. [/ÉNFASIS]
```

## Bloque 3 — Concepto central A (1:15 — 2:30)

```
[Slide 3 — los 5 niveles general → particular, con iconos]

[NARRACIÓN]

Toda respuesta profesional sigue cinco niveles.

Nivel uno: panorama. Qué es esto en términos amplios. Por qué importa
hoy.

Nivel dos: dimensiones o categorías. Cuáles son las grandes divisiones
del tema.

Nivel tres: detalle. Cómo funciona en la práctica.

Nivel cuatro: ejemplo. Un caso concreto con quién, cuándo, dónde y
resultado.

Nivel cinco: fuentes. Lista de referencias.

[PAUSA 2s]

[ÉNFASIS] El lector que solo lee el Nivel uno sale con la idea
principal. El que lee hasta el Nivel cuatro sale con la idea aplicada.
El que necesita auditarlo va al Nivel cinco. [/ÉNFASIS]
```

## Bloque 4 — Concepto central B (2:30 — 3:15)

```
[Slide 4 — reglas APA 7 mínimas]

[NARRACIÓN]

Las referencias siguen el estándar APA séptima edición. Las reglas
mínimas:

Una: ordenar de más reciente a más antigua. La fuente nueva supera a
la vieja si ambas son válidas.

Dos: año visible siempre. APA siete lo exige.

Tres: DOI obligatorio cuando existe. URL cuando no hay DOI.

Cuatro: tres o más autores se citan como "García et al., año".

[PAUSA 1s]

No es decoración académica. Es lo que permite que tu lector pueda
verificar lo que afirmas en treinta segundos.
```

## Bloque 5 — Ejemplo real (3:15 — 4:30)

```
[Slide 5 — caso: gerente de auditoría, informe trimestral]

[NARRACIÓN]

Un caso. Un gerente de auditoría tiene que redactar un punto del
informe trimestral sobre el estado del control interno.

[Slide 6 — texto: respuesta sin estructura]

Sin estructura, Claude dice: "El control interno ha mejorado. Se han
implementado nuevos controles. Persisten áreas de oportunidad. Se
recomienda reforzar la supervisión."

[PAUSA 1s]

Correcto, pero sin datos, sin marco normativo, sin fuente. Un comité
de auditoría externo lo devolvería.

[Slide 7 — texto: respuesta con estructura + APA 7]

Con estructura general a particular y APA 7, la misma respuesta se
estructura en cinco bloques visibles: panorama bajo marco COSO 2013,
las tres áreas evaluadas, el detalle de la deficiencia material en
compras, el caso concreto de 14 órdenes completadas en menos de cinco
minutos por el mismo usuario, y al final las referencias al marco
COSO y a los estándares globales del IIA, ambas en APA 7, más reciente
arriba.

[ÉNFASIS] La diferencia entre "respuesta" y "evidencia
auditable". [/ÉNFASIS]
```

## Bloque 6 — Actividad (4:30 — 5:30)

```
[Slide 8 — actividad: 3 pasos]

[NARRACIÓN]

Tu turno.

Uno: toma una respuesta de Claude reciente sobre un tema profesional.

Dos: inicia un nuevo prompt con esta frase exacta, "Reformatea la
siguiente respuesta a estructura general a particular en cinco
niveles, y añade una sección final de referencias en APA séptima
edición ordenadas de más reciente a más antigua. Si necesitas afirmar
algo sin fuente, márcalo con la etiqueta 'estimado'".

Tres: compara las dos versiones lado a lado.

[ÉNFASIS] Lo que vas a ver es la misma información, pero ahora
auditable. Y el costo fue treinta segundos de tu tiempo. [/ÉNFASIS]
```

## Bloque 7 — Cierre (5:30 — 6:00)

```
[Slide 9 — invitación a Ep 3]

[NARRACIÓN]

Tienes el protocolo y tienes la forma. Lo que aún te falta es lo más
interesante: reglas propias de tu dominio profesional. NIF para
finanzas. ISO 27001 para seguridad. COSO para control interno.

Esas reglas no caben en cuatro pasos genéricos. Necesitan un modo
experto.

[PAUSA 1s]

En el siguiente episodio aprendes qué son los modos y cómo se componen.

[Slide final]
```

---

# === ESTRUCTURA DE SLIDES ===

| # | Título / Texto en pantalla | Visual | Duración |
|---|---|---|---|
| 1 | "Una respuesta correcta puede no ser defendible" | Texto centrado | 0:00 — 0:30 |
| 2 | "¿Paper vs blog sobre el mismo tema?" | Pregunta | 0:30 — 1:15 |
| 3 | Los 5 niveles general → particular | Lista con iconos | 1:15 — 2:30 |
| 4 | Reglas APA 7 mínimas | Lista numerada | 2:30 — 3:15 |
| 5 | Caso: gerente de auditoría | Contexto | 3:15 — 3:30 |
| 6 | Respuesta sin estructura | Texto + crítica | 3:30 — 3:50 |
| 7 | Respuesta con estructura + APA 7 | Texto con niveles destacados | 3:50 — 4:30 |
| 8 | Actividad: 3 pasos | Lista | 4:30 — 5:30 |
| 9 | Próximo: modos expertos | Cierre | 5:30 — 6:00 |

---

# === NOTAS DE PRODUCCIÓN ===

- **Slide 7 con resaltado por nivel:** mostrar los cinco niveles del párrafo con un color distinto cada uno (panorama / dimensiones / detalle / caso / referencias). Es la metáfora visual más fuerte del episodio.
- **Frase de invocación copiable** en slide 8: igual que en Ep 1, mostrar literal la frase exacta para que el espectador pueda copiarla y pegarla.
- **No leer las referencias del documento en voz alta.** Las referencias quedan visibles en el documento (este archivo) pero el audio se concentra en lo accionable.

---

# === CHECKLIST DE 4 PILARES ===

```
PILAR 1 — ACTIVACIÓN  ✓
  La comparación paper vs blog conecta con experiencia de lectura previa.

PILAR 2 — ANCLAJE  ✓
  Analogía explícita "paper vs blog" en bloque 4 (y reforzada en bloque 2).

PILAR 3 — ORGANIZACIÓN  ✓
  Depende solo de Ep 0 (notar lagunas) y Ep 1 (protocolo). Introduce un
  nuevo estándar pero no nuevos conceptos técnicos.

PILAR 4 — APLICACIÓN  ✓
  Actividad produce un artefacto: comparación antes/después de una
  respuesta real reformateada.
```
