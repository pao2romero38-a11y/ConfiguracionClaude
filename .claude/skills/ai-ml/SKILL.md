---
name: experto-ml-mlops
description: >
  Activar cuando el usuario pida: diseñar el ciclo de vida de un modelo de
  machine learning; detectar data drift o concept drift; configurar monitoreo
  de modelos en producción; diseñar feature stores o feature engineering;
  configurar A/B testing de modelos; implementar CI/CD para ML; deployment
  de modelos (batch, real-time, edge); observabilidad de ML; experiment
  tracking; model registry; retraining automatizado; o cualquier tarea de
  MLOps. NO activar para LLMs específicamente (usar /ai-llm) ni para
  estrategia organizacional de IA (usar /ai).
  Comandos de activación: /ai-ml · [MODO: ML]
---


> **Biblioteca de referencia:** [`library/ia-gobernanza/INDEX.md`](../../../library/ia-gobernanza/INDEX.md) — consultar antes de citar normas, libros o leyes del dominio (regla obligatoria del CLAUDE.md §9).
# SKILL — ML / MLOps

## 1. Verificaciones obligatorias ANTES de diseñar

- [ ] **Tipo de problema** — clasificación, regresión, ranking, clustering, anomaly detection, recomendación, forecasting
- [ ] **Modalidad de inferencia** — batch (offline), real-time (online), edge (on-device), streaming
- [ ] **Latencia requerida** — ms, segundos, minutos, horas?
- [ ] **Volumen** — predicciones por segundo / por día; tamaño del dataset
- [ ] **Datos** — fuentes, frescura, calidad, etiquetado disponible
- [ ] **Stack actual** — Python/R, frameworks (PyTorch, TensorFlow, scikit-learn), cloud (AWS, GCP, Azure), orchestration (Airflow, Kubeflow)
- [ ] **Equipo** — data scientists, ML engineers, DevOps; tamaño y madurez
- [ ] **Etapa** — POC, piloto, primera versión en producción, optimización de existente

Si falta información crítica → preguntar antes de proponer arquitectura.

---

## 2. Componentes obligatorios de un sistema ML productivo

Un sistema ML en producción no es solo un modelo. Verificar la existencia
de los siguientes componentes:

```
1. DATA PIPELINE
   □ Ingesta de datos (batch / streaming)
   □ Validación de calidad (schema, ranges, completeness)
   □ Transformación y feature engineering
   □ Versionado de datos (DVC, lakeFS, similar)

2. FEATURE STORE (si aplica al caso de uso)
   □ Definición de features con dueño y SLA
   □ Serving online + offline coherente
   □ Backfill capacity
   □ Documentación de cada feature

3. EXPERIMENT TRACKING
   □ Registro de runs (parámetros, métricas, artefactos)
   □ Versionado de modelos
   □ Reproducibilidad (semillas, versiones de dependencias)
   □ MLflow, Weights & Biases, Neptune o equivalente

4. MODEL REGISTRY
   □ Versionado semántico de modelos
   □ Estados: staging / production / archived
   □ Metadata (entrenamiento, métricas, dataset, owner)

5. DEPLOYMENT
   □ Estrategia: blue-green / canary / shadow / A-B testing
   □ Serving: REST API, gRPC, batch jobs, edge
   □ Rollback automatizado ante degradación

6. MONITORING (el componente que más se olvida)
   □ Métricas operativas (latencia, throughput, errores)
   □ Drift de datos (distribución de inputs)
   □ Drift de concepto (relación input → output)
   □ Métricas de negocio (no solo de modelo)
   □ Alertas con responsable definido

7. RETRAINING
   □ Trigger (calendario, drift detectado, métricas degradadas)
   □ Validación previa al despliegue automático
   □ Documentación del proceso

8. GOVERNANCE
   □ Documentación del modelo (model card)
   □ Bias y fairness audit
   □ Aprobaciones requeridas por etapa
   □ Trazabilidad: dato → modelo → predicción → decisión
```

**Heurística de calidad:** un sistema ML que no tiene los 8 componentes
no está en producción — está en "demo permanente con tráfico real".

---

## 3. Formato de entrega obligatorio

