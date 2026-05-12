---
name: programador-diseno-apis
description: >
  Activar cuando el usuario pida: diseñar o revisar una API REST o GraphQL;
  definir endpoints, métodos HTTP y códigos de respuesta; crear o validar un
  contrato OpenAPI/Swagger; diseñar estrategias de versionado, paginación o
  manejo de errores en APIs; evaluar la seguridad de una API; diseñar
  autenticación con JWT u OAuth 2.0; documentar una API existente; o cualquier
  tarea donde el diseño o la especificación de una interfaz de programación
  sea el entregable principal.
  Comandos de activación: /dev-api · [MODO: API]
---

# SKILL — Diseño de APIs REST y GraphQL

## 1. Verificaciones obligatorias ANTES de diseñar

- [ ] **Tipo de API** — ¿REST, GraphQL, gRPC, WebSocket, o combinación?
- [ ] **Consumidores** — ¿clientes web, móvil, terceros, internos (microservicios)?
- [ ] **Autenticación** — ¿API Key, JWT, OAuth 2.0, mTLS?
- [ ] **Versionado** — ¿hay versiones previas que mantener? ¿estrategia: URL, header, parámetro?
- [ ] **Contrato** — ¿se genera código desde el contrato (contract-first) o se documenta el código existente?
- [ ] **SLAs** — ¿hay requisitos de latencia, disponibilidad o rate limits?

---

## 2. Madurez REST — Richardson Maturity Model

```
NIVEL 0 — Un solo endpoint, todo por POST
  /api  POST {"action": "getUser", "id": 123}
  → Evitar: no es REST, es RPC sobre HTTP.

NIVEL 1 — Recursos identificados por URL
  /api/users/123  POST {"action": "get"}
  → Mejor, pero los verbos HTTP no se usan correctamente.

NIVEL 2 — Verbos HTTP correctos + códigos de estado (MÍNIMO ACEPTABLE)
  GET /api/users/123  → 200 OK
  POST /api/users     → 201 Created
  → Este nivel es el estándar profesional para la mayoría de APIs.

NIVEL 3 — HATEOAS (hipermedia como motor del estado)
  La respuesta incluye links a las siguientes acciones posibles.
  → Usar en APIs públicas de gran escala; opcional para APIs internas.

OBJETIVO MÍNIMO: Nivel 2 en toda API nueva.
```

---

## 3. Convenciones de diseño — obligatorias

```
URLs:
  □ Sustantivos en plural, minúsculas, guiones medios: /invoice-items
  □ NUNCA verbos en la URL: ✗ /getUser  ✓ GET /users/{id}
  □ Jerarquía refleja relaciones: /users/{userId}/orders/{orderId}
  □ Máximo 3 niveles de anidación: /a/{id}/b/{id}/c — más profundo → revisar diseño
  □ Versión en la URL: /v1/users  (alternativa: header Accept: application/vnd.api+json;version=1)

Verbos HTTP y su semántica:
  GET     → Leer. Idempotente. Sin body. No modifica estado.
  POST    → Crear. No idempotente. Body con el nuevo recurso.
  PUT     → Reemplazar completo. Idempotente. Body con el recurso completo.
  PATCH   → Modificar parcial. Body con solo los campos que cambian.
  DELETE  → Eliminar. Idempotente. Generalmente sin body.

Códigos de respuesta — usar el correcto siempre:
  200 OK              → GET, PUT, PATCH exitoso
  201 Created         → POST exitoso; incluir Location header con URL del nuevo recurso
  204 No Content      → DELETE exitoso; PUT/PATCH sin body de respuesta
  400 Bad Request     → Validación fallida; incluir detalle del error
  401 Unauthorized    → No autenticado (falta o token inválido)
  403 Forbidden       → Autenticado pero sin permiso
  404 Not Found       → Recurso no existe
  409 Conflict        → Conflicto de estado (ej: email duplicado)
  422 Unprocessable   → Entidad semánticamente inválida
  429 Too Many Req.   → Rate limit excedido; incluir Retry-After header
  500 Internal Error  → Error del servidor; nunca exponer stack trace
```

