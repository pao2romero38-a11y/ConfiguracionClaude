---
name: programador-metadata-driven
description: >
  Activar cuando el usuario pida: diseñar o revisar el modelo de metadata
  del sistema; agregar/modificar tablas, campos, procesos, semáforos,
  variables o componentes en las tablas de metadata; subir niveles de
  capacidad (1-9); versionar la metadata con SemVer; generar código desde
  metadata (types, OpenAPI, MSW handlers); o cualquier tarea donde la
  fuente de verdad sea la metadata declarada en BD.
  Skill maestro de la familia metadata-driven. Referenciado por
  /init-proyecto, /stack-pick, /back-scaffold-from-meta,
  /front-scaffold-from-meta, /meta-add-tabla, /meta-bump, /meta-validate,
  /diff-meta, /arq-derive.
  Comandos de activación: /dev-meta · [MODO: METADATA-DRIVEN]
---

# SKILL — Metadata-driven SSOT y 9 niveles progresivos

## 1. Principio rector

> La metadata es **la única fuente de verdad** del sistema. Backend y
> frontend la **leen**, nunca la duplican ni la inventan. Cada cambio en
> el modelo del sistema (tabla, columna, proceso, semáforo, variable,
> componente) **se hace primero en la metadata**, después en el código.

Este skill define el contrato verificable que vuelve esto exigible. El
CLAUDE.md §4 ter establece el método; este skill establece **cómo se
implementa**.

---

## 2. Verificaciones obligatorias ANTES de tocar metadata

- [ ] **Nivel actual del sistema** — leer `metadata_versiones`, ver el
      mayor nivel declarado. ¿La capacidad propuesta está dentro del
      nivel actual o requiere subir? Si requiere subir → `/meta-bump`.
- [ ] **Versión actual** — ver `metadata_versiones.version`. Cualquier
      cambio implica bump SemVer (PATCH / MINOR / MAJOR).
- [ ] **¿Es agregar o modificar?** — agregar tabla nueva → `/meta-add-tabla`.
      Modificar tabla existente → migración con `ALTER` + actualización
      de `campos_sistema`.
- [ ] **Fase del proyecto** — la metadata se construye en Fase 1.
      Modificaciones después de Fase 5 (en producción) requieren bump
      MAJOR y plan de migración de datos.
- [ ] **¿Afecta interfaces externas?** — si la tabla tiene
      `generar_ui_crud=1` o `endpoint_publico=1`, el cambio impacta
      contratos. Verificar idempotencia y versionado aditivo de API.

---

## 3. Tablas de metadata — núcleo obligatorio

Toda implementación del método tiene **al menos** estas 7 tablas en su
bootstrap (`templates/migrations/001-007`). Más se agregan al subir
niveles (ver §5).

### 3.1 `tablas_sistema` — catálogo de tablas del sistema

```sql
CREATE TABLE tablas_sistema (
    nombre_tabla       VARCHAR(100)  NOT NULL,
    funcion            VARCHAR(50)   NOT NULL,
    descripcion        VARCHAR(500)  NOT NULL,
    nivel_metadata     SMALLINT      NOT NULL DEFAULT 1,
    version_metadata   VARCHAR(20)   NOT NULL DEFAULT '1.0.0',
    tabla_uso          VARCHAR(50)   NOT NULL DEFAULT 'crud',
    generar_ui_crud    SMALLINT      NOT NULL DEFAULT 0,
    endpoint_publico   SMALLINT      NOT NULL DEFAULT 0,
    mensaje_ayuda      VARCHAR(500)  NOT NULL DEFAULT '',
    nota_admin         VARCHAR(500)  NOT NULL DEFAULT '',
    creado_en          VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_tablas_sistema PRIMARY KEY (nombre_tabla),
    CONSTRAINT ck_tablas_sistema_funcion
        CHECK (funcion IN ('CATALOGO', 'OPERATIVA', 'TRANSACCIONAL',
                           'BITACORA', 'CONFIGURACION', 'METADATA')),
    CONSTRAINT ck_tablas_sistema_nivel CHECK (nivel_metadata BETWEEN 1 AND 9),
    CONSTRAINT ck_tablas_sistema_generar_ui CHECK (generar_ui_crud IN (0, 1)),
    CONSTRAINT ck_tablas_sistema_endpoint CHECK (endpoint_publico IN (0, 1)),
    CONSTRAINT ck_tablas_sistema_uso
        CHECK (tabla_uso IN ('crud', 'lectura', 'bitacora', 'sistema'))
);
```

