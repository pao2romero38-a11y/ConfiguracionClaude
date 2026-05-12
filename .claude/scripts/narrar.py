#!/usr/bin/env python3
"""
narrar.py — Generador de narración para episodios de la serie de capacitación.

Uso:
    python3 narrar.py <episodio.md> [output_dir]

Lee un episodio en formato Markdown con la estructura
"# === SCRIPT DE NARRACIÓN ===", extrae los bloques de narración,
respeta los marcadores [PAUSA Ns], y genera:

  · <output_dir>/<episodio>/bloque-NN.wav  (un wav por bloque)
  · <output_dir>/<episodio>-completo.wav   (todos los bloques concatenados)

Dependencias:
  · piper-tts (CLI) instalado vía pip
  · ffmpeg en PATH
  · Modelo de voz Piper en ~/.local/share/piper/voices/

Configuración (variables al inicio del script):
  · VOICE_PATH     ruta al modelo .onnx
  · LENGTH_SCALE   velocidad (1.0 default, 1.1 pedagógico, 1.15 pausado)
  · SENTENCE_SILENCE  silencio entre frases (s)
  · INTER_BLOCK_SILENCE  silencio entre bloques (s)
"""
import sys
import os
import re
import subprocess
import tempfile
from pathlib import Path

# === CONFIGURACIÓN ===
PIPER = os.path.expanduser("~/Library/Python/3.9/bin/piper")
VOICE_PATH = os.path.expanduser("~/.local/share/piper/voices/es_MX-claude-high.onnx")
LENGTH_SCALE = 1.08
SENTENCE_SILENCE = 0.35
INTER_BLOCK_SILENCE = 1.5
SAMPLE_RATE = 22050  # piper default; debe coincidir para concatenar sin reencoding

# === DICCIONARIO DE PRONUNCIACIÓN ===
# Términos de origen inglés que un mexicano profesional pronunciaría a la inglesa.
# Se aplican como reemplazo de texto ANTES de mandar a piper para que las
# fonéticas del TTS español produzcan un sonido cercano al inglés.
#
# Reglas:
#   · Solo entran términos cuya pronunciación natural en boca de un mexicano
#     profesional es claramente inglesa (Claude, GAAP, ROI, etc.).
#   · Acrónimos en español o asimilados al español NO entran (NIF, ISO, APA,
#     TIR, VPN, COSO, NIST, AMVO, PROFECO, INAI, COFECE, NOM, ...).
#   · Las claves se evalúan en orden; las primeras tienen prioridad.

PRONUNCIATION_FIXES_LITERAL = [
    # Compuestos primero (antes de que sus partes coincidan por separado)
    ("US GAAP",        "yú es gap"),
    ("GO/NO-GO",       "góu, nóu-góu"),
    ("e-commerce",     "i-cómers"),
    ("E-commerce",     "I-cómers"),
    ("/prompt",        "diagonal prompt"),
    ("/capacidad",     "diagonal capacidad"),
]

PRONUNCIATION_FIXES_WORD = {
    # Nombre del producto (clave del proyecto)
    "Claude":          "Clod",
    "claude":          "clod",

    # Estándares y métricas anglosajonas
    "GAAP":            "gap",
    "ROI":             "ar óu ai",
    "WACC":            "uak",
    "DCF":             "di si ef",
    "PMBOK":           "pimbok",
    "IFRS":            "ai ef ar es",

    # Anglicismos comunes en negocios y tech (pronunciados a la inglesa)
    "retail":          "rítel",
    "Retail":          "Rítel",
    "online":          "ónlain",
    "Online":          "Ónlain",
    "software":        "sóftuer",
    "Software":        "Sóftuer",
    "hardware":        "járduer",
    "Hardware":        "Járduer",
    "prompt":          "prómpt",
    "Prompt":          "Prómpt",
    "prompts":         "prómpts",
    "Prompts":         "Prómpts",
    "stack":           "stak",
    "Stack":           "Stak",
    "feedback":        "fídbak",
    "Feedback":        "Fídbak",

    # Nombres propios que aparecen en narración (autores de marcos)
    "Bloom":           "Blum",
    "Kirkpatrick":     "Kirk-pátrik",
    "Ausubel":         "Áu-su-bel",
    "Anderson":        "Ánder-son",
    "Krathwohl":       "Krát-vol",
    "Merrill":         "Mé-ril",
}


