# `library/` — Biblioteca de referencias confiables

Esta carpeta es un **catálogo curado de fuentes profesionales** que los
skills del proyecto citan y consultan. Resuelve la pregunta operativa:

> *"Cuando un skill cita una norma, un libro o una ley, ¿cómo se sabe
> que esa cita está vigente y dónde se obtiene la versión canónica?"*

---

## Modelo: B + E + D (combinación de tres piezas)

La biblioteca NO almacena documentos copyrighted. Combina tres
mecanismos complementarios:

### Pieza B — Catálogo central (`CATALOG.yaml`)

Archivo YAML machine-readable con metadatos de cada fuente: título,
autor(es), año, edición vigente, DOI/URL oficial, idiomas, traducciones
recomendadas, license, status (vigente / superseded), skills que la
referencian.

Es la **única fuente de verdad** sobre qué edición de cada fuente debe
citarse en cualquier modo.

### Pieza E — Índices por dominio (`<dominio>/INDEX.md`)

Documentos narrativos por dominio profesional con:

- Panorama del cuerpo de literatura
- Relaciones entre fuentes (qué supera a qué, qué complementa a qué)
- Orden recomendado de lectura cuando aplica
- Advertencias sobre ediciones obsoletas
- Cross-references a entradas del catálogo central

Cada dominio crece independientemente. Hoy hay once:

| Dominio | INDEX | Estado |
|---|---|---|
| Pedagogía y aprendizaje significativo | [`pedagogia/INDEX.md`](pedagogia/INDEX.md) | v1 — 8 entradas |
| Regulación MX (datos, fiscal, mercantil, laboral, salud) | [`regulacion-mx/INDEX.md`](regulacion-mx/INDEX.md) | v2 — 21 entradas |
| Finanzas | [`finanzas/INDEX.md`](finanzas/INDEX.md) | v1 — 8 entradas |
| Seguridad y cumplimiento | [`seguridad-cumplimiento/INDEX.md`](seguridad-cumplimiento/INDEX.md) | v1 — 13 entradas |
| Auditoría | [`auditoria/INDEX.md`](auditoria/INDEX.md) | v1 — 6 entradas |
| IA — Gobernanza, riesgo y ética | [`ia-gobernanza/INDEX.md`](ia-gobernanza/INDEX.md) | v1 — 6 entradas |
| Marketing | [`marketing/INDEX.md`](marketing/INDEX.md) | v1 — 8 entradas |
| UX / UI | [`ux-ui/INDEX.md`](ux-ui/INDEX.md) | v1 — 8 entradas |
| Tecnología empresarial | [`tecnologia-empresarial/INDEX.md`](tecnologia-empresarial/INDEX.md) | v1 — 7 entradas |
| Costos | [`costos/INDEX.md`](costos/INDEX.md) | v1 — 7 entradas |
| Investigación | [`investigacion/INDEX.md`](investigacion/INDEX.md) | v1 — 6 entradas |

**Total catalogado:** ~98 entradas en 11 dominios.

Próximos candidatos (orden sugerido):

- **Profundización por dominio existente**: añadir 5-10 entradas más
  donde se note un hueco recurrente (ej. más NOMs en salud, más
  marcos de IA aplicados a sectores).
- **Sector financiero MX específico**: CNBV, CONDUSEF, Ley FinTech.
- **Sector telecomunicaciones MX**: IFT, Ley Federal de Telecomunicaciones.
- **Estándares de calidad**: ISO 9001:2015, modelos de excelencia (EFQM, Baldrige).
- **Sustentabilidad / ESG**: GRI Standards, SASB, TCFD, ISSB.
- **Traducción**: marcos de traducción profesional (ISO 17100, Newmark, Nida) — para `/tra`.

### Pieza D — Mirror local del usuario (`local/`)

Carpeta ignorada por git donde cada usuario puede colocar (o symlinkear)
sus copias legalmente adquiridas de los documentos del catálogo. Esto
permite trabajar **offline** y respeta el copyright (cada usuario es
dueño de sus propias copias).

El script [`.claude/scripts/biblioteca-sync.py`](../.claude/scripts/biblioteca-sync.py)
automatiza el mapeo entre el catálogo y las copias locales del usuario.

