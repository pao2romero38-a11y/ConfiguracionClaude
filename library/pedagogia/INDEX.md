# Pedagogía y aprendizaje significativo — Índice

Este índice cubre los marcos teóricos que sostienen el skill `/edu`
del proyecto: aprendizaje significativo, taxonomías cognitivas,
diseño instruccional y evaluación de transferencia.

Todas las entradas están en
[`CATALOG.yaml`](../CATALOG.yaml) bajo `pedagogia`. Aquí se agregan
relaciones entre teorías y orden recomendado de lectura.

---

## Mapa de la literatura pedagógica usada por `/edu`

```
NIVEL FUNDACIONAL (qué ES aprender significativamente)
─────────────────────────────────────────────────────
  ausubel-1963                       ← punto de partida obligatorio
    Aprendizaje significativo:
    "el factor más importante que influye en el aprendizaje
     es lo que el alumno ya sabe"

NIVEL DE OBJETIVOS (qué se debe poder hacer)
─────────────────────────────────────────────────────
  bloom-1956                         ← clásico histórico
       │ revisión 2001
       ▼
  anderson-krathwohl-2001            ← VIGENTE — usar este

NIVEL DE DISEÑO INSTRUCCIONAL (cómo se diseña una clase)
─────────────────────────────────────────────────────
  gagne-conditions-1985              ← 9 eventos de instrucción
  merrill-first-principles-2002      ← 5 principios universales
  cast-udl-2.2-2018                  ← accesibilidad y diversidad

NIVEL DE EVALUACIÓN (cómo se mide aprendizaje + transferencia)
─────────────────────────────────────────────────────
  kirkpatrick-four-levels-2016       ← 4 niveles: reacción, aprendizaje, 
                                       comportamiento, resultados

NIVEL METODOLÓGICO (cómo se investiga lo anterior)
─────────────────────────────────────────────────────
  booth-craft-research-2016          ← cuando /edu se combina con /inv
```

---

## Cómo se usan en una sesión `/edu` típica

El skill `/edu` impone un formato de entrega con 10 secciones (ver
`.claude/skills/edu/SKILL.md`). Cada sección consume al menos una de
las teorías catalogadas:

| Sección del skill | Teoría que la fundamenta | Entrada en catálogo |
|---|---|---|
| [PANORAMA] | Organizador avanzado | [`ausubel-1963`](../CATALOG.yaml) |
| [ACTIVACIÓN] | Conexión con conocimiento previo | [`ausubel-1963`](../CATALOG.yaml) · [`merrill-first-principles-2002`](../CATALOG.yaml) |
| [CONCEPTO CENTRAL] | Diferenciación progresiva | [`ausubel-1963`](../CATALOG.yaml) |
| [ANALOGÍA / ANCLA] | Anclaje conceptual | [`ausubel-1963`](../CATALOG.yaml) |
| [EJEMPLO REAL] | Aplicación contextualizada | [`merrill-first-principles-2002`](../CATALOG.yaml) |
| [COMPETENCIA EN ACCIÓN] | Indicadores observables | [`anderson-krathwohl-2001`](../CATALOG.yaml) |
| [ACTIVIDAD INTEGRADORA] | Aprender haciendo | [`merrill-first-principles-2002`](../CATALOG.yaml) · [`gagne-conditions-1985`](../CATALOG.yaml) |
| [EVALUACIÓN] | Rúbrica con verbos Bloom | [`anderson-krathwohl-2001`](../CATALOG.yaml) |
| [TRANSFERENCIA AL PUESTO] | Kirkpatrick Nivel 3 | [`kirkpatrick-four-levels-2016`](../CATALOG.yaml) |
| [REFERENCIAS] | APA 7 + actualidad | (todas las anteriores) |

Esta tabla es trazabilidad operativa: cada elemento del diseño
instruccional remite a una fuente catalogada y citable.

---

## Reglas de actualidad (heredadas del CLAUDE.md §3.1)

- **Bloom 1956 está superseded** por Anderson & Krathwohl 2001. Citar
  Bloom solo como referencia histórica; usar Anderson & Krathwohl para
  diseño curricular contemporáneo.
- **Kirkpatrick 1959** (el original de Donald) sigue siendo válido
  conceptualmente pero la versión 2016 de los Kirkpatrick hijos
  incorpora 50 años de práctica. Citar 2016.
- **CAST UDL 2.2 (2018)** es la versión más reciente al corte de este
  índice. Verificar si CAST ha publicado UDL 3.0+ antes de citar.

---

## Orden de lectura recomendado (para alguien que parte de cero)

1. **Ausubel 1963** — para entender qué significa "aprendizaje
   significativo" como opuesto a memorización. Sin este, los demás
   marcos suenan a tecnicismo vacío.
2. **Anderson & Krathwohl 2001** — para aprender a redactar objetivos
   de aprendizaje en verbos observables (los 6 niveles cognitivos).
3. **Merrill 2002** — síntesis pragmática de 5 principios que se
   verifican en cualquier diseño instruccional efectivo. Solo 17
   páginas, lectura obligatoria.
4. **Gagné 1985** — para diseñar la secuencia operativa de una clase
   o módulo (los 9 eventos de instrucción).
5. **Kirkpatrick 2016** — cuando se necesita demostrar que la
   capacitación cambió el comportamiento o produjo resultados de
   negocio, no solo "gustó al participante".
6. **CAST UDL 2.2** — cuando hay diversidad de aprendices o
   accesibilidad como requisito.
7. **Booth et al. 2016** — para investigación pedagógica empírica,
   tesis o publicación académica del propio diseño instruccional.

---

## Validación práctica

Los 7 episodios de la serie `serie-mejora-continua` (en `training/`)
son un caso real de aplicación de este cuerpo teórico:

- Cada episodio tiene las 10 secciones del skill `/edu`
- Cada sección referencia (implícita o explícitamente) una de las
  fuentes de este índice
- La rúbrica final de la serie usa el modelo Kirkpatrick
- Los verbos de las actividades integradoras siguen Anderson & Krathwohl
- Las analogías centrales explotan el anclaje al estilo Ausubel

Si quieres ver la teoría en acción antes de adoptarla en tu propio
trabajo, revisa `training/serie-mejora-continua/episodio-0-...md` como
punto de entrada.

---

## Pendientes conocidos del dominio

- **Vygotsky** (zona de desarrollo próximo) — relevante para
  capacitación con apoyo entre pares. Pendiente catalogar.
- **Brookfield** (educación crítica de adultos) — para audiencias
  profesionales experimentadas. Pendiente.
- **Sweller** (Cognitive Load Theory) — para diseño de materiales
  con alta densidad cognitiva (caso típico de capacitación técnica).
  Pendiente.
- **Schön** (The Reflective Practitioner) — para aprendizaje basado
  en práctica reflexiva, relevante para coaching y mentoría. Pendiente.

PRs bienvenidos para extender este índice. Ver `CONTRIBUTING.md` §1.
