#!/usr/bin/env python3
"""
componer.py — Compone video sincronizado audio + slides.

Uso:
    python3 componer.py <episodio.md>

Toma:
  · audio/<episodio>-completo.wav         (de narrar.py)
  · slides-render/<episodio>/slide-NN.png (de slides.py)
  · slides-render/<episodio>/timing.json  (timing con audio_duration_target y conclusiones)

Produce:
  · video/<episodio>.mp4    (1280x720, H.264 + AAC, slides sincronizados al audio)

Invariantes:
  · Todos los slides excepto el de Conclusiones se escalan PROPORCIONALMENTE
    para que la suma de sus duraciones iguale exactamente la duración real
    del audio. Esto elimina el "último slide absorbe residual" y produce
    sincronía visualmente correcta.
  · El slide de Conclusiones (si existe) se añade DESPUÉS del audio,
    extendiendo la duración total del video en 8 segundos.
  · Si la duración de audio difiere >10 % de las duraciones declaradas en
    el markdown, error explícito: el markdown debe corregirse.
"""
import sys
import os
import json
import subprocess
import tempfile
from pathlib import Path

WIDTH = 1280
HEIGHT = 720
FPS = 30
TOLERANCE_HARD = 0.30   # 30% — error si supera (audio vs declarado).
                        # El escalado proporcional absorbe diferencias menores;
                        # solo bloqueamos en desajustes catastróficos.


def get_audio_duration(wav: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(wav)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"ERROR ffprobe: {result.stderr}")
    return float(result.stdout.strip())


def render_slide_segment(png: Path, duration: float, out_mp4: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-i", str(png),
        "-t", f"{duration:.3f}",
        "-c:v", "libx264", "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-vf",
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease,"
        f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:black",
        "-r", str(FPS),
        str(out_mp4),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"ERROR ffmpeg slide segment ({png.name}): {proc.stderr}")


def concat_video_segments(segments: "list[Path]", out_mp4: Path) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for s in segments:
            f.write(f"file '{s.resolve()}'\n")
        list_path = f.name
    try:
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "concat", "-safe", "0",
            "-i", list_path,
            "-c", "copy",
            str(out_mp4),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            sys.exit(f"ERROR ffmpeg concat: {proc.stderr}")
    finally:
        os.unlink(list_path)


def generate_silence(duration_s: float, out_wav: Path) -> None:
    """Genera un WAV de silencio para extender el audio durante el slide de Conclusiones."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "lavfi",
        "-i", f"anullsrc=r=22050:cl=mono",
        "-t", str(duration_s),
        "-c:a", "pcm_s16le",
        str(out_wav),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"ERROR ffmpeg silencio: {proc.stderr}")


def concat_audio(audios: "list[Path]", out_wav: Path) -> None:
    """Concatena WAVs."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for a in audios:
            f.write(f"file '{a.resolve()}'\n")
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
            sys.exit(f"ERROR ffmpeg concat audio: {proc.stderr}")
    finally:
        os.unlink(list_path)


