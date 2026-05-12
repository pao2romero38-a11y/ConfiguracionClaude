# UX / UI — Diseño centrado en el usuario — Índice de fuentes confiables

Cubre los marcos de diseño de interacción, usabilidad y accesibilidad
que el skill `/dis` consume. Tangencialmente útil a `/seg` (componentes
de UX que afectan seguridad) y `/edu` (diseño de materiales didácticos).

Las entradas están en [`CATALOG.yaml`](../CATALOG.yaml) bajo `ux-ui`.

---

## Capas del cuerpo de literatura

```
NIVEL TEÓRICO (cómo se diseña pensando en el usuario)
─────────────────────────────────────────────────────
  norman-design-everyday-things-2013      ← human-centered design
  cooper-about-face-2014                  ← interaction design sistemático

NIVEL DE USABILIDAD (cómo se evalúa)
─────────────────────────────────────────────────────
  nielsen-10-heuristics-1994              ← rúbrica universal de evaluación
  krug-dont-make-me-think-2014            ← pragmático, lectura corta

NIVEL DE PLATAFORMA (cómo se diseña para X)
─────────────────────────────────────────────────────
  ios-hig                                  ← Apple (iOS / macOS / etc.)
  material-design-3                        ← Google (Android, Material Web)

NIVEL DE ACCESIBILIDAD Y ESTÁNDARES
─────────────────────────────────────────────────────
  wcag-2-2-2023                            ← W3C — estándar mundial
  iso-9241-110-2020                        ← ISO ergonomía sistemas-humano
```

---

## Cuándo citar qué

| Caso de uso | Marco principal | Complementos |
|---|---|---|
| Diseño de un producto nuevo | **Norman + Cooper** | Material o iOS HIG según plataforma |
| Evaluación heurística de un producto existente | **Nielsen** | WCAG si hay requerimiento de accesibilidad |
| Audit de accesibilidad | **WCAG 2.2** | ISO 9241-110 para contexto industrial |
| Onboarding o microcopy | **Krug** + Nielsen | — |
| Diseño para iOS / macOS / Vision Pro | **iOS HIG** | Norman y Cooper como complemento conceptual |
| Diseño para Android / Material Web | **Material Design 3** | Norman y Cooper como complemento conceptual |
| Diseño de equipos industriales / paneles complejos | **ISO 9241-110** + Norman | — |

---

## WCAG 2.2 — nivel mínimo operativo

Para cumplimiento legal en la mayoría de jurisdicciones (EU
Accessibility Act 2025, ADA US, etc.), el nivel mínimo operativo es
**AA** (no A). Para sectores públicos o sensibles (salud, educación,
banca), apuntar a **AAA** en componentes críticos.

WCAG 2.2 añade 9 criterios sobre 2.1:

- 2.4.11 Focus Not Obscured (Minimum) — AA
- 2.4.12 Focus Not Obscured (Enhanced) — AAA
- 2.4.13 Focus Appearance — AAA
- 2.5.7 Dragging Movements — AA
- 2.5.8 Target Size (Minimum) — AA
- 3.2.6 Consistent Help — A
- 3.3.7 Redundant Entry — A
- 3.3.8 Accessible Authentication (Minimum) — AA
- 3.3.9 Accessible Authentication (Enhanced) — AAA

**Cita obligatoria** del nivel WCAG en cualquier especificación de UX.

---

## Las 10 heurísticas de Nielsen (vigentes; refinadas 2020)

Referencia rápida porque son la rúbrica más usada en evaluaciones:

1. **Visibilidad del estado del sistema**
2. **Match entre el sistema y el mundo real**
3. **Control y libertad del usuario**
4. **Consistencia y estándares**
5. **Prevención de errores**
6. **Reconocimiento en lugar de recuerdo**
7. **Flexibilidad y eficiencia de uso**
8. **Estética y diseño minimalista**
9. **Ayuda al usuario a reconocer, diagnosticar y recuperarse de errores**
10. **Ayuda y documentación**

---

## Decisión Material 3 vs iOS HIG

Si tu producto cruza ambas plataformas (cosa común hoy):

- **Adoptar el HIG de la plataforma** cuando la app es nativa de ella.
  Los usuarios esperan los patrones de "su" plataforma.
- **Diseñar un sistema propio** que pueda renderizar según plataforma
  si el producto es multiplataforma con consistencia de marca como
  prioridad.
- **No mezclar patrones** (ej. botones con sombras Material en iOS o
  switches iOS en Android) — produce sensación de "app extraña".

---

## Pendientes conocidos del dominio

- **Garrett — The Elements of User Experience** — modelo en 5 capas
  (estrategia → alcance → estructura → esqueleto → superficie).
  Pendiente.
- **Buxton — Sketching User Experiences** — pendiente.
- **Tufte — The Visual Display of Quantitative Information** — para
  visualización de datos. Pendiente.
- **GOV.UK Design System** y **U.S. Web Design System** — sistemas
  públicos. Pendientes.
- **Sistema de diseño Cobalt (Adobe)**, **Carbon (IBM)**, **Polaris
  (Shopify)** — pendientes según relevancia del cliente.
- **ARIA Authoring Practices Guide** — para componentes web
  accesibles. Pendiente.

PRs bienvenidos. Ver `CONTRIBUTING.md` §1.
