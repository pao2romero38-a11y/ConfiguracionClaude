# Regulación mexicana — Índice de fuentes confiables

Este índice cubre el marco normativo mexicano más citado por los skills
del proyecto: regulación de datos personales, protección civil,
continuidad operativa, y referencias estructurales (CPEUM, CPF, DOF).

Todas las entradas están registradas en
[`CATALOG.yaml`](../CATALOG.yaml) bajo la sección `regulacion-mx`. Aquí
se complementan con relaciones entre normas, advertencias de uso, y la
arquitectura del cuerpo regulatorio.

---

## Panorama del cuerpo regulatorio mexicano relevante

El sistema legal mexicano para los dominios técnicos de este repo se
organiza en cuatro capas:

```
┌──────────────────────────────────────────────────┐
│  CONSTITUCIÓN POLÍTICA (CPEUM)                   │
│  Base de todo el ordenamiento                    │
└──────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  LEYES FEDERALES (Congreso de la Unión)          │
│  · LFPDPPP — datos personales en privados        │
│  · LGPDPPSO — datos personales en públicos        │
│  · LGPC — protección civil                       │
│  · CPF — derecho penal federal                   │
└──────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  REGLAMENTOS (Ejecutivo Federal)                 │
│  · Reglamento de LFPDPPP                          │
└──────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  LINEAMIENTOS Y GUÍAS (INAI, organismos)         │
│  · Lineamientos INAI en protección de datos      │
└──────────────────────────────────────────────────┘

DOF (Diario Oficial de la Federación) — vehículo de publicación oficial
de todo lo anterior. Cita obligatoria al referenciar fechas exactas.
```

---

## Datos personales — el bloque más solicitado

### Aplicabilidad: sector privado vs sector público

| Tipo de entidad | Ley aplicable | Reglamento | Lineamientos |
|---|---|---|---|
| **Empresa privada** sin recursos públicos | [`lfpdppp-2010`](../CATALOG.yaml) | [`reglamento-lfpdppp-2011`](../CATALOG.yaml) | [`inai-lineamientos-datos`](../CATALOG.yaml) |
| **Entidad pública** o privada con recursos públicos | [`lgpdppso-2017`](../CATALOG.yaml) | (lineamientos INAI hacen las veces) | [`inai-lineamientos-datos`](../CATALOG.yaml) |
| Tratamiento **transfronterizo** | Ambas + reglas de transferencia internacional | Ver capítulo respectivo en el Reglamento | INAI publica criterios específicos |

**Error común a evitar**: aplicar LFPDPPP a un organismo público (o
LGPDPPSO a una empresa privada sin recursos públicos). Son leyes
distintas con responsables y autoridades diferentes.

### Cómo se citan en una evaluación de cumplimiento

```
Marco regulatorio aplicable:
  · LFPDPPP (DOF 5 de julio de 2010, última reforma 27 de enero de 2017)
  · Reglamento de la LFPDPPP (DOF 21 de diciembre de 2011)
  · Lineamientos generales INAI vigentes en materia de datos personales
```

Citar siempre las **tres** cuando se evalúa cumplimiento de un
particular en México. Omitir cualquiera deja la evaluación incompleta
ante un auditor o autoridad.

---

## Penal y seguridad informática

El [`cpf`](../CATALOG.yaml) (Código Penal Federal) tiene capítulos
relevantes a:

- **Acceso ilícito a sistemas y equipos de informática** (Título Noveno)
- **Revelación de secretos** (relacionado con privacidad de datos)
- **Falsificación de documentos electrónicos** (relevante a auditoría)

Para cualquier evaluación de riesgo en ciberseguridad mexicana, el CPF
es la referencia mínima de obligaciones penales aplicables al
responsable.

---

## Continuidad operativa y protección civil

La [`lgpc-2012`](../CATALOG.yaml) (Ley General de Protección Civil) es
referencia obligatoria para Business Continuity Plans (BCP) en México.
Define las responsabilidades del responsable en materia de continuidad
ante eventos disruptivos (sismos, incendios, ciberincidentes mayores).

---

## DOF — el vehículo oficial

El [`dof`](../CATALOG.yaml) NO es una ley, sino el órgano de
publicación oficial. Toda referencia formal a una ley o reglamento
**debe** citar:

- Fecha de publicación en DOF (formato: DOF DD de mes de YYYY)
- Última fecha de reforma significativa
- Cuando aplica, número de sección y página

Ejemplo correcto en APA 7:

> Ley Federal de Protección de Datos Personales en Posesión de los
> Particulares, Diario Oficial de la Federación (2010, 5 de julio).
> https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf

---

## Mantenimiento de este índice

Cuando una ley se reforme significativamente en DOF:

1. Actualizar el campo `edicion_vigente` de su entrada en `CATALOG.yaml`.
2. Si hay cambios estructurales (no solo de números o adiciones
   menores), actualizar la sección correspondiente en este INDEX.
3. Registrar en `CHANGELOG.md` del repo bajo "library/".

Para nuevas leyes que entren al catálogo, abrir PR explicando el caso
de uso que la justifica y el skill que la consumirá.

---

---

## Marco fiscal (nuevo en v2.9.0)

| Norma | Catálogo | Cuándo citar |
|---|---|---|
| Código Fiscal de la Federación | [`cff-1981`](../CATALOG.yaml) | Cualquier evaluación tributaria — marco general |
| Ley del Impuesto Sobre la Renta | [`lisr-2013`](../CATALOG.yaml) | Impuesto a la renta personas físicas / morales |
| Ley del Impuesto al Valor Agregado | [`liva-1978`](../CATALOG.yaml) | IVA — tasa general 16%, frontera 8%, alimentos/medicinas 0% |
| Ley del IEPS | [`liepys-1980`](../CATALOG.yaml) | Bebidas alcohólicas, tabaco, hidrocarburos, bebidas saborizadas |
| Resolución Miscelánea Fiscal | [`rmf-anual`](../CATALOG.yaml) | Reglas operativas anuales del SAT — verificar última publicada |

**Pendientes fiscales conocidos**: LFD (Ley Federal de Derechos), LIETU (derogada pero a veces citada históricamente), Ley Aduanera, Tratados internacionales para evitar doble tributación, Reglamentos de las leyes citadas.

---

## Marco mercantil (nuevo en v2.9.0)

| Norma | Catálogo | Cuándo citar |
|---|---|---|
| Código de Comercio | [`codigo-comercio-1889`](../CATALOG.yaml) | Actos de comercio, contratos mercantiles, juicios mercantiles |
| Ley General de Sociedades Mercantiles | [`lgsm-1934`](../CATALOG.yaml) | Constitución y operación de sociedades; SAS para startups |
| Ley General de Títulos y Operaciones de Crédito | [`lgtoc-1932`](../CATALOG.yaml) | Letra, pagaré, cheque, fideicomisos, bonos |

**Pendientes mercantiles**: Ley de Concursos Mercantiles, Ley del Mercado de Valores, Ley General de Organizaciones y Actividades Auxiliares del Crédito, Código de Comercio (reformas FinTech 2018), Ley FinTech (LRITF 2018).

---

## Marco laboral (nuevo en v2.9.0)

| Norma | Catálogo | Cuándo citar |
|---|---|---|
| Ley Federal del Trabajo | [`lft-1970`](../CATALOG.yaml) | Cualquier relación laboral; reforma 2019 cambió justicia laboral |
| Ley del Seguro Social | [`lss-1995`](../CATALOG.yaml) | Régimen IMSS; reforma 2020 modificó subcontratación |
| Ley INFONAVIT | [`linfonavit-1972`](../CATALOG.yaml) | Aportaciones patronales para vivienda (5% del SBC) |
| NOM-035-STPS-2018 | [`nom-035-stps-2018`](../CATALOG.yaml) | Factores de riesgo psicosocial; cumplimiento por tamaño de centro |

**Pendientes laborales**: NOM-030-STPS (servicios de seguridad e higiene), NOM-019-STPS (comisiones de seguridad e higiene), reglas del SAT sobre nómina y CFDI 4.0, Ley del ISSSTE (sector público).

---

## Marco de salud (nuevo en v2.9.0)

| Norma | Catálogo | Cuándo citar |
|---|---|---|
| Ley General de Salud | [`lgs-1984`](../CATALOG.yaml) | Marco federal — competencias, establecimientos, investigación clínica |
| NOM-004-SSA3-2012 | [`nom-004-ssa3-2012`](../CATALOG.yaml) | **Expediente clínico** — obligatoria para todo establecimiento médico |
| NOM-024-SSA3-2012 | [`nom-024-ssa3-2012`](../CATALOG.yaml) | **Sistemas de Información de Registro Electrónico para la Salud (SIRES)** |
| NOM-035-SSA3-2012 | [`nom-035-ssa3-2012`](../CATALOG.yaml) | Integración del sistema de información en salud |

**Cita combinada típica para diseñar EMR / sistemas hospitalarios en MX**: LFPDPPP + LGPDPPSO + LGS + NOM-004-SSA3 + NOM-024-SSA3 (los datos clínicos son datos personales sensibles bajo LFPDPPP).

**Pendientes salud**: NOM-007-SSA2 (atención embarazo, parto, puerperio), NOM-046-SSA2 (violencia familiar y sexual), Ley General de los Derechos de Niñas, Niños y Adolescentes.

---

## Pendientes globales del dominio

- **Sector específico (CNBV, CONDUSEF, CFE, COFECE)**: regulación sectorial. Se añade conforme aparezcan casos de uso.
- **Tratados internacionales firmados por México**: T-MEC, OECD, OIT, etc.
- **Reglamentos** de las leyes catalogadas (varios pendientes).

PRs bienvenidos para llenar cualquiera de estos huecos (ver
`CONTRIBUTING.md` y `library/README.md` §"Cómo contribuir entradas").
