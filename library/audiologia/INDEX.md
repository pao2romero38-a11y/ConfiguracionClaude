# Audiología — Índice de fuentes confiables

Cubre los cuatro subdominios de la residencia de Audiología y
Otoneurología: audiología clínica, foniatría, otoneurología y
patología del lenguaje. El skill `/audiologia` consume estas fuentes.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `audiologia`.

---

## Capas del cuerpo de literatura audiológica

```
NIVEL DE GUÍAS CLÍNICAS VIGENTES (prioridad máxima para práctica clínica)
──────────────────────────────────────────────────────────────────────────
  inr-guia-meniere-2020           ← Enfermedad de Ménière (INR MX)
  inr-guia-presbivestibulopatia-2020 ← Presbivestibulopatía (INR MX)
  barany-bppv-2015                ← VPPB — Clasificación y diagnóstico (Sociedad de Bárány)
  barany-meniere-2015             ← Criterios diagnósticos Ménière (Sociedad de Bárány)
  bsa-hearing-children-2020       ← Evaluación auditiva neonatal/pediátrica (BSA/JCIH)
  ci-practice-guidelines          ← Guías de práctica para implante coclear
  ci-comparison-chart             ← Tabla comparativa de dispositivos IC (v12.4c)

NIVEL DE TEXTOS CLÍNICOS (referencia de fisiopatología y diagnóstico)
──────────────────────────────────────────────────────────────────────
  atlas-pruebas-vestibulares      ← Pérez Fernández — pruebas vestibulares
  dx-tto-orl-cabeza-cuello        ← Diagnóstico y tto. ORL (ver medicina)

NIVEL DE CONOCIMIENTO DE BASE PEDIÁTRICO (hipoacusia en niños)
──────────────────────────────────────────────────────────────────────
  nelson-pediatrics-21            ← Hipoacusia hereditaria, síndromes, neuropatología (ver medicina)
```

---

## Subdominios y fuentes prioritarias

### Audiología clínica
Cubre: hipoacusia conductiva/sensorioneural/mixta, audiometría tonal y verbal,
timpanometría, PEATC, EOA, tamiz auditivo neonatal, adaptación de auxiliares
auditivos, implante coclear, hipoacusia hereditaria y sindrómica.

| Pregunta clínica | Fuente primaria | Fuente complementaria |
|---|---|---|
| Criterios diagnósticos de hipoacusia | Guías BSA/JCIH 2020 | Nelson 21ª |
| Evaluación auditiva neonatal | bsa-hearing-children-2020 | CI Practice Guidelines |
| Indicaciones para IC | ci-practice-guidelines | ci-comparison-chart |
| Hipoacusia hereditaria sindrómica | nelson-pediatrics-21 | Clases residencia R1/R2 |
| Ototoxicidad | Clases residencia R2 | nelson-pediatrics-21 |

### Foniatría
Cubre: evaluación de voz, patología laríngea benigna y maligna, disfonía,
rehabilitación vocal, disfagia, parálisis cordal.

| Pregunta clínica | Fuente primaria | Fuente complementaria |
|---|---|---|
| Clasificación patología laríngea | Clases residencia R2 (Presentaciones) | dx-tto-orl-cabeza-cuello |
| Técnicas de rehabilitación vocal | Clases residencia R2 (5º parcial) | — |
| Disfagia — maniobras | Extras R3 (Disfagia taller) | — |
| Carcinoma laríngeo | Clases residencia R2 (4º parcial) | dx-tto-orl-cabeza-cuello |

### Otoneurología
Cubre: VPPB, Enfermedad de Ménière, vestibulopatía unilateral y bilateral,
migraña vestibular, schwannoma vestibular, rehabilitación vestibular, fístula
perilinfática, SCDS (dehiscencia de canal semicircular), MPPP.

| Pregunta clínica | Fuente primaria | Fuente complementaria |
|---|---|---|
| Criterios diagnósticos VPPB | barany-bppv-2015 | atlas-pruebas-vestibulares |
| Criterios diagnósticos Ménière | barany-meniere-2015 | inr-guia-meniere-2020 |
| Presbivestibulopatía | inr-guia-presbivestibulopatia-2020 | Clases residencia R2 OTN |
| Maniobras de reposición (VPPB) | barany-bppv-2015 | atlas-pruebas-vestibulares |
| Antivertiginosos | Clases residencia R2 OTN (16) | — |

### Patología del lenguaje
Cubre: afasias, trastornos mixtos del lenguaje, evaluación neuropsicológica,
evaluación del lenguaje (ENI, IPTAPLON, EPLE).

| Pregunta clínica | Fuente primaria | Fuente complementaria |
|---|---|---|
| Clasificación afasias | Extras R2 (Ardila-Ostrosky) | Clases PL R2 |
| Instrumentos de evaluación | Clases PL R2/R3 (ENI, IPTAPLON) | — |
| Alexia | Clases PL R2 (4º parcial) | — |

---

## Abreviaturas clave del dominio

| Abreviatura | Significado |
|---|---|
| VPPB | Vértigo Posicional Paroxístico Benigno |
| PEATC | Potenciales Evocados Auditivos de Tronco Cerebral |
| EOA | Emisiones Otoacústicas |
| SCDS | Dehiscencia de Canal Semicircular (Superior Canal Dehiscence Syndrome) |
| IC | Implante Coclear |
| AA | Auxiliares Auditivos |
| INR | Instituto Nacional de Rehabilitación (México) |
| OTN | Otoneurología |
| PL | Patología del Lenguaje |
| MPPP | Mareo Perceptual Postural Persistente |
| IMIP | Médico Interno de Pregrado |
| BSA | British Society of Audiology |
| JCIH | Joint Committee on Infant Hearing |

---

## Pendientes conocidos

- **Guías ASHA / AAA** (American Speech-Language-Hearing Association /
  American Academy of Audiology) — pendiente de catalogar
- **Timpanometría de banda ancha** — artículos de tesis pendientes de catalogar
  (`Protocolo tesis/Artículos/Timpanometría banda ancha`)
- **Síndrome opercular** — artículos AMCAOF 2026 pendientes
- **Farmacología audiológica** — clases R2 pendientes de referencia formal

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