```
library/local/
├── .gitkeep                    # solo para que git preserve la carpeta
├── ausubel-1963.pdf            # tu copia legal, no versionada
├── nif-2024/                   # tu copia legal del CINIF
└── ...
```

Configuración del usuario (no versionada — vive en `~/.config/biblioteca-local.yaml`):

```yaml
# Mapeo: catalog_id → ruta local en tu disco
ausubel-1963: ~/Documents/libros/psicologia-aprendizaje-verbal-significativo.pdf
nif-2024: ~/Documents/contabilidad/CINIF-NIF-2024/
lfpdppp-2010: # vacío — biblioteca-sync descargará la versión pública desde el URL del catálogo
```

---

## Integración con los skills

Los skills consultan la biblioteca de dos maneras:

1. **En sus referencias del dominio** (sección final APA 7): cuando
   citan una norma, libro o ley, deben apuntar a la entrada del
   catálogo (`id: <slug>`) para que el lector pueda verificar la
   versión vigente.

2. **En tiempo de uso del modo**: el modo `/inv` como apoyo transversal
   consulta el catálogo antes de etiquetar una afirmación como
   `[DOCUMENTADO]`. Si la fuente citada no está en el catálogo o tiene
   `status: superseded`, lo señala explícitamente.

Esta integración se documenta en `CLAUDE.md` §9 (Comportamientos
obligatorios) como regla operativa.

---

## Cómo contribuir entradas

Para añadir una fuente al catálogo:

1. Verificar que cumple criterios mínimos:
   - Es una **fuente primaria** (norma oficial, libro publicado por
     editor reconocido, ley en gaceta oficial, paper peer-reviewed).
   - Tiene **edición o versión identificable**.
   - Su contenido es **citable** (DOI, URL oficial, ISBN, número de
     publicación oficial).
2. Añadir entrada en `CATALOG.yaml` con todos los campos obligatorios
   (ver schema en el propio catálogo).
3. Si el dominio aún no tiene `INDEX.md`, crearlo (mínimo: panorama
   del dominio + 3 fuentes ya catalogadas).
4. Si la entrada modifica relaciones (`superseded_by`, `complements`),
   actualizar las entradas afectadas.
5. PR al repo con descripción de la fuente y justificación de su
   inclusión.

Ver `CONTRIBUTING.md` §1 para criterios generales y §2 para criterios
de aceptación.

---

## Schema del catálogo (resumido)

```yaml
- id: <slug-único>                       # obligatorio
  titulo: Título oficial                  # obligatorio
  autores: [Apellido, N. N.; ...]         # obligatorio (puede ser un organismo)
  año: 2024                               # obligatorio (año de edición vigente)
  edicion_vigente: "2nd ed. (2024)"       # obligatorio
  categoria: norma|libro|regulacion|guia|articulo|gaceta
  dominios: [finanzas, seguridad, ...]    # qué dominios la citan
  skills: [/fin, /seg, ...]               # qué skills la referencian
  license: copyright|public_domain|creative_commons
  status: vigente|superseded_by:<id>      # obligatorio
  doi: 10.xxxx/yyyy                       # cuando existe
  url_oficial: https://...                # obligatorio si no hay DOI
  idiomas: [es, en, ...]
  traduccion_es:                          # cuando aplica
    titulo_es: ...
    editor_es: ...
    isbn_es: ...
  confianza: alta|media|baja              # juicio del curador
  notas: |
    Texto libre con advertencias relevantes.
```

---

## ¿Por qué no incluir los PDFs directamente?

- **Copyright**: la mayoría de fuentes profesionales (NIF, IFRS, ISO,
  libros académicos) están sujetas a derechos de autor activos. Su
  redistribución sin licencia es ilegal.
- **Bloat**: PDFs académicos pesan 10–50 MB cada uno. Una biblioteca
  modesta de 50 fuentes excedería 1 GB.
- **Obsolescencia silenciosa**: si una norma se actualiza, tener el PDF
  desactualizado en el repo *parece* autoritativo sin serlo.

El catálogo de metadatos resuelve los tres problemas: cero copyright
violation, peso mínimo (kilobytes vs gigabytes), y trazabilidad
explícita de versión vigente.
