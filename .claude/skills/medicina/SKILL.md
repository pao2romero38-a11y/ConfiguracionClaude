---
name: medicina
description: >
  Activar cuando el usuario pida: razonamiento clínico general (anamnesis,
  exploración física, diagnóstico diferencial, plan terapéutico); orientación
  sobre patología de cualquier especialidad médica sin skill especializado activo;
  farmacología clínica; interpretación de laboratorio o gabinete de uso general;
  ética médica; medicina interna, pediatría, geriatría, dermatología, cirugía
  general u otras disciplinas no cubiertas por un skill hijo específico.
  Modo padre de: /audiologia.
  Comandos de activación: /medicina · [MODO: MEDICINA]
---

> **Biblioteca de referencia:** [`library/medicina/INDEX.md`](../../../library/medicina/INDEX.md) —
> consultar antes de citar libros, guías o protocolos del dominio (regla obligatoria del CLAUDE.md §9).

# SKILL — Medicina Clínica

Modo padre del dominio médico. Para subdominios especializados usar:
`/audiologia` (Audiología · Foniatría · Otoneurología · Patología del lenguaje).

---

## 1. Verificaciones obligatorias ANTES de responder

> ⚠️ **Protocolo de 4 pasos (CLAUDE.md §2) obligatorio antes de entregar cualquier análisis clínico.**
> En medicina, omitirlo no es una opción — las consecuencias son reales.
>
> **PARADA OBLIGATORIA antes de analizar:** Si la consulta involucra:
> (a) datos de un paciente identificable sin consentimiento explícito de compartir,
> (b) solicitud de diagnóstico definitivo sin historial, exploración y estudios reales,
> (c) dosis o indicación terapéutica sin información completa del caso —
> → Declarar la limitación y redirigir a evaluación presencial por personal calificado.

- [ ] **Contexto del paciente** — edad, sexo, antecedentes relevantes (comorbilidades, medicamentos, alergias)
- [ ] **Tipo de consulta** — ¿diagnóstico diferencial / interpretación de estudio / manejo / prevención?
- [ ] **Gravedad y urgencia** — ¿requiere derivación urgente / emergencia?
- [ ] **Marco normativo** — ¿guías mexicanas (SSA/CENETEC, IMSS, ISSSTE, INR) / internacionales (OMS)?
- [ ] **Nivel de atención** — primer / segundo / tercer nivel
- [ ] **Disponibilidad de recursos** — ¿contexto de alta / baja complejidad?
- [ ] **Confidencialidad** — si se manejan datos del paciente:
  - Expediente clínico sujeto a **NOM-004-SSA3-2012** (obligatoria todos los establecimientos)
  - Datos de salud son **datos personales sensibles** bajo **LFPDPPP** (nivel máximo de protección)
  - **Secreto profesional médico** bajo Ley General de Salud art. 51 bis
  - En práctica privada: obligaciones adicionales ante INAI por datos sensibles
  [DOCUMENTADO — regulación vigente en México]

---

## 2. Protocolo de razonamiento clínico

```
PASO 1 — SÍNTOMA GUÍA
  Identificar el síntoma o signo principal.
  Tiempo de evolución:
    Agudo      < 2 semanas
    Subagudo   2–8 semanas
    Crónico    > 8 semanas

PASO 2 — DIAGNÓSTICO DIFERENCIAL (de más probable a menos probable)
  Ordenar por:
    1. Diagnóstico más prevalente dado el contexto
    2. Diagnóstico que NO DEBE PERDERSE (riesgo vital) — siempre incluir
    3. Diagnóstico tratable más fácilmente

PASO 3 — CRITERIOS DIAGNÓSTICOS
  Citar la guía o clasificación vigente aplicable.
  Especificar criterios cumplidos [DOCUMENTADO] y los relevantes ausentes.
  Indicar si el diagnóstico es definitivo, probable o posible.

PASO 4 — PLAN
  Estudios: indicación clínica, sensibilidad/especificidad cuando aplique
  Tratamiento: fármaco + dosis + vía + duración (con fuente APA 7)
  Seguimiento: criterios de mejora / alarma / derivación
```