### 3.2 `campos_sistema` — catálogo de columnas con ~20 metadatos

```sql
CREATE TABLE campos_sistema (
    nombre_tabla          VARCHAR(100)  NOT NULL,
    nombre_campo          VARCHAR(100)  NOT NULL,
    nombre_corto          VARCHAR(50)   NOT NULL,
    nombre_largo          VARCHAR(200)  NOT NULL,
    tipo_sql              VARCHAR(50)   NOT NULL,
    longitud              INTEGER       NOT NULL DEFAULT 0,
    precision_decimal     INTEGER       NOT NULL DEFAULT 0,
    formato_despliegue    VARCHAR(50)   NOT NULL,
    tipo_validacion       VARCHAR(50)   NOT NULL DEFAULT 'NINGUNA',
    regex_validacion      VARCHAR(500)  NOT NULL DEFAULT '',
    mensaje_ayuda         VARCHAR(500)  NOT NULL DEFAULT '',
    valor_default         VARCHAR(500)  NOT NULL DEFAULT '',
    obligatorio           SMALLINT      NOT NULL DEFAULT 0,
    visible_en_lista      SMALLINT      NOT NULL DEFAULT 1,
    visible_en_form       SMALLINT      NOT NULL DEFAULT 1,
    editable              SMALLINT      NOT NULL DEFAULT 1,
    sensible_lfpdppp      SMALLINT      NOT NULL DEFAULT 0,
    categoria_dato_personal VARCHAR(50) NOT NULL DEFAULT '',
    roles_lectura         VARCHAR(500)  NOT NULL DEFAULT '*',
    roles_modificacion    VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    orden_despliegue      INTEGER       NOT NULL DEFAULT 0,
    creado_en             VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_campos_sistema PRIMARY KEY (nombre_tabla, nombre_campo),
    CONSTRAINT fk_campos_sistema_tabla
        FOREIGN KEY (nombre_tabla) REFERENCES tablas_sistema (nombre_tabla),
    CONSTRAINT ck_campos_sistema_obligatorio CHECK (obligatorio IN (0, 1)),
    CONSTRAINT ck_campos_sistema_visible_lista CHECK (visible_en_lista IN (0, 1)),
    CONSTRAINT ck_campos_sistema_visible_form CHECK (visible_en_form IN (0, 1)),
    CONSTRAINT ck_campos_sistema_editable CHECK (editable IN (0, 1)),
    CONSTRAINT ck_campos_sistema_sensible CHECK (sensible_lfpdppp IN (0, 1))
);
```

**Valores válidos por columna**:

| Columna | Valores aceptados |
|---|---|
| `tipo_sql` | CHAR, VARCHAR, INTEGER, SMALLINT, NUMERIC, DATE, TIMESTAMP |
| `formato_despliegue` | UUID, TEXTO, NUMERO, IMPORTE_MXN, IMPORTE_USD, PORCENTAJE, FECHA, FECHA_HORA, BOOLEANO_ACTIVO, EMAIL, TELEFONO_E164, URL, CODIGO_POSTAL, CURP, RFC, SELECT_RELACION, ENUM |
| `tipo_validacion` | NINGUNA, REGEX, RANGO_NUMERICO, LONGITUD, EMAIL, FK |
| `categoria_dato_personal` | (vacío), IDENTIFICACION, CONTACTO, FINANCIERO, SALUD, SENSIBLE, BIOMETRICO |

### 3.3 `roles` — 5 roles obligatorios (heredado de `/dev` §6)

