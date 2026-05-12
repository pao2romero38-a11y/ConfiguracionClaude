-- ============================================================
-- Migración 0001 — tablas_sistema (catálogo maestro de tablas)
-- Nivel: 1 (Estructural) — obligatoria en todo sistema del método
-- SQL-92 estricto, portable a los 6 DBMS (ver PORTABLE-SQL.md)
-- ============================================================

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

-- Auto-registro: tablas_sistema se documenta a sí misma
INSERT INTO tablas_sistema
  (nombre_tabla, funcion, descripcion, nivel_metadata, version_metadata,
   tabla_uso, generar_ui_crud, endpoint_publico,
   mensaje_ayuda, nota_admin, creado_en)
VALUES
  ('tablas_sistema', 'METADATA',
   'Catálogo maestro de tablas del sistema. SSOT.',
   1, '1.0.0', 'sistema', 0, 0,
   'Catálogo de todas las tablas del sistema con su clasificación funcional.',
   'No editar a mano. Modificar via migraciones con bump SemVer.',
   '2026-05-11T00:00:00.000Z');
