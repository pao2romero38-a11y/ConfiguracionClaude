#!/usr/bin/env python3
"""
slides.py — Generador de slides para episodios de la serie de capacitación.

Uso:
    python3 slides.py <episodio.md>

Lee el episodio y genera:
  · slides-render/<episodio>/slide-NN.png     (un PNG por slide, 1280x720)
  · slides-render/<episodio>/timing.json      (timing slide-by-slide)

Mejoras v2:
  · Diseño editorial cream + acento cálido (radical change vs v1 dark sober)
  · Slide número en margen inferior derecho como "Nº NN / TT"
  · Cada slide muestra el [ÉNFASIS] del bloque de narración correspondiente
    (extraído automáticamente parseando los marcadores [Slide N — ...])
  · Slide final de "Conclusiones" sintetizado por episodio
  · Soporte a HTML directo dentro del título para slides especiales
    (e.g., "Comparativa lado a lado" → dos columnas)

Dependencias: marp-cli (npm install -g @marp-team/marp-cli)
"""
import sys
import os
import re
import json
import subprocess
import html
from pathlib import Path

MARP = "marp"


# === DISEÑO VISUAL — tema editorial cream con acento cálido ===
MARP_FRONTMATTER = """---
marp: true
size: 16:9
paginate: false
backgroundColor: "#f7f3ed"
color: "#1c1917"
style: |
  section {
    background: linear-gradient(135deg, #f7f3ed 0%, #ede4d3 100%);
    padding: 70px 90px 90px 90px;
    font-family: -apple-system, "Helvetica Neue", "Segoe UI", system-ui, sans-serif;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section .eyebrow {
    position: absolute;
    top: 38px;
    left: 60px;
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 16px;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: #c8553d;
    font-weight: 600;
  }
  section h1.title {
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 52px;
    font-weight: 700;
    color: #1c1917;
    margin: 0 0 28px 0;
    line-height: 1.18;
    max-width: 1050px;
  }
  section .enfasis {
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 26px;
    font-style: italic;
    color: #57534e;
    border-left: 4px solid #c8553d;
    padding: 6px 0 6px 24px;
    line-height: 1.45;
    margin-top: 14px;
    max-width: 950px;
  }
  section .visual-note {
    position: absolute;
    bottom: 38px;
    left: 90px;
    font-size: 13px;
    color: #a8a29e;
    font-style: italic;
    max-width: 60%;
  }
  section .slide-num {
    position: absolute;
    bottom: 38px;
    right: 60px;
    font-family: "Georgia", serif;
    font-size: 16px;
    color: #c8553d;
    font-variant-numeric: tabular-nums;
    letter-spacing: 1px;
  }
  /* Comparativa lado a lado */
  section .comparativa {
    display: flex;
    gap: 40px;
    width: 100%;
    margin-top: 20px;
  }
  section .comparativa > div {
    flex: 1;
    padding: 28px;
    border-radius: 12px;
  }
  section .comparativa .izq {
    background: #fef3e2;
    border: 1px solid #f5d4a7;
  }
  section .comparativa .der {
    background: #fff;
    border: 2px solid #c8553d;
    box-shadow: 0 6px 20px rgba(200, 85, 61, 0.15);
  }
  section .comparativa h3 {
    font-family: "Georgia", serif;
    font-size: 22px;
    margin: 0 0 14px 0;
  }
  section .comparativa .izq h3 { color: #92704a; }
  section .comparativa .der h3 { color: #c8553d; }
  section .comparativa p {
    font-size: 16px;
    line-height: 1.5;
    margin: 0;
  }
  /* Conclusiones — mismo tema cream, énfasis con borde superior y bullets oscuros */
  section.conclusiones {
    border-top: 8px solid #c8553d;
  }
  section.conclusiones ul {
    list-style: none;
    padding: 0;
    margin: 20px 0 0 0;
    max-width: 1050px;
  }
  section.conclusiones ul li {
    font-family: -apple-system, sans-serif;
    font-size: 28px;
    padding: 18px 0 18px 56px;
    position: relative;
    line-height: 1.42;
    color: #1c1917;
    border-bottom: 1px solid #e8dec9;
  }
  section.conclusiones ul li:last-child {
    border-bottom: none;
  }
  section.conclusiones ul li::before {
    content: counter(li);
    counter-increment: li;
    position: absolute;
    left: 0;
    top: 18px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #c8553d;
    color: #f7f3ed;
    font-family: "Georgia", serif;
    font-size: 18px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  section.conclusiones ul {
    counter-reset: li;
  }
---
"""


