-- ============================================================
-- Migración 0009 — semaforos (Nivel 2: estados con transiciones)
-- Nivel: 2. Depende de 0002_campos_sistema.
-- ============================================================

CREATE TABLE semaforos (
    nombre_tabla         VARCHAR(100)  NOT NULL,
    nombre_campo         VARCHAR(100)  NOT NULL,
    estado_origen        VARCHAR(50)   NOT NULL,
    estado_destino       VARCHAR(50)   NOT NULL,
    transicion_permitida SMALLINT      NOT NULL DEFAULT 1,
    roles_transicion     VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    mensaje_ayuda        VARCHAR(500)  NOT NULL DEFAULT '',
    creado_en            VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_semaforos
        PRIMARY KEY (nombre_tabla, nombre_campo, estado_origen, estado_destino),
    CONSTRAINT fk_semaforos_campo
        FOREIGN KEY (nombre_tabla, nombre_campo)
        REFERENCES campos_sistema (nombre_tabla, nombre_campo),
    CONSTRAINT ck_semaforos_permitida CHECK (transicion_permitida IN (0, 1))
);
