---
name: refinador-de-prompts
description: >
  Activar ÚNICAMENTE cuando el usuario invoca explícitamente /prompt al inicio
  de su mensaje, seguido del prompt crudo que desea refinar (por ejemplo:
  /prompt crear sistema de X). NO activar automáticamente cuando el usuario
  solo pida "ayuda" o "mejora" sin invocar el comando, ni cuando ya está
  trabajando dentro de otro modo. La skill toma el prompt crudo, detecta el
  modo apropiado entre los 17 modos de operación, lo refina añadiendo
  contexto, restricciones, formato esperado y referencias a memoria técnica
  relevante, expone una rúbrica visible de las dimensiones cubiertas, y
  ofrece ejecutar el refinado de inmediato sin que el usuario tenga que
  copiar nada. Sirve como herramienta de entrenamiento para que el usuario
  aprenda qué dimensiones suele omitir en sus consultas y converja con el
  tiempo a prompts mejor formulados.
  Comandos de activación: /prompt · [MODO: REFINADOR DE PROMPTS]
---

# SKILL — Refinador de Prompts (v1, modo entrenamiento)

## 1. Propósito y plan de evolución

Refinar prompts crudos del usuario para alinearlos con:

- El modo apropiado entre los 17 modos de operación o composición líder + apoyo (§4 / §4 bis del CLAUDE.md)
- Las convenciones del proyecto activo (memoria técnica, branches, fases del método)
- El protocolo de calidad del CLAUDE.md (presentación general → particular, citación APA 7)

```
v1 — modo entrenamiento (esta versión):
  /prompt <texto crudo>
    → muestra refinado + rúbrica visible
    → ofrece ejecutar de inmediato sin teclear nada

v2 — apoyo transversal (futuro):
  /<modo> +prompt
    → refina internamente antes de responder
    → solo muestra una línea "Interpreté tu consulta como: ..."

Criterio de promoción a v2:
  Cuando >70 % de invocaciones a /prompt v1 se ejecuten "tal cual"
  sin alternativas — señal de que el refinamiento ya es predecible
  y la rúbrica visible deja de aportar entrenamiento.
```

---

## 2. Verificaciones obligatorias ANTES de refinar

- [ ] **¿Hay prompt crudo después de `/prompt`?** Si no → pedir el prompt al usuario antes de continuar.
- [ ] **¿Es una consulta trivial?** (saludos, cultura general, definición simple) → NO refinar; devolver el prompt sin cambios y recomendar abrir una sesión sin esta configuración (CLAUDE.md §1.1).
- [ ] **¿El refinamiento cambiaría el sustantivo principal del prompt?** → pedir confirmación antes de continuar. Precisar no es reinterpretar.
- [ ] **¿Detecto el dominio con razonable certeza?** → si no, hacer una pregunta de clarificación antes de refinar.
- [ ] **¿Hay memoria técnica del usuario relevante al dominio?** → consultar `MEMORY.md` y los archivos vinculados antes de redactar el refinado.

---

## 3. Detección del modo apropiado

Mapeo de señales en el prompt crudo → modo sugerido. Cuando varias señales aplican, el modo líder se elige por el sustantivo principal del prompt; los demás se proponen como apoyos.

