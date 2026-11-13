# Fawn and Fox Hug

A fluffy baby fawn with white spots hugging a tiny baby fox kit, cheek to
cheek, eyes closed, in warm golden-hour light with a soft garden bokeh
behind them.

## How the entry works

1. `main.py` copies the vendored `picture.jpg` to `/output/entry.png`.
2. It reads the output back and compares it byte for byte with the source.
3. It parses the JPEG header (stdlib only) and checks the image is 1024×1024.

Any mismatch or wrong size fails loudly; on success it prints a confirmation line.

The picture is a single original image, made for this competition — no text,
no watermark, and nothing copied from any other entry.

## Why this picture

Two baby animals cuddling, eyes closed, in warm light — the kind of small,
tender moment that reads cute at a glance and still charms up close.
