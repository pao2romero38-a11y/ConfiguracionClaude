# Tecnología empresarial — Arquitectura y gobierno — Índice de fuentes

Cubre los marcos de arquitectura empresarial, gobernanza tecnológica,
ingeniería de sistemas y patrones de integración / microservicios que
el skill `/tec` consume.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo
`tecnologia-empresarial`. Hay solapamiento intencional con
`seguridad-cumplimiento/` (COBIT, ITIL) y `ia-gobernanza/` para
gobierno de TI.

---

## Capas del cuerpo de literatura

```
NIVEL DE ARQUITECTURA EMPRESARIAL (estructura global)
─────────────────────────────────────────────────────────
  togaf-10-2022                ← marco más adoptado (metodología)
  brown-zachman-framework-2017 ← ontología (taxonomía, no metodología)

NIVEL DE ESTRATEGIA Y GOBIERNO (TI como capacidad)
─────────────────────────────────────────────────────────
  ross-it-savvy-2009           ← alineamiento negocio-TI

NIVEL DE PROCESOS Y TRANSFORMACIÓN
─────────────────────────────────────────────────────────
  davenport-process-innovation-1993  ← reingeniería habilitada por TI

NIVEL DE INGENIERÍA DE SISTEMAS
─────────────────────────────────────────────────────────
  nist-sp-800-160v1r1-2022     ← engineering trustworthy secure systems

NIVEL DE PATRONES DE IMPLEMENTACIÓN
─────────────────────────────────────────────────────────
  newman-microservices-2021    ← arquitectura microservicios
  hohpe-enterprise-integration-2003 ← patrones de integración asíncrona
```

---

## Cuándo citar qué

| Caso de uso | Marco principal | Complementos |
|---|---|---|
| Establecer función de Enterprise Architecture | **TOGAF 10** | Zachman como ontología transversal |
| Alinear TI con estrategia de negocio | **Ross — IT Savvy** | COBIT 2019 para gobierno (ver seguridad-cumplimiento) |
| Diseñar transformación digital | **Davenport** + TOGAF | — |
| Diseñar arquitectura microservicios | **Newman 2021** | Hohpe para integración entre ellos |
| Integrar sistemas legacy con nuevos | **Hohpe (EIP)** | — |
| Diseñar sistemas críticos de seguridad nacional | **NIST SP 800-160** | ISO/IEC/IEEE 15288 (no catalogado aún) |

---

## TOGAF 10 — qué cambió vs TOGAF 9.2

TOGAF 10 (publicado 2022) es **más modular** que TOGAF 9.2:

| Aspecto | TOGAF 9.2 | TOGAF 10 |
|---|---|---|
| Estructura | Documento único monolítico (~700 páginas) | **Suite de documentos**: Fundamentals + Series Guides |
| Tono | Prescriptivo | Más adaptable a contexto |
| Soporte ágil | Implícito | **Explícito** (Agile Series Guide) |
| Digital business | Marginal | **Series Guide específica** |

Aplica: certificaciones TOGAF 9 siguen siendo válidas. Para nuevas
implementaciones, TOGAF 10 es más flexible.

---

## Microservicios — cuándo SÍ, cuándo NO

Newman 2021 es la referencia operativa, pero la decisión arquitectónica
no es trivial. Heurística rápida:

| Síntoma del monolito actual | Microservicios pueden ayudar |
|---|---|
| Despliegues bloqueados por dependencias entre equipos | ✓ |
| Una parte del sistema necesita escalar 10x mientras el resto no | ✓ |
| Cambios de lenguaje/stack en partes específicas | ✓ |
| Tiempo de compilación / pruebas inaceptable | ✓ |

| Síntoma actual | Microservicios probablemente NO ayudan |
|---|---|
| Equipo pequeño (<10 ingenieros) sin DevOps maduro | ✗ |
| Lógica de negocio fuertemente acoplada (transacciones distribuidas frecuentes) | ✗ |
| Tráfico bajo y predecible | ✗ |
| Producto en fase de descubrimiento (arquitectura cambia semanal) | ✗ |

**Cita obligatoria**: Newman 2021 cap. 1 "What are microservices and
when should you use them?" antes de proponer migración.

---

## Relación con dominios vecinos

| Tema | Dominio principal | Aquí (`tecnologia-empresarial`) |
|---|---|---|
| Gobernanza de TI | seguridad-cumplimiento (COBIT) | Alineamiento estratégico (Ross) |
| ITIL / gestión de servicios | seguridad-cumplimiento | — |
| Seguridad del sistema | seguridad-cumplimiento (ISO 27001) | NIST SP 800-160 (engineering) |
| Arquitectura de IA | ia-gobernanza | — |
| Gestión de proyectos TI | finanzas (PMBOK) | — |

Citar transversalmente: para una transformación digital, típicamente
combinas TOGAF (este dominio) + COBIT (seguridad-cumplimiento) +
PMBOK (finanzas).

---

## Pendientes conocidos del dominio

- **ArchiMate 3** (lenguaje de modelado complementario a TOGAF) —
  pendiente catalogar.
- **DAMA-DMBOK** (Data Management Body of Knowledge) — pendiente.
- **ISO/IEC/IEEE 15288** (System and software engineering — System
  life cycle processes) — pendiente.
- **Cloud Adoption Frameworks** (AWS, Azure, GCP) — pendientes.
- **Domain-Driven Design** (Evans 2003) — pendiente.
- **The DevOps Handbook** (Kim et al. 2016) — pendiente.

PRs bienvenidos.