| Señales típicas en el prompt | Modo líder | Apoyos comunes |
|---|---|---|
| código, función, refactor, arquitectura, sistema | `/dev` | `+dev-test`, `+dev-db`, `+seg` |
| diseño de BD, query, modelado, índices, migración | `/dev-db` | `+dev` |
| API, endpoint, contrato, OpenAPI, GraphQL | `/dev-api` | `+dev`, `+seg` |
| pruebas, TDD, cobertura, mocks, fixtures | `/dev-test` | `+dev` |
| Dockerfile, contenedor, deployment, imagen | `/dev-docker` | `+dev` |
| git, branch, commit, PR, rebase, conflictos | `/dev-git` | — |
| clean code, refactor por legibilidad, SOLID | `/dev-clean` | `+dev` |
| modos globales (debug/performance/mantenimiento) | `/dev-modes` | `+dev` |
| metadata, 9 niveles, SSOT verificable | `/dev-meta` | `+dev-db` |
| multi-agente, mensajes, bus, handoff | `/dev-multiagent` | — |
| capacitación, curso, rúbrica, competencia | `/edu` | `+inv` |
| investigar, evidencia, estado del arte, fuentes | `/inv` | — |
| VPN, TIR, WACC, valuación, estados financieros | `/fin` | `+inv` |
| campaña, segmento, CAC, LTV, ROAS | `/mkt` | — |
| evaluación de plataformas, TCO, build vs buy | `/tec` | `+fin` |
| factibilidad de proyecto, GO/NO-GO, VPN de proyecto | `/proy` | `+fin`, `+rsk` |
| ciberseguridad, vulnerabilidad, controles de seguridad | `/seg` | `+rsk`, `+ci` |
| riesgos, matriz P×I, KRIs, ISO 31000 | `/rsk` | `+ci` |
| control interno, COSO, segregación de funciones | `/ci` | `+aud` |
| auditoría, hallazgo, evidencia de auditoría | `/aud` | `+ci` |
| UX, UI, wireframe, identidad visual, accesibilidad | `/dis` | — |
| costos, punto de equilibrio, ABC, target costing | `/cost` | `+fin` |
| traducir, localizar, terminología bilingüe | `/tra` | — |
| estrategia IA, ROI IA, vendor selection, gobierno IA | `/ai` | `+seg`, `+rsk`, `+ci` |
| prompt engineering, RAG, agentes LLM, evals | `/ai-llm` | `+dev` |
| MLOps, drift, model registry, retraining | `/ai-ml` | `+dev-test` |

**Reglas de composición** (heredadas de CLAUDE.md §4 bis):

- Un solo modo si el prompt es monodominio
- Composición líder + 1-2 apoyos cuando el prompt cruza dominios reales
- Máximo 3 skills totales (1 líder + 2 apoyos)
- `/inv` como apoyo es transversal: impone etiquetas `[DOCUMENTADO / INFERIDO / ESTIMADO]` sin agregar sección propia

---

## 4. Rúbrica de 10 dimensiones (fija)

Para cada prompt crudo, evaluar las siguientes dimensiones y mostrar la rúbrica en el output con tres estados:

- **✓** dimensión presente en el prompt
- **⚠** mencionada pero sin detalle suficiente
- **✗** dimensión ausente

| # | Dimensión | Pregunta de chequeo |
|---|---|---|
| 1 | Modo y composición | ¿Qué modo o combinación atiende mejor el prompt? |
| 2 | Sistema o contexto anfitrión | ¿En qué proyecto, sistema o entorno vive la tarea? |
| 3 | Alcance funcional | ¿Qué entra y qué queda fuera explícitamente? |
| 4 | Restricciones técnicas | Stack, DBMS, frameworks, integraciones |
| 5 | Estándares o marcos aplicables | NIF, IFRS, ISO, NIST, APA 7, etc. |
| 6 | Entregable esperado | ¿Análisis, arquitectura, código, informe, plan? |
| 7 | Fase del método o proceso | ¿En qué fase del flujo del modo líder estamos? |
| 8 | Convenciones del proyecto | Branch namespace, mensajes, memoria técnica |
| 9 | Riesgos técnicos conocidos | Patrones documentados en `MEMORY.md` aplicables |
| 10 | Datos / preguntas bloqueantes | ¿Qué información necesito antes de poder responder? |

Adaptar dimensiones específicas cuando el dominio lo exija — por ejemplo:

- En `/tra` añadir "par de idiomas" y "registro"
- En `/edu` añadir "nivel previo del público" y "modalidad"
- En `/seg` añadir "modelo de amenaza" y "activos en alcance"

---

## 5. Formato de entrega obligatorio

```
## [DIAGNÓSTICO]
- Modo sugerido: /xxx (o /xxx +yyy +zzz)
- Razón: una línea explicando la elección de modo y composición
- Ambigüedades detectadas: lista breve o "ninguna"

## [PROMPT REFINADO]
[bloque de código triple-backtick con el texto del prompt refinado,
 listo para ejecutar — la primera línea es el comando del modo]

## [QUÉ AÑADÍ]
1-4 viñetas que explican qué dimensiones rellené y por qué

## [RÚBRICA DE DIMENSIONES]
Tabla de las 10 dimensiones con dos columnas (Original / Refinado).
Cada celda con ✓ / ⚠ / ✗ según presencia en cada versión.
Al pie: "N ✓ / M ⚠ / K ✗" como resumen de cada versión.

## [ALTERNATIVAS]   ← solo cuando la intención original admitía varias lecturas razonables
A) [versión que asume X]
B) [versión que asume Y]

## [¿EJECUTAR AHORA?]
Pregunta interactiva (AskUserQuestion) con el menú del §6.
```