---

## 4. Formato de respuesta — estándar

```
RESPUESTA EXITOSA (objeto):
{
  "data": {
    "id": "usr_01J2K...",
    "email": "usuario@empresa.com",
    "created_at": "2024-11-15T10:30:00Z"
  }
}

RESPUESTA EXITOSA (colección paginada):
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 342,
    "total_pages": 18,
    "next": "/v1/users?page=2",
    "prev": null
  }
}

RESPUESTA DE ERROR — RFC 9457 Problem Details (obligatorio):
{
  "type": "https://api.empresa.com/errors/validation-error",
  "title": "Error de validación",
  "status": 400,
  "detail": "El campo 'email' no tiene un formato válido.",
  "instance": "/v1/users",
  "errors": [
    {"field": "email", "message": "Formato de email inválido", "value": "no-es-email"}
  ]
}
```

---

## 5. Paginación — estrategias y cuándo usar cada una

| Estrategia | Cuándo usar | Ventaja | Limitación |
|------------|-------------|---------|------------|
| **Offset/limit** | Datasets pequeños (<100k), UI con páginas numeradas | Simple de implementar | Inconsistente si los datos cambian; lento en páginas altas |
| **Cursor** | Feeds, listas en tiempo real, datasets grandes | Consistente, eficiente | No permite saltar a página N directamente |
| **Keyset** | Ordenamiento por columna con índice | Muy eficiente en BD | Requiere columna con índice único |

Reglas:
- Siempre paginar colecciones — nunca retornar listas ilimitadas
- Tamaño máximo de página: definirlo y documentarlo (recomendado: max 100)
- Default de página: explícito en la documentación (recomendado: 20)

---

## 6. Roles de usuario — obligatorios en toda API con usuarios

Toda API que gestione usuarios debe implementar y documentar los siguientes
5 roles mínimos. Deben reflejarse en el contrato OpenAPI y en la lógica
de autorización de cada endpoint.

```
ROLES MÍNIMOS OBLIGATORIOS:

  administrador
    Acceso a todos los endpoints sin excepción.
    Puede gestionar usuarios, roles, configuración y parámetros del sistema.
    Identificar en el contrato: security scope "admin" o claim role=administrador

  operador
    Acceso a endpoints de operación del negocio (crear, modificar registros).
    No accede a endpoints de gestión de usuarios ni configuración del sistema.
    Identificar en el contrato: security scope "operador"

  usuario
    Acceso a endpoints propios de su perfil funcional.
    Solo puede leer y modificar sus propios recursos, no los de otros.
    Identificar en el contrato: security scope "usuario"

  desarrollador
    Acceso a endpoints técnicos: health, métricas, logs, configuración técnica.
    No accede a datos de negocio de usuarios finales en producción.
    Identificar en el contrato: security scope "developer"

  visualizador
    Acceso exclusivo a endpoints GET (solo lectura).
    Cualquier endpoint que modifique estado debe retornar 403 para este rol.
    Identificar en el contrato: security scope "viewer"
```

**Implementación en el contrato OpenAPI:**

```yaml
# Definir los scopes en securitySchemes
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

# En cada endpoint, declarar qué roles tienen acceso:
paths:
  /usuarios:
    get:
      security:
        - bearerAuth: []
      x-roles-permitidos: [administrador, visualizador]
      # 403 Forbidden para: operador, usuario, desarrollador
    post:
      security:
        - bearerAuth: []
      x-roles-permitidos: [administrador, operador]
      # 403 Forbidden para: usuario, desarrollador, visualizador

# Matriz de acceso obligatoria en la documentación:
# Endpoint              | admin | operador | usuario | developer | visualizador
# GET  /recursos        |   ✓   |    ✓     |    ✓    |     ✓     |      ✓
# POST /recursos        |   ✓   |    ✓     |    *    |     ✗     |      ✗
# PUT  /recursos/{id}   |   ✓   |    ✓     |    *    |     ✗     |      ✗
# DELETE /recursos/{id} |   ✓   |    ✗     |    ✗    |     ✗     |      ✗
# GET  /config          |   ✓   |    ✗     |    ✗    |     ✓     |      ✗
# * = solo sus propios recursos
```

