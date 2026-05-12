-- ============================================================
-- Migración 0002 — campos_sistema (catálogo de columnas con ~20 metadatos)
-- Nivel: 1 (Estructural). Depende de 0001_tablas_sistema.
-- ============================================================

CREATE TABLE campos_sistema (
    nombre_tabla            VARCHAR(100)  NOT NULL,
    nombre_campo            VARCHAR(100)  NOT NULL,
    nombre_corto            VARCHAR(50)   NOT NULL,
    nombre_largo            VARCHAR(200)  NOT NULL,
    tipo_sql                VARCHAR(50)   NOT NULL,
    longitud                INTEGER       NOT NULL DEFAULT 0,
    precision_decimal       INTEGER       NOT NULL DEFAULT 0,
    formato_despliegue      VARCHAR(50)   NOT NULL,
    tipo_validacion         VARCHAR(50)   NOT NULL DEFAULT 'NINGUNA',
    regex_validacion        VARCHAR(500)  NOT NULL DEFAULT '',
    mensaje_ayuda           VARCHAR(500)  NOT NULL DEFAULT '',
    valor_default           VARCHAR(500)  NOT NULL DEFAULT '',
    obligatorio             SMALLINT      NOT NULL DEFAULT 0,
    visible_en_lista        SMALLINT      NOT NULL DEFAULT 1,
    visible_en_form         SMALLINT      NOT NULL DEFAULT 1,
    editable                SMALLINT      NOT NULL DEFAULT 1,
    sensible_lfpdppp        SMALLINT      NOT NULL DEFAULT 0,
    categoria_dato_personal VARCHAR(50)   NOT NULL DEFAULT '',
    roles_lectura           VARCHAR(500)  NOT NULL DEFAULT '*',
    roles_modificacion      VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    orden_despliegue        INTEGER       NOT NULL DEFAULT 0,
    creado_en               VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_campos_sistema
        PRIMARY KEY (nombre_tabla, nombre_campo),
    CONSTRAINT fk_campos_sistema_tabla
        FOREIGN KEY (nombre_tabla) REFERENCES tablas_sistema (nombre_tabla),
    CONSTRAINT ck_campos_sistema_obligatorio CHECK (obligatorio IN (0, 1)),
    CONSTRAINT ck_campos_sistema_visible_lista CHECK (visible_en_lista IN (0, 1)),
    CONSTRAINT ck_campos_sistema_visible_form CHECK (visible_en_form IN (0, 1)),
    CONSTRAINT ck_campos_sistema_editable CHECK (editable IN (0, 1)),
    CONSTRAINT ck_campos_sistema_sensible CHECK (sensible_lfpdppp IN (0, 1)),
    CONSTRAINT ck_campos_sistema_tipo_sql
        CHECK (tipo_sql IN ('CHAR', 'VARCHAR', 'INTEGER', 'SMALLINT',
                            'NUMERIC', 'DATE', 'TIMESTAMP'))
);

CREATE INDEX idx_campos_sistema_tabla ON campos_sistema (nombre_tabla);
