-- ============================================================
-- Migración 0004 — usuarios + usuarios_roles (asignación auditable)
-- Nivel: 1. Depende de 0003_roles.
-- ============================================================

CREATE TABLE usuarios (
    id              CHAR(36)      NOT NULL,
    email           VARCHAR(254)  NOT NULL,
    nombre          VARCHAR(200)  NOT NULL,
    password_hash   VARCHAR(500)  NOT NULL,
    activo          SMALLINT      NOT NULL DEFAULT 1,
    creado_en       VARCHAR(40)   NOT NULL,
    modificado_en   VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_usuarios         PRIMARY KEY (id),
    CONSTRAINT uq_usuarios_email   UNIQUE (email),
    CONSTRAINT ck_usuarios_activo  CHECK (activo IN (0, 1))
);

CREATE TABLE usuarios_roles (
    usuario_id    CHAR(36)      NOT NULL,
    rol_id        CHAR(36)      NOT NULL,
    asignado_en   VARCHAR(40)   NOT NULL,
    asignado_por  CHAR(36)      NOT NULL,
    activo        SMALLINT      NOT NULL DEFAULT 1,
    CONSTRAINT pk_usuarios_roles
        PRIMARY KEY (usuario_id, rol_id),
    CONSTRAINT fk_usuarios_roles_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
    CONSTRAINT fk_usuarios_roles_rol
        FOREIGN KEY (rol_id) REFERENCES roles (id),
    CONSTRAINT fk_usuarios_roles_asignado_por
        FOREIGN KEY (asignado_por) REFERENCES usuarios (id),
    CONSTRAINT ck_usuarios_roles_activo CHECK (activo IN (0, 1))
);

CREATE INDEX idx_usuarios_roles_usuario ON usuarios_roles (usuario_id);
CREATE INDEX idx_usuarios_roles_rol     ON usuarios_roles (rol_id);