**Verificación obligatoria en el diseño de cada endpoint:**
```
□ ¿Está documentado qué roles tienen acceso a este endpoint?
□ ¿El visualizador queda restringido a solo GET?
□ ¿El desarrollador no puede acceder a datos de negocio en producción?
□ ¿Existe al menos un endpoint accesible solo por administrador?
□ ¿Los errores de autorización retornan 403 (no 401)?
  401 = no autenticado (token faltante o inválido)
  403 = autenticado pero sin permiso (rol insuficiente)
```

---

## 7. Autenticación y seguridad — checklist

```
JWT:
  □ Firmar con RS256 (asimétrico) en lugar de HS256 para APIs públicas
  □ Expiración corta en access token: 15-60 minutos
  □ Refresh token con rotación: invalidar el anterior al emitir uno nuevo
  □ No almacenar información sensible en el payload (es decodificable)
  □ Validar: firma, expiración, issuer, audience

HEADERS DE SEGURIDAD OBLIGATORIOS:
  □ Authorization: Bearer {token}  (no en URL, no en query params)
  □ Strict-Transport-Security: max-age=31536000  (solo HTTPS)
  □ X-Content-Type-Options: nosniff
  □ X-Frame-Options: DENY

RATE LIMITING — headers de respuesta estándar:
  □ X-RateLimit-Limit: 1000
  □ X-RateLimit-Remaining: 847
  □ X-RateLimit-Reset: 1700000000  (Unix timestamp)
  □ Retry-After: 60  (en respuesta 429)

VALIDACIÓN DE INPUT:
  □ Validar tipo, formato y rango de TODOS los campos del request
  □ Sanitizar inputs para prevenir injection (SQL, NoSQL, command)
  □ Limitar tamaño del request body (ej: max 1MB)
  □ Nunca confiar en el Content-Type declarado — validar el contenido real
```

---

## 8. OpenAPI / Swagger — contrato obligatorio

```
ESTRUCTURA MÍNIMA DEL CONTRATO (OpenAPI 3.1):
  openapi: "3.1.0"
  info:
    title: Nombre de la API
    version: "1.0.0"
    description: Qué hace esta API y para quién es
  servers:
    - url: https://api.empresa.com/v1
      description: Producción
    - url: https://api-staging.empresa.com/v1
      description: Staging
  paths:
    /users/{userId}:
      get:
        summary: Obtener usuario por ID
        parameters: [...]
        responses:
          "200":
            description: Usuario encontrado
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/User"
          "404":
            $ref: "#/components/responses/NotFound"
  components:
    schemas: [...]
    responses: [...]
    securitySchemes: [...]

REGLAS:
  □ Documentar TODOS los códigos de respuesta posibles, no solo el 200
  □ Incluir ejemplos (examples) en cada schema
  □ Usar $ref para reutilizar schemas y evitar duplicación
  □ Documentar los parámetros de autenticación en securitySchemes
```

---

## 9. GraphQL — cuándo y cómo

```
USAR GraphQL cuando:
  ✓ Los clientes necesitan consultas flexibles (diferentes campos por cliente)
  ✓ Hay múltiples tipos de clientes (web, móvil, terceros) con necesidades distintas
  ✓ El modelo de datos es un grafo con muchas relaciones
  ✓ Se quiere evitar over-fetching y under-fetching

USAR REST cuando:
  ✓ API pública con terceros desconocidos
  ✓ Operaciones simples CRUD
  ✓ Cacheo agresivo a nivel HTTP es importante
  ✓ El equipo no tiene experiencia con GraphQL

PROBLEMAS OBLIGATORIOS A RESOLVER en GraphQL:
  □ N+1 queries → usar DataLoader (batching)
  □ Query depth excesiva → limitar profundidad máxima (recomendado: 5)
  □ Query complexity → implementar cost analysis
  □ Introspección en producción → deshabilitarla o protegerla
```

---

## 10. Versionado — estrategia y reglas de compatibilidad

