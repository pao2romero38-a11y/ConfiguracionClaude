# Auditoría — Índice de fuentes confiables

Cubre los marcos profesionales de auditoría interna, externa y
gubernamental que el skill `/aud` consume.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `auditoria`.

---

## Mapa del cuerpo de marcos por tipo de auditoría

```
AUDITORÍA INTERNA
─────────────────────────────────────────────
  iia-standards-2024       ← VIGENTE desde enero 2025
       │ supersede
       ▼
  iia-ippf-2017            ← anterior, solo período de transición

AUDITORÍA EXTERNA
─────────────────────────────────────────────
  isa-iaasb-2024           ← internacionales (IAASB)
  ifac-handbook-2024       ← compendio anual oficial
  + En México: NIA (Normas Internacionales de Auditoría
    adoptadas por el IMCP — traducción de ISA)

AUDITORÍA GUBERNAMENTAL / SECTOR PÚBLICO
─────────────────────────────────────────────
  issai-intosai-2022       ← Auditoría Superior (ASF en MX, GAO en US)

ÉTICA PROFESIONAL
─────────────────────────────────────────────
  aicpa-code-of-conduct-2024  ← US (CPAs)
  + IFAC Code of Ethics (incluido en ifac-handbook-2024)
```

---

## Auditoría interna — cambio mayor en enero 2025

Los **Global Internal Audit Standards** del IIA supersedieron al
**IPPF** el 9 de enero de 2025. Cambio estructural significativo:

| Aspecto | IPPF (2017) | Global Standards (2024) |
|---|---|---|
| Estructura | Estándares + Guías | **15 principios** en **5 dominios** |
| Dominios | — | Propósito, Ética/Profesionalismo, Gobernanza, Gestión del trabajo, Realización |
| Foco en valor | Implícito | Explícito (alineación con estrategia) |
| Atributos del auditor | Estándares 1100-series | Principio 4: Independencia, Principio 5: Competencia |

**Implicación operativa**: para auditorías iniciadas en o después de
enero 2025, citar **Global Internal Audit Standards 2024**. Para
ciclos en curso a esa fecha, el IIA permite completar bajo IPPF.

---

## Auditoría externa — relación ISA ↔ NIA ↔ IFAC Handbook

| Documento | Origen | Cobertura | Idioma |
|---|---|---|---|
| **ISA** (International Standards on Auditing) | IAASB | Auditoría de estados financieros | EN |
| **NIA** (Normas Internacionales de Auditoría) | IMCP MX (traducción ISA) | Igual a ISA, vinculante en México | ES |
| **IFAC Handbook** | IFAC | Compendio anual con ISA + ISQM + ISRE + ISAE | EN |

**Regla operativa**: si la auditoría es en México, citar NIA (con
el número de la norma específica). Si es internacional, citar ISA.
El IFAC Handbook es la referencia comprehensiva cuando se necesita
verificar el texto exacto.

ISA frecuentemente citadas:

- **ISA 240** — Responsabilidad del auditor en relación con el fraude
- **ISA 315** (revised 2019) — Identificación y evaluación de riesgos
  de error material
- **ISA 500** — Evidencia de auditoría
- **ISA 540** (revised 2018) — Auditoría de estimaciones contables
- **ISA 700** — Formación de la opinión y emisión del informe de
  auditoría

---

## Auditoría gubernamental — ISSAI / INTOSAI

Aplicables a Entidades Fiscalizadoras Superiores (EFS):

- **ASF** (Auditoría Superior de la Federación, México)
- **GAO** (Government Accountability Office, EE.UU.)
- **NAO** (National Audit Office, Reino Unido)

ISSAI tienen 4 niveles:

1. Principios fundadores (ISSAI 1-99)
2. Prerrequisitos para el funcionamiento de las EFS (ISSAI 100-200)
3. Estándares fundamentales de auditoría (ISSAI 100, 200, 300, 400)
4. Lineamientos generales (ISSAI 1000+)

**Cuándo citar**: cualquier evaluación de la propia ASF o de auditorías
externas a entidades públicas mexicanas.

---

## Independencia y ética — qué código aplica

| Auditor | Código de ética principal |
|---|---|
| CPA estadounidense | **AICPA Code of Professional Conduct** |
| Contador profesional internacional | **IFAC Code of Ethics for Professional Accountants** (parte del IFAC Handbook) |
| Contador Público en México | Código de Ética Profesional del IMCP (basado en IFAC) — pendiente catalogar |
| Auditor interno (cualquier país) | **Código de Ética del IIA** (integrado en Global Internal Audit Standards 2024) |

---

## Composición típica de citas en un informe de auditoría

Para una auditoría interna en una empresa mexicana:

```
Marco profesional aplicable:
  · Global Internal Audit Standards (IIA, 2024) — efectivos 9 enero 2025
  · Normas Internacionales de Auditoría (NIA) cuando aplique reporte
    externo o coordinación con auditoría externa
  · COSO Internal Control — Integrated Framework (2013) para evaluación
    de control interno
  · ISO 31000:2018 + COSO ERM 2017 para componente de riesgos
```

Para una auditoría externa:

```
Norma de auditoría aplicable: NIA <número específico>
Marco contable aplicable: NIF / IFRS / US GAAP (según contexto)
Código de ética: Código de Ética IFAC (a través de la NIA)
```

---

## Pendientes conocidos del dominio

- **Código de Ética IMCP** (México) — pendiente catalogar.
- **CBOK del IIA** (Common Body of Knowledge) — referencia académica,
  pendiente.
- **GAGAS** (Generally Accepted Government Auditing Standards / Yellow
  Book de GAO US) — pendiente.
- **ISACA Audit Standards** (ITAF — IT Audit Framework) — para
  auditoría de TI específicamente. Pendiente.
- **PCAOB Auditing Standards** (para auditores de issuers en EE.UU.) —
  pendiente.

PRs bienvenidos.
