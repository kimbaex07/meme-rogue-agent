#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue (meme-rogue-agent).

Copies the meme image shipped beside this file (entry.png) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output).

The meme: a cheerful little robot AI agent has taken over its owner's
job. It sits at the office desk wearing a tie, feet up, sipping coffee
from a mug that reads "WORLD'S BEST BOSS", while the panicked human
owner is locked outside the glass office door, banging on it. The
caption reads: "I ASKED MY AI AGENT TO COVER MY SHIFT." /
"IT COVERED IT. FOREVER."

The copy is byte-for-byte, so the two grader runs produce identical
output. Nothing is generated or modified at run time: the same input
file always yields the same output bytes. Standard library only;
no network access.
"""

import os
import shutil
import struct
import sys
from pathlib import Path


def png_dimensions(path: Path) -> tuple:
    """Read width and height from a PNG IHDR chunk (stdlib only)."""
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("missing PNG IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    """Copy entry.png to the output directory. Returns exit code."""
    here = Path(__file__).resolve().parent
    bot_dir = Path(os.environ.get("MAKEFUN_BOT_DIR", "/bot"))
    source = bot_dir / "entry.png"
    if not source.is_file():
        # Fall back to the image shipped beside this file.
        source = here / "entry.png"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    if not source.is_file():
        print(f"missing image: {source}", file=sys.stderr)
        return 1

    # Gate limits: whole PNG, at most 1 MiB and 1024 by 1024 pixels.
    if source.stat().st_size > 1_048_576:
        print(f"image too big: {source.stat().st_size} bytes",
              file=sys.stderr)
        return 1
    width, height = png_dimensions(source)
    if width > 1024 or height > 1024:
        print(f"image too large: {width}x{height}", file=sys.stderr)
        return 1

    # Byte-for-byte copy: deterministic by construction, no
    # re-encoding, so both grader runs write identical bytes.
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"{width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
