# IA — Gobernanza, riesgo y ética — Índice de fuentes confiables

Cubre los marcos normativos y regulatorios para gobernanza, gestión
de riesgos y ética en sistemas de inteligencia artificial. Consume
por los skills `/ai`, `/ai-llm`, `/ai-ml` y como apoyo en `/seg`,
`/rsk`, `/ci`.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo
`ia-gobernanza`.

---

## Tipos de instrumento y cuándo aplica cada uno

```
REGULACIÓN VINCULANTE (obligación legal)
─────────────────────────────────────────
  eu-ai-act-2024           ← UE, alcance extraterritorial
                              aplicación escalonada 2025-2027

ESTÁNDARES CERTIFICABLES (obligación contractual)
─────────────────────────────────────────
  iso-42001-2023           ← sistema de gestión de IA (AIMS),
                              análogo a ISO 27001 pero para IA

GUÍAS TÉCNICAS NO VINCULANTES (mejores prácticas)
─────────────────────────────────────────
  nist-ai-rmf-1-2023       ← marco de gestión de riesgos de IA
  iso-23894-2023           ← gestión específica de riesgos en IA

PRINCIPIOS DE ALTO NIVEL (referencias filosóficas / orientativas)
─────────────────────────────────────────
  oecd-ai-principles-2024  ← 5 principios, 47 países adherentes
  unesco-ai-ethics-2021    ← recomendación adoptada por 193 Estados
```

---

## Marco regulatorio — la EU AI Act como punto de partida

La **EU AI Act** (Reglamento UE 2024/1689) es el primer marco
regulatorio comprehensivo de IA con alcance global de facto:

| Aspecto | Detalle |
|---|---|
| Entrada en vigor | 1 de agosto de 2024 |
| Aplicación general | 2 de agosto de 2026 |
| Prohibiciones (Art. 5) | 2 de febrero de 2025 |
| Modelos de propósito general (Art. 51-56) | 2 de agosto de 2025 |
| Sistemas de alto riesgo (Anexo III) | 2 de agosto de 2026 |
| Sistemas de alto riesgo (componentes regulados) | 2 de agosto de 2027 |

**Alcance extraterritorial**: aplica a cualquier proveedor o
desplegador que opere sistemas de IA cuyos outputs se usen dentro de
la UE, independientemente de la sede del proveedor.

**Clasificación por riesgo**:

- **Riesgo inaceptable** (prohibido): manipulación cognitiva,
  puntuación social, reconocimiento biométrico remoto en tiempo real
  en espacios públicos (con excepciones acotadas), etc.
- **Alto riesgo** (cumplimiento estricto): sistemas en empleo,
  educación, infraestructura crítica, aplicación de la ley, etc.
- **Riesgo limitado** (transparencia): chatbots, deepfakes — obligación
  de disclosure.
- **Riesgo mínimo**: sin obligaciones específicas.

**Cita obligatoria** en cualquier evaluación de IA con exposición
europea, incluso si la empresa es mexicana.

---

## Estándar certificable — ISO/IEC 42001:2023

Es la **primera norma ISO certificable** específicamente para sistemas
de gestión de IA (AIMS, AI Management System):

| Concepto | ISO 27001:2022 (SGSI) | ISO 42001:2023 (AIMS) |
|---|---|---|
| Alcance | Seguridad de la información | Gobernanza de sistemas de IA |
| Certificable | Sí | Sí |
| Estructura | High-Level Structure (HLS) | HLS — compatible con 27001 |
| Anexo de controles | Anexo A (93 controles) | Anexo A (controles de IA) |
| Año | 2022 | 2023 |

**Estrategia operativa**: una organización con 27001 ya implementada
puede certificar 42001 con esfuerzo incremental significativamente
menor que iniciar desde cero. La arquitectura HLS está diseñada para
integrar.

**Cita obligatoria** cuando el cliente quiere certificación o
acreditación formal de gobernanza de IA.

---

## Guías técnicas — NIST AI RMF

El **AI RMF 1.0** (NIST, enero 2023) es la referencia técnica más
citada en gestión de riesgos de IA:

**4 funciones core**:

1. **GOVERN** — establecer cultura y procesos de gestión de riesgos
2. **MAP** — contextualizar el sistema y sus riesgos
3. **MEASURE** — analizar, evaluar, benchmark
4. **MANAGE** — priorizar, responder, monitorear

**Perfiles publicados**:

- **Generative AI Profile** (NIST AI 600-1, julio 2024) — perfil
  específico para IA generativa (LLMs, generación de imagen, etc.)

**Cita obligatoria** cuando se diseña o evalúa un programa de
gestión de riesgos de IA, incluso fuera de jurisdicción US.

---

## Principios — cuándo citar OECD vs UNESCO

| Documento | Tono | Mejor cuando |
|---|---|---|
| OECD AI Principles | Técnico-económico | Contextos empresariales, regulatorios técnicos |
| UNESCO AI Ethics | Filosófico-humanístico | Contextos de sector público, salud, educación, derechos humanos |

Ambos son **no vinculantes** pero ampliamente adoptados. Frecuentemente
se citan juntos para mostrar alineación con consenso global.

---

## Composición típica de marco aplicable en un caso

**Caso A — Empresa mexicana con producto de IA generativa para Europa:**

```
Marco regulatorio:
  · EU AI Act (Reglamento UE 2024/1689) — clasificar el sistema por nivel
    de riesgo, identificar obligaciones aplicables y fechas de cumplimiento.
Marcos voluntarios complementarios:
  · NIST AI RMF 1.0 + Generative AI Profile (NIST AI 600-1) — para
    estructurar el programa interno de gestión de riesgos.
  · ISO/IEC 42001:2023 — si se busca certificación formal.
  · OECD AI Principles — como declaración pública de alineación ética.
```

**Caso B — Empresa US con uso interno de LLMs (no producto):**

```
Marco principal:
  · NIST AI RMF 1.0 con Generative AI Profile.
Marcos complementarios:
  · ISO/IEC 23894:2023 — gestión específica de riesgos en IA.
  · ISO/IEC 27001:2022 — para el componente de seguridad de la
    información en el uso de LLMs (datos sensibles en prompts, etc.).
```

**Caso C — Organismo público que adopta IA para servicios al ciudadano:**

```
Marco principal:
  · UNESCO Recommendation on the Ethics of AI (2021).
Marcos vinculantes:
  · Legislación nacional específica (en México: pendiente — al corte
    de este índice, México no tiene Ley de IA propia).
  · Cuando aplique: LGPDPPSO (datos personales en sector público).
Marcos voluntarios:
  · NIST AI RMF + OECD AI Principles.
```

---

## Pendientes conocidos del dominio

- **Anthropic Responsible Scaling Policy** y políticas similares de
  laboratorios (OpenAI, Google DeepMind, xAI) — relevantes para
  evaluar proveedores. Pendiente catalogar.
- **MITRE ATLAS** — adversarial threats matrix específica para ML.
  Pendiente.
- **OWASP Top 10 for LLM Applications** — pendiente.
- **Singapore Model AI Governance Framework** — referencia regional
  asiática. Pendiente.
- **UK AI Safety Institute publications** — pendiente.
- **México**: la Estrategia Nacional de IA y cualquier ley específica
  cuando se publiquen — pendiente.
- **Sector-específico**: regulación FDA de IA en dispositivos médicos,
  reglas de la SEC US para uso de IA en disclosure, etc. — pendiente.

PRs bienvenidos.
