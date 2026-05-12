-- ============================================================
-- Migración 0007 — configuracion_sistema + variables iniciales (SYSTEM_MODE)
-- Nivel: 1. Define las variables globales referenciadas por /dev-modes.
-- ============================================================

CREATE TABLE configuracion_sistema (
    clave           VARCHAR(100)  NOT NULL,
    valor           VARCHAR(500)  NOT NULL,
    descripcion     VARCHAR(500)  NOT NULL,
    modificado_en   VARCHAR(40)   NOT NULL,
    modificado_por  CHAR(36)      NOT NULL,
    CONSTRAINT pk_configuracion_sistema PRIMARY KEY (clave)
);

-- Variables globales obligatorias del sistema (ver /dev-modes §3)
INSERT INTO configuracion_sistema (clave, valor, descripcion, modificado_en, modificado_por) VALUES
  ('SYSTEM_MODE', 'PERFORMANCE',
   'Modo de operación del sistema. Valores: DEBUG | PERFORMANCE | MAINTENANCE',
   '2026-05-11T00:00:00.000Z', '00000001-0000-0000-0000-000000000001'),
  ('DEBUG_LOG_LEVEL', 'DEBUG',
   'Nivel de log en modo DEBUG. Valores: DEBUG | INFO | WARNING | ERROR',
   '2026-05-11T00:00:00.000Z', '00000001-0000-0000-0000-000000000001'),
  ('MAINTENANCE_OUTPUT_PATH', '/var/system/mantenimiento',
   'Ruta donde se depositan los scripts generados en modo MAINTENANCE',
   '2026-05-11T00:00:00.000Z', '00000001-0000-0000-0000-000000000001'),
  ('PERFORMANCE_CACHE_TTL_SECONDS', '300',
   'Tiempo de vida del caché en segundos en modo PERFORMANCE',
   '2026-05-11T00:00:00.000Z', '00000001-0000-0000-0000-000000000001');