```
CAMBIOS COMPATIBLES (no requieren nueva versión):
  ✓ Añadir nuevos endpoints
  ✓ Añadir campos opcionales a respuestas
  ✓ Añadir parámetros opcionales a requests
  ✓ Añadir nuevos valores a enums (con cuidado)

CAMBIOS INCOMPATIBLES (requieren nueva versión):
  ✗ Eliminar o renombrar endpoints
  ✗ Cambiar el tipo de un campo
  ✗ Hacer obligatorio un campo que era opcional
  ✗ Cambiar la semántica de un campo sin cambiar su nombre

POLÍTICA DE DEPRECACIÓN:
  □ Anunciar con mínimo 6 meses de anticipación
  □ Incluir Deprecation header en las respuestas de endpoints deprecados
  □ Mantener versiones anteriores al menos 12 meses después del anuncio
  □ Documentar la ruta de migración en la misma notificación
```

---

## 11. Formato de entrega obligatorio

```
### [Decisiones de diseño]
Por qué REST vs. GraphQL vs. gRPC para este caso.
Estrategia de versionado elegida y justificación.

### [Contrato de la API]
Especificación OpenAPI 3.1 completa o esquema GraphQL.
Incluir ejemplos de request y response para cada operación.

### [Endpoints / Operaciones]
Tabla resumen:
| Método | Path | Descripción | Auth | Rate limit |
|--------|------|-------------|------|------------|

### [Manejo de errores]
Catálogo de errores posibles con su código HTTP y estructura RFC 9457.

### [Seguridad]
Mecanismo de autenticación y autorización.
Headers de seguridad configurados.

### [Advertencias]
Limitaciones conocidas, casos no cubiertos, deuda técnica.

### [Referencias]  ← APA 7, más reciente → más antigua
```

---

## 12. Modos globales — comportamiento de la API por modo

Toda API debe responder de forma diferente según el `SYSTEM_MODE` activo.
Ver skill `/dev-modes` para la especificación completa.

```
MODO DEBUG (SYSTEM_MODE=DEBUG):
  □ Incluir en el header de respuesta:
      X-Correlation-ID: <uuid>
      X-Response-Time-Ms: <ms>
      X-System-Mode: DEBUG
  □ En errores 4xx/5xx incluir en el body (solo en DEBUG):
      "debug": {
        "correlation_id": "...",
        "timestamp": "...",
        "duracion_ms": 45.2,
        "modulo": "pagos.procesar_pago",
        "stack_trace": "..."   ← solo en DEBUG, nunca en PERFORMANCE
      }
  □ Loggear cada request con método, path, parámetros y respuesta completa
  □ Loggear cada query SQL ejecutada con parámetros expandidos
  □ Nunca incluir passwords ni tokens en los logs de DEBUG

MODO PERFORMANCE (SYSTEM_MODE=PERFORMANCE):
  □ Headers mínimos en respuesta (sin headers de debug)
  □ Activar caché de respuestas donde sea correcto (Cache-Control, ETag)
  □ Comprimir respuestas (gzip/br) si el cliente lo soporta
  □ Nivel de log: solo WARNING y ERROR
  □ Sin stack traces en respuestas de error — solo mensaje genérico

MODO MANTENIMIENTO (SYSTEM_MODE=MAINTENANCE):
  □ Los endpoints GET (lectura) responden con normalidad
  □ Los endpoints POST/PUT/PATCH/DELETE retornan:
      HTTP 503 Service Unavailable
      Retry-After: <timestamp estimado de fin de mantenimiento>
      {
        "type": "https://api.sistema.com/errors/maintenance",
        "title": "Sistema en mantenimiento",
        "status": 503,
        "detail": "Las operaciones de escritura están temporalmente suspendidas.
                   Los cambios serán procesados al finalizar el mantenimiento.",
        "instance": "/v1/pagos",
        "maintenance_script": "20241115_103000_pagos_procesar_pago.sql"
      }
  □ Internamente: generar script SQL y retornar referencia al script en el body

VERIFICACIÓN EN EL DISEÑO DE CADA ENDPOINT:
  □ ¿Está documentado el comportamiento del endpoint en modo MAINTENANCE?
  □ ¿Los errores incluyen debug info solo en modo DEBUG?
  □ ¿El caché está configurado correctamente para modo PERFORMANCE?
```

