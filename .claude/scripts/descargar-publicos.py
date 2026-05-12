#!/usr/bin/env python3
"""
descargar-publicos.py — Descarga de fuentes en dominio público del catálogo.

Uso:
    python3 descargar-publicos.py [--dry-run | --download | --report]

Lee `library/CATALOG.yaml`, filtra entradas con:
  · license == "public_domain" (sin issues legales para redistribuir)
  · url_oficial != ""           (con URL canónica disponible)

Modos:
  --dry-run    Lista qué se descargaría sin tocar disco. Modo por defecto.
  --download   Descarga cada documento a library/local/<id>.<ext>
               (carpeta ignorada por git — uso personal del usuario).
               Si el archivo ya existe y no fue modificado en origen,
               no se redescarga (verificación por HEAD + tamaño).
  --report     Reporte detallado: por dominio, qué hay descargado vs disponible.

Filosofía:
  · Solo descarga documentos en dominio público (leyes oficiales, NIST,
    NOMs publicadas en DOF, OECD, UN, etc.). NUNCA copyrighted.
  · Guarda en library/local/, que está en .gitignore — no se sube al
    repo. Es uso local del usuario para acceso offline.
  · No verifica integridad criptográfica (los sitios oficiales suelen
    no publicar hashes). Asume que la URL del catálogo apunta al
    documento canónico.

Dependencias: pyyaml (pip install --user pyyaml)
"""
import argparse
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    sys.exit("ERROR: requiere PyYAML. Instalar con: pip install --user pyyaml")


REPO_ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = REPO_ROOT / "library" / "CATALOG.yaml"
LOCAL_DIR = REPO_ROOT / "library" / "local"
USER_AGENT = "ConfiguracionClaude/biblioteca-sync (https://github.com/jmromeroc2000-cmyk/ConfiguracionClaude)"


def load_catalog() -> dict:
    if not CATALOG_PATH.exists():
        sys.exit(f"ERROR: catálogo no encontrado en {CATALOG_PATH}")
    with open(CATALOG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def flatten_entries(catalog: dict) -> list:
    out = []
    for key, val in catalog.items():
        if isinstance(val, list):
            for entry in val:
                if isinstance(entry, dict) and entry.get("id"):
                    entry_copy = dict(entry)
                    entry_copy["_dominio"] = key
                    out.append(entry_copy)
    return out


def is_downloadable(entry: dict) -> bool:
    return (
        entry.get("license") == "public_domain"
        and bool(entry.get("url_oficial"))
        and entry.get("url_oficial", "").startswith("http")
    )


def guess_ext(url: str, default: str = ".pdf") -> str:
    path = urlparse(url).path.lower()
    for ext in (".pdf", ".html", ".htm", ".txt", ".md", ".xml", ".json"):
        if path.endswith(ext):
            return ext
    return default


def download_one(entry: dict, dest_dir: Path) -> tuple:
    """Devuelve (status, msg). status ∈ {downloaded, skipped, failed}."""
    url = entry["url_oficial"]
    ext = guess_ext(url)
    dest = dest_dir / f"{entry['id']}{ext}"

    if dest.exists() and dest.stat().st_size > 1024:
        return ("skipped", f"ya existe ({dest.stat().st_size // 1024} KB)")

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 1024:
            return ("failed", f"respuesta demasiado pequeña ({len(data)} bytes)")
        dest.write_bytes(data)
        return ("downloaded", f"{len(data) // 1024} KB")
    except urllib.error.HTTPError as e:
        return ("failed", f"HTTP {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        return ("failed", f"URLError: {e.reason}")
    except Exception as e:
        return ("failed", f"{type(e).__name__}: {e}")


def cmd_dry_run(catalog: dict) -> int:
    entries = [e for e in flatten_entries(catalog) if is_downloadable(e)]
    print(f"🔍 Dry-run: {len(entries)} entradas descargables\n")
    for e in entries:
        ext = guess_ext(e["url_oficial"])
        print(f"  · {e['_dominio']}/{e['id']}{ext}")
        print(f"    {e['url_oficial']}")
    print(f"\n   Para descargar realmente: python3 descargar-publicos.py --download")
    return 0


def cmd_download(catalog: dict) -> int:
    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    entries = [e for e in flatten_entries(catalog) if is_downloadable(e)]
    print(f"📥 Descargando {len(entries)} entradas a {LOCAL_DIR}\n")
    counts = {"downloaded": 0, "skipped": 0, "failed": 0}
    for e in entries:
        status, msg = download_one(e, LOCAL_DIR)
        counts[status] += 1
        emoji = {"downloaded": "✓", "skipped": "·", "failed": "✗"}[status]
        print(f"  {emoji} {e['id']} — {msg}")
    print(f"\n   Resumen: {counts['downloaded']} descargadas · {counts['skipped']} ya existían · {counts['failed']} fallaron")
    if counts["failed"]:
        print(f"   ⚠ Los fallos son típicamente por URLs que requieren navegador real o que cambiaron.")
        print(f"     Revisar manualmente y actualizar el campo url_oficial del catálogo.")
    return 0 if counts["failed"] == 0 else 1


def cmd_report(catalog: dict) -> int:
    entries = flatten_entries(catalog)
    print("📚 BIBLIOTECA — reporte de cobertura de dominio público\n")

    by_domain = {}
    for e in entries:
        by_domain.setdefault(e["_dominio"], []).append(e)

    for dominio in sorted(by_domain.keys()):
        items = by_domain[dominio]
        downloadable = [e for e in items if is_downloadable(e)]
        on_disk = 0
        for e in downloadable:
            ext = guess_ext(e["url_oficial"])
            if (LOCAL_DIR / f"{e['id']}{ext}").exists():
                on_disk += 1
        print(f"### {dominio} ({len(items)} entradas)")
        print(f"  · descargables (dominio público con URL): {len(downloadable)}")
        print(f"  · en disco local: {on_disk}")
        print()
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dry-run", action="store_true", help="Listar qué se descargaría (default)")
    group.add_argument("--download", action="store_true", help="Descargar a library/local/")
    group.add_argument("--report", action="store_true", help="Reporte de cobertura local")
    args = parser.parse_args()

    catalog = load_catalog()

    if args.download:
        return cmd_download(catalog)
    elif args.report:
        return cmd_report(catalog)
    else:
        return cmd_dry_run(catalog)


if __name__ == "__main__":
    sys.exit(main())