def apply_pronunciation_fixes(text: str) -> str:
    """Aplica el diccionario de pronunciación antes de mandar a piper."""
    # 1. Reemplazos literales (palabras con caracteres especiales como '/' o '-')
    for original, phonetic in PRONUNCIATION_FIXES_LITERAL:
        text = text.replace(original, phonetic)
    # 2. Reemplazos con límite de palabra (acrónimos y nombres simples)
    for original, phonetic in PRONUNCIATION_FIXES_WORD.items():
        pattern = r'\b' + re.escape(original) + r'\b'
        text = re.sub(pattern, phonetic, text)
    return text


def find_narration_section(md_text: str) -> str:
    """Localiza el bloque entre '=== SCRIPT DE NARRACIÓN ===' y el siguiente '===' o '#'."""
    pattern = r"# === SCRIPT DE NARRACIÓN ===(.*?)(?=^# ===|\Z)"
    m = re.search(pattern, md_text, re.DOTALL | re.MULTILINE)
    if not m:
        sys.exit("ERROR: no se encontró sección '# === SCRIPT DE NARRACIÓN ==='")
    return m.group(1)


def extract_blocks(narration_section: str) -> list[tuple[str, str]]:
    """Devuelve lista de (titulo_bloque, contenido_fence) en orden."""
    block_re = re.compile(
        r"##\s+(Bloque\s+\d+[^\n]*)\n+```\n(.*?)\n```",
        re.DOTALL,
    )
    return [(m.group(1).strip(), m.group(2)) for m in block_re.finditer(narration_section)]


def clean_and_split_by_pausas(fence_text: str) -> list[tuple[str, str]]:
    """
    Procesa el contenido del fence de un bloque.
    Devuelve lista de (tipo, valor) donde:
      · tipo='text'   → valor es texto limpio para piper
      · tipo='pausa'  → valor es duración en segundos (str)
    """
    # Quitar líneas que son solo markers de slide
    lines = []
    for line in fence_text.split("\n"):
        stripped = line.strip()
        # Eliminar marcadores que no contribuyen a la narración
        if stripped.startswith("[Slide ") or stripped == "[NARRACIÓN]":
            continue
        lines.append(line)
    text = "\n".join(lines)

    # Quitar marcadores [ÉNFASIS] y [/ÉNFASIS] (piper no soporta énfasis,
    # pero conservamos el texto entre ellos)
    text = text.replace("[ÉNFASIS]", "").replace("[/ÉNFASIS]", "")

    # Dividir por [PAUSA Ns]
    pause_re = re.compile(r"\[PAUSA\s+(\d+(?:\.\d+)?)s?\]", re.IGNORECASE)
    parts = []
    cursor = 0
    for m in pause_re.finditer(text):
        before = text[cursor:m.start()].strip()
        if before:
            parts.append(("text", before))
        parts.append(("pausa", m.group(1)))
        cursor = m.end()
    tail = text[cursor:].strip()
    if tail:
        parts.append(("text", tail))

    return parts