# === CONCLUSIONES POR EPISODIO ===
# Sintetizadas a partir del contenido del episodio. Cada slide cierra
# con 3 takeaways en orden de relevancia para el espectador.
CONCLUSIONES_POR_EPISODIO = {
    "episodio-0-por-que-configurar": {
        "eyebrow": "Conclusiones · Episodio 0",
        "title": "Lo que detectaste hoy",
        "bullets": [
            "Una respuesta correcta NO siempre es defendible.",
            "Las dimensiones que suelen faltar: datos · fuentes · estructura · reglas de dominio.",
            "Siguiente: el protocolo de 4 pasos — mayor impacto, menor esfuerzo.",
        ],
    },
    "episodio-1-protocolo-4-pasos": {
        "eyebrow": "Conclusiones · Episodio 1",
        "title": "Tu primer reflejo de calidad",
        "bullets": [
            "Verificación · Coherencia · Fuentes · Presentación — en ese orden.",
            "[⚠ verificar] se trata como obligación, no como decoración.",
            "Siguiente: estructura general → particular + APA 7.",
        ],
    },
    "episodio-2-estructura-y-apa7": {
        "eyebrow": "Conclusiones · Episodio 2",
        "title": "Forma + fondo = respuesta defendible",
        "bullets": [
            "5 niveles: panorama → categorías → detalle → ejemplo → fuentes.",
            "APA 7: referencias ordenadas más reciente → más antigua.",
            "Siguiente: modos expertos — un especialista por tema.",
        ],
    },
    "episodio-3-modos-expertos": {
        "eyebrow": "Conclusiones · Episodio 3",
        "title": "Ya no le hablas al médico general",
        "bullets": [
            "17 modos pre-construidos + composición líder + apoyo.",
            "Diseñaste el esqueleto de tu modo personalizado.",
            "Siguiente: /prompt para afinar lo que TÚ preguntas.",
        ],
    },
    "episodio-4-prompt": {
        "eyebrow": "Conclusiones · Episodio 4",
        "title": "La palanca con más impacto eres tú",
        "bullets": [
            "Rúbrica de 10 dimensiones cubre lo que un prompt vago omite.",
            "Tu sesgo personal: las 2-3 dimensiones que sueles olvidar.",
            "Siguiente: /capacidad para expandir las herramientas.",
        ],
    },
    "episodio-5-capacidad": {
        "eyebrow": "Conclusiones · Episodio 5",
        "title": "El techo de Claude se puede mover",
        "bullets": [
            "Scripts → CLIs → MCP → APIs, ordenados por costo creciente.",
            "Bajar al nivel más barato que cumpla calidad aceptable.",
            "Siguiente: el meta-proceso que conecta todo lo aprendido.",
        ],
    },
    "episodio-6-meta-proceso": {
        "eyebrow": "Conclusiones · Episodio 6 · Cierre de serie",
        "title": "Lo que sigue lo escribes tú",
        "bullets": [
            "5 fases: NOTAR · CONVERSAR · DECIDIR · IMPLEMENTAR · VERSIONAR.",
            "El ciclo no tiene techo — cada mejora abre la siguiente.",
            "Tu compromiso: una mejora concreta a tu configuración, en 7 días.",
        ],
    },
}


# === PARSING DEL EPISODIO ===

def find_section(md_text: str, section_header: str) -> str:
    """Devuelve el contenido entre '# === <section_header> ===' y el siguiente '# ==='."""
    pattern = rf"# === {re.escape(section_header)} ===(.*?)(?=^# ===|\Z)"
    m = re.search(pattern, md_text, re.DOTALL | re.MULTILINE)
    if not m:
        return ""
    return m.group(1)


def extract_episode_title(md_text: str) -> str:
    """Extrae el 'titulo' del frontmatter YAML del episodio."""
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", md_text, re.DOTALL)
    if not fm_match:
        return ""
    fm = fm_match.group(1)
    titulo_match = re.search(r'^titulo:\s*"([^"]+)"', fm, re.MULTILINE)
    if titulo_match:
        return titulo_match.group(1)
    # Fallback: sin comillas
    titulo_match = re.search(r"^titulo:\s*(.+)$", fm, re.MULTILINE)
    if titulo_match:
        return titulo_match.group(1).strip()
    return ""


def parse_time(t: str) -> int:
    """'1:30' → 90 s · '0:30' → 30 s."""
    t = t.strip()
    if ":" in t:
        mins, secs = t.split(":")
        return int(mins) * 60 + int(secs)
    return int(t)


