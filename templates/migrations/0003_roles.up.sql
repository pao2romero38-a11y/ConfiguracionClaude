-- ============================================================
-- Migración 0003 — roles (5 roles obligatorios del método)
-- Nivel: 1. Ver /dev §6 y /dev-db §4 para la regla.
-- ============================================================

CREATE TABLE roles (
    id           CHAR(36)      NOT NULL,
    nombre       VARCHAR(50)   NOT NULL,
    descripcion  VARCHAR(500)  NOT NULL,
    protegido    SMALLINT      NOT NULL DEFAULT 0,
    activo       SMALLINT      NOT NULL DEFAULT 1,
    creado_en    VARCHAR(40)   NOT NULL,
    CONSTRAINT pk_roles         PRIMARY KEY (id),
    CONSTRAINT uq_roles_nombre  UNIQUE (nombre),
    CONSTRAINT ck_roles_protegido CHECK (protegido IN (0, 1)),
    CONSTRAINT ck_roles_activo    CHECK (activo IN (0, 1))
);

-- 5 roles obligatorios del método. protegido=1 → no se pueden eliminar
-- ni renombrar. UUIDs reservados 00000001-0000-...-001 a 005.
INSERT INTO roles (id, nombre, descripcion, protegido, activo, creado_en) VALUES
  ('00000001-0000-0000-0000-000000000001', 'administrador',
   'Acceso total al sistema. Gestiona usuarios, configuración y parámetros.',
   1, 1, '2026-05-11T00:00:00.000Z'),
  ('00000001-0000-0000-0000-000000000002', 'operador',
   'Ejecuta operaciones del negocio. Crea y modifica registros operativos.',
   1, 1, '2026-05-11T00:00:00.000Z'),
  ('00000001-0000-0000-0000-000000000003', 'usuario',
   'Acceso estándar. Usa las funciones del sistema según su perfil.',
   1, 1, '2026-05-11T00:00:00.000Z'),
  ('00000001-0000-0000-0000-000000000004', 'desarrollador',
   'Herramientas técnicas, logs, configuración y entornos de prueba.',
   1, 1, '2026-05-11T00:00:00.000Z'),
  ('00000001-0000-0000-0000-000000000005', 'visualizador',
   'Solo lectura. Consulta información sin modificar registros.',
   1, 1, '2026-05-11T00:00:00.000Z');