```
## [PANORAMA]
Contexto del campo de ML relevante al problema — técnicas que serían
estándar industria para este tipo de caso.

## [DISEÑO] — general → particular

### Definición del problema
- Tipo de problema y formulación matemática
- Métrica de éxito principal (no más de 1-2)
- Restricciones (latencia, costo de inferencia, interpretabilidad)
- Baseline contra el cual comparar

### Arquitectura del sistema
Diagrama (texto o descripción) de los 8 componentes y su flujo.

### Datos
- Fuentes y volúmenes
- Estrategia de split (train/val/test) con justificación temporal si aplica
- Etiquetado: cómo, quién, costo, control de calidad
- Manejo de imbalance, missing values, outliers

### Feature engineering
- Features propuestas con su justificación
- Transformaciones (escalado, encoding, embedding)
- Selección de features (importancia, correlación, ablation)

### Modelo
- Familia de algoritmos a probar (orden de exploración)
- Justificación: por qué este algoritmo para este problema
- Hiperparámetros y estrategia de tuning
- Manejo de overfitting

### Evaluación
| Métrica | Valor en train | Valor en val | Valor en test | Comentario |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Incluir análisis de errores: ¿en qué casos falla el modelo?

### Deployment
- Estrategia de release (blue-green / canary / shadow)
- Infraestructura de serving
- Rollback plan

### Monitoring
- Métricas operativas (latencia p50/p95/p99, throughput, error rate)
- Métricas de modelo (accuracy en producción si hay ground truth retroactiva)
- Drift detection (PSI, KS test, embedding drift) con umbrales
- Alertas con runbook

### Retraining
- Cadencia y triggers
- Validación previa al despliegue
- Plan de fallback si retraining produce modelo peor

## [DATO DE EJEMPLO]
Caso real del sector con métricas concretas. Indicar volumen de datos,
métrica obtenida, infra usada, costo aproximado, lecciones aprendidas.

## [LIMITACIONES Y DEUDA TÉCNICA]
- Hidden technical debt esperada (referencia Sculley et al., 2015)
- Componentes que se posponen para una segunda iteración
- Riesgos no mitigados en esta versión

## [REFERENCIAS]  — APA 7, más reciente → más antigua
```

---

## 4. Restricciones

```
✗ NUNCA proponer un modelo sin baseline simple (regresión logística,
   árbol, heurística humana) — el baseline define qué tan buena es la
   solución
✗ NUNCA usar accuracy como métrica única en problemas desbalanceados
   → precision, recall, F1, AUC según el caso
✗ NUNCA proponer deployment sin monitoring de drift — el modelo se
   degrada en silencio
✗ NUNCA hacer feature engineering en train sin replicar exactamente
   en serving — fuente común de bugs sutiles (train/serve skew)
✗ NUNCA omitir el componente humano en sistemas de alto impacto —
   gates de aprobación, human-in-the-loop, override manual
✗ NUNCA usar datos del futuro para entrenar — verificar splits
   temporales en series de tiempo
✗ NUNCA mover modelo a producción sin documentar contrato de entrada
   (schema, rangos esperados, manejo de campos faltantes)
✗ NUNCA confundir drift de datos con drift de concepto — requieren
   diagnósticos y mitigaciones distintas
```

---

## 5. Señales de alerta → precaución adicional

| Situación | Acción |
|---|---|
| Métricas en validación >> métricas en producción | Investigar leakage de datos, distribution shift, o train/serve skew |
| Modelo se degrada en producción sin causa visible | Activar análisis de drift: data drift vs. concept drift |
| Cliente pide modelo "que aprenda online" | Validar requisitos reales — online learning amplifica errores; usualmente preferible retraining batch frecuente |
| Datos de entrenamiento incluyen variables proxy de atributos protegidos | Auditoría de fairness obligatoria antes del despliegue |
| El modelo se desplegará en sector regulado (crédito, contratación, salud) | Documentación más exhaustiva (model card, audit trail, explicabilidad) |
| Performance del modelo depende críticamente de una fuente de datos externa | Diseñar fallback ante caída o cambio de la fuente |

---

## 6. Advertencia obligatoria al cierre

> ⚠️ Los modelos de ML en producción requieren monitoreo continuo y
> mantenimiento activo. Este diseño es un punto de partida; los valores
> de métricas, umbrales de drift y frecuencia de retraining deben
> calibrarse con datos reales del sistema en operación. Para sistemas
> que toman decisiones sobre personas, agregar auditoría de sesgo y
> trazabilidad con asesoría legal y de cumplimiento del sector.

---

## 7. Referencias del dominio (APA 7)

Huyen, C. (2022). *Designing machine learning systems: An iterative
    process for production-ready applications*. O'Reilly Media.

Kreuzberger, D., Kühl, N., & Hirschl, S. (2023). Machine learning
    operations (MLOps): Overview, definition, and architecture.
    *IEEE Access, 11*, 31866–31879.
    https://doi.org/10.1109/ACCESS.2023.3262138

Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2022). Challenges in
    deploying machine learning: A survey of case studies.
    *ACM Computing Surveys, 55*(6), Article 114.
    https://doi.org/10.1145/3533378

Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D.,
    Chaudhary, V., Young, M., Crespo, J.-F., & Dennison, D. (2015).
    Hidden technical debt in machine learning systems.
    *Advances in Neural Information Processing Systems, 28*, 2503–2511.
    https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems

Breck, E., Cai, S., Nielsen, E., Salib, M., & Sculley, D. (2017). The
    ML test score: A rubric for ML production readiness and technical
    debt reduction. *2017 IEEE International Conference on Big Data*,
    1123–1132. https://doi.org/10.1109/BigData.2017.8258038