```sql
CREATE TABLE roles (
    id           CHAR(36)      NOT NULL,
    nombre       VARCHAR(50)   NOT NULL,
    descripcion  VARCHAR(500)  NOT NULL,
    protegido    SMALLINT      NOT NULL DEFAULT 0,
    activo       SMALLINT      NOT NULL DEFAULT 1,
    CONSTRAINT pk_roles         PRIMARY KEY (id),
    CONSTRAINT uq_roles_nombre  UNIQUE (nombre),
    CONSTRAINT ck_roles_protegido CHECK (protegido IN (0, 1)),
    CONSTRAINT ck_roles_activo    CHECK (activo IN (0, 1))
);

INSERT INTO roles (id, nombre, descripcion, protegido) VALUES
  ('00000001-0000-0000-0000-000000000001', 'administrador', 'Acceso total al sistema', 1),
  ('00000001-0000-0000-0000-000000000002', 'operador',      'Operaciones del negocio', 1),
  ('00000001-0000-0000-0000-000000000003', 'usuario',       'Funciones de su perfil',  1),
  ('00000001-0000-0000-0000-000000000004', 'desarrollador', 'Herramientas técnicas',   1),
  ('00000001-0000-0000-0000-000000000005', 'visualizador',  'Solo lectura',            1);
```

`protegido=1` significa **no se puede eliminar ni renombrar**. Aplica a
los 5 roles base.

### 3.4 `procesos` — flujos de negocio del sistema (Nivel 2+)

```sql
CREATE TABLE procesos (
    nombre              VARCHAR(100)  NOT NULL,
    descripcion         VARCHAR(500)  NOT NULL,
    modulo              VARCHAR(100)  NOT NULL,
    nivel_metadata      SMALLINT      NOT NULL DEFAULT 2,
    requiere_aprobacion SMALLINT      NOT NULL DEFAULT 0,
    roles_ejecucion     VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    CONSTRAINT pk_procesos PRIMARY KEY (nombre),
    CONSTRAINT ck_procesos_aprobacion CHECK (requiere_aprobacion IN (0, 1))
);
```

### 3.5 `semaforos` — estados con transiciones permitidas (Nivel 2+)

```sql
CREATE TABLE semaforos (
    nombre_tabla        VARCHAR(100)  NOT NULL,
    nombre_campo        VARCHAR(100)  NOT NULL,
    estado_origen       VARCHAR(50)   NOT NULL,
    estado_destino      VARCHAR(50)   NOT NULL,
    transicion_permitida SMALLINT     NOT NULL DEFAULT 1,
    roles_transicion    VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    CONSTRAINT pk_semaforos
        PRIMARY KEY (nombre_tabla, nombre_campo, estado_origen, estado_destino),
    CONSTRAINT fk_semaforos_campo
        FOREIGN KEY (nombre_tabla, nombre_campo)
        REFERENCES campos_sistema (nombre_tabla, nombre_campo),
    CONSTRAINT ck_semaforos_permitida CHECK (transicion_permitida IN (0, 1))
);
```

### 3.6 `variables_sistema` — configuración runtime (Nivel 2+)

```sql
CREATE TABLE variables_sistema (
    nombre              VARCHAR(100)  NOT NULL,
    valor               VARCHAR(500)  NOT NULL,
    tipo_valor          VARCHAR(50)   NOT NULL DEFAULT 'TEXTO',
    descripcion         VARCHAR(500)  NOT NULL,
    modulo              VARCHAR(100)  NOT NULL DEFAULT 'sistema',
    requiere_reinicio   SMALLINT      NOT NULL DEFAULT 0,
    roles_modificacion  VARCHAR(500)  NOT NULL DEFAULT 'administrador',
    sensible            SMALLINT      NOT NULL DEFAULT 0,
    modificado_en       VARCHAR(40)   NOT NULL,
    modificado_por      CHAR(36)      NOT NULL,
    CONSTRAINT pk_variables_sistema PRIMARY KEY (nombre),
    CONSTRAINT ck_variables_sistema_reinicio CHECK (requiere_reinicio IN (0, 1)),
    CONSTRAINT ck_variables_sistema_sensible CHECK (sensible IN (0, 1))
);

INSERT INTO variables_sistema VALUES
  ('SYSTEM_MODE', 'PERFORMANCE', 'ENUM',
   'Modo de operación: DEBUG | PERFORMANCE | MAINTENANCE',
   'sistema', 1, 'administrador', 0, '...', '...'),
  ('MAINTENANCE_OUTPUT_PATH', '/var/system/mantenimiento', 'TEXTO',
   'Ruta donde se depositan scripts en modo MANTENIMIENTO',
   'sistema', 1, 'administrador', 0, '...', '...'),
  ('PERFORMANCE_CACHE_TTL_SECONDS', '300', 'NUMERO',
   'TTL del caché en modo PERFORMANCE',
   'sistema', 1, 'administrador', 0, '...', '...');
```

