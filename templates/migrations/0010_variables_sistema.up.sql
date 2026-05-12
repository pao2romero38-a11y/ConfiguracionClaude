-- ============================================================
-- Migración 0010 — variables_sistema (Nivel 2: configuración runtime tipada)
-- Nivel: 2. Complementa a configuracion_sistema con tipo, modulo y roles.
-- ============================================================

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
    CONSTRAINT ck_variables_sistema_tipo
        CHECK (tipo_valor IN ('TEXTO', 'NUMERO', 'ENUM', 'BOOLEANO_0_1', 'JSON_STR')),
    CONSTRAINT ck_variables_sistema_reinicio CHECK (requiere_reinicio IN (0, 1)),
    CONSTRAINT ck_variables_sistema_sensible CHECK (sensible IN (0, 1))
);
