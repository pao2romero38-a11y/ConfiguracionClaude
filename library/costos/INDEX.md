# Costos — Contabilidad administrativa y gestión estratégica — Índice

Cubre los marcos de contabilidad de costos, sistemas de costeo,
performance management y lean / kaizen aplicado a costos que el skill
`/cost` consume.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `costos`.

---

## Capas del cuerpo de literatura

```
NIVEL DE MANUAL ESTÁNDAR (fundamento)
─────────────────────────────────────────
  horngren-cost-accounting-2021      ← manual mundial; cualquier
                                       sistema de costeo está cubierto

NIVEL DE COSTEO ESPECIALIZADO
─────────────────────────────────────────
  cooper-kaplan-abc-1991             ← Activity-Based Costing
  monden-toyota-1998                 ← Target Costing y Kaizen Costing
  imai-kaizen-1986                   ← mejora continua aplicada

NIVEL DE COSTOS ESTRATÉGICOS
─────────────────────────────────────────
  shank-strategic-cost-mgmt-1993     ← costos + estrategia (Porter)
  kaplan-norton-balanced-scorecard-1996 ← Balanced Scorecard

NIVEL DE PERFORMANCE INTEGRAL
─────────────────────────────────────────
  cokins-performance-management-2009 ← integra costos, BSC, riesgos
```

---

## Cuándo citar qué sistema de costeo

| Contexto | Sistema | Fuente |
|---|---|---|
| Producción simple, mix homogéneo | Costeo absorbente tradicional | Horngren |
| Mix complejo de productos con cost drivers diversos | **Activity-Based Costing (ABC)** | Cooper & Kaplan |
| Producto nuevo con precio definido por mercado | **Target costing** | Monden (Toyota) |
| Mejora continua de costos en producción | **Kaizen costing** | Imai + Monden |
| Decisiones short-term (incremental, marginal) | Costeo directo / variable | Horngren cap. correspondiente |
| Análisis competitivo (no contabilidad) | **Strategic Cost Management** | Shank |
| Sustentar KPIs estratégicos no financieros | **Balanced Scorecard** | Kaplan & Norton |

---

## La trampa del ABC mal implementado

ABC es teóricamente superior al costeo tradicional pero su
implementación tiene altos costos administrativos. Heurística:

**ABC tiene sentido cuando**:

- Cost drivers son claramente identificables y medibles
- Mix de productos es heterogéneo
- Costos indirectos representan >30% del costo total
- Las decisiones (pricing, descontinuación, outsourcing) realmente
  dependen de la precisión

**ABC NO tiene sentido cuando**:

- Costos indirectos son bajos
- Volúmenes pequeños donde el costo administrativo del sistema supera
  la mejora en precisión
- Producto único o casi único

Cita obligatoria de Cooper & Kaplan 1991 cap. 1 al recomendar ABC.

---

## Target costing — cómo opera

Modelo japonés (Toyota, Honda) opuesto al cost-plus tradicional:

```
TRADICIONAL (cost-plus):
  Costo + Margen = Precio
                  ↑ precio se ajusta para cubrir costos

TARGET COSTING:
  Precio (mercado) − Margen (objetivo) = Costo permitido
                                       ↑ costo se diseña para alcanzar el precio
```

Aplicable cuando:

- Precio está definido por mercado competitivo (no por el productor)
- El diseño del producto aún no está congelado (las decisiones de
  costo se toman antes de iniciar producción)
- La organización tiene capacidad de re-diseñar productos
  iterativamente (cross-functional teams)

Fuente: Monden 1998 (Toyota Production System) + Cooper-Slagmulder
(no catalogado aún) para tratamientos posteriores.

---

## Balanced Scorecard — las 4 perspectivas

Kaplan & Norton 1996 introducen el BSC como complemento al control
de costos puro:

| Perspectiva | Pregunta | Métricas típicas |
|---|---|---|
| **Financiera** | ¿Cómo nos ven los accionistas? | ROI, EBITDA, margen, crecimiento |
| **Cliente** | ¿Cómo nos ven los clientes? | NPS, satisfacción, retención, share |
| **Procesos** | ¿En qué procesos debemos sobresalir? | Calidad, tiempo de ciclo, costos de proceso |
| **Aprendizaje** | ¿Podemos seguir mejorando? | Rotación, capacitación, innovación |

Cita obligatoria del BSC al recomendar KPIs que vayan más allá de
métricas financieras puras.

---

## Pendientes conocidos del dominio

- **Cooper-Slagmulder** (Target Costing and Value Engineering) —
  tratamiento moderno del target costing. Pendiente.
- **Anthony & Govindarajan** (Management Control Systems) — pendiente.
- **Drury** (Management and Cost Accounting) — alternativa europea
  a Horngren. Pendiente.
- **Theory of Constraints** (Goldratt — The Goal) — pendiente.
- **Throughput Accounting** — pendiente.
- **Beyond Budgeting** (Hope & Fraser) — pendiente.
- **TDABC** (Time-Driven Activity-Based Costing, Kaplan 2007) —
  simplificación práctica del ABC clásico. Pendiente.

PRs bienvenidos.
