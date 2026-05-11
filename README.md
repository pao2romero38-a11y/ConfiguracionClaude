# ConfiguracionClaude

Configuración base de **Claude Code** para trabajo profesional especializado.
Pensada para especialistas que necesitan un agente de IA con comportamiento
riguroso, citación APA 7, marcos normativos vigentes y formato de respuesta
predecible en su dominio de experticia.

**Versión vigente:** ver archivo [`VERSION`](VERSION) · **Estándar de citación:** APA 7ª edición

---

## ¿Para quién es?

Para profesionales que trabajan con Claude Code en alguno de estos 14 dominios:

| Familia | Modos disponibles |
|---|---|
| **Programación** | `/dev` `/dev-api` `/dev-clean` `/dev-db` `/dev-docker` `/dev-git` `/dev-modes` `/dev-test` |
| **Análisis y dominio** | `/edu` `/inv` `/fin` `/mkt` `/tec` `/proy` `/seg` `/rsk` `/ci` `/aud` `/dis` `/cost` `/tra` |

Total: **21 skills** (8 de programación + 13 de dominio). Cada uno carga un
comportamiento experto verificable.

> **Fuera de alcance:** consultas triviales o de cultura general. Para eso
> se recomienda usar Claude sin esta configuración. Aquí cada respuesta
> sigue un protocolo de calidad pensado para entregables profesionales.

---

## Origen del proyecto

`ConfiguracionClaude` nace como una evolución de un repositorio personal
previo (`ConfiguracionAI`) que se usaba para experimentar con instrucciones
de comportamiento para Claude Code. Tras una revisión de la configuración
en términos de **especialización, asertividad, eficiencia, tamaño de contexto
y método de perfiles**, se identificaron oportunidades concretas de refactor
que justificaban abrir un repo nuevo con gobierno explícito y versionado
semántico.

El objetivo del nuevo repo es triple:

1. **Compartir** la configuración para que otros especialistas la usen como
   base para sus propios proyectos.
2. **Recibir mejoras** de esos especialistas en sus dominios de experticia
   vía pull requests.
3. **Mantener versionado** trazable de cada cambio aprobado.

La línea base (`v1.0.0-baseline`) es la copia literal de `ConfiguracionAI`
al momento de la bifurcación. La versión `v1.0.0` agrega la documentación
del proyecto. Versiones siguientes aplican refactores y nuevos modos.

---

## Quick start

### 1. Clonar el repo

```bash
git clone https://github.com/<usuario>/ConfiguracionClaude.git
cd ConfiguracionClaude
```

### 2. Empezar un proyecto sobre esta configuración

Tres opciones — ver [`USAGE.md`](USAGE.md) para detalles:

```bash
# A) Usar el clon como base de tu proyecto
cd ConfiguracionClaude && claude

# B) Copiar la configuración a un proyecto existente
cp CLAUDE.md /ruta/a/mi-proyecto/
cp -R .claude /ruta/a/mi-proyecto/
cd /ruta/a/mi-proyecto && claude

# C) Instalar globalmente (aplica a todos tus proyectos)
cp CLAUDE.md ~/.claude/
cp -R .claude/skills ~/.claude/
```

### 3. Activar un modo

Dentro de Claude Code, en el prompt:

```
/fin Analiza la rentabilidad de esta empresa manufacturera con los siguientes estados.
```

Claude carga automáticamente el SKILL del dominio y aplica el formato esperado.

---

## Estructura del repositorio

```
ConfiguracionClaude/
├── README.md           ← este archivo
├── USAGE.md            ← cómo configurar y usar la configuración
├── CONTRIBUTING.md     ← cómo proponer mejoras a tu modo experto
├── GOVERNANCE.md       ← cómo se decide y se versiona
├── CHANGELOG.md        ← bitácora versionada de cambios
├── VERSION             ← versión vigente (formato SemVer)
├── CLAUDE.md           ← instrucciones de comportamiento globales
└── .claude/
    └── skills/         ← 21 skills especializados
        ├── README.md   ← índice de skills
        └── <modo>/SKILL.md ...
```

---

## Cómo contribuir

Si eres especialista en uno de los dominios cubiertos y detectas una
oportunidad de mejora en su SKILL correspondiente, lee
[`CONTRIBUTING.md`](CONTRIBUTING.md). El proceso resumido:

1. Crea una rama `proposal/<modo>-<descripción>`.
2. Modifica el SKILL.md del modo donde tienes experticia.
3. Documenta tu cambio en el commit y agrega entrada en [`CHANGELOG.md`](CHANGELOG.md).
4. Abre un Pull Request.
5. El mantenedor revisa contra los criterios de [`GOVERNANCE.md`](GOVERNANCE.md)
   y, si procede, autoriza el merge y publica una nueva versión.

---

## Relación con `ConfiguracionAI`

Este repo supersede al `CLAUDE.md` v1.0 ubicado en `~/Documents/AI/Proyectos/CLAUDE.md`
(directorio padre del proyecto original). Ese archivo queda intacto como
referencia histórica pero no es la fuente vigente.

Cuando trabajes con un proyecto basado en `ConfiguracionClaude`, esta
configuración es la única que debe estar activa.

---

## Licencia

Pendiente de definir. Hasta que se agregue un archivo `LICENSE`, los
derechos sobre el contenido son del autor del repositorio.

---

*Proyecto: ConfiguracionClaude · Configuración base de Claude Code para trabajo profesional especializado*