Referenciado por `/dev-modes` para SYSTEM_MODE.

### 3.7 `componentes_sistema` — stack tecnológico (Fase 3, Nivel 1+)

```sql
CREATE TABLE componentes_sistema (
    nombre              VARCHAR(100)  NOT NULL,
    categoria           VARCHAR(50)   NOT NULL,
    version             VARCHAR(50)   NOT NULL,
    licencia            VARCHAR(50)   NOT NULL,
    justificacion       VARCHAR(500)  NOT NULL,
    url_oficial         VARCHAR(500)  NOT NULL DEFAULT '',
    obligatorio         SMALLINT      NOT NULL DEFAULT 1,
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    CONSTRAINT pk_componentes_sistema PRIMARY KEY (nombre),
    CONSTRAINT ck_componentes_sistema_categoria
        CHECK (categoria IN ('INFRAESTRUCTURA', 'BD', 'BACKEND',
                             'FRONTEND', 'PRUEBAS', 'OBSERVABILIDAD',
                             'CI', 'SEGURIDAD')),
    CONSTRAINT ck_componentes_sistema_obligatorio CHECK (obligatorio IN (0, 1))
);
```

### 3.8 `metadata_versiones` — versionado SemVer del modelo

```sql
CREATE TABLE metadata_versiones (
    version             VARCHAR(20)   NOT NULL,
    fecha               VARCHAR(10)   NOT NULL,
    niveles             VARCHAR(50)   NOT NULL,
    tablas_incluidas    INTEGER       NOT NULL,
    descripcion         VARCHAR(500)  NOT NULL,
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    nota_admin          VARCHAR(500)  NOT NULL DEFAULT '',
    nota_programador    VARCHAR(500)  NOT NULL DEFAULT '',
    nota_operador       VARCHAR(500)  NOT NULL DEFAULT '',
    aplicada_en         VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_metadata_versiones PRIMARY KEY (version)
);
```

Cada migración nueva inserta una fila. `version` sigue SemVer:
- **PATCH** (`1.0.X`) — cosmético: cambio de `mensaje_ayuda`, `descripcion`
- **MINOR** (`1.X.0`) — aditivo: tabla nueva, columna nueva opcional
- **MAJOR** (`X.0.0`) — breaking: eliminar tabla/columna, cambiar tipo

---

## 4. Reglas de integridad obligatorias

```
□ TODA tabla real del sistema tiene entrada en tablas_sistema
□ TODA columna real tiene entrada en campos_sistema
□ TODA columna con visible_en_form=1 tiene mensaje_ayuda no vacío
□ TODA columna con sensible_lfpdppp=1 tiene categoria_dato_personal declarada
□ TODA columna con tipo_validacion=REGEX tiene regex_validacion no vacío
□ Los 5 roles base existen en roles y tienen protegido=1
□ TODAS las variables del sistema (SYSTEM_MODE, etc.) están en variables_sistema
□ El stack está completo en componentes_sistema antes de Fase 4
```

`/meta-validate` ejecuta estos checks (17 en total) y bloquea Fase 5 si
hay gaps. Ver `meta-validate/SKILL.md` §3 para el listado completo.

