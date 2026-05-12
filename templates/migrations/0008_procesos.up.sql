-- ============================================================
-- Migración 0008 — procesos (Nivel 2: flujos de negocio)
-- Nivel: 2 (Operacional). Habilitar con /meta-bump a Nivel 2.
-- ============================================================

CREATE TABLE procesos (
    nombre              VARCHAR(100)  NOT NULL,
    descripcion         VARCHAR(500)  NOT NULL,
    modulo              VARCHAR(100)  NOT NULL,
    nivel_metadata      SMALLINT      NOT NULL DEFAULT 2,
    requiere_aprobacion SMALLINT      NOT NULL DEFAULT 0,
    roles_ejecucion     VARCHAR(500)  NOT NULL DEFAULT 'administrador,operador',
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    creado_en           VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_procesos PRIMARY KEY (nombre),
    CONSTRAINT ck_procesos_aprobacion CHECK (requiere_aprobacion IN (0, 1))
);
