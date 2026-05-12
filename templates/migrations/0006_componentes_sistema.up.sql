-- ============================================================
-- Migración 0006 — componentes_sistema (stack tecnológico, Fase 3)
-- Nivel: 1. Poblado por /stack-pick.
-- ============================================================

CREATE TABLE componentes_sistema (
    nombre              VARCHAR(100)  NOT NULL,
    categoria           VARCHAR(50)   NOT NULL,
    version             VARCHAR(50)   NOT NULL,
    licencia            VARCHAR(50)   NOT NULL,
    justificacion       VARCHAR(500)  NOT NULL,
    url_oficial         VARCHAR(500)  NOT NULL DEFAULT '',
    obligatorio         SMALLINT      NOT NULL DEFAULT 1,
    mensaje_ayuda       VARCHAR(500)  NOT NULL DEFAULT '',
    creado_en           VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_componentes_sistema PRIMARY KEY (nombre),
    CONSTRAINT ck_componentes_sistema_categoria
        CHECK (categoria IN ('INFRAESTRUCTURA', 'BD', 'BACKEND',
                             'FRONTEND', 'PRUEBAS', 'OBSERVABILIDAD',
                             'CI', 'SEGURIDAD')),
    CONSTRAINT ck_componentes_sistema_obligatorio CHECK (obligatorio IN (0, 1))
);
