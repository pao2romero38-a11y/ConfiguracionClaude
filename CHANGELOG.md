# Changelog

Todos los cambios relevantes a este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/es/1.1.0/)
y este proyecto adhiere a [Semantic Versioning 2.0.0](https://semver.org/lang/es/).

---

## [Unreleased]

Cambios en preparación que aún no se han publicado en una versión.

---

## [2.10.0] — 2026-05-12

**Cierre del ciclo de biblioteca — 100 % cobertura skill ↔ library
+ integración explícita en SKILL.md + tercera receta estándar de
`/capacidad`.** Bump MENOR. Pasamos de 11 → 13 dominios y de ~101 →
~122 entradas.

Cuatro tracks completados en este commit:

1. **Cobertura del último skill sin biblioteca** (`/tra`): nuevo
   dominio `traduccion/` con 7 entradas (ISO 17100, ISO 20771,
   Newmark, Nida & Taber, Venuti, Hurtado Albir, ATA Code of Ethics).
2. **Integración explícita** en cada `SKILL.md`: 16 skills con campo
   `Biblioteca de referencia` apuntando al INDEX del dominio
   correspondiente. Operacionaliza la regla obligatoria del
   `CLAUDE.md` §9 al hacer visible el pointer dentro del propio
   skill.
3. **Receta estándar `/capacidad` §9 bis.3**: descarga automatizada
   de documentos en dominio público desde URL oficial al catálogo.
   Wrapper `descargar-publicos.py` (3 modos: `--dry-run`, `--download`,
   `--report`). 46 entradas elegibles al corte.
4. **Profundización selectiva**: nuevo dominio `esg-sustentabilidad/`
   (7 entradas: GRI, SASB, IFRS S1/S2, TCFD, ISO 14001, OECD MNE,
   UN SDGs); extensión de `regulacion-mx/` con sub-bloque sectorial
   (CNBV, CONDUSEF, IFT, COFEPRIS, COFECE) y NOMs adicionales de
   salud (NOM-007-SSA2, NOM-046-SSA2).

### Added

#### Track 1 — `library/traduccion/INDEX.md` (7 entradas)

- `iso-17100-2015` — Translation services (certificable)
- `iso-20771-2020` — Legal translation (specific)
- `newmark-textbook-translation-1988` — métodos semántico vs comunicativo
- `nida-taber-translation-1982` — equivalencia dinámica vs formal
- `venuti-translators-invisibility-2008` — domesticación vs extranjerización
- `hurtado-albir-traductologia-2017` — manual estándar en español
- `ata-code-of-ethics` — código ético ATA (US)

#### Track 2 — Integración en 16 SKILL.md (× 2 copias: repo + activa)

Skills actualizados con bloque `> **Biblioteca de referencia:**`:
- `/edu` → `pedagogia`
- `/inv` → `investigacion`
- `/fin`, `/proy` → `finanzas`
- `/mkt` → `marketing`
- `/tec` → `tecnologia-empresarial`
- `/seg`, `/rsk`, `/ci` → `seguridad-cumplimiento`
- `/aud` → `auditoria`
- `/dis` → `ux-ui`
- `/cost` → `costos`
- `/tra` → `traduccion` (recién creado en este commit)
- `/ai`, `/ai-llm`, `/ai-ml` → `ia-gobernanza`

#### Track 3 — Tercera receta `/capacidad` §9 bis.3

- `.claude/scripts/descargar-publicos.py` (~180 líneas) — descarga
  fuentes con `license: public_domain` + `url_oficial` válido a
  `library/local/` (ignorado por git). 3 modos: `--dry-run`,
  `--download`, `--report`.
- Filtros duros: NUNCA descarga copyrighted; nunca redistribuye;
  guarda solo en uso personal del usuario.
- `.claude/skills/capacidad/SKILL.md` §9 bis.3 documenta la receta.

#### Track 4 — `library/esg-sustentabilidad/INDEX.md` (7 entradas)

- `gri-standards-2021` — más adoptado globalmente; doble materialidad
- `sasb-standards-2018` — específicos por industria; ahora bajo ISSB
- `issb-s1-s2-2023` — IFRS Sustainability Disclosure Standards
- `tcfd-recommendations-2017` — superseded by IFRS S2 desde 2024
- `iso-14001-2015` — SGA certificable
- `oecd-multinationals-2023` — conducta empresarial responsable
- `un-sdgs-2015` — 17 ODS agenda 2030

#### Track 4 — extensión de `regulacion-mx/` (7 entradas adicionales)

Sub-bloque sectorial:
- `cnbv-disposiciones` — Comisión Nacional Bancaria y de Valores
- `condusef-disposiciones` — protección al usuario financiero
- `ift-lineamientos` — Instituto Federal de Telecomunicaciones
- `cofepris-disposiciones` — Protección contra Riesgos Sanitarios
- `cofece-disposiciones` — Competencia Económica

NOMs salud adicionales:
- `nom-007-ssa2-2016` — Embarazo, parto y puerperio
- `nom-046-ssa2-2005` — Violencia familiar, sexual y contra las mujeres

### Changed

- **`library/CATALOG.yaml`** — ~122 entradas en 13 dominios.
- **`library/README.md`** — tabla de 13 dominios; próximos candidatos
  refinados a temas específicos (Ley FinTech, T-MEC, ISO 9001, etc.).
- **`library/regulacion-mx/INDEX.md`** — secciones nuevas para sector
  específico y NOMs salud adicionales.

### Cambios en numeración

- `VERSION`: `2.9.0` → `2.10.0`.

### Compatibilidad

- 100 % backward-compatible con v2.9.0. Solo añade.

### Cobertura final skill ↔ biblioteca tras v2.10.0

| Skill | Biblioteca | Estado |
|---|---|---|
| `/edu` | pedagogia | ✓ con bloque en SKILL.md |
| `/inv` | investigacion | ✓ |
| `/fin`, `/proy`, `/cost`, `/mkt`, `/tec`, `/dis` | dominio propio cada uno | ✓ |
| `/seg`, `/rsk`, `/ci`, `/aud` | seguridad-cumplimiento + regulacion-mx + auditoria | ✓ |
| `/ai`, `/ai-llm`, `/ai-ml` | ia-gobernanza | ✓ |
| `/tra` | **traduccion** (nuevo) | ✓ |

**Cobertura total**: 100 % de los 17 skills profesionales del repo
tienen al menos un dominio de biblioteca asociado y referenciado
explícitamente en su `SKILL.md`.

### Decisiones técnicas

- Slides PNG SÍ versionados, audio/video NO (decidido en v2.6.0;
  mantenido).
- Documentos copyrighted NUNCA en el repo; pointer a URL oficial
  como fuente de verdad (decidido en v2.7.0; mantenido).
- `library/local/` ignorado por git para copias personales del
  usuario (decidido en v2.7.0; mantenido).
- `library/CATALOG.yaml` permanece como única fuente de verdad
  machine-readable; los INDEX son narrativa complementaria.

### Próximas iteraciones (no incluidas)

Las direcciones de crecimiento estructural están cubiertas. Las
próximas adiciones serán **temáticas según demanda**: nuevas normas
publicadas, sectores específicos que un PR cubra, traducciones
adicionales, marcos de calidad (ISO 9001), tratados internacionales
firmados por México.

---

## [2.9.0] — 2026-05-12

**Expansión del catálogo a 11 dominios — 5 nuevos dominios + 4
sub-bloques en regulación MX.** Bump MENOR. Pasamos de 49 → ~101
entradas en 6 → 11 dominios.

Cierra los huecos identificados en v2.8.0 para los skills sin cobertura
(`/mkt`, `/dis`) y añade dominios complementarios (tecnología
empresarial, costos, investigación). Refuerza `regulacion-mx` con los
4 marcos legales más solicitados después de datos personales.

### Added — 5 nuevos dominios

#### `library/marketing/INDEX.md` (8 entradas)

- `kotler-keller-marketing-management-2022` — manual estándar mundial, 16ª ed.
- `porter-competitive-strategy-1980` — 5 fuerzas competitivas
- `aaker-brand-equity-1991` — 5 dimensiones del valor de marca
- `ries-trout-positioning-2001` — posicionamiento de marca
- `kahneman-thinking-2011` — heurísticas y sesgos del consumidor
- `christensen-innovators-dilemma-1997` — disrupción tecnológica
- `godin-permission-marketing-1999` — marketing digital opt-in
- `ama-definition-marketing-2017` — definición oficial AMA

#### `library/ux-ui/INDEX.md` (8 entradas)

- `norman-design-everyday-things-2013` — human-centered design
- `nielsen-10-heuristics-1994` — rúbrica universal de evaluación
- `krug-dont-make-me-think-2014` — usabilidad pragmática
- `cooper-about-face-2014` — interaction design sistemático
- `wcag-2-2-2023` — accesibilidad W3C (estándar legal en muchas jurisdicciones)
- `material-design-3` — sistema de diseño Google
- `ios-hig` — Apple Human Interface Guidelines
- `iso-9241-110-2020` — ergonomía sistemas-humano

#### `library/tecnologia-empresarial/INDEX.md` (7 entradas)

- `togaf-10-2022` — marco más adoptado de Enterprise Architecture
- `brown-zachman-framework-2017` — ontología (taxonomía EA)
- `ross-it-savvy-2009` — alineamiento TI-negocio para directivos
- `davenport-process-innovation-1993` — reingeniería habilitada por TI
- `newman-microservices-2021` — arquitectura microservicios
- `hohpe-enterprise-integration-2003` — patrones de integración asíncrona
- `nist-sp-800-160v1r1-2022` — engineering trustworthy secure systems

#### `library/costos/INDEX.md` (7 entradas)

- `horngren-cost-accounting-2021` — manual estándar mundial, 17ª ed.
- `cooper-kaplan-abc-1991` — Activity-Based Costing por sus autores
- `monden-toyota-1998` — Toyota Production System (target costing, kaizen)
- `imai-kaizen-1986` — mejora continua aplicada
- `shank-strategic-cost-mgmt-1993` — costos + estrategia
- `kaplan-norton-balanced-scorecard-1996` — BSC con 4 perspectivas
- `cokins-performance-management-2009` — integración costos + BSC + riesgos

#### `library/investigacion/INDEX.md` (6 entradas)

- `creswell-research-design-2023` — cuali/cuanti/mixto, 6ª ed.
- `hernandez-sampieri-metodologia-2014` — estándar iberoamericano
- `saunders-research-methods-2023` — investigación aplicada en negocios
- `yin-case-study-2018` — estudios de caso, 6ª ed.
- `kuhn-scientific-revolutions-1962` — paradigmas científicos
- `oecd-frascati-2015` — definición y medición de I+D (estándar global)

### Added — extensión de `regulacion-mx` con 4 sub-bloques

#### Sub-bloque fiscal (5 entradas)

- `cff-1981` — Código Fiscal de la Federación
- `lisr-2013` — Ley del Impuesto Sobre la Renta
- `liva-1978` — Ley del Impuesto al Valor Agregado
- `liepys-1980` — Ley del IEPS
- `rmf-anual` — Resolución Miscelánea Fiscal anual del SAT

#### Sub-bloque mercantil (3 entradas)

- `codigo-comercio-1889` — Código de Comercio
- `lgsm-1934` — Ley General de Sociedades Mercantiles (incluye SAS)
- `lgtoc-1932` — Ley General de Títulos y Operaciones de Crédito

#### Sub-bloque laboral (4 entradas)

- `lft-1970` — Ley Federal del Trabajo (con reforma 2019)
- `lss-1995` — Ley del Seguro Social (con reforma 2020 de subcontratación)
- `linfonavit-1972` — Ley INFONAVIT
- `nom-035-stps-2018` — Factores de riesgo psicosocial en el trabajo

#### Sub-bloque salud (4 entradas)

- `lgs-1984` — Ley General de Salud
- `nom-004-ssa3-2012` — Expediente clínico
- `nom-024-ssa3-2012` — Sistemas de Registro Electrónico para la Salud (SIRES)
- `nom-035-ssa3-2012` — Información en salud

### Changed

- **`library/CATALOG.yaml`** — extendido a ~101 entradas en 11 dominios.
- **`library/README.md`** — tabla de dominios con 11 entradas; lista de
  próximos candidatos refinada (profundización por dominio, sectores
  específicos MX, sustentabilidad/ESG, traducción).
- **`library/regulacion-mx/INDEX.md`** — añadidas 4 secciones para los
  sub-bloques nuevos con tablas de cita rápida.

### Cambios en numeración

- `VERSION`: `2.8.0` → `2.9.0`.

### Compatibilidad

- 100 % backward-compatible con v2.8.0. Solo añade.

### Cobertura skill ↔ biblioteca tras v2.9.0

| Skill | Dominios con cobertura |
|---|---|
| `/edu` | pedagogia · investigacion |
| `/inv` | investigacion · pedagogia (transversal) |
| `/fin` | finanzas · regulacion-mx (fiscal/mercantil) |
| `/proy` | finanzas (PMBOK) · regulacion-mx (mercantil) · marketing · tecnologia-empresarial |
| `/cost` | costos · finanzas |
| `/mkt` | **marketing** (nuevo) |
| `/dis` | **ux-ui** (nuevo) |
| `/tec` | **tecnologia-empresarial** (nuevo) · seguridad-cumplimiento |
| `/seg` | seguridad-cumplimiento · regulacion-mx |
| `/rsk` | seguridad-cumplimiento · regulacion-mx · ia-gobernanza |
| `/ci` | seguridad-cumplimiento · regulacion-mx (todos los sub-bloques) |
| `/aud` | auditoria · seguridad-cumplimiento · regulacion-mx |
| `/ai`, `/ai-llm`, `/ai-ml` | ia-gobernanza |
| **Sin cobertura aún** | `/tra` |

Solo `/tra` queda sin cobertura específica; será atendido en una
próxima iteración con marcos de traducción profesional (ISO 17100,
Newmark, Nida, Venuti).

### Próximas iteraciones (no incluidas)

- Cobertura específica para `/tra` (marcos de traducción).
- Profundización en dominios existentes (más NOMs, más estándares ESG).
- Integración explícita en cada `SKILL.md`: campo `library:`
  apuntando al INDEX del dominio.
- Receta `/capacidad` §9 bis.3 para descarga automatizada de
  documentos en dominio público desde URL oficial.

---

## [2.8.0] — 2026-05-12

**Expansión del catálogo a 4 dominios profesionales adicionales.**
Bump MENOR. Pasamos de 16 → 49 entradas en 2 → 6 dominios. Los 4
nuevos cubren las disciplinas más solicitadas por los skills del repo.

### Added

#### `library/finanzas/INDEX.md` (8 entradas)

- `nif-2024` — Normas de Información Financiera, CINIF, México
- `cinif-marco-conceptual` — Marco conceptual de las NIF
- `ifrs-2024` — International Financial Reporting Standards, IASB
- `us-gaap-fasb-codification` — FASB Accounting Standards Codification
- `pmbok-7-2021` — PMI Project Management Body of Knowledge, 7th ed
- `brealey-myers-corporate-finance-2022` — Principles of Corporate Finance, 14th ed
- `ross-westerfield-corporate-finance-2022` — Fundamentals of Corporate Finance, 13th ed
- `damodaran-investment-valuation-2012` — Damodaran on valuación

#### `library/seguridad-cumplimiento/INDEX.md` (13 entradas)

- `iso-27001-2022` — SGSI certificable
- `iso-27002-2022` — controles de seguridad (guía)
- `iso-27005-2022` — gestión de riesgos de seguridad
- `iso-31000-2018` — marco general de riesgos
- `nist-csf-2-2024` — Cybersecurity Framework 2.0 (con función GOVERN)
- `nist-sp-800-53r5` — controles de seguridad y privacidad
- `nist-sp-800-30r1` — guía de evaluación de riesgos
- `coso-ic-2013` — Internal Control — Integrated Framework
- `coso-erm-2017` — Enterprise Risk Management
- `cobit-2019` — gobernanza de TI
- `itil-4-2019` — gestión de servicios de TI
- `pci-dss-4-2022` — seguridad de datos de tarjetas
- `gdpr-2016` — Reglamento General de Protección de Datos UE

#### `library/auditoria/INDEX.md` (6 entradas)

- `iia-standards-2024` — Global Internal Audit Standards (vigentes desde enero 2025)
- `iia-ippf-2017` — IPPF anterior (superseded por iia-standards-2024)
- `isa-iaasb-2024` — International Standards on Auditing
- `ifac-handbook-2024` — compendio anual oficial
- `issai-intosai-2022` — Auditoría gubernamental
- `aicpa-code-of-conduct-2024` — Código ético CPA US

#### `library/ia-gobernanza/INDEX.md` (6 entradas)

- `eu-ai-act-2024` — Reglamento UE 2024/1689 con aplicación escalonada
- `iso-42001-2023` — primera norma ISO certificable para AIMS
- `iso-23894-2023` — gestión de riesgos en IA
- `nist-ai-rmf-1-2023` — AI Risk Management Framework
- `oecd-ai-principles-2024` — 5 principios de IA confiable
- `unesco-ai-ethics-2021` — Recomendación global de ética en IA

### Changed

- **`library/CATALOG.yaml`** — extendido a 49 entradas en 6 dominios.
- **`library/README.md`** — tabla de dominios actualizada (6 dominios
  catalogados) y lista de próximos candidatos refinada (marketing,
  UX/UI, costos, investigación, marco fiscal/mercantil/laboral/salud MX).

### Cambios en numeración

- `VERSION`: `2.7.0` → `2.8.0`.

### Compatibilidad

- 100 % backward-compatible con v2.7.0. La extensión del catálogo no
  modifica ninguna entrada existente; solo añade.

### Cobertura por skill (estado actual)

| Skill | Dominios con cobertura en library/ |
|---|---|
| `/edu` | pedagogia |
| `/fin` | finanzas |
| `/proy` | finanzas (PMBOK) |
| `/cost` | finanzas |
| `/seg` | seguridad-cumplimiento, regulacion-mx |
| `/rsk` | seguridad-cumplimiento, regulacion-mx, ia-gobernanza |
| `/ci` | seguridad-cumplimiento, regulacion-mx |
| `/aud` | auditoria, seguridad-cumplimiento, regulacion-mx |
| `/tec` | seguridad-cumplimiento |
| `/ai` | ia-gobernanza |
| `/ai-llm` | ia-gobernanza (vía `/ai`) |
| `/ai-ml` | ia-gobernanza (vía `/ai`) |

Sin cobertura aún: `/mkt`, `/dis`, `/tra`, `/inv` directamente
(este último consulta transversalmente).

### Próximas iteraciones (no incluidas)

- Marketing, UX/UI, costos como dominios completos.
- Cobertura del marco fiscal y laboral mexicano dentro de regulacion-mx.
- Integración explícita en cada `SKILL.md`: campo `library:` apuntando
  al INDEX del dominio.
- Receta `/capacidad` §9 bis.3 para descarga automatizada de
  documentos en dominio público desde URL oficial.

---

## [2.7.0] — 2026-05-12

**Biblioteca de referencias confiables** — nueva sección `library/` del
repo siguiendo el modelo B + E + D: catálogo central + índices por
dominio + sincronización local. Bump MENOR.

### Motivación

Los skills citan normas, leyes, libros y estándares. Hasta ahora, cada
SKILL.md tenía su propia sección "Referencias del dominio (APA 7)"
inconsistentes entre sí, sin trazabilidad de versión vigente y sin
forma de verificar si un usuario tiene acceso local a la fuente. Esta
versión centraliza ese conocimiento.

Tres piezas complementarias:

- **B — Catálogo central YAML**: única fuente de verdad sobre qué
  edición de cada fuente debe citarse, con metadatos (DOI, URL oficial,
  license, status vigente/superseded, idiomas, traducciones).
- **E — Índices por dominio**: documentos narrativos con panorama,
  relaciones entre fuentes, advertencias de uso, orden recomendado de
  lectura.
- **D — Sincronización local**: script para mapear copias legalmente
  adquiridas del usuario en `library/local/` (gitignored).

### Added

- **`library/README.md`** — explicación del modelo, schema del catálogo,
  cómo contribuir entradas.

- **`library/CATALOG.yaml`** — catálogo central machine-readable. 16
  entradas iniciales en 2 dominios:
  - **pedagogia** (8): Ausubel 1963, Bloom 1956 (superseded),
    Anderson & Krathwohl 2001, Merrill 2002, Gagné 1985, CAST UDL 2.2,
    Kirkpatrick 2016, Booth et al. 2016.
  - **regulacion-mx** (8): CPEUM, CPF, DOF, LFPDPPP 2010, Reglamento
    LFPDPPP 2011, LGPDPPSO 2017, LGPC 2012, INAI Lineamientos.

- **`library/regulacion-mx/INDEX.md`** — panorama del cuerpo regulatorio
  mexicano, jerarquía constitución→leyes→reglamentos→lineamientos,
  diferencias LFPDPPP vs LGPDPPSO, cómo citar en evaluaciones de
  cumplimiento, pendientes conocidos.

- **`library/pedagogia/INDEX.md`** — mapa de la literatura pedagógica
  consumida por `/edu`, trazabilidad sección-del-skill ↔ teoría,
  reglas de actualidad (Bloom superseded por Anderson & Krathwohl),
  orden de lectura recomendado, validación práctica con la serie de
  capacitación.

- **`.claude/scripts/biblioteca-sync.py`** — wrapper que verifica
  cobertura local del usuario, genera symlinks de copias propias en
  `library/local/`, y produce reportes detallados del catálogo.
  Tres modos: `--check`, `--link`, `--report`.

- **`library/local/.gitkeep`** — placeholder para que git preserve la
  carpeta donde el usuario coloca sus copias legales (ignorada por
  `.gitignore`).

- **`CLAUDE.md` §9 — Comportamientos obligatorios**: nueva regla
  *"Antes de citar una norma, ley, libro o estándar profesional,
  consultar primero library/CATALOG.yaml o el INDEX.md del dominio
  correspondiente para confirmar la versión vigente y la edición
  canónica."*

### Cambios en numeración

- `VERSION`: `2.6.0` → `2.7.0`.

### Compatibilidad

- 100 % backward-compatible con v2.6.0. La biblioteca es de
  consulta opcional; los skills siguen funcionando sin consultarla
  pero pierden la garantía de actualidad de las citas.

### Próximas iteraciones (no incluidas)

- Más dominios: finanzas (NIF, IFRS, US GAAP), seguridad (ISO 27001,
  NIST CSF, COSO, ITIL 4), auditoría (IIA Standards, ISA), IA (NIST
  AI RMF, EU AI Act, ISO/IEC 42001).
- Integración explícita en cada `SKILL.md`: añadir campo `library:`
  apuntando al INDEX del dominio.
- Receta `/capacidad` §9 bis.3 para descarga automatizada de
  documentos en dominio público desde URL oficial.

---

## [2.6.0] — 2026-05-12

**Segunda receta estándar — render de slides + composición de video
sincronizado con audio.** Bump MENOR (funcionalidad nueva compatible
con v2.5.0). Cierra el ciclo de producción de material de capacitación:
markdown → audio + slides + video listo para publicar.

### Added

- **Skill `/capacidad` §9 bis.2 — render de slides + composición video
  con sincronización obligatoria**:
  - Motor de slides: `marp-cli` (npm install -g @marp-team/marp-cli).
  - Composición: ffmpeg con escalado proporcional para slide ↔ audio.
  - Diseño editorial cream + acento terracota, número de slide en
    esquina inferior derecha (solo el número), título del episodio en
    esquina superior izquierda.
  - Slide de conclusiones opcional al final con bullets numerados
    (cero render si el episodio no tiene entrada en el dict de
    conclusiones).
  - Comparativa lado a lado para slides con dos paneles.
  - Tolerancia hard 30 % entre audio real y duraciones declaradas;
    escalado proporcional absorbe diferencias menores transparentemente.

- **`.claude/scripts/slides.py`** (~320 líneas): wrapper que parsea la
  sección `# === ESTRUCTURA DE SLIDES ===` de cada episodio, asocia
  los `[ÉNFASIS]` del bloque de narración correspondiente como
  subtítulo de remate, y renderiza un PNG por slide más un `timing.json`.

- **`.claude/scripts/componer.py`** (~180 líneas): wrapper que combina
  audio (de `narrar.py`) + slides PNG (de `slides.py`) + timing en un
  mp4 final 1280×720 @ 30 fps con sincronización proporcional.

- **`training/serie-mejora-continua/slides-render/`**: 74 slides PNG
  versionados (~3.3 MB total) cubriendo los 7 episodios de la serie.
  Los videos finales NO se versionan (~37 MB combinados), se regeneran
  con `componer.py` a partir de los slides + audio.

- **`training/serie-mejora-continua/episodio-0-por-que-configurar.md`**:
  añadido el slide 8 (comparativa lado a lado) entre las respuestas
  por defecto y configurada del caso del analista junior de
  consultoría financiera. Renumerados slides 9-10.

### Changed

- `CONCLUSIONES_POR_EPISODIO` en `slides.py` ahora es estrictamente
  condicional: episodios sin entrada (o con bullets vacíos) NO reciben
  slide de conclusiones.

### Cambios en numeración

- `VERSION`: `2.5.0` → `2.6.0`.

### Compatibilidad

- 100 % backward-compatible con v2.5.0. Las recetas estándar
  acumuladas en `/capacidad` §9 bis crecen sin afectar capacidades
  ya investigadas.

### Pipeline de producción completo (verificado)

```bash
python3 .claude/scripts/narrar.py    <ep>.md   # audio narrado
python3 .claude/scripts/slides.py    <ep>.md   # slides PNG
python3 .claude/scripts/componer.py  <ep>.md   # video mp4 sincronizado
```

Tiempo total estimado para una serie de 7 episodios de 5-6 min:
~30-45 min de cómputo. Costo recurrente: cero.

---

## [2.5.0] — 2026-05-12

**Receta estándar de TTS + materiales de capacitación versionados.**
Bump MENOR (funcionalidad nueva compatible con v2.4.0).

Tres aportes complementarios al repo, derivados del trabajo real de
producir la primera serie de capacitación:

1. **Primera receta estándar pre-validada del protocolo `/capacidad`**:
   TTS local en español mexicano vía piper-tts + es_MX-claude-high, con
   parámetros, dependencias, bug conocido y diccionario de pronunciación
   inglesa documentados. Las próximas invocaciones de `/capacidad` para
   esta capacidad omiten los pasos de investigación y comparativa.
2. **Wrapper reutilizable `narrar.py`** versionado en `.claude/scripts/`.
   Lee scripts de capacitación en markdown, respeta marcadores
   `[PAUSA Ns]`, aplica el diccionario de pronunciación, y produce un wav
   por bloque + un wav concatenado por episodio.
3. **Sección `training/`** establecida en el repo como ubicación oficial
   de materiales de capacitación complementarios. Primera serie incluida
   (`serie-mejora-continua`, 7 episodios, ~38 min) como referencia que
   cualquier usuario del repo puede consumir, regenerar audio, modificar
   o tomar como plantilla para crear sus propias series.

### Added

- **`.claude/skills/capacidad/SKILL.md` §9 bis — Recetas estándar
  pre-validadas**: nueva sección con la primera receta documentada
  (TTS español MX cero costo) y las reglas para añadir nuevas recetas
  (solo entran tras smoke test exitoso + conformidad del usuario +
  afinación en uso real).
- **`.claude/scripts/narrar.py`** (~250 líneas): wrapper TTS para
  scripts en markdown con secciones `# === SCRIPT DE NARRACIÓN ===`.
- **`training/`** (sección nueva del repo):
  - `README.md` que explica el propósito, las series disponibles, el
    flujo de producción, el roadmap (slides + video composición con
    requisito de sincronización slide↔audio) y el modelo de
    contribución de series complementarias.
  - `serie-mejora-continua/` — 1 archivo de diseño maestro + 7
    archivos de episodio con script de narración, slides estructurados
    y notas de producción.
- **`CONTRIBUTING.md` §1**: ampliación del alcance esperado de
  contribuciones para incluir series nuevas, recetas estándar
  validadas, wrappers reutilizables y configuraciones derivadas.
- **`.gitignore`**: patrones para excluir audio/video producido bajo
  `training/**/` (se regenera con `narrar.py` o herramientas de render).

### Cambios en numeración

- `VERSION`: `2.4.0` → `2.5.0`.

### Compatibilidad

- 100 % backward-compatible con v2.4.0. La receta estándar es opcional —
  el protocolo `/capacidad` sigue funcionando para capacidades no
  documentadas. La serie en `training/` no afecta a ningún skill ni
  ninguna regla del repo.

### Próxima iteración (no incluida en esta versión)

- Receta estándar de render de slides para complementar la serie de
  capacitación. La descripción del problema y los 4 niveles candidatos
  ya están en `training/README.md` — ejecutar el protocolo `/capacidad`
  para evaluar y elegir cuando alguien lo necesite.
- Script de composición video con sincronización slide ↔ audio
  derivada del eje temporal del markdown.

---

## [2.4.0] — 2026-05-12

Nueva **meta-skill** `/capacidad` para detectar, investigar e instalar
herramientas que faltan cuando una petición las requiere. Bump MENOR
(funcionalidad nueva compatible con v2.3.0).

Esta versión también introduce dos reglas de comportamiento — una
prohibida y una obligatoria — que formalizan en `CLAUDE.md` §8 y §9 la
obligación de invocar `/capacidad` antes de declarar imposibilidad por
falta de herramienta. Es la primera regla de comportamiento del proyecto
con una skill operativa asociada.

### Added

- **Skill `/capacidad`** (`.claude/skills/capacidad/SKILL.md`) — gestor de
  capacidades. Se auto-activa cuando se detecta una brecha real entre lo
  que la petición requiere y los tools disponibles. También invocable
  manualmente. El protocolo:
  - **Diagnóstico de brecha**: capacidad requerida + tools relevantes
    + confianza de que la brecha es real.
  - **Investigación en 4 niveles ordenados por costo creciente**:
    Nivel 1 Scripts helper · Nivel 2 CLIs locales · Nivel 3 MCP servers
    · Nivel 4 APIs externas. Cada opción se evalúa contra 4 ejes
    (costo · setup · calidad · latencia) usando `/inv` como apoyo
    transversal para etiquetado epistémico.
  - **Recomendación + plan B** con justificación.
  - **Menú interactivo** (`AskUserQuestion`) para que el usuario apruebe
    o cancele.
  - **Implementación específica por nivel** con reglas duras (nunca
    versionar API keys; nunca instalar sin aprobación; nunca omitir
    validación post-instalación).
  - **Smoke test** obligatorio: input mínimo conocido → output esperado.
  - **Registro en `MEMORY.md`** como reference memory para evitar
    re-investigar la misma capacidad en sesiones futuras.
  - **Regreso a la tarea original** si la activación fue automática.

- **CLAUDE.md §8 — Comportamientos prohibidos**: nueva regla
  *"Declarar imposibilidad para cumplir una petición sin antes evaluar
  si el bloqueo es por falta de herramienta y, si lo es, invocar
  /capacidad."*

- **CLAUDE.md §9 — Comportamientos obligatorios**: nueva regla
  *"Invocar /capacidad antes de declarar imposibilidad por falta de
  herramienta — investigar primero opciones (Scripts → CLIs → MCP →
  APIs), proponer la menos costosa que cumpla y, si el usuario aprueba,
  implementarla."*

- **CLAUDE.md §5 — Índice de skills**: nueva entrada `/capacidad`.
  Total de skills: 40 → 41. Sub-grupo *Meta-skills*: 1 → 2.

- **CLAUDE.md §11 — Banner de inicio**: línea `Meta-skills:` actualizada
  para incluir `/capacidad`.

- **CLAUDE.md §12 — Comandos rápidos**: nueva entrada `/capacidad` en
  la sección *Meta-skills*.

### Cambios en numeración

- `VERSION`: `2.3.0` → `2.4.0`.
- Footer de `CLAUDE.md`: 40 → 41 skills.

### Compatibilidad

- 100 % backward-compatible con v2.3.0. La auto-activación solo dispara
  cuando hay una brecha real entre la petición y los tools disponibles;
  no afecta a modos existentes ni a peticiones que sí se pueden cumplir.
  Ninguna instalación ocurre sin aprobación explícita del usuario.

---

## [2.3.0] — 2026-05-12

Nueva **meta-skill** `/prompt` para refinar prompts crudos del usuario antes
de ejecutarlos, con rúbrica visible de 10 dimensiones y menú interactivo
de ejecución. Bump MENOR (funcionalidad nueva compatible con v2.2.1).

Diseñada como v1 modo entrenamiento. Plan documentado en el propio `SKILL.md`
para migrarla a v2 apoyo transversal (`+prompt` componible con cualquier
modo líder) cuando el patrón de refinamiento sea predecible (>70 % de
ejecuciones "tal cual" sin alternativas).

### Added

- **Skill `/prompt`** (`.claude/skills/prompt/SKILL.md`) — refinador de
  prompts modo-aware. Detecta el modo apropiado entre los 17 modos de
  operación a partir de señales en el prompt crudo, propone composición
  líder + apoyo cuando aplica, refina el prompt añadiendo las dimensiones
  ausentes y expone una **rúbrica de 10 dimensiones** (modo, contexto,
  alcance, restricciones técnicas, estándares, entregable, fase, convenciones,
  riesgos, datos bloqueantes) con tres estados (✓ / ⚠ / ✗).
  Tras mostrar el refinado, ofrece un menú interactivo (`AskUserQuestion`)
  con tres ramas (sin alternativas) o cuatro (con alternativas):
  ejecutar tal cual, ejecutar variante A/B, empezar de nuevo, o cerrar.
  La rama *empezar de nuevo* incluye pista derivada de la rúbrica anterior
  para acelerar la convergencia.

- **CLAUDE.md §5 — Índice de skills**: nueva entrada `/prompt`, sub-grupo
  *Meta-skills*. Total de skills: 39 → 40.

- **CLAUDE.md §11 — Banner de inicio**: línea adicional `Meta-skills:` con
  `/prompt`.

- **CLAUDE.md §12 — Comandos rápidos**: nueva categoría *Meta-skills* con
  `/prompt`.

### Cambios en numeración

- `VERSION`: `2.2.1` → `2.3.0`.
- Footer de `CLAUDE.md`: 39 → 40 skills.

### Compatibilidad

- 100 % backward-compatible con v2.2.1. La skill solo se activa cuando el
  usuario invoca explícitamente `/prompt`. Ningún cambio en modos
  existentes, agentes, templates ni en el método de desarrollo (§4 ter).

---

## [2.2.1] — 2026-05-12

Bump PATCH (corrección cosmética sin cambio funcional).

### Fixed

- **`CLAUDE.md` §1.1 y §10 yaml**: corregidas 2 ocurrencias residuales
  de "14 dominios cubiertos" → "17 dominios cubiertos" que se quedaron
  del estado pre-v2.1.0 (antes de añadir la familia `/ai`). El §5
  total, el §10 yaml `modos_disponibles`/`skills_total`/`agentes` y el
  footer ya estaban correctos; estos dos strings se habían omitido en
  el pase de documentación de v2.1.0.

### Compatibilidad

- 100% backward-compatible con v2.2.0. Ningún cambio en skills, agentes,
  templates ni comportamiento. Solo texto descriptivo.

---

## [2.2.0] — 2026-05-11

Adopción de la **maquinaria operativa del método de desarrollo de sistemas**.
Bump MENOR (funcionalidad nueva compatible con v2.1.0). Trabajo publicado
como **ola única** según el plan en
`ConfiguracionAI/PROPUESTA-MODO-DEV.md` y guiado por
`ConfiguracionAI/CRITERIOS-EVALUACION-DEV.md`.

### Added

- **CLAUDE.md §4 ter — Método de desarrollo de sistemas.** Sección nueva
  que define las **5 fases secuenciales** (Metadata → Arquitectura →
  Stack → Bootstrap → Desarrollo), los **9 niveles progresivos de
  metadata**, la metadata como SSOT verificable, el patrón multi-DBMS,
  la convivencia multi-agente y la Definition of Done compartida.

- **Skill `/dev-meta`** (~430 líneas) — núcleo metadata-driven. Define
  las 7 tablas obligatorias (`tablas_sistema`, `campos_sistema`, `roles`,
  `procesos`, `semaforos`, `variables_sistema`, `componentes_sistema`,
  `metadata_versiones`) con DDL SQL-92 estricto, los 9 niveles
  progresivos, los 3 codegen obligatorios y 17 reglas de integridad.

- **Skill `/dev-multiagent`** — convivencia multi-agente opcional con
  bus obligatorio si se activa. Mensajes append-only, pendientes split
  por scope, identidad de agente en git.

- **10 skills de ciclo de vida del proyecto**: `/init-proyecto`,
  `/stack-pick`, `/install-from-stack`, `/back-scaffold-from-meta`,
  `/front-scaffold-from-meta`, `/meta-add-tabla`, `/meta-bump`,
  `/meta-validate`, `/diff-meta`, `/arq-derive`.

- **3 skills de operación multi-agente**: `/status`, `/handoff`,
  `/inbox`.

- **4 agentes especializados en `.claude/agents/`**:
  - `be-reviewer` (backend, default si hay división backend/frontend)
  - `ui-reviewer` (frontend, default si hay división)
  - `code-reviewer` (fallback genérico si no hay división)
  - `message-bus` (enrutador de mensajes inter-agente)

- **`templates/` con maquinaria ejecutable del método**:
  - `migrate.js` — runner multi-DBMS up/down/status/triggers
  - `bootstrap.sh` — script de inicialización
  - `migrations/` con 11 migraciones bootstrap SQL-92 (0001-0011) y la
    guía `PORTABLE-SQL.md`
  - `db-adapters/` con 6 motores: postgres, mysql, sqlserver, oracle,
    db2, spanner. Cada uno con `adapter.js` + `triggers.sql`
  - `codegen/` con 3 scripts: `meta-derive-types.js`,
    `meta-derive-openapi.js`, `front-msw-from-meta.js`
  - `backend/` con `health.js`, `logger.js`
  - `eslint-rules/local-rules.js` (no-hardcoded-querykey, etc.)
  - `.husky/pre-commit` — hook genérico (lint + orphan-check + secret
    detection + message-bus-validate)
  - `scripts/orphan-migration-check.sh`,
    `scripts/message-bus-validate.js`
  - `.github/workflows/` con 5 workflows: `ci.yml`, `ci-matrix.yml`
    (postgres+mysql+sqlserver bloqueante), `ci-matrix-opt.yml`
    (oracle+db2 opt-in), `audit.yml` (npm audit semanal),
    `release-please.yml` (semantic release)

- **Identidad de agente en git**: `.claude/agents-config.json` +
  `.claude/apply-agent-identity.js` para inyectar trailer
  `Authored-Agent:` en commits cuando se activa multi-agente.

- **Template `templates/.claude/settings.local.json`** con 24 permisos
  auto-aprobados recomendados para proyectos del método: npm scripts
  (test/lint/build/dev/typecheck/preflight, meta:types/openapi/msw),
  scripts (migrate.js, message-bus-validate.js, codegen), git read-only
  (status/diff/log/branch/show) y lectura del cwd (`Read(./**)`). NO
  incluye permisos de escritura, push, deploy ni acciones destructivas.
  El `/init-proyecto` puede copiarlo al `.claude/settings.local.json` del
  proyecto generado. También sugerido a nivel `~/.claude/settings.local.json`
  un subconjunto mínimo (npm test/lint, git status/diff, lectura de la
  carpeta de proyectos).

- **Memoria técnica creciente** — 17 lecciones reutilizables agregadas a
  `~/.claude/projects/.../memory/` (timestamp-precision-cross-dbms,
  trigger-double-insert, session-replication-role, set-local-transaction,
  tailwind-v4-silent-fail, tanstack-querykey-mismatch, safari-date-input,
  rhf-controller-vs-register, dark-mode-contrast,
  scrollable-region-focusable, mobile-drawer-vs-sidebar, msw-handler-drift,
  tanstack-query-cache-cross-resource, branch-namespace,
  migrations-vs-service, protocolo-mensajes, pendientes-ssot).

### Changed

- **`/dev/SKILL.md` §11 — Definition of Done compartida.** Una sola DoD
  que adoptan los tres reviewers. Incluye CÓDIGO, CONCURRENCIA,
  DATOS Y BD, METADATA, API, PRUEBAS, ROLES, MODOS GLOBALES, más
  extensiones específicas para be-reviewer y ui-reviewer.

- **`/dev-api/SKILL.md` §15 — Contrato canónico.** Matriz HTTP por verbo,
  Problem+JSON (RFC 9457), envelope `{data, next_cursor}`, serialización
  canónica (TIMESTAMP → ISO, BOOLEANO → 0|1), idempotencia con
  `Idempotency-Key`, versionado aditivo con paralelo 90 días.

- **`CLAUDE.md` §5 (índice de skills):** 15 skills nuevos añadidos
  (10 ciclo de vida + 3 multi-agente + 2 dev-* nuevos).
  Total actualizado: 24 → 39.

- **`CLAUDE.md` §10 yaml:** conteos actualizados (39 skills, 4 agentes);
  nueva sección `metodo_desarrollo` con fases=5, niveles_metadata=9,
  dbms_soportados=6.

- **`CLAUDE.md` §11 mensaje de inicio:** familia /dev, ciclo de vida,
  multi-agente, agentes listados; comandos `/fases`, `/niveles` añadidos.

- **`CLAUDE.md` §12 comandos rápidos:** 15 comandos nuevos.

- **`README.md` raíz:** tabla de familias actualizada con las nuevas;
  estructura del repo expandida con `templates/` y `agents/`.

- **`.claude/skills/README.md`:** conteos actualizados; nuevas secciones
  de ciclo de vida y multi-agente.

### Criterios de las decisiones

Las decisiones aplicaron los criterios de
`ConfiguracionAI/CRITERIOS-EVALUACION-DEV.md`:

1. **Metadata-driven y 5 fases como OBLIGATORIOS** (no opcionales) — son
   el propósito del método (§2.1, §2.2 del criterios).
2. **Multi-DBMS preservado como diferenciador** — los 6 adapters van como
   templates concretos, no como guía abstracta (§2.3).
3. **Memoria expandible con filtro "reutilizable"**, no "agnóstico" — las
   17 lecciones aplican a todo proyecto del mismo paradigma (§2.4).
4. **Reviewers be/ui como DEFAULT, code-reviewer como FALLBACK** — la
   mayoría de sistemas tienen división backend/frontend (§3.2).
5. **DoD una sola, compartida por los 3 reviewers** (§3.3).
6. **Multi-agente opcional pero bus obligatorio si activo** (§3.1).
7. **Una sola ola, no 3 fases separadas** — los cambios son coherentes y
   no destructivos.

### Beneficios medibles

- Skills totales: **24 → 39** (+62%).
- Agentes especializados: **0 → 4**.
- DBMS soportados: **0 → 6** con adapter pattern.
- Niveles de capacidad declarables: **0 → 9**.
- Lecciones técnicas en memoria: **0 → 17**.
- Workflows de CI listos para copiar: **0 → 5**.
- Skills cubriendo ciclo de vida del proyecto end-to-end: **0 → 10**.
- Conteo de archivos en `templates/`: **0 → ~50**.

### Compatibilidad

- v2.2.0 es compatible con v2.1.0 (bump MINOR según SemVer).
- Los skills nuevos NO afectan los modos existentes.
- Las invariantes preservadas: APA 7, presentación general → particular,
  composición de modos, SYSTEM_MODE, 5 roles obligatorios, SQL-92
  estricto, protocolo de concurrencia, protocolo de calidad de 4 pasos.

---

## [2.1.0] — 2026-05-11

Primera adición de una nueva familia de skills al repo. Bump MINOR
(funcionalidad nueva compatible con la versión anterior).

### Added

- **Familia `/ai` con 3 skills.** Cubre los tres perfiles profesionales
  reales del campo de IA, siguiendo el patrón de la familia `/dev`
  (un skill principal + sub-skills por sub-dominio):

  - **`/ai` — Experto en IA (estrategia y gobierno).**
    Casos de uso, ROI/TCO, vendor selection, build vs. buy vs. partner,
    marcos regulatorios (EU AI Act 2024, NIST AI RMF 1.0 + GenAI Profile
    2024, ISO/IEC 42001:2023), AI literacy, hoja de ruta de adopción.
    Audiencia: AI lead, director, consultor, PM, arquitecto.

  - **`/ai-llm` — Aplicaciones de LLMs.**
    Prompt engineering, RAG, agentes, selección de modelo
    (Claude/GPT/Gemini/open source), evaluación (golden datasets,
    LLM-as-judge, benchmarks), mitigación de prompt injection y jailbreaks.
    Incluye jerarquía de técnicas (prompting → few-shot → CoT → RAG →
    agents → fine-tuning) con regla de escalamiento solo ante fallo.
    Audiencia: ML engineer con LLMs, prompt engineer, agent builder.

  - **`/ai-ml` — ML / MLOps.**
    Ciclo de vida del modelo, detección de drift (datos y concepto),
    monitoring en producción, feature stores, A/B testing, retraining.
    Define los **8 componentes obligatorios** de un sistema ML productivo
    (heurística: si faltan componentes, no está en producción, está en
    "demo permanente con tráfico real"). Referencia Sculley et al.
    (2015) sobre deuda técnica oculta en ML.
    Audiencia: ML engineer tradicional, MLOps engineer, data scientist
    productivo.

- **Combinaciones de modos recomendadas con IA** (en CLAUDE.md §4 bis):
  - `/ai +tec` — Estrategia de adopción de IA en una organización
  - `/ai +seg +rsk` — Evaluación de riesgo de un sistema de IA en producción
  - `/ai +ci` — Controles internos para uso de IA generativa
  - `/ai-llm +dev` — Implementación técnica de aplicación con LLMs
  - `/ai-ml +dev-test` — ML con cobertura de pruebas y eval suite

### Changed

- **`CLAUDE.md` §4 (tabla de modos):** 3 filas nuevas para `/ai`,
  `/ai-llm`, `/ai-ml`.
- **`CLAUDE.md` §5 (índice de skills):** 3 filas nuevas y total
  actualizado a 24 skills.
- **`CLAUDE.md` §10 (yaml):** `modos_disponibles` 14 → 17,
  `skills_total` 21 → 24, nueva sub-categoría `ia: [ai, ai-llm, ai-ml]`.
- **`CLAUDE.md` §11 (mensaje de inicio):** nueva fila "IA:" en la lista
  de modos disponibles.
- **`CLAUDE.md` §12 (comandos rápidos):** 3 filas nuevas.
- **`CLAUDE.md` pie de página:** "14 modos · 21 skills" → "17 modos · 24 skills".
- **`.claude/skills/README.md`:** nueva sección "Skills de IA (3)",
  conteo 21 → 24, footer actualizado a la identidad del proyecto.
- **`README.md` raíz:** familia "Inteligencia Artificial" agregada
  a la tabla de modos, conteo "21 skills" → "24 skills", "14 dominios"
  → "17 dominios".
- **`GOVERNANCE.md`:** "14 dominios" → "17 dominios" en el rol Contribuidor.

### Criterios de las decisiones

1. **Tres skills, no uno.** Cubrir los tres perfiles profesionales reales
   (estratega / LLM engineer / MLOps) en archivos separados respeta el
   patrón de la familia `/dev` y permite que cada usuario active solo el
   skill relevante a su trabajo del día.
2. **Audiencia profesional confirmada.** Lenguaje técnico, terminología
   sin simplificar, sin disclaimers patronizantes — solo advertencia de
   evolución rápida del campo.
3. **Sin implicaciones legales especiales** (a diferencia de `/med` y
   `/psi`), por lo que no se introducen protocolos de seguridad
   adicionales. Sí se mantienen advertencias estándar de no-asesoría
   legal/regulatoria.
4. **Marcos de referencia vigentes:** EU AI Act 2024, NIST AI RMF 1.0
   + GenAI Profile 2024, ISO/IEC 42001:2023, OWASP Top 10 for LLM
   Applications 2025.

### Beneficios medibles

- Cobertura de dominio: **14 → 17 dominios** (+21%).
- Skills totales: **21 → 24** (+14%).
- Profesionales de IA atendidos: **0 → 3 perfiles claros** (estratega,
  LLM engineer, MLOps engineer).

### Pendiente

- `/med` y `/psi` postergados — requieren cierre de alcance y validación
  de protocolos de derivación. Se agregarán en una iteración futura.
- `LICENSE` sigue pendiente; el repo es público bajo "all rights reserved"
  implícito hasta que se agregue.

---

## [2.0.0] — 2026-05-11

Primera ronda de refactor sobre la configuración heredada. Cambios
estructurales en `CLAUDE.md` y correcciones transversales en skills.

### Added

- **CLAUDE.md §1.1 — Principio de no-trivialidad.** Regla explícita que
  documenta el alcance del proyecto: configuración para trabajo profesional
  especializado, no para consultas triviales. Para preguntas casuales,
  Claude debe sugerir abrir una sesión sin esta configuración.
- **CLAUDE.md §4 bis — Composición de modos.** Nuevas reglas para combinar
  varios modos en un mismo prompt usando el patrón "líder + apoyo".
  Define sintaxis (`/lider +apoyo1 +apoyo2`), 6 reglas de composición
  (verificaciones unificadas, referencias fundidas, advertencias
  concatenadas, máximo 3 skills), y 7 combinaciones recomendadas.
  Resuelve comportamiento previamente indefinido al invocar modos múltiples.

### Changed

- **CLAUDE.md §5 — De especificación duplicada a índice delgado.** La
  versión anterior duplicaba literalmente el contenido de cada SKILL.md
  (~690 líneas, ~40 KB). Ahora §5 es un índice que apunta a
  `.claude/skills/<modo>/SKILL.md` como única fuente de verdad. Reduce
  `CLAUDE.md` de 1273 a 724 líneas (-43%), libera ~30 KB de contexto en
  cada sesión, y elimina riesgo de desincronización entre las dos copias.
- **CLAUDE.md — Marcador de versión.** Eliminada la referencia "v2.1"
  del encabezado y el pie. La versión vigente ahora se gobierna desde
  el archivo `VERSION` en la raíz del repo (SemVer).
- **CLAUDE.md §10 — Contexto del proyecto.** Yaml actualizado para
  reflejar la identidad nueva del repo (`ConfiguracionClaude`), audiencia
  profesional, gobierno y referencia a `GOVERNANCE.md` y `VERSION`.
- **CLAUDE.md §11 — Mensaje de inicio de sesión.** Reemplazado para
  referenciar `VERSION` en vez de marca interna estática, y mencionar
  la disponibilidad de §4 bis (composición).

### Fixed

- **Corte temporal de conocimiento — `ago 2025` → `enero 2026`.**
  Actualizadas 8 ocurrencias en 3 archivos: `CLAUDE.md` (4 lugares),
  `.claude/skills/inv/SKILL.md` (3 lugares),
  `.claude/skills/dev-test/SKILL.md` (1 lugar). El modelo activo de
  Claude tiene corte enero 2026; la marca anterior estaba desfasada
  5 meses respecto al modelo en uso.
- **`.claude/skills/README.md` — Conteo de skills.** Corregido el
  encabezado de "20 skills" a "21 skills" (8 dev-* + 13 dominio), que
  ya era correcto en el pie de página y coincide con los directorios
  reales en `.claude/skills/`.

### Criterios de las decisiones

Los cambios siguen los criterios formalizados en la sesión de revisión
previa al refactor:

1. **Eliminar duplicación** entre `CLAUDE.md` y los `SKILL.md` (deuda
   técnica identificada como la principal en la evaluación inicial).
2. **Documentar reglas implícitas** (principio de no-trivialidad,
   composición de modos) que hasta ahora vivían solo en la cabeza del
   mantenedor.
3. **Alinear con el modelo activo** (corte temporal correcto).
4. **No tocar los SKILL.md** salvo para correcciones puntuales: el
   contenido especializado se respeta y queda como única fuente de verdad
   de cada dominio.

### Beneficios medibles

- Tamaño de contexto cargado en cada sesión: **-43%** en `CLAUDE.md`.
- Fuentes de verdad para cada modo: **2 → 1** (elimina riesgo de divergencia).
- Reglas para combinar modos: **indefinido → 6 reglas + 7 ejemplos**.
- Coherencia temporal: **5 meses de desfase → 0**.
- Conteo de skills: **inconsistente (20 vs 21) → 21 en todos lados**.

---

## [1.0.0] — 2026-05-11

### Added

- **Documentación inicial del proyecto:**
  - `README.md` con origen, audiencia, quick start y estructura.
  - `USAGE.md` con tres opciones de instalación (clon como base, copia a
    proyecto existente, instalación global) y verificación de configuración.
  - `CONTRIBUTING.md` con alcance, criterios de aceptación, flujo Git y
    plantilla de PR.
  - `GOVERNANCE.md` con roles, proceso de decisión, política SemVer y
    cadencia de releases.
  - `CHANGELOG.md` (este archivo).
  - `VERSION` con la versión vigente en formato SemVer.
  - `.gitignore` para excluir ruido de macOS y archivos de editores.

### Notes

Esta versión establece la base documental del proyecto sobre la
configuración importada en `v1.0.0-baseline`. No modifica la configuración
en sí (CLAUDE.md ni SKILL.md). La primera ronda de refactor se publica
en v2.0.0.

---

## [1.0.0-baseline] — 2026-05-11

### Added

- **Configuración importada desde ConfiguracionAI:**
  - `CLAUDE.md` v2.1 con 14 modos de operación (4 core + 10 dominio).
  - 21 skills bajo `.claude/skills/`:
    - **Programación (8):** `/dev` `/dev-api` `/dev-clean` `/dev-db`
      `/dev-docker` `/dev-git` `/dev-modes` `/dev-test`.
    - **Dominio (13):** `/edu` `/inv` `/fin` `/mkt` `/tec` `/proy`
      `/seg` `/rsk` `/ci` `/aud` `/dis` `/cost` `/tra`.
  - `.claude/skills/README.md` con índice de skills.

### Notes

Punto de partida del repositorio. Copia literal de `ConfiguracionAI/`
sin modificaciones. Este tag se preserva como referencia histórica del
estado inicial.

---

## Criterios de versionado (resumen)

```
MAYOR (X.0.0) — Cambios incompatibles
MENOR (1.X.0) — Funcionalidad nueva compatible
PATCH (1.0.X) — Correcciones sin cambio funcional
```

Detalle completo en [`GOVERNANCE.md`](GOVERNANCE.md) §3.

---

*Mantenido por el mantenedor del repo. Todo cambio publicado pasa por el
proceso descrito en `GOVERNANCE.md`.*
