# Investigación — Metodología y diseño — Índice de fuentes

Cubre los marcos de metodología de investigación cuali, cuanti y mixta
que el skill `/inv` consume directamente y `/edu` consume como apoyo.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo
`investigacion`. Booth et al. (2016) está en `pedagogia` por su uso
transversal en `/edu` pero aplica plenamente aquí también.

---

## Capas del cuerpo de literatura

```
NIVEL FILOSÓFICO (qué es conocimiento, qué es ciencia)
─────────────────────────────────────────────────────
  kuhn-scientific-revolutions-1962   ← paradigmas científicos

NIVEL METODOLÓGICO GENERAL
─────────────────────────────────────────────────────
  creswell-research-design-2023      ← cuali/cuanti/mixto
  hernandez-sampieri-metodologia-2014 ← estándar iberoamericano
  saunders-research-methods-2023     ← investigación aplicada en negocios

NIVEL ESPECÍFICO POR ENFOQUE
─────────────────────────────────────────────────────
  yin-case-study-2018                ← estudios de caso

NIVEL DE ESTÁNDARES INSTITUCIONALES
─────────────────────────────────────────────────────
  oecd-frascati-2015                 ← I+D — definición y medición

Ver también:
  pedagogia/INDEX.md → booth-craft-research-2016 (transversal)
```

---

## Cuándo citar qué

| Tipo de investigación | Marco principal | Complementos |
|---|---|---|
| Tesis de maestría o doctorado (académica) | **Creswell** o **Hernández-Sampieri** | Yin si es estudio de caso |
| Investigación aplicada en negocios | **Saunders et al.** | Yin para casos múltiples |
| Investigación experimental (cuanti puro) | **Creswell** cap. cuanti | — |
| Investigación cualitativa (etnografía, fenomenología) | **Creswell** cap. cuali | Yin si caso |
| Investigación mixta (cuali + cuanti) | **Creswell** específicamente | — |
| Estudios de caso (única o múltiple) | **Yin** | Creswell como contexto metodológico |
| Reportar I+D a autoridad fiscal o estímulos | **Frascati Manual (OECD)** | — |
| Cuestionar supuestos vs operar dentro de paradigma | **Kuhn** | Necesario para investigación disruptiva |

---

## Decisión enfoque cuanti vs cuali vs mixto

Heurística para elegir (Creswell):

| Pregunta | Enfoque sugerido |
|---|---|
| ¿Qué tan frecuente es X? ¿Hay relación entre X e Y? | **Cuanti** |
| ¿Cómo experimenta la gente X? ¿Qué significa X para ellos? | **Cuali** |
| ¿Por qué los datos cuanti muestran Y pero hay casos extremos inexplicables? | **Mixto secuencial explicativo** (cuanti → cuali) |
| ¿Cómo se manifiesta X cuanti vs cuali simultáneamente? | **Mixto convergente** (cuanti + cuali paralelo) |
| ¿Es generalizable lo que descubrí cuali? | **Mixto secuencial exploratorio** (cuali → cuanti) |

---

## El "research onion" de Saunders

Para investigación aplicada en negocios, Saunders organiza las
decisiones metodológicas en capas concéntricas (de afuera hacia
adentro):

```
   Filosofía (positivismo / interpretivismo / pragmatismo / ...)
    └─ Enfoque (deductivo / inductivo / abductivo)
        └─ Estrategia (encuesta / caso / experimento / etnografía / ...)
            └─ Elección (mono-método / multi-método / mixto)
                └─ Horizonte temporal (transversal / longitudinal)
                    └─ Técnicas y procedimientos
```

Útil como **diagrama de coherencia metodológica**: cada decisión interna
debe ser consistente con las externas.

---

## Frascati Manual — relevancia operativa

El Frascati Manual (OECD 2015) define qué cuenta como **I+D**
(Investigación y Desarrollo) vs otras actividades de innovación.
Importante porque:

- **Estímulos fiscales mexicanos** (EFIDT) requieren clasificación
  Frascati de la actividad.
- **Reportes internacionales** de empresas multinacionales usan
  definiciones Frascati.
- **Métricas de PIB de I+D** se calculan con Frascati.

Las 3 categorías:

1. **Investigación básica** — sin aplicación específica
2. **Investigación aplicada** — orientada a problema específico
3. **Desarrollo experimental** — generar productos / procesos nuevos
   o mejorados sustancialmente

Criterios novedad + creatividad + incertidumbre + sistematicidad +
transferibilidad/reproducibilidad — los 5 deben cumplirse para
clasificar como I+D.

---

## Pendientes conocidos del dominio

- **Popper** (The Logic of Scientific Discovery) — falsacionismo,
  complemento a Kuhn. Pendiente.
- **Lakatos** (programas de investigación científica) — pendiente.
- **Bunge** (epistemología científica en español) — pendiente para
  audiencia iberoamericana.
- **Maxwell** (Qualitative Research Design) — alternativa profunda
  a Creswell para cuali. Pendiente.
- **Patton** (Qualitative Research and Evaluation Methods) — pendiente.
- **Field** (Discovering Statistics Using SPSS) — para análisis
  cuantitativo aplicado. Pendiente.
- **PRISMA Statement** — para revisiones sistemáticas. Pendiente.
- **SAGE Encyclopedia of Research Methods** — referencia exhaustiva.
  Pendiente.

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