def normalize_text_for_piper(text: str) -> str:
    """Limpia el texto antes de mandarlo a piper: pronunciación, espacios, saltos."""
    text = apply_pronunciation_fixes(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def gen_piper(text: str, out_wav: Path) -> None:
    """Genera un WAV con piper para un texto dado."""
    cmd = [
        PIPER,
        "-m", VOICE_PATH,
        "--length-scale", str(LENGTH_SCALE),
        "--sentence-silence", str(SENTENCE_SILENCE),
        "-f", str(out_wav),
    ]
    proc = subprocess.run(
        cmd,
        input=text,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.exit(f"ERROR piper: {proc.stderr}")
    if not out_wav.exists() or out_wav.stat().st_size < 1000:
        sys.exit(f"ERROR: piper no generó audio válido para: {text[:60]}...")


def gen_silence(duration_s: float, out_wav: Path) -> None:
    """Genera un WAV de silencio de la duración pedida."""
    cmd = [
        "ffmpeg",
        "-y", "-loglevel", "error",
        "-f", "lavfi",
        "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
        "-t", str(duration_s),
        "-c:a", "pcm_s16le",
        str(out_wav),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"ERROR ffmpeg silencio: {proc.stderr}")


def concat_wavs(wavs: list[Path], out_wav: Path) -> None:
    """Concatena WAVs con ffmpeg usando el demuxer concat."""
    if not wavs:
        return
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for w in wavs:
            f.write(f"file '{w.resolve()}'\n")
        list_path = f.name
    try:
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "concat", "-safe", "0",
            "-i", list_path,
            "-c", "copy",
            str(out_wav),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            sys.exit(f"ERROR ffmpeg concat: {proc.stderr}")
    finally:
        os.unlink(list_path)


def process_block(parts: list[tuple[str, str]], block_dir: Path, block_num: int) -> Path:
    """Genera un WAV por bloque (concatenando segmentos de texto y silencios)."""
    block_dir.mkdir(parents=True, exist_ok=True)
    segments = []
    seg_idx = 0
    for kind, value in parts:
        seg_idx += 1
        seg_wav = block_dir / f"_seg-{seg_idx:02d}.wav"
        if kind == "text":
            text = normalize_text_for_piper(value)
            if not text:
                continue
            gen_piper(text, seg_wav)
        elif kind == "pausa":
            gen_silence(float(value), seg_wav)
        segments.append(seg_wav)

    block_wav = block_dir / f"bloque-{block_num:02d}.wav"
    concat_wavs(segments, block_wav)

    # Limpiar segmentos temporales
    for s in segments:
        s.unlink(missing_ok=True)

    return block_wav


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: narrar.py <episodio.md> [output_dir]")

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        sys.exit(f"ERROR: no existe {md_path}")

    default_out = md_path.parent / "audio" / md_path.stem
    out_dir = Path(sys.argv[2]) if len(sys.argv) >= 3 else default_out
    out_dir.mkdir(parents=True, exist_ok=True)

    text = md_path.read_text(encoding="utf-8")
    narration = find_narration_section(text)
    blocks = extract_blocks(narration)

    if not blocks:
        sys.exit("ERROR: no se encontraron '## Bloque N' en la sección de narración.")

    print(f"[narrar] {md_path.name}  →  {len(blocks)} bloques")
    print(f"[narrar] voz: {Path(VOICE_PATH).name} · length={LENGTH_SCALE} · silencio_frase={SENTENCE_SILENCE}s")
    print(f"[narrar] salida: {out_dir}")

    block_wavs = []
    for i, (title, content) in enumerate(blocks, start=1):
        parts = clean_and_split_by_pausas(content)
        bw = process_block(parts, out_dir, i)
        size_kb = bw.stat().st_size // 1024
        print(f"  ✓ Bloque {i:02d}: {title} → {bw.name} ({size_kb} KB)")
        block_wavs.append(bw)

    # Concatenar todos los bloques con silencio entre ellos
    inter_silence = out_dir / "_inter.wav"
    gen_silence(INTER_BLOCK_SILENCE, inter_silence)
    full_sequence = []
    for i, bw in enumerate(block_wavs):
        full_sequence.append(bw)
        if i < len(block_wavs) - 1:
            full_sequence.append(inter_silence)

    full_wav = out_dir.parent / f"{md_path.stem}-completo.wav"
    concat_wavs(full_sequence, full_wav)
    inter_silence.unlink(missing_ok=True)

    # Duración total estimada
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(full_wav)],
        capture_output=True, text=True,
    )
    if probe.returncode == 0:
        duration = float(probe.stdout.strip())
        mins = int(duration // 60)
        secs = int(duration % 60)
        size_mb = full_wav.stat().st_size / (1024 * 1024)
        print(f"\n[narrar] ✓ Episodio completo: {full_wav.name}")
        print(f"         Duración: {mins}:{secs:02d}  ·  Tamaño: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
