# Traducción profesional — Índice de fuentes confiables

Cubre los marcos teóricos y normativos de traducción profesional que
el skill `/tra` consume.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `traduccion`.

---

## Capas del cuerpo de literatura

```
NIVEL TEÓRICO (qué es traducir bien)
─────────────────────────────────────────
  nida-taber-translation-1982       ← equivalencia dinámica vs formal
  newmark-textbook-translation-1988 ← métodos semántico vs comunicativo
  venuti-translators-invisibility-2008 ← domesticación vs extranjerización

NIVEL DE TRADUCTOLOGÍA APLICADA
─────────────────────────────────────────
  hurtado-albir-traductologia-2017  ← manual estándar en español

NIVEL NORMATIVO (estándares profesionales)
─────────────────────────────────────────
  iso-17100-2015                    ← servicios de traducción (certificable)
  iso-20771-2020                    ← traducción jurídica específica

NIVEL ÉTICO PROFESIONAL
─────────────────────────────────────────
  ata-code-of-ethics                ← código de la ATA (US)
```

---

## Cuándo citar qué

| Caso de uso | Marco principal | Complementos |
|---|---|---|
| Filosofía de traducción del proyecto | **Nida & Taber** | Newmark, Venuti según postura |
| Manual de iniciación traductológica en español | **Hurtado Albir** | Newmark |
| Evaluar proveedor de servicios de traducción | **ISO 17100** | ISO 20771 si es jurídica |
| Traducción jurídica certificada | **ISO 20771** + ISO 17100 | — |
| Resolución de dilemas éticos | **ATA Code** | Código IFAC si confluye con auditoría |
| Traducción literaria / cultural | **Venuti** | Newmark |
| Adaptación cultural (localización) | **Newmark** + Hurtado Albir | — |

---

## Equivalencia dinámica vs formal — la decisión central

Nida & Taber establecieron las dos posturas opuestas que aún hoy
estructuran la decisión de cada traducción:

| Equivalencia formal | Equivalencia dinámica |
|---|---|
| Reproduce las palabras del original | Reproduce el efecto del original |
| Conserva la estructura sintáctica fuente | Adapta a la estructura natural del idioma destino |
| Lector sabe que está leyendo una traducción | Lector siente que el texto fue escrito en su idioma |
| Apropiada en: textos sagrados, jurídicos, técnicos donde la forma importa | Apropiada en: prosa, marketing, capacitación, comunicación general |

El skill `/tra` adopta **equivalencia dinámica como default** (ver
SKILL.md §2 "Principios de traducción"). Excepciones explícitas:
jurídico (formal por requisito legal), técnico cuando se mantienen
términos en inglés por convención del sector.

---

## ISO 17100 — flujo mínimo de calidad

El estándar exige que toda traducción profesional pase por:

1. **Traducción** por traductor competente (criterios definidos)
2. **Revisión** por persona distinta (criterios definidos)
3. **Aprobación final** (revisión por experto del dominio cuando aplique)

**Implicación operativa**: una traducción producida solo por un
traductor (sin revisor independiente) NO cumple ISO 17100. Para
trabajos críticos (legales, médicos, financieros oficiales) este
flujo es obligatorio.

---

## Cuándo se requiere traducción jurada / certificada en México

ISO 20771 cubre el aspecto técnico, pero en México la certificación
formal de traducciones requiere:

- **Perito traductor** registrado ante el Consejo de la Judicatura
  Federal o local — para procedimientos judiciales.
- **Notario público** — para autenticación pública en algunos
  contextos.
- **Apostilla** — para documentos extranjeros oficiales (Convención
  de La Haya).

El SKILL.md de `/tra` incluye advertencia obligatoria en traducciones
jurídicas: la traducción de Claude NO tiene valor legal sin
certificación humana correspondiente.

---

## Pendientes conocidos del dominio

- **Vinay & Darbelnet** (Stylistique comparée du français et de
  l'anglais) — fundacional sobre procedimientos de traducción. Pendiente.
- **House** (Translation Quality Assessment) — pendiente.
- **Reiss & Vermeer** (Skopos theory) — pendiente.
- **Toury** (Descriptive Translation Studies) — pendiente.
- **ASTM F2575-14** — Standard Guide for Quality Assurance in
  Translation (US). Pendiente.
- **CSA Research / GALA** — estándares de la industria moderna de
  localización. Pendiente.

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