---

## 5. 9 niveles progresivos — qué habilita cada uno

Un sistema declara su **nivel máximo activo** en `metadata_versiones`.
`/arq-derive` rechaza propuestas que excedan ese nivel.

```
NIVEL 1 — ESTRUCTURAL                    | Tablas obligatorias:
                                          | tablas_sistema, campos_sistema,
                                          | roles, metadata_versiones,
                                          | componentes_sistema
                                          | + las tablas de negocio

NIVEL 2 — OPERACIONAL                    | Agregar:
                                          | procesos, semaforos,
                                          | variables_sistema

NIVEL 3 — AUDITORÍA                      | Agregar:
                                          | bitacora_operaciones,
                                          | bitacora_login,
                                          | bitacora_modificaciones_metadata
                                          | + correlation_id obligatorio

NIVEL 4 — PERMISOS GRANULARES             | Agregar (en campos_sistema):
                                          | roles_lectura por campo
                                          | roles_modificacion por campo
                                          | + vistas por rol

NIVEL 5 — CACHÉ                          | Agregar:
                                          | cache_policies
                                          | (tabla, query, ttl, invalidacion)

NIVEL 6 — TIEMPO REAL                    | Agregar:
                                          | event_bus_topics, websocket_channels,
                                          | push_subscriptions

NIVEL 7 — BÚSQUEDA Y CDN                 | Agregar:
                                          | search_indexes (full-text),
                                          | cdn_assets (hot/cold)

NIVEL 8 — OBSERVABILIDAD                 | Agregar:
                                          | metricas (counters/gauges/histograms),
                                          | alertas (umbrales, destinatarios),
                                          | dashboards (paneles derivados)

NIVEL 9 — ALTA DISPONIBILIDAD            | Agregar:
                                          | replication_topology,
                                          | failover_policies,
                                          | circuit_breakers,
                                          | bulkhead_partitions
```

**Reglas**:
- No se salta nivel. Para activar Nivel N hay que haber poblado los
  N-1 anteriores.
- Subir de nivel = migración con bump MINOR mínimo + revisión por reviewer.
- Bajar de nivel **no se permite** sin bump MAJOR + plan de migración
  documentado.

---

## 6. Codegen desde metadata — los 3 obligatorios

Los scripts viven en `templates/codegen/` y se invocan desde npm
scripts del proyecto generado por `/install-from-stack`.

### 6.1 `meta-derive-types.js` — TypeScript interfaces

Lee `campos_sistema` y `tablas_sistema`, emite `Dev/frontend/src/api/types/_generated.ts`:

```typescript
// AUTO-GENERADO — no editar a mano. Regenerar con: npm run meta:types
export interface Usuario {
  id:            string;
  email:         string;
  nombre:        string;
  activo:        0 | 1;
  creado_en:     string;  // ISO 8601
}

export interface ApiResponse<T> {
  data:        T;
  next_cursor: string | null;
}

export interface ProblemDetail {
  type:     string;
  title:    string;
  status:   number;
  detail:   string;
  instance: string;
  errors?:  Array<{ field: string; code: string }>;
}
```

### 6.2 `meta-derive-openapi.js` — OpenAPI 3.1 YAML

Emite `Dev/openapi.yaml` con paths `/v1/<recurso>` derivados de tablas
con `endpoint_publico=1`.

### 6.3 `front-msw-from-meta.js` — MSW v2 handlers + fixtures

Emite `Dev/frontend/src/test/msw/_generated.ts` con handlers GET / POST /
PATCH / DELETE por tabla con `generar_ui_crud=1`, más fixtures
determinísticos derivados de `tipo_validacion` (nunca `Math.random()`).

### 6.4 CI enforcement

Job `metadata-snapshot-sync` en `ci-matrix.yml` corre los 3 codegen y
`git diff --exit-code`. **Falla el PR** si hay drift. Esto vuelve
imposible olvidar regenerar.

---

## 7. Convivencia con SQL-92 y modos globales