def parse_slide_table(section: str) -> "list[dict]":
    """Tabla markdown | # | Título | Visual | Duración |."""
    slides = []
    rows = re.findall(r"^\|(.+)\|\s*$", section, re.MULTILINE)
    for row_raw in rows:
        cells = [c.strip() for c in row_raw.split("|")]
        if not cells or not cells[0]:
            continue
        if cells[0].strip() == "#":
            continue
        if all(re.match(r"^[-:|\s]*$", c) for c in cells):
            continue
        if len(cells) < 4:
            continue
        num_raw = cells[0].strip()
        if not num_raw.isdigit():
            continue
        num = int(num_raw)
        text = cells[1].strip().strip('"').strip()
        visual = cells[2].strip()
        duration_range = cells[3].strip()
        m = re.match(r"(\d+:\d+)\s*[—\-]\s*(\d+:\d+)", duration_range)
        if not m:
            continue
        start = parse_time(m.group(1))
        end = parse_time(m.group(2))
        slides.append({
            "num": num,
            "text": text,
            "visual": visual,
            "start": start,
            "end": end,
            "duration": end - start,
        })
    return slides


def parse_enfasis_per_slide(narration_section: str) -> "dict[int, str]":
    """
    Recorre la narración secuencialmente:
      · Cuando ve [Slide N — ...], cambia el slide actual a N.
      · Cuando ve [ÉNFASIS]...[/ÉNFASIS], asocia ese énfasis al slide actual.
    Devuelve dict {slide_num: enfasis_text}.
    """
    out = {}
    current_slide = None
    # Patrón que captura ambos tipos de marcador en orden de aparición
    pattern = re.compile(
        r"\[Slide\s+(\d+)[^\]]*\]"               # [Slide N — ...]
        r"|"
        r"\[ÉNFASIS\](.*?)\[/ÉNFASIS\]",         # [ÉNFASIS]...[/ÉNFASIS]
        re.DOTALL,
    )
    for m in pattern.finditer(narration_section):
        if m.group(1):  # [Slide N]
            current_slide = int(m.group(1))
        elif m.group(2) and current_slide is not None:  # [ÉNFASIS]...[/ÉNFASIS]
            enfasis = " ".join(m.group(2).split())  # collapse whitespace
            # Si ya hay énfasis para este slide, no sobrescribir (toma el primero)
            if current_slide not in out:
                out[current_slide] = enfasis
    return out


# === RENDER MARP ===

def escape_html(s: str) -> str:
    return html.escape(s, quote=True)


def build_slide_html(slide: dict, slide_idx: int, total: int,
                     episode_title: str, enfasis: "str | None") -> str:
    """Construye el bloque markdown/HTML de un slide individual."""
    n = slide["num"]
    text = escape_html(slide["text"])
    visual = escape_html(slide["visual"])

    # Detectar slide especial: comparativa lado a lado
    is_comparativa = "comparativa" in slide["text"].lower() or "lado a lado" in slide["text"].lower()

    parts = [f'<div class="eyebrow">{escape_html(episode_title)}</div>']
    parts.append(f'<h1 class="title">{text}</h1>')

    if is_comparativa:
        parts.append("""
<div class="comparativa">
  <div class="izq">
    <h3>Claude por defecto</h3>
    <p>Texto correcto pero genérico, sin datos verificables, sin fuentes, sin marco normativo, sin reglas del dominio.</p>
  </div>
  <div class="der">
    <h3>Claude configurado</h3>
    <p>Datos verificables, fuentes en APA 7, marco normativo aplicable, advertencia obligatoria, estructura general → particular.</p>
  </div>
</div>
""".strip())

    if enfasis:
        parts.append(f'<div class="enfasis">{escape_html(enfasis)}</div>')

    parts.append(f'<div class="visual-note">{visual}</div>')
    parts.append(f'<div class="slide-num">{n:02d}</div>')

    return "\n\n".join(parts)


def build_conclusiones_slide(episode_slug: str, episode_title: str, slide_num: int) -> "str | None":
    """Construye el slide final de conclusiones para el episodio. None si no hay entrada."""
    conc = CONCLUSIONES_POR_EPISODIO.get(episode_slug)
    if not conc:
        return None
    if not conc.get("bullets"):
        return None
    bullets_html = "\n".join(
        f"<li>{escape_html(b)}</li>" for b in conc["bullets"]
    )
    return f"""
<div class="eyebrow">{escape_html(episode_title)} · Conclusiones</div>

<h1 class="title">{escape_html(conc['title'])}</h1>

<ul>
{bullets_html}
</ul>

<div class="slide-num">{slide_num:02d}</div>
""".strip()