def mux_audio_video(video: Path, audio: Path, out_mp4: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video),
        "-i", str(audio),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "128k",
        str(out_mp4),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"ERROR ffmpeg mux: {proc.stderr}")


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: componer.py <episodio.md>")

    md_path = Path(sys.argv[1]).resolve()
    serie_dir = md_path.parent
    audio_wav = serie_dir / "audio" / f"{md_path.stem}-completo.wav"
    slides_dir = serie_dir / "slides-render" / md_path.stem
    timing_path = slides_dir / "timing.json"

    if not audio_wav.exists():
        sys.exit(f"ERROR: falta audio {audio_wav} — correr narrar.py primero.")
    if not timing_path.exists():
        sys.exit(f"ERROR: falta timing {timing_path} — correr slides.py primero.")

    timing = json.loads(timing_path.read_text(encoding="utf-8"))
    audio_dur = get_audio_duration(audio_wav)
    declared_audio = timing.get("audio_duration_target", timing["total_duration"])
    has_conclusiones = timing.get("has_conclusiones", False)

    print(f"[componer] {md_path.stem}")
    print(f"  audio real: {audio_dur:.2f}s  ·  declarado en markdown: {declared_audio}s")

    diff_pct = abs(audio_dur - declared_audio) / max(audio_dur, declared_audio)
    print(f"  desviación: {diff_pct*100:.2f}%")
    if diff_pct > TOLERANCE_HARD:
        sys.exit(
            f"ERROR: desviación > {TOLERANCE_HARD*100:.0f}% entre audio y declaración. "
            f"Corregir las duraciones en la tabla de slides del markdown."
        )

    # Separar slides de contenido (escalables) del slide de conclusiones (duración fija)
    content_slides = [s for s in timing["slides"] if not s.get("is_conclusiones")]
    conc_slide = next((s for s in timing["slides"] if s.get("is_conclusiones")), None)

    # Escalado proporcional: cada slide se estira/encoge para que la suma calce con audio_dur
    declared_total_content = sum(s["duration"] for s in content_slides)
    scale = audio_dur / declared_total_content if declared_total_content > 0 else 1.0
    print(f"  escalado proporcional: ×{scale:.4f}")

    scaled_durations = []
    cumulative = 0.0
    for i, s in enumerate(content_slides):
        if i < len(content_slides) - 1:
            d = s["duration"] * scale
        else:
            # último slide de contenido absorbe rounding error mínimo
            d = audio_dur - cumulative
        scaled_durations.append(d)
        cumulative += d

    # Componer segmentos de video
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        segments = []
        for i, (s, d) in enumerate(zip(content_slides, scaled_durations)):
            png = slides_dir / s["file"]
            if not png.exists():
                sys.exit(f"ERROR: falta slide {png}")
            seg = tmp_dir / f"seg-{i:02d}.mp4"
            render_slide_segment(png, d, seg)
            segments.append(seg)
            preview = s["text"][:48] + ("…" if len(s["text"]) > 48 else "")
            print(f"  ✓ slide {s['num']:02d}  declarado={s['duration']:5.1f}s → real={d:5.2f}s  {preview}")

        # Slide de conclusiones (si existe) — duración fija, va después del audio
        if conc_slide:
            png = slides_dir / conc_slide["file"]
            if not png.exists():
                sys.exit(f"ERROR: falta slide conclusiones {png}")
            seg = tmp_dir / f"seg-conc.mp4"
            render_slide_segment(png, conc_slide["duration"], seg)
            segments.append(seg)
            print(f"  ✓ slide {conc_slide['num']:02d}  [Conclusiones]  {conc_slide['duration']:.1f}s "
                  f"(después del audio)")

        # Concatenar video
        concat_path = tmp_dir / "concat.mp4"
        concat_video_segments(segments, concat_path)

        # Construir audio extendido (audio real + silencio para conclusiones si aplica)
        if conc_slide:
            silence_path = tmp_dir / "silence.wav"
            generate_silence(conc_slide["duration"], silence_path)
            extended_audio = tmp_dir / "extended.wav"
            concat_audio([audio_wav, silence_path], extended_audio)
            audio_to_mux = extended_audio
        else:
            audio_to_mux = audio_wav

        out_dir = serie_dir / "video"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_mp4 = out_dir / f"{md_path.stem}.mp4"
        mux_audio_video(concat_path, audio_to_mux, out_mp4)

    final_dur = get_audio_duration(out_mp4)
    size_mb = out_mp4.stat().st_size / (1024 * 1024)
    print(f"\n[componer] ✓ {out_mp4.name}")
    print(f"           dur={final_dur:.2f}s · size={size_mb:.1f} MB · {WIDTH}x{HEIGHT} @ {FPS}fps")


if __name__ == "__main__":
    main()
