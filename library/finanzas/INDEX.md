# Finanzas — Índice de fuentes confiables

Cubre los marcos de información financiera, valuación, finanzas
corporativas y gestión de proyectos que los skills `/fin`, `/proy`,
`/aud`, `/cost` consumen.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `finanzas`.

---

## Capas del cuerpo de literatura financiera

```
NIVEL DE MARCOS CONTABLES (qué reglas se aplican)
─────────────────────────────────────────────────
  nif-2024                  ← obligatorio en México (privadas)
  cinif-marco-conceptual    ← fundamento conceptual de las NIF
  ifrs-2024                 ← global, cotizadas internacionales
  us-gaap-fasb-codification ← obligatorio en EE.UU. (SEC registrants)

NIVEL TEÓRICO (cómo se piensa el problema)
─────────────────────────────────────────────────
  brealey-myers-corporate-finance-2022    ← finanzas corporativas estándar
  ross-westerfield-corporate-finance-2022 ← alternativa accesible
  damodaran-investment-valuation-2012     ← valuación universal

NIVEL DE GESTIÓN DE PROYECTOS (cuando finanzas + proyectos)
─────────────────────────────────────────────────
  pmbok-7-2021              ← vigente; cambio radical vs PMBOK 6
```

---

## Marcos contables — cuándo citar qué

| Contexto del cliente | Marco principal | Complementos |
|---|---|---|
| Empresa mexicana no cotizada | **NIF MX** | Para operaciones internacionales: reconciliación con IFRS |
| Empresa mexicana que cotiza en mercados extranjeros | **IFRS** | Reconciliación con NIF para reporte local |
| Filial mexicana de empresa US | NIF para reporte local + **US GAAP** para reporte a casa matriz | Reconciliación obligatoria |
| Empresa europea | **IFRS** | — |
| Empresa US registrada en SEC | **US GAAP** | — |
| Sector gubernamental MX | NICSP (no catalogadas aún) | NIF cuando aplique |

**Regla operativa para `/fin`**: si el cliente es mexicano, citar NIF
como marco principal. Si tiene operaciones que cruzan jurisdicciones,
declarar explícitamente cuál marco aplica a cuál parte del análisis.

---

## Cambios de PMBOK 6 → PMBOK 7 (cita obligatoria si aplica)

La 7ª edición (2021) **NO es una extensión de la 6ª** sino un rediseño:

| Aspecto | PMBOK 6 (2017) | PMBOK 7 (2021) |
|---|---|---|
| Enfoque | Procesos (49 procesos) | Principios (12 principios) |
| Estructura | 10 áreas de conocimiento | 8 dominios de desempeño |
| Metodología | Predictiva ("waterfall") implícita | Métodos múltiples explícitos (predictivo / ágil / híbrido) |
| Tamaño | ~750 páginas | ~370 páginas |

**Implicación para `/proy`**: cuando el cliente usa una organización
basada en PMBOK 6 (común si su PMO se estableció antes de 2022), no
asumir que PMBOK 7 aplica automáticamente. Preguntar.

---

## Valuación — orden de consulta recomendado

Para un análisis de valuación de empresa:

1. **Damodaran** primero — leer el capítulo correspondiente al método
   elegido (DCF, múltiplos comparables, opciones reales, etc.). Su
   tratamiento es el más profundo.
2. **Datos actualizados de Damodaran.com** — para múltiplos sectoriales,
   tasas libres de riesgo, primas de mercado. Su sitio es fuente de
   verdad para datos numéricos.
3. **Brealey-Myers** como complemento conceptual cuando el caso es
   atípico (estructura compleja, sector regulado, etc.).
4. Marco contable aplicable (NIF / IFRS / US GAAP) para reconocimiento
   y valuación contable de los activos/pasivos involucrados.

---

## Pendientes conocidos

- **CINIF — boletines posteriores a la edición vigente**: el CINIF
  publica boletines durante el año fiscal. Verificar trimestralmente
  cuando se trabaja sobre cierres recientes.
- **Análisis de costos**: el dominio se solapa con `/cost` (skill
  específico). Marcos pendientes: target costing (Kato 1993), ABC,
  contabilidad de costos en escenarios lean.
- **Tributario MX**: CFF, LISR, LIVA, LIEPS — pendiente; ver
  `regulacion-mx/INDEX.md` pendientes.
- **Finanzas conductuales**: Kahneman, Thaler — pendiente.
- **Mercados de capitales emergentes**: literatura específica de
  Latinoamérica — pendiente.

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
