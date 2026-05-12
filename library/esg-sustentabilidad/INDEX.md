# ESG y sustentabilidad — Índice de fuentes confiables

Cubre los marcos de reportes ESG (Environmental, Social, Governance),
divulgación climática, gestión ambiental y conducta empresarial
responsable. Consume transversalmente por `/fin`, `/aud`, `/ci`, `/rsk`
cuando el caso incluye dimensión de sustentabilidad.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo
`esg-sustentabilidad`.

---

## Capas del cuerpo de marcos

```
ESTÁNDARES DE DIVULGACIÓN (qué reportar y cómo)
─────────────────────────────────────────────────
  gri-standards-2021         ← más adoptado mundialmente
  sasb-standards-2018        ← específicos por industria; ahora bajo ISSB
  issb-s1-s2-2023            ← IFRS Sustainability — adopción jurisdiccional creciente

DIVULGACIÓN CLIMÁTICA ESPECÍFICA
─────────────────────────────────────────────────
  tcfd-recommendations-2017  ← fundacional; ahora absorbido por IFRS S2

SISTEMAS DE GESTIÓN CERTIFICABLES
─────────────────────────────────────────────────
  iso-14001-2015             ← gestión ambiental (SGA)

CONDUCTA EMPRESARIAL Y AGENDA GLOBAL
─────────────────────────────────────────────────
  oecd-multinationals-2023   ← debida diligencia y conducta responsable
  un-sdgs-2015               ← 17 ODS, agenda 2030
```

---

## Cuándo citar qué

| Caso de uso | Marco principal | Complementos |
|---|---|---|
| Primer reporte de sustentabilidad corporativo | **GRI** | SDGs para alineamiento; SASB si industria específica |
| Reporte de empresa cotizada con foco financiero | **IFRS S1 + S2** | SASB para materialidad financiera por industria |
| Divulgación climática específica | **IFRS S2** | TCFD para contextos pre-2024 |
| Certificar gestión ambiental | **ISO 14001** | — |
| Política corporativa de derechos humanos / debida diligencia | **OECD MNE Guidelines** | UN Guiding Principles on Business and Human Rights (pendiente catalogar) |
| Estrategia corporativa de sustentabilidad | **SDGs** | GRI como marco de medición |

---

## GRI vs SASB vs ISSB — la diferencia clave

| Aspecto | GRI | SASB | ISSB (IFRS S1/S2) |
|---|---|---|---|
| Foco principal | Impacto en stakeholders amplios | Materialidad financiera específica por industria | Materialidad financiera global |
| Audiencia | Múltiples stakeholders | Inversionistas | Inversionistas |
| Adopción | Voluntaria; ~80% empresas grandes | Voluntaria; uso creciente | Adopción regulatoria por jurisdicciones (UK, EU, Canada, otros desde 2024) |
| Origen | Global Reporting Initiative (1997) | Sustainability Accounting Standards Board (2011); ahora bajo IFRS Foundation (2022) | International Sustainability Standards Board (creado 2021 por IFRS Foundation) |
| Relación con TCFD | Compatible | Compatible | **IFRS S2 absorbió y profundizó TCFD** |

**Operativa típica**: una empresa madura reporta GRI (para amplitud)
+ SASB (para materialidad por industria) o IFRS S1/S2 (cuando aplica
mandato regulatorio). Las tres son compatibles entre sí.

---

## Doble materialidad — concepto clave

GRI usa **doble materialidad**:

- **Materialidad financiera** (de adentro hacia afuera): cómo
  problemas ESG afectan la empresa.
- **Materialidad de impacto** (de adentro hacia afuera): cómo la
  empresa impacta el entorno.

ISSB/SASB usan **materialidad simple** (financiera). La EU CSRD
adopta doble materialidad (alineada con GRI).

**Implicación**: al asesorar empresas con operaciones en UE, usar
doble materialidad. Para inversores globales puros, materialidad
financiera suele bastar.

---

## TCFD → IFRS S2 — la transición

El TCFD fue disuelto en 2023 después de que sus principios fueron
**absorbidos por IFRS S2**. Implicaciones para citar:

- **2017-2023**: TCFD era la referencia internacional.
- **Desde 2024**: IFRS S2 es la referencia internacional vigente.
- **Reino Unido**: TCFD obligatorio desde 2022 para grandes empresas;
  transición a IFRS S2 prevista pero la regulación aún cita TCFD.
- **México**: voluntario; muchas empresas grandes cotizadas siguen
  citando TCFD. Para reportes 2025+ recomendable migrar a IFRS S2.

---

## Pendientes conocidos del dominio

- **UN Guiding Principles on Business and Human Rights** (Ruggie 2011) —
  pendiente catalogar.
- **GHG Protocol** (Corporate Standard, Scope 3 Standard) — pendiente.
- **CDP** (Carbon Disclosure Project) cuestionarios — pendiente.
- **EU CSRD** (Corporate Sustainability Reporting Directive) y
  **ESRS** (European Sustainability Reporting Standards) — pendiente.
- **ISO 26000:2010** (Social responsibility — guía no certificable) —
  pendiente.
- **ISO 45001:2018** (Salud y seguridad ocupacional) — pendiente,
  complementario a ISO 14001 en sistemas de gestión integrados.
- **Estándares B Corp** — pendiente para empresas certificadas.
- **México**: criterios ESG de la CNBV para emisores; pendiente.

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