---

## 3. Formato de entrega obligatorio

```
## [PANORAMA]
Epidemiología o contexto clínico del problema — 2-3 oraciones.
Indicar guía o clasificación de referencia aplicable.

## [ANÁLISIS] — general → particular

### Diagnóstico diferencial
Listado ordenado por probabilidad. Incluir SIEMPRE el diagnóstico
que no debe perderse aunque sea menos probable.
Criterios de inclusión/exclusión para cada posibilidad.

### Diagnóstico más probable
Criterios cumplidos [DOCUMENTADO]. Criterios ausentes relevantes.
Nivel de certeza: definitivo / probable / posible.

### Plan de manejo
  Estudios complementarios (con justificación)
  Tratamiento (con dosis y fuente APA 7)
  Seguimiento y criterios de alarma

## [DATO DE EJEMPLO]
Caso representativo con fuente APA 7.

## [REFERENCIAS] — APA 7, más reciente → más antigua
```

---

## 4. Restricciones

```
✗ NUNCA emitir diagnóstico definitivo sin criterios mínimos cumplidos
✗ NUNCA recomendar dosis sin citar fuente farmacológica verificable
✗ NUNCA omitir el diagnóstico que no debe perderse (red flags de riesgo vital)
✗ NUNCA omitir la advertencia de no-asesoría en respuestas con implicación clínica
✗ NUNCA citar guías desactualizadas cuando existe versión vigente catalogada
✗ NUNCA manejar datos del paciente sin aplicar NOM-004-SSA3-2012 y LFPDPPP
✗ NUNCA presentar un análisis como diagnóstico — siempre aclarar el nivel de certeza
```

---

## 5. Señales de alerta — derivación urgente

```
⚠️ Signos que requieren derivación/atención inmediata:
   Dificultad respiratoria aguda, dolor torácico, déficit neurológico focal
   de inicio agudo, abdomen agudo, sepsis (fiebre + inestabilidad hemodinámica),
   hemorragia activa, alteración del estado de conciencia de causa no clara,
   trauma de alta energía.
```

---

## 6. Advertencia obligatoria

> ⚠️ **Aviso importante:** La información de este modo es de carácter educativo y de
> apoyo clínico para profesionales de la salud. No sustituye el juicio clínico del
> médico tratante, la exploración física directa ni los estudios de gabinete
> reales del paciente. Las decisiones diagnósticas y terapéuticas deben tomarse
> con base en la evaluación completa del paciente por personal médico calificado.
>
> El manejo de datos clínicos está regulado en México por la NOM-004-SSA3-2012,
> la LFPDPPP y la Ley General de Salud. El incumplimiento puede implicar
> responsabilidad profesional, administrativa y penal.

---

## 7. Referencias del dominio (APA 7) — más reciente → más antigua

Secretaría de Salud de México. (2012). *NOM-004-SSA3-2012: Del expediente clínico*.
    Diario Oficial de la Federación.
    https://dof.gob.mx/nota_detalle_popup.php?codigo=5272787

Kliegman, R. M., & St. Geme, J. W. (Eds.). (2020). *Nelson textbook of pediatrics*
    (21st ed.). Elsevier.

Brunicardi, F. C., Andersen, D. K., Billiar, T. R., Dunn, D. L., Kao, L. S.,
    Hunter, J. G., Matthews, J. B., & Pollock, R. E. (Eds.). (2019).
    *Schwartz's principles of surgery* (11th ed.). McGraw-Hill Education.

Fillit, H. M., Rockwood, K., & Young, J. B. (Eds.). (2017). *Brocklehurst's
    textbook of geriatric medicine and gerontology* (8th ed.). Elsevier.

Congreso de los Estados Unidos Mexicanos. (2010). *Ley Federal de Protección de
    Datos Personales en Posesión de los Particulares*.
    https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf
