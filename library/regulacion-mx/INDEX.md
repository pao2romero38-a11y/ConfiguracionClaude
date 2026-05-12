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

## Pendientes conocidos (huecos del dominio)

- **Marco fiscal**: Código Fiscal de la Federación, ISR, IVA — relevante para `/fin` y `/aud`. Aún no incluido.
- **Mercantil**: Código de Comercio, Ley General de Sociedades Mercantiles — relevante para `/proy` y `/fin`. Aún no incluido.
- **Laboral**: LFT, IMSS — relevante si se diseña capacitación corporativa. Aún no incluido.
- **Salud**: Ley General de Salud, NOM-004-SSA3, NOM-024-SSA3 (expediente clínico electrónico) — pendiente.
- **Sector específico (CNBV, CONDUSEF, CFE, COFECE)**: regulación sectorial. Se añade conforme aparezcan casos de uso.

PRs bienvenidos para llenar cualquiera de estos huecos (ver
`CONTRIBUTING.md` y `library/README.md` §"Cómo contribuir entradas").
