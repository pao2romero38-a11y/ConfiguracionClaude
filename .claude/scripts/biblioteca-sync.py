#!/usr/bin/env python3
"""
biblioteca-sync.py — Sincroniza copias locales del usuario con el catálogo.

Uso:
    python3 biblioteca-sync.py [--check | --link | --report]

Lee el catálogo `library/CATALOG.yaml` y la configuración del usuario en
`~/.config/biblioteca-local.yaml` (formato: catalog_id → ruta local).

Modos:
  --check    Verifica el estado del catálogo y la cobertura local del usuario.
             No modifica nada. Modo por defecto.
  --link     Crea symlinks de las copias locales del usuario en library/local/.
             Útil para acceso uniforme desde scripts.
  --report   Reporte detallado: qué hay en el catálogo, qué tiene cobertura
             local, qué está en dominio público y se puede descargar.

Filosofía:
  · NO descarga material copyrighted.
  · NO redistribuye nada.
  · Solo organiza las copias que el usuario YA POSEE legalmente.
  · Para material en dominio público (LFPDPPP, DOF, etc.) puede ofrecerse
    descarga futura desde URL oficial — por ahora solo se reporta.

Dependencias: pyyaml (pip install --user pyyaml)
"""
import argparse
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: requiere PyYAML. Instalar con: pip install --user pyyaml")


REPO_ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = REPO_ROOT / "library" / "CATALOG.yaml"
LOCAL_DIR = REPO_ROOT / "library" / "local"
USER_CONFIG = Path.home() / ".config" / "biblioteca-local.yaml"


def load_catalog() -> dict:
    if not CATALOG_PATH.exists():
        sys.exit(f"ERROR: catálogo no encontrado en {CATALOG_PATH}")
    with open(CATALOG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_user_config() -> dict:
    if not USER_CONFIG.exists():
        return {}
    with open(USER_CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def flatten_entries(catalog: dict) -> list:
    """Devuelve la lista plana de entries, anotando dominio en cada uno."""
    out = []
    for key, val in catalog.items():
        if isinstance(val, list):
            for entry in val:
                if isinstance(entry, dict) and entry.get("id"):
                    entry_copy = dict(entry)
                    entry_copy["_dominio"] = key
                    out.append(entry_copy)
    return out


def cmd_check(catalog: dict, user_cfg: dict) -> int:
    entries = flatten_entries(catalog)
    print(f"📚 Catálogo: {len(entries)} entradas en {sum(1 for k,v in catalog.items() if isinstance(v, list))} dominios")
    print(f"📁 Configuración usuario: {USER_CONFIG}")
    if not user_cfg:
        print("   (sin configuración — todas las entradas se reportan sin cobertura local)")
        return 0

    covered = 0
    missing_local = 0
    public_no_local = 0

    for entry in entries:
        eid = entry["id"]
        local_path_str = user_cfg.get(eid)
        if local_path_str:
            local_path = Path(local_path_str).expanduser()
            if local_path.exists():
                covered += 1
            else:
                missing_local += 1
                print(f"   ⚠ {eid}: ruta configurada pero no existe: {local_path}")
        else:
            if entry.get("license") == "public_domain":
                public_no_local += 1

    print(f"\n   ✓ con copia local accesible: {covered}/{len(entries)}")
    print(f"   ⚠ con ruta configurada pero archivo ausente: {missing_local}")
    print(f"   ℹ públicas sin cobertura local (descargables desde URL oficial): {public_no_local}")
    return 0


def cmd_link(catalog: dict, user_cfg: dict) -> int:
    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    entries = flatten_entries(catalog)
    created = 0
    skipped_missing = 0
    for entry in entries:
        eid = entry["id"]
        local_path_str = user_cfg.get(eid)
        if not local_path_str:
            continue
        local_path = Path(local_path_str).expanduser()
        if not local_path.exists():
            print(f"   ⚠ {eid}: ruta del usuario no existe ({local_path})")
            skipped_missing += 1
            continue
        # Determinar extensión del symlink
        ext = local_path.suffix if local_path.is_file() else ""
        link_target = LOCAL_DIR / f"{eid}{ext}"
        if link_target.exists() or link_target.is_symlink():
            link_target.unlink()
        link_target.symlink_to(local_path)
        created += 1
        print(f"   ✓ {eid} → {local_path}")
    print(f"\n   creados: {created} · omitidos por ruta inexistente: {skipped_missing}")
    return 0


def cmd_report(catalog: dict, user_cfg: dict) -> int:
    entries = flatten_entries(catalog)
    print(f"📚 BIBLIOTECA — reporte detallado\n")
    by_domain = {}
    for entry in entries:
        by_domain.setdefault(entry["_dominio"], []).append(entry)

    for dominio in sorted(by_domain.keys()):
        print(f"### {dominio}\n")
        for entry in sorted(by_domain[dominio], key=lambda x: x["id"]):
            eid = entry["id"]
            license_tag = entry.get("license", "?")
            status = entry.get("status", "?")
            license_emoji = {
                "public_domain": "🌍",
                "creative_commons": "🔓",
                "copyright": "🔒",
            }.get(license_tag, "❓")

            local_path_str = user_cfg.get(eid, "")
            local_path = Path(local_path_str).expanduser() if local_path_str else None
            local_status = "✓ local" if (local_path and local_path.exists()) else "—"

            print(f"  {license_emoji} {eid}")
            print(f"    Título: {entry['titulo']}")
            print(f"    Edición: {entry['edicion_vigente']}")
            print(f"    Status: {status}")
            print(f"    Cobertura local: {local_status}")
            if entry.get("doi"):
                print(f"    DOI: {entry['doi']}")
            elif entry.get("url_oficial"):
                print(f"    URL: {entry['url_oficial']}")
            print()
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Verifica cobertura (default)")
    group.add_argument("--link", action="store_true", help="Crea symlinks en library/local/")
    group.add_argument("--report", action="store_true", help="Reporte detallado del catálogo")
    args = parser.parse_args()

    catalog = load_catalog()
    user_cfg = load_user_config()

    if args.link:
        return cmd_link(catalog, user_cfg)
    elif args.report:
        return cmd_report(catalog, user_cfg)
    else:
        return cmd_check(catalog, user_cfg)


if __name__ == "__main__":
    sys.exit(main())