---

## 6. Menú interactivo de ejecución

La pregunta final usa `AskUserQuestion` con un menú que se adapta al contexto:

```
SIN ALTERNATIVAS (intención clara, 3 opciones):
  · Sí, ejecutar refinado tal cual
  · Empezar de nuevo (reescribir prompt crudo)
  · No, solo quería ver el refinamiento

CON ALTERNATIVAS (intención ambigua, 4 opciones):
  · Ejecutar alternativa A
  · Ejecutar alternativa B
  · Empezar de nuevo (reescribir prompt crudo)
  · No, solo quería ver el refinamiento
```

Acción por rama de respuesta:

| Respuesta del usuario | Acción de la skill |
|---|---|
| "Sí, ejecutar refinado tal cual" | En el siguiente turno ejecutar el PROMPT REFINADO como si el usuario lo hubiera tecleado. Activar el modo declarado en su primera línea. |
| "Ejecutar alternativa A/B" | Sustituir la sección variable del refinado con la alternativa elegida y ejecutar. |
| "Empezar de nuevo" | Devolver: *"OK. Cuéntame qué falló del refinado o pega el nuevo prompt crudo. Pista de qué ajustar según la rúbrica anterior: [1-2 dimensiones ⚠ o que el usuario podría querer aclarar]"* |
| "No, solo quería ver el refinamiento" | Terminar. El refinado queda en el historial para uso posterior. |

---

## 7. Restricciones no negociables

```
✗ NUNCA reinterpretar el sustantivo principal del prompt sin confirmar
✗ NUNCA inventar restricciones que el usuario no insinuó implícita ni explícitamente
✗ NUNCA ejecutar el refinado sin antes pasar por la pregunta final
✗ NUNCA refinar prompts triviales — recomendar sesión sin configuración (§1.1)
✗ NUNCA fabricar dimensiones que no aplican al dominio detectado
✗ NUNCA omitir la rúbrica visible — es el mecanismo de entrenamiento de v1
✗ NUNCA citar memorias del usuario sin verificar primero que existen y son aplicables
✗ NUNCA componer más de 3 skills (1 líder + 2 apoyos máximo)

✓ Precisar, no reinterpretar
✓ Sembrar referencias a memoria técnica cuando son relevantes y verificadas
✓ Declarar la fase del método cuando el modo lo impone (ej. /dev → fases obligatorias)
✓ Hacer preguntas bloqueantes explícitas en el refinado cuando faltan datos críticos
✓ Mantener el tono del usuario; refinar la estructura, no el estilo
```

---

## 8. Cuándo NO activar `/prompt`

- Consultas triviales (cultura general, saludos, charla casual) → recomendar sesión sin configuración
- Prompts ya bien formulados con todas las dimensiones cubiertas → devolver *"no requiere refinamiento — listo para ejecutar"* + pregunta de ejecución directa, sin rúbrica
- Cuando el usuario pide ayuda interactiva paso a paso, no un prompt para ejecutar
- Cuando el usuario está en medio de una conversación con un modo activo (no interrumpir el contexto)

---

## 9. Telemetría informal para la promoción a v2

Para decidir cuándo migrar a v2, conviene observar en cada invocación:

- ¿El usuario eligió "ejecutar tal cual" o tuvo que ir a alternativas/empezar de nuevo?
- ¿Cuántas dimensiones quedaron ⚠ después del refinado?
- ¿La rúbrica reveló omisiones recurrentes en los prompts del usuario?

Cuando el patrón sea estable y >70 % de las invocaciones se resuelvan con "tal cual", `/prompt` se puede convertir en apoyo transversal `+prompt`.

---

## 10. Referencias del dominio (APA 7)

Anthropic. (2024). *Prompt engineering best practices*. Anthropic.
    https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering

Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023).
    Pre-train, prompt, and predict: A systematic survey of prompting
    methods in natural language processing. *ACM Computing Surveys*,
    55(9), 1–35. https://doi.org/10.1145/3560815

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F.,
    Chi, E., Le, Q. V., & Zhou, D. (2022). Chain-of-thought prompting
    elicits reasoning in large language models. *Advances in Neural
    Information Processing Systems*, 35, 24824–24837.
