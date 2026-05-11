# CONTRIBUTING — Cómo proponer mejoras

Esta configuración crece con aportes de especialistas en cada uno de los
dominios cubiertos. Si trabajas profesionalmente en un dominio y detectas
una oportunidad de mejora en su SKILL correspondiente, este documento
explica cómo enviar tu propuesta.

---

## 1. Alcance esperado de las contribuciones

### ✅ Sí se reciben

- Mejoras al `SKILL.md` del modo donde tienes experticia profesional.
- Correcciones de referencias APA 7 desactualizadas o erróneas.
- Nuevos marcos normativos vigentes que falten en un skill (ej. una norma
  ISO actualizada, una guía clínica revisada).
- Nuevos ejemplos concretos que mejoren la sección `[DATO DE EJEMPLO]`.
- Combinaciones de modos típicas en tu disciplina que valga la pena documentar.

### ⚠ Requiere discusión previa antes de enviar PR

- Cambios al `CLAUDE.md` raíz (afectan a todos los modos).
- Cambios estructurales al modelo de skills (frontmatter, secciones).
- Modificación de advertencias obligatorias (especialmente en `/fin`, `/med`, `/psi`).
- Cambios al modelo de gobierno o versionado.

Para estos, abre primero un **issue de discusión** antes de invertir
tiempo en el PR.

### ❌ No se reciben sin justificación fuerte

- Cambios cosméticos sin impacto funcional.
- Reorganización general "porque queda mejor así".
- Inclusión de fuentes sin DOI/URL verificable.
- Material en formato distinto a APA 7.

---

## 2. Criterios de aceptación

Todo PR se evalúa contra los principios del `CLAUDE.md` raíz. Para que
proceda, debe cumplir:

```
□ Estructura general → particular en cualquier texto agregado
□ Referencias APA 7, ordenadas más reciente → más antigua
□ DOI cuando la fuente lo tiene; URL cuando no
□ Marcadores de certeza [DOCUMENTADO/INFERIDO/ESTIMADO] donde aplique
□ No introducir ceremonia para casos triviales (fuera de alcance del repo)
□ Marcos normativos citados son la versión vigente
□ Cambios trazables: un solo tema por PR
□ Entrada en CHANGELOG.md describiendo el cambio
```

---

## 3. Flujo de Git

### Paso 1 — Fork y rama

```bash
# Fork desde GitHub o trabajar sobre tu clon local
git clone https://github.com/<tu-usuario>/ConfiguracionClaude.git
cd ConfiguracionClaude
git checkout -b proposal/<modo>-<descripcion-corta>
```

**Convención de nombre de rama:**
```
proposal/fin-actualizar-WACC-2026
proposal/seg-agregar-NIST-CSF-2.0-profile
proposal/edu-corregir-referencia-CAST
```

### Paso 2 — Cambios

Modifica únicamente los archivos del modo en el que tienes experticia.
PRs que toquen múltiples skills sin justificación cruzada se devuelven
para dividir.

### Paso 3 — Commit

Usa **Conventional Commits** (referenciado por el skill `/dev-git`):

```
feat(skills/fin): agregar análisis de modelo de Gordon
fix(skills/seg): corregir referencia a NIST SP 800-207
docs(skills/edu): actualizar lista de marcos pedagógicos
```

El cuerpo del commit debe explicar:
- **Qué** cambia
- **Por qué** (justificación profesional)
- **Fuente** APA 7 que respalda el cambio (si aplica)

### Paso 4 — CHANGELOG

Agrega una entrada bajo la sección `## [Unreleased]` en `CHANGELOG.md`
con el tipo de cambio:

```markdown
## [Unreleased]

### Changed
- skills/fin: agregar modelo de Gordon como técnica adicional de valoración
  por dividendos. Justificación: complementa DCF para empresas maduras con
  pago de dividendo estable. Ref: Brealey, Myers & Allen (2020).
```

### Paso 5 — Pull Request

Abre el PR contra `main`. La plantilla esperada:

```markdown
## Resumen
[1-2 oraciones describiendo el cambio]

## Justificación profesional
[Por qué este cambio mejora el skill — desde tu experticia]

## Referencias APA 7 que respaldan el cambio
[Lista ordenada de más reciente a más antigua]

## Modo afectado
/<modo>

## Tipo de cambio
[ ] Mejora a contenido existente
[ ] Nueva sección o capacidad
[ ] Corrección de error
[ ] Actualización de referencia
```

---

## 4. Proceso de revisión

Una vez abierto el PR:

1. El mantenedor revisa en una **sesión de Claude Code** dedicada a
   evaluar contribuciones (ver `GOVERNANCE.md`).
2. La decisión se documenta como comentario en el PR:
   - **Aceptado** → merge + bump de versión + nueva entrada CHANGELOG
   - **Aceptado con cambios** → comentarios específicos a resolver antes de merge
   - **Rechazado** → justificación contra los criterios de aceptación
3. La cadencia de revisión es **no garantizada** — depende de la disponibilidad
   del mantenedor. PRs sin actividad por 90 días se cierran automáticamente.

---

## 5. Reconocimiento

Toda contribución aceptada se registra en `CHANGELOG.md` con el autor
del PR. El historial de Git también preserva la autoría.

---

## 6. Código de conducta

- Respetar la experticia ajena en otros dominios.
- No proponer cambios a un skill fuera de tu área profesional sin
  consulta previa con el mantenedor.
- Reconocer que el formato del repo (APA 7, general→particular, marcos
  vigentes) no es negociable — son las reglas del juego.

---

*Si tienes dudas sobre si un cambio aplica, abre un issue antes de
invertir tiempo en el PR.*
