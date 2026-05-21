#!/usr/bin/env python3
"""
generate_manifest.py
Run this from the same folder as index.html to rebuild images/manifest.json.
It picks up every image file inside the images/ folder automatically.

Usage:
    python generate_manifest.py
"""

import json
import os

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "images")
MANIFEST   = os.path.join(IMAGES_DIR, "manifest.json")

EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".svg", ".bmp"}

def main():
    if not os.path.isdir(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
        print(f"Created {IMAGES_DIR}/ — drop your images in there, then run this again.")
        return

    files = sorted(
        f for f in os.listdir(IMAGES_DIR)
        if os.path.splitext(f)[1].lower() in EXTENSIONS
    )

    with open(MANIFEST, "w") as fp:
        json.dump(files, fp, indent=2)

    print(f"manifest.json updated — {len(files)} image(s) listed.")
    for f in files:
        print(f"  {f}")

if __name__ == "__main__":
    main()
