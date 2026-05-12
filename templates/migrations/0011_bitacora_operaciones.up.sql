-- ============================================================
-- Migración 0011 — bitacora_operaciones (Nivel 3: auditoría)
-- Nivel: 3. Habilitar con /meta-bump a Nivel 3.
-- ============================================================

CREATE TABLE bitacora_operaciones (
    id                CHAR(36)      NOT NULL,
    correlation_id    CHAR(36)      NOT NULL,
    usuario_id        CHAR(36)      NOT NULL,
    modulo            VARCHAR(100)  NOT NULL,
    operacion         VARCHAR(200)  NOT NULL,
    nombre_tabla      VARCHAR(100)  NOT NULL DEFAULT '',
    registro_id       CHAR(36)      NOT NULL DEFAULT '',
    valor_anterior    VARCHAR(4000) NOT NULL DEFAULT '',
    valor_nuevo       VARCHAR(4000) NOT NULL DEFAULT '',
    direccion_ip      VARCHAR(45)   NOT NULL DEFAULT '',
    user_agent        VARCHAR(500)  NOT NULL DEFAULT '',
    resultado         VARCHAR(50)   NOT NULL,
    mensaje_error     VARCHAR(2000) NOT NULL DEFAULT '',
    duracion_ms       INTEGER       NOT NULL DEFAULT 0,
    creado_en         VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_bitacora_operaciones PRIMARY KEY (id),
    CONSTRAINT ck_bitacora_operaciones_resultado
        CHECK (resultado IN ('OK', 'ERROR', 'WARNING', 'BLOCKED'))
);

CREATE INDEX idx_bitacora_operaciones_correlation
    ON bitacora_operaciones (correlation_id);
CREATE INDEX idx_bitacora_operaciones_usuario_fecha
    ON bitacora_operaciones (usuario_id, creado_en);
CREATE INDEX idx_bitacora_operaciones_tabla_registro
    ON bitacora_operaciones (nombre_tabla, registro_id);