---

## 13. Restricciones

```
MODOS GLOBALES:
✗ No incluir stack traces en respuestas de error en modo PERFORMANCE
✗ No retornar escrituras directas a BD en modo MAINTENANCE — generar script
✗ No omitir el header X-Correlation-ID en modo DEBUG

ROLES DE USUARIO:

```
ROLES DE USUARIO:
✗ No diseñar APIs con usuarios sin documentar los 5 roles mínimos obligatorios:
  administrador, operador, usuario, desarrollador, visualizador
✗ No dejar endpoints sin declarar qué roles tienen acceso
✗ No retornar 401 cuando el problema es de autorización (rol insuficiente) — usar 403
✗ No dar al visualizador acceso a endpoints que modifiquen estado

DISEÑO:
✗ No retornar 200 OK con un body que describe un error
✗ No exponer stack traces o información interna en respuestas de error
✗ No almacenar tokens o credenciales en query parameters (aparecen en logs)
✗ No diseñar endpoints sin documentar sus códigos de error posibles
✗ No omitir paginación en endpoints que retornan colecciones
✗ No usar HTTP en producción — solo HTTPS
✗ No cambiar contratos existentes sin versionado y plan de deprecación
```

---

## 15. Contrato canónico — uniformidad obligatoria

Cuando el sistema sigue el método de desarrollo (CLAUDE.md §4 ter), las
APIs respetan un **contrato canónico** que vuelve uniforme la experiencia
de quien las consume. Esto NO reemplaza §3 (convenciones) — lo cierra
con reglas precisas y verificables.

### 15.1 Matriz HTTP por verbo (obligatoria)

```
GET     → 200 (ok), 304 (not-modified), 400 (params malos),
          401 (sin auth), 403 (rol insuficiente), 404 (no existe)

POST    → 201 (created, con Location del nuevo recurso),
          200 (acción ok sin recurso nuevo),
          400, 401, 403,
          409 (conflicto: duplicado, estado inválido),
          422 (validación de campos falló)

PUT     → 200 (replaced), 201 (created por upsert),
          400, 401, 403, 404, 409, 422

PATCH   → 200, 400, 401, 403, 404, 409, 422

DELETE  → 204 (no-content), 200 (con cuerpo de confirmación),
          401, 403, 404, 409 (no se puede eliminar por integridad)

Cualquier escritura puede retornar:
  423 (locked, sistema en modo MANTENIMIENTO — /dev-modes §2.3)
  503 (service unavailable, BD down o down stream caído)

Códigos NUNCA usar:
  ✗ 200 con { error: ... } (usar 4xx/5xx con Problem+JSON)
  ✗ 500 para errores de validación (usar 422)
  ✗ 403 para "no encontrado" (usar 404, salvo razón explícita de seguridad)
```

### 15.2 Errores en Problem+JSON (RFC 9457)

```
Content-Type: application/problem+json

{
  "type":     "https://errors.midominio.com/validation",
  "title":    "Validation failed",
  "status":   422,
  "detail":   "El campo 'email' es obligatorio.",
  "instance": "/v1/usuarios",
  "errors": [
    { "field": "email", "code": "required" },
    { "field": "telefono", "code": "format_e164" }
  ]
}
```

Helper obligatorio en backend (no construir el cuerpo a mano):

```javascript
// templates/backend/createProblem.js
export function createProblem(req, status, type, detail, errors) {
  return {
    type:     `https://errors.${process.env.DOMAIN}/${type}`,
    title:    titleForStatus(status),
    status,
    detail,
    instance: req.originalUrl,
    ...(errors && { errors }),
  };
}
```

### 15.3 Envelope obligatorio en listados

```
GET /v1/productos
→ 200 OK
{
  "data": [
    { "id": "...", "nombre": "...", ... },
    ...
  ],
  "next_cursor": "eyJpZCI6MTIzfQ=="   // base64-encoded; null si no hay más
}
```

- `data` siempre array
- `next_cursor` siempre presente (null si no hay más)
- **No** usar `meta.totalCount` salvo SLA explícito que lo requiera
  (es caro en BDs grandes)
- **No** usar `links` HATEOAS salvo decisión explícita de equipo

### 15.4 Serialización canónica

```
TIMESTAMP   → string ISO 8601 con Z (UTC):  "2026-05-12T14:30:00.000Z"
DATE        → string YYYY-MM-DD:             "2026-05-12"
BOOLEAN     → 0 | 1 (no true / false)        // portabilidad SQL-92
DECIMAL     → string:                        "123.45"
              (evita pérdida de precisión en JSON.parse)
