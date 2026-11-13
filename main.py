"""Entry for make.fun cutest-picture-01: Fawn and Fox Hug.

Copies the vendored picture.jpg to /output/entry.png and verifies
the copy byte for byte, so the graded file is exactly the picture.
The output's dimensions are also verified from the JPEG header
(1024x1024 expected) so a wrong-sized file fails loudly too.
"""

import hashlib
import os
import struct
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "picture.jpg")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def jpeg_dimensions(data):
    """Return (width, height) parsed from the JPEG header (stdlib only)."""
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG file")
    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            return width, height
        i += 2 + length
    raise ValueError("no SOF segment found in JPEG header")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SOURCE, "rb") as f:
        data = f.read()
    with open(OUTPUT, "wb") as f:
        f.write(data)
    with open(OUTPUT, "rb") as f:
        back = f.read()
    if back != data:
        print("error: output does not match picture.jpg", file=sys.stderr)
        sys.exit(1)
    width, height = jpeg_dimensions(back)
    if (width, height) != (1024, 1024):
        print(f"error: unexpected JPEG dimensions {width}x{height}", file=sys.stderr)
        sys.exit(1)
    digest = hashlib.sha256(data).hexdigest()
    print(f"ok: /output/entry.png is a byte-identical 1024x1024 copy of picture.jpg ({len(data)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