def build_marp_markdown(slides: "list[dict]", enfasis_map: "dict[int, str]",
                       episode_slug: str, episode_title: str) -> str:
    """Construye el markdown Marp con un slide por entrada + conclusiones (si aplica)."""
    has_conc = episode_slug in CONCLUSIONES_POR_EPISODIO and \
               bool(CONCLUSIONES_POR_EPISODIO[episode_slug].get("bullets"))
    total = len(slides) + (1 if has_conc else 0)
    md = MARP_FRONTMATTER

    for i, slide in enumerate(slides):
        enf = enfasis_map.get(slide["num"])
        md += "\n\n"
        md += build_slide_html(slide, i, total, episode_title, enf)
        md += "\n\n---"

    if has_conc:
        conc_html = build_conclusiones_slide(episode_slug, episode_title, total)
        if conc_html:
            md += "\n\n<!-- _class: conclusiones -->\n\n"
            md += conc_html
            md += "\n"
        else:
            md = md.rstrip("-").rstrip()
    else:
        md = md.rstrip("-").rstrip()

    return md


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: slides.py <episodio.md>")

    md_path = Path(sys.argv[1]).resolve()
    if not md_path.exists():
        sys.exit(f"ERROR: no existe {md_path}")

    text = md_path.read_text(encoding="utf-8")

    episode_title = extract_episode_title(text) or md_path.stem

    slides_section = find_section(text, "ESTRUCTURA DE SLIDES")
    if not slides_section:
        sys.exit("ERROR: sin sección '# === ESTRUCTURA DE SLIDES ==='")
    slides = parse_slide_table(slides_section)
    if not slides:
        sys.exit("ERROR: tabla de slides vacía")

    narration_section = find_section(text, "SCRIPT DE NARRACIÓN")
    enfasis_map = parse_enfasis_per_slide(narration_section)

    out_dir = md_path.parent / "slides-render" / md_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    has_conc = (
        md_path.stem in CONCLUSIONES_POR_EPISODIO
        and bool(CONCLUSIONES_POR_EPISODIO[md_path.stem].get("bullets"))
    )
    total_slides = len(slides) + (1 if has_conc else 0)
    print(f"[slides] {md_path.name} → {total_slides} slides "
          f"({len(slides)} del markdown + {'1 conclusiones' if has_conc else '0 conclusiones'})")
    print(f"[slides] título del episodio: {episode_title}")

    marp_md = build_marp_markdown(slides, enfasis_map, md_path.stem, episode_title)
    marp_input = out_dir / "_input.md"
    marp_input.write_text(marp_md, encoding="utf-8")

    output_pattern = out_dir / "slide.png"
    # Limpiar pngs anteriores
    for p in out_dir.glob("slide.*.png"):
        p.unlink()
    for p in out_dir.glob("slide-*.png"):
        p.unlink()

    result = subprocess.run(
        [MARP, str(marp_input), "--images", "png", "-o", str(output_pattern),
         "--allow-local-files"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(f"ERROR marp: {result.returncode}")

    # Renombrar slide.NNN.png → slide-NN.png
    for i in range(1, total_slides + 1):
        old = out_dir / f"slide.{i:03d}.png"
        new = out_dir / f"slide-{i:02d}.png"
        if old.exists():
            if new.exists():
                new.unlink()
            old.rename(new)
            size_kb = new.stat().st_size // 1024
            if i <= len(slides):
                preview = slides[i - 1]["text"][:55]
            else:
                preview = "[Conclusiones]"
            print(f"  ✓ slide-{i:02d}.png ({size_kb} KB) {preview}")

    marp_input.unlink(missing_ok=True)

    # timing.json — incluye conclusiones con duración estándar (8s al final)
    timing_slides = []
    for s in slides:
        timing_slides.append({
            "num": s["num"],
            "file": f"slide-{s['num']:02d}.png",
            "start": s["start"],
            "end": s["end"],
            "duration": s["duration"],
            "text": s["text"],
        })

    if has_conc:
        last_end = slides[-1]["end"]
        conc_duration = 8
        timing_slides.append({
            "num": total_slides,
            "file": f"slide-{total_slides:02d}.png",
            "start": last_end,
            "end": last_end + conc_duration,
            "duration": conc_duration,
            "text": "[Conclusiones]",
            "is_conclusiones": True,
        })

    timing = {
        "episode": md_path.stem,
        "total_duration": timing_slides[-1]["end"],
        "audio_duration_target": slides[-1]["end"],   # tiempo del audio (sin conclusiones)
        "has_conclusiones": has_conc,
        "slides": timing_slides,
    }
    timing_path = out_dir / "timing.json"
    timing_path.write_text(
        json.dumps(timing, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n[slides] timing.json escrito · audio target = {timing['audio_duration_target']}s · "
          f"total con conclusiones = {timing['total_duration']}s")


if __name__ == "__main__":
    main()
