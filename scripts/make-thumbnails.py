#!/usr/bin/env python3
"""Shrink the site's pictures after Jekyll has built it.

Runs on the finished site folder (default: _site), never on the originals.
For every .jpg/.jpeg/.png under assets/ it:
  1. makes a small copy named <name>-thumb.jpg (longest side 800 px) for
     galleries and grids, and
  2. shrinks the full-size picture itself if its longest side is over 2000 px.

If a picture is missing its thumbnail, pages fall back to the full picture,
so a failure here never breaks the site.  Needs: pip install pillow
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

THUMB_PX = 800
FULL_PX = 2000
SKIP_DIRS = {"icons"}
EXTS = {".jpg", ".jpeg", ".png"}


def flatten(im):
    """Thumbnails are JPEG, which has no transparency: put them on white."""
    if im.mode in ("RGBA", "LA") or "transparency" in im.info:
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site") / "assets"
    if not root.is_dir():
        sys.exit(f"No assets folder at {root}")

    made = shrunk = 0
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in EXTS or path.stem.endswith("-thumb"):
            continue
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        try:
            with Image.open(path) as im:
                im = ImageOps.exif_transpose(im)
                original_size = path.stat().st_size

                thumb = flatten(im)
                thumb.thumbnail((THUMB_PX, THUMB_PX), Image.LANCZOS)
                thumb.save(path.with_name(path.stem + "-thumb.jpg"),
                           "JPEG", quality=82, optimize=True, progressive=True)
                made += 1

                if max(im.size) > FULL_PX:
                    full = im.copy()
                    full.thumbnail((FULL_PX, FULL_PX), Image.LANCZOS)
                    tmp = path.with_name(path.name + ".tmp")
                    if path.suffix.lower() == ".png":
                        full.save(tmp, "PNG", optimize=True)
                    else:
                        flatten(full).save(tmp, "JPEG", quality=85,
                                           optimize=True, progressive=True)
                    # Keep the new file only if it really is smaller
                    if tmp.stat().st_size < original_size:
                        tmp.replace(path)
                        shrunk += 1
                        print(f"shrunk {path.relative_to(root)}: "
                              f"{original_size // 1024} KB -> {path.stat().st_size // 1024} KB")
                    else:
                        tmp.unlink()
        except Exception as err:  # one bad file must not stop the rest
            print(f"::warning::Could not process {path}: {err}")

    print(f"Thumbnails made: {made}; full-size pictures shrunk: {shrunk}")


if __name__ == "__main__":
    main()
