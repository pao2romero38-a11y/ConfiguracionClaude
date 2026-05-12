# Seguridad y cumplimiento — Índice de fuentes confiables

Cubre los marcos de ciberseguridad, cumplimiento, control interno,
gestión de riesgos y gobernanza de TI que `/seg`, `/rsk`, `/ci`, `/aud`,
`/tec` consumen.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo
`seguridad-cumplimiento`.

---

## Mapa del cuerpo de marcos

```
GOBIERNO Y CUMPLIMIENTO EMPRESARIAL
───────────────────────────────────────
  coso-ic-2013         ← control interno (5 componentes, 17 principios)
  coso-erm-2017        ← gestión de riesgos empresariales (estrategia)
  cobit-2019           ← gobernanza y gestión de TI

GESTIÓN DE SEGURIDAD DE LA INFORMACIÓN
───────────────────────────────────────
  iso-27001-2022       ← SGSI certificable (93 controles en 4 temas)
  iso-27002-2022       ← guía de implementación de los 93 controles
  iso-27005-2022       ← gestión de riesgos específica de seguridad
  nist-csf-2-2024      ← marco voluntario US/global (6 funciones)
  nist-sp-800-53r5     ← catálogo detallado de 1000+ controles

GESTIÓN GENERAL DE RIESGOS
───────────────────────────────────────
  iso-31000-2018       ← marco general (NO certificable, es guía)
  nist-sp-800-30r1     ← procedimiento de evaluación de riesgos

SERVICIOS DE TI
───────────────────────────────────────
  itil-4-2019          ← gestión de servicios (supersede ITIL v3)

REGULACIÓN ESPECÍFICA POR DATOS
───────────────────────────────────────
  gdpr-2016            ← UE; alcance extraterritorial
  pci-dss-4-2022       ← datos de tarjetas de crédito

Ver también:
  regulacion-mx/INDEX.md → LFPDPPP, LGPDPPSO (datos personales MX)
```

---

## Cómo elegir el marco principal

| Caso de uso | Marco principal | Complementos |
|---|---|---|
| Certificar SGSI internacional | **ISO/IEC 27001:2022** | 27002, 27005 |
| Evaluación de madurez US/global voluntaria | **NIST CSF 2.0** | SP 800-53 para detalle |
| Sistemas federales US o contratistas | **NIST SP 800-53 Rev 5** | NIST RMF (800-37) |
| Procesamiento de tarjetas de crédito | **PCI DSS 4.0** | + 27001 para SGSI general |
| Empresa con clientes europeos | **GDPR** | + 27001 para implementar controles |
| Control interno SOX | **COSO IC 2013** | + COBIT para componente TI |
| Gestión de riesgos empresariales | **COSO ERM 2017** | + ISO 31000 |
| Gestión de TI / servicios | **ITIL 4 / COBIT 2019** | dependiendo de foco operativo vs gobernanza |

---

## Cambios de ISO 27001:2013 → 27001:2022 (cita obligatoria)

La versión 2022 reorganiza significativamente el Anexo A:

| Aspecto | 2013 | 2022 |
|---|---|---|
| Número de controles | 114 | 93 |
| Estructura del Anexo A | 14 dominios | 4 temas (Organizacional, Personas, Físico, Tecnológico) |
| Atributos por control | No | Sí (5 atributos: tipo, propiedades CIA, conceptos NIST CSF, capacidades operativas, dominios de seguridad) |
| Período de transición | — | Octubre 2022 - octubre 2025 |

**Implicación operativa**: certificaciones bajo 2013 expiran en
octubre 2025. Cualquier auditoría posterior debe ser bajo 2022.

---

## Cambios de NIST CSF 1.1 → 2.0 (publicado feb 2024)

| Aspecto | CSF 1.1 (2018) | CSF 2.0 (2024) |
|---|---|---|
| Funciones core | 5 (Identify, Protect, Detect, Respond, Recover) | **6** (añade **Govern**) |
| Audiencia explícita | Infraestructura crítica US | **Cualquier organización** (incluyendo PYMES) |
| Implementación | Tiers + Profiles | Tiers + Profiles + **Quick-Start Guides** |

La función nueva **Govern** (GV) integra gestión de riesgos
empresariales con ciberseguridad. Citar 2.0 como vigente.

---

## Relación COSO ↔ ISO ↔ NIST

Los tres marcos NO son mutuamente excluyentes; son complementarios:

| Capa | Marco recomendado | Función |
|---|---|---|
| Gobierno corporativo (board, control interno) | **COSO IC + COSO ERM** | Establece responsabilidad y rendición de cuentas |
| Gestión específica de TI (servicios, gobernanza) | **COBIT + ITIL** | Operacionaliza el "cómo" de TI |
| Gestión de seguridad de la información | **ISO 27001 / NIST CSF** | SGSI con controles específicos |
| Riesgos generales | **ISO 31000 / COSO ERM** | Metodología transversal |

Una empresa madura usa los tres niveles en cascada. Una empresa
arrancando debe priorizar el nivel donde está expuesta primero
(usualmente seguridad: ISO 27001 o NIST CSF).

---

## Pendientes conocidos del dominio

- **CIS Controls v8.1** — alternativa US práctica al SP 800-53.
  Pendiente catalogar.
- **NIST Privacy Framework 1.0** (2020) — pendiente.
- **NIST RMF (SP 800-37 Rev 2)** — proceso completo para sistemas
  federales. Pendiente.
- **OWASP Top 10** y **OWASP ASVS** — para seguridad de aplicaciones.
  Pendiente.
- **CSA Cloud Controls Matrix** — para cloud. Pendiente.
- **HIPAA** (US salud) — pendiente.
- **HITRUST CSF** — pendiente.

PRs bienvenidos.
