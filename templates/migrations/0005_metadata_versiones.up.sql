-- ============================================================
-- Migración 0005 — metadata_versiones (SemVer del modelo)
-- Nivel: 1. Cada cambio en metadata inserta una fila.
-- ============================================================

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

INSERT INTO metadata_versiones
  (version, fecha, niveles, tablas_incluidas, descripcion,
   mensaje_ayuda, nota_admin, nota_programador, nota_operador, aplicada_en)
VALUES
  ('1.0.0', '2026-05-11', '1', 5,
   'Bootstrap Nivel 1: tablas_sistema, campos_sistema, roles, usuarios, metadata_versiones.',
   'Versión inicial del modelo. Sistema operable en Nivel 1.',
   'Aplicar 0001-0007 en orden estricto.',
   'Toda nueva tabla debe registrarse en tablas_sistema y campos_sistema.',
   'Sistema listo para uso básico de catálogos y CRUD.',
   '2026-05-11T00:00:00.000Z');
