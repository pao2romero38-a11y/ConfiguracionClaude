# USAGE — Cómo usar ConfiguracionClaude

Guía para configurar el agente Claude Code con esta configuración base y
empezar a trabajar en un proyecto propio.

---

## 1. Requisitos previos

- **Claude Code** instalado y autenticado.
  Ver: https://docs.anthropic.com/claude-code
- **Git** ≥ 2.30 para clonar el repo.
- Conocimiento del dominio en el que vas a operar (esta configuración
  está pensada para trabajo profesional, no para consultas triviales).

---

## 2. Opciones de instalación

### Opción A — Clonar como base de un proyecto nuevo

Cuando vas a empezar un proyecto desde cero y quieres que la configuración
aplique a ese proyecto exclusivamente:

```bash
git clone https://github.com/<usuario>/ConfiguracionClaude.git mi-proyecto
cd mi-proyecto
rm -rf .git           # opcional: si quieres iniciar tu propio historial
git init
claude                # Claude Code detecta CLAUDE.md y .claude/skills/
```

### Opción B — Copiar la configuración a un proyecto existente

Cuando ya tienes un proyecto con su propio control de versiones y quieres
incorporar la configuración:

```bash
cd /ruta/a/tu-proyecto
cp /ruta/al/clon/CLAUDE.md .
cp -R /ruta/al/clon/.claude .
claude
```

Si tu proyecto ya tiene un `CLAUDE.md`, combina manualmente las dos
configuraciones — no sobrescribas sin revisar.

### Opción C — Instalación global

Cuando quieres que la configuración aplique a **todos** tus proyectos sin
copiarla a cada uno:

```bash
cp /ruta/al/clon/CLAUDE.md ~/.claude/
cp -R /ruta/al/clon/.claude/skills ~/.claude/
```

Claude Code carga la configuración global como fallback para cualquier
proyecto que no tenga su propio `CLAUDE.md`. Útil si trabajas siempre en
el mismo dominio.

---

## 3. Activación de modos

Cada modo se activa de tres formas equivalentes:

```
/fin                            ← comando corto
[MODO: FINANZAS]                ← etiqueta explícita
(detección automática)          ← Claude lo activa por el contenido del prompt
```

**Lista completa de modos:** ver [`.claude/skills/README.md`](.claude/skills/README.md)
o `/modos` dentro de la sesión.

### Ejemplos por familia

```
# Programación
/dev Implementa un parser de logs de Claude Code en Python 3.11 con FastAPI.

# Análisis de negocio
/fin Calcula el VPN de este proyecto con WACC del 12% y horizonte de 5 años.

# Diseño instruccional
/edu Diseña una lección sobre control interno para auditores junior.

# Investigación
/inv ¿Cuál es el estado del arte en evaluación de modelos de lenguaje grandes?
```

---

## 4. Composición de modos (próximamente)

A partir de la versión 2.0.0, dos modos pueden combinarse en un mismo
prompt usando la regla **"líder + apoyo"**:

```
/proy +fin +rsk    ← /proy lidera la estructura; /fin y /rsk aportan criterios
```

Detalles en `CLAUDE.md` §4 bis (sección que se agrega en v2.0.0).

---

## 5. Personalización

Después de instalar, puedes:

- **Editar `CLAUDE.md`** localmente para ajustar reglas globales a tu
  contexto específico.
- **Editar un `SKILL.md`** localmente para adaptar el formato de respuesta
  de un modo.
- **Agregar nuevos skills** propios en `.claude/skills/<nombre>/SKILL.md`.

Estos cambios viven en tu copia. Si crees que la mejora aplica a todos
los usuarios del repo, ver [`CONTRIBUTING.md`](CONTRIBUTING.md) para enviarla
de vuelta como PR.

---

## 6. Verificación de que la configuración está activa

Al iniciar una sesión de Claude Code en un proyecto con esta configuración,
puedes escribir:

```
/config
```

Debería responder con el resumen del estado:

```
✓ CLAUDE.md cargado
Modo activo: NEUTRO
Protocolo de calidad: ACTIVO
Presentación: General → Particular
Referencias: APA 7ª edición · Más reciente → Más antigua
```

Si no responde así, revisa que `CLAUDE.md` esté en la raíz del proyecto y
que `.claude/skills/` exista con sus subdirectorios.

---

## 7. Problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| `/fin` no se activa | `CLAUDE.md` no en raíz del proyecto | Verifica ubicación del archivo |
| Modo activa, pero formato no se respeta | Versión vieja del modelo de Claude | Actualiza Claude Code y reinicia |
| Skills no aparecen | `.claude/skills/` con permisos incorrectos | `chmod -R u+r .claude/` |
| Respuestas en inglés cuando debería ser español | Falta indicación de idioma en el prompt | Agrega "responde en español" al primer mensaje |

---

*Para preguntas que no resuelve esta guía, abre un issue en el repo.*