Este skill **no reemplaza** `/dev-db` ni `/dev-modes` — los amplifica:

| Aporta `/dev-db` | Aporta `/dev-modes` | Aporta `/dev-meta` |
|---|---|---|
| Tipos SQL-92 portables | SYSTEM_MODE en código | Las **declaraciones** de esos tipos en `campos_sistema.tipo_sql` |
| Tabla de tipos prohibidos | Variable SYSTEM_MODE en BD | La **declaración** en `variables_sistema` |
| 5 roles obligatorios en BD | Logging por modo | Los 5 roles en `roles` con `protegido=1` |

**Patrón**: lo que `/dev-db` y `/dev-modes` prescriben en código,
`/dev-meta` lo declara como dato. La metadata es **la forma**, no la
sustitución.

---

## 8. Formato de entrega obligatorio

```
### [Cambio propuesto a metadata]
  Qué tabla(s) / columna(s) / proceso(s) / etc. se modifican.
  Razón del negocio que motiva el cambio.
  Nivel de metadata involucrado.

### [Bump SemVer]
  PATCH | MINOR | MAJOR — justificación.

### [Migración]
\`\`\`sql
-- Migración NNNN_<nombre>.up.sql
-- SQL-92 estricto (ver /dev-db §3 y templates/migrations/PORTABLE-SQL.md)
...
\`\`\`

### [Down migration]
\`\`\`sql
-- Migración NNNN_<nombre>.down.sql
...
\`\`\`

### [Impacto en codegen]
  - Tipos TypeScript: ¿cambia _generated.ts?
  - OpenAPI: ¿cambia openapi.yaml?
  - MSW handlers: ¿cambia handlers o fixtures?
  Si SÍ → recordar que CI metadata-snapshot-sync va a fallar hasta
  regenerar y commitear.

### [Validaciones a correr]
  - /meta-validate antes de aplicar
  - npm run meta:types  (regenera _generated.ts)
  - npm run meta:openapi (regenera openapi.yaml)
  - npm run meta:msw    (regenera handlers MSW)

### [Referencias] APA 7, más reciente → más antigua
```

---

## 9. Restricciones

```
✗ No declarar tablas o columnas reales sin entrada en tablas_sistema /
  campos_sistema. La metadata es SSOT.
✗ No usar tipos exclusivos de un motor en tipo_sql (BOOLEAN, JSONB,
  SERIAL, TIMESTAMPTZ, etc.) — solo tipos SQL-92 (/dev-db §3)
✗ No usar valores de formato_despliegue fuera del catálogo de §3.2
✗ No omitir mensaje_ayuda cuando visible_en_form=1
✗ No omitir categoria_dato_personal cuando sensible_lfpdppp=1
✗ No eliminar los 5 roles base (protegido=1)
✗ No subir de nivel sin agregar las tablas que el nivel exige
✗ No saltarse niveles (de 2 a 4 sin pasar por 3)
✗ No modificar metadata sin bump SemVer en metadata_versiones
✗ No emitir codegen "a mano" — siempre via scripts de templates/codegen/
✗ No silenciar el job metadata-snapshot-sync con commits que regeneran
  sin reflejar el cambio en migración (eso es drift escondido)
✗ No generar UUIDs con extensiones del motor (gen_random_uuid, NEWID).
  Generar en aplicación con crypto.randomUUID() / uuid.v4() / etc.
```

---

## 10. Referencias del dominio (APA 7)

International Organization for Standardization. (2022).
   *ISO/IEC 19075-2:2022 — Information technology — Guidance for the use
   of database language SQL*. ISO.

Newman, S. (2019). *Monolith to microservices: Evolutionary patterns to
   transform your monolith*. O'Reilly Media.

Kleppmann, M. (2017). *Designing data-intensive applications: The big
   ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media.

Fowler, M. (2018). *Refactoring: Improving the design of existing code*
   (2nd ed.). Addison-Wesley.

International Organization for Standardization. (1992).
   *ISO/IEC 9075:1992 — Information technology: Database language SQL*. ISO.