INTEGER     → number nativo de JSON:         123
UUID        → string:                        "550e8400-e29b-..."
NULL        → JSON null explícito            // nunca omitir la propiedad
ENUM        → string con valor exacto del enum: "PENDIENTE"
```

### 15.5 Idempotencia uniforme

Endpoints `POST`, `PUT`, `PATCH` y `DELETE` aceptan header
`Idempotency-Key`. Si llega un request con la misma clave en una ventana
configurable (24 h por defecto), retornar la misma respuesta que la
primera vez, con `sin_cambio: true`:

```
POST /v1/transferencias
Idempotency-Key: e7c1f4d2-8a3b-...

→ 201 Created (primera vez)
  { "id": "...", "estado": "PROCESADA" }

→ 200 OK (segunda llamada con misma key)
  { "id": "...", "estado": "PROCESADA", "sin_cambio": true }
```

### 15.6 Versionado aditivo

```
✓ Agregar endpoints nuevos a /v1/...        — sin bump, es aditivo
✓ Agregar campos opcionales a respuestas     — sin bump, es aditivo
✓ Agregar valores nuevos a un enum           — sin bump, documentar
✗ Eliminar campos, renombrar, cambiar tipo  — bump a /v2/...

REGLA DE PARALELO:
  /v1/ y /v2/ corren en paralelo mínimo 90 días.
  /v1/ envía header de deprecación durante ese período:
    Deprecation: true
    Sunset: <fecha ISO>
    Link: </v2/recurso>; rel="successor-version"
```

### 15.7 Helper recomendado de cliente

```typescript
// Frontend — todo fetch pasa por aquí
async function apiFetch<T>(
  path: string,
  options?: RequestInit & { idempotencyKey?: string }
): Promise<ApiResponse<T>> {
  const res = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options?.idempotencyKey && {
        'Idempotency-Key': options.idempotencyKey,
      }),
      ...options?.headers,
    },
  });

  if (!res.ok) {
    const problem = await res.json() as ProblemDetail;
    throw new ApiError(problem);
  }

  return res.json() as Promise<ApiResponse<T>>;
}
```

### 15.8 Checklist antes de mergear cambios de API

```
□ Endpoint en matriz HTTP canónica (15.1)
□ Errores en Problem+JSON, NO en { error: ... } legacy
□ Listados con envelope { data, next_cursor }
□ Serialización canónica para TIMESTAMP, BOOLEAN, DECIMAL
□ Idempotency-Key respetada en escrituras
□ Versionado aditivo (no breaking en major existente)
□ OpenAPI regenerado (/dev-meta meta-derive-openapi)
□ Tests del contrato pasan en CI (postgres + mysql + sqlserver)
```

---

## 16. Referencias del dominio (APA 7)

OpenAPI Initiative. (2021). *OpenAPI specification 3.1.0*.
    https://spec.openapis.org/oas/v3.1.0

Internet Engineering Task Force. (2023). *RFC 9457: Problem details for
    HTTP APIs*. IETF. https://www.rfc-editor.org/rfc/rfc9457

Masse, M. (2011). *REST API design rulebook*. O'Reilly Media.

Fielding, R. T. (2000). *Architectural styles and the design of
    network-based software architectures* [Doctoral dissertation,
    University of California, Irvine].
    https://ics.uci.edu/~fielding/pubs/dissertation/top.htm
