# Medicina — Índice de fuentes confiables

Cubre los textos de referencia clínica general que los skills `/medicina`
y `/audiologia` consumen como conocimiento de base: cirugía, pediatría,
geriatría, dermatología y medicina interna de pregrado.

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `medicina`.

---

## Capas del cuerpo de literatura médica general

```
NIVEL DE REPASO CLÍNICO INTEGRAL (visión panorámica multidisciplinaria)
──────────────────────────────────────────────────────────────────────
  cto-manual-9                ← repaso MIR/ENARM; cubre 20+ especialidades
  manual-mip-2                ← referencia para el médico interno de pregrado MX

NIVEL DE ESPECIALIDADES BÁSICAS
──────────────────────────────────────────────────────────────────────
  Cirugía:
    schwartz-principles-11    ← referencia internacional estándar (EN)
    schwartz-principios-10    ← versión en español (ES)
    pocket-surgery-2          ← referencia rápida de bolsillo

  Pediatría:
    nelson-pediatrics-21      ← referencia internacional estándar (EN)
    pediatria-martinez-8      ← referencia clásica México/Latinoamérica
    intro-pediatria-7         ← introducción clínica pediátrica en español

  Geriatría:
    brocklehurst-geriatrics-8 ← texto base de geriatría y gerontología (EN)
    manual-residente-geriatria ← guía práctica en español

  Dermatología:
    arenas-dermatologia       ← atlas diagnóstico y tratamiento MX

  ORL / Cabeza y cuello:
    dx-tto-orl-cabeza-cuello  ← referencia diagnóstico-terapéutica en español

  Cardiología básica:
    entiendo-ecg              ← introducción práctica al ECG

  Oftalmología:
    cto-oftalmo-10            ← repaso MIR/ENARM oftalmología
    ocular-emergency          ← urgencias oftalmológicas
```

---

## Jerarquía de consulta recomendada

### Para preguntas quirúrgicas
1. **Schwartz 11ª ed. (EN)** para fisiopatología y técnica quirúrgica actualizada
2. **Schwartz 10ª ed. (ES)** cuando se necesita citar en español
3. **Pocket Surgery** para decisiones rápidas perioperatorias

### Para preguntas pediátricas
1. **Nelson 21ª ed.** para evidencia actualizada internacional
2. **Pediatría Martínez 8ª** para contexto latinoamericano y criterios nacionales
3. **Introducción a la Pediatría** para conceptos básicos pediátricos

### Para preguntas geriátricas
1. **Brocklehurst 8ª** para fisiopatología del envejecimiento y síndromes geriátricos
2. **Manual del Residente en Geriatría** para guías prácticas del manejo clínico

### Para contexto clínico general (repaso MX)
- **CTO-9** cubre el temario del ENARM; útil como mapa conceptual rápido
- **Manual del MIP** para protocolos básicos de medicina interna de pregrado

---

## Solapamiento con dominio audiología

`dx-tto-orl-cabeza-cuello` se usa tanto en `/audiologia` como en este
dominio — es la referencia principal de ORL que conecta los dos cuerpos
de literatura.

El skill `/audiologia` cita `nelson-pediatrics-21` para hipoacusia
pediátrica y síndromes congénitos con repercusión auditiva.

---

## Pendientes conocidos

- **Medicina interna adultos** (Harrison, Cecil, Goldman-Cecil) — pendiente de agregar
- **Farmacología** (Goodman & Gilman, Katzung) — pendiente
- **Urgencias/Emergencias** — pendiente más allá de oftalmología
- **Neurología** — pendiente (relevante para otoneurología)
- **Radiología** — pendiente (imágenes de oído, mastoides, ángulo pontocerebeloso)

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
