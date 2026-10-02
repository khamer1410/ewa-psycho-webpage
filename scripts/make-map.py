#!/usr/bin/env python3
"""
Generuje statyczną mapę do sekcji „Gabinety” z kafelków OpenStreetMap.

Uruchamiane RĘCZNIE, w czasie przygotowania strony (nie w runtime strony).
Strona po opublikowaniu nie wysyła żadnych zapytań do serwerów OSM:
korzysta wyłącznie z gotowego pliku img/mapa-warszawa.webp.

Co robi skrypt:
  1. Liczy obszar (bbox) obejmujący wszystkie pinezki z marginesem.
  2. Pobiera potrzebne kafelki 256 px (Web Mercator) z tile.openstreetmap.org.
  3. Skleja je, kadruje wokół środka bboxa i powiększa do rozmiaru docelowego.
  4. Delikatnie wycisza kolory (odbarwienie + ciepła nakładka w kolorze tła strony).
  5. Zapisuje img/mapa-warszawa.webp oraz img/mapa-warszawa.json.
  6. Wypisuje procentowe pozycje pinezek (--x / --y) do wklejenia w index.html.

Pinezki NIE są rysowane na bitmapie — to elementy HTML nałożone w CSS.

Wymagania: Python 3 + Pillow (pip install pillow).
Uruchomienie z katalogu głównego repozytorium:
    python3 scripts/make-map.py
"""

import io
import json
import math
import sys
import time
import urllib.request
from pathlib import Path

try:
    from PIL import Image, ImageEnhance
except ImportError:
    sys.exit("Brak biblioteki Pillow. Zainstaluj: python3 -m pip install pillow "
             "(np. w wirtualnym środowisku: python3 -m venv .venv && .venv/bin/pip install pillow)")

# ---------------------------------------------------------------------------
# Konfiguracja
# ---------------------------------------------------------------------------

# Pinezki: współrzędne z Nominatim (OpenStreetMap), środek odcinka ulicy.
# TODO: klientka — po podaniu numerów budynków podmienić lat/lon na dokładne
#       współrzędne budynku i uruchomić skrypt ponownie.
PINS = [
    {"id": "gabinet-1", "label": "1", "name": "Wola, ul. Łucka",      "lat": 52.2324, "lon": 20.9886},
    {"id": "gabinet-2", "label": "2", "name": "Mokotów, ul. Sielecka", "lat": 52.2052, "lon": 21.0391},
]

ZOOM = 13                 # poziom kafelków OSM (13 = czytelne nazwy dzielnic i główne ulice)
CROP_SIZE = (600, 450)    # wycinek w natywnej rozdzielczości kafelków (4:3)
OUTPUT_SCALE = 2          # powiększenie do 1200×900 (ostrzej na ekranach Retina przy ~600 px)
MARGIN = 0.2              # minimalny margines wokół pinezek (ułamek wymiaru kadru)

# Wyciszenie kolorów (wypalone w bitmapie)
SATURATION = 0.6          # 1.0 = oryginał; 0.6 = odbarwienie o ok. 40%
WARM_OVERLAY = (0xFB, 0xF1, 0xE1)   # --bg strony
WARM_ALPHA = 0.18
WEBP_QUALITY = 80

TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
USER_AGENT = "ewa-psycho-webpage-map-script/1.0 (krzysztof.hamerszmit@syzygy.pl)"
TILE = 256

ROOT = Path(__file__).resolve().parent.parent
OUT_IMAGE = ROOT / "img" / "mapa-warszawa.webp"
OUT_JSON = ROOT / "img" / "mapa-warszawa.json"

# ---------------------------------------------------------------------------


def to_world_px(lat, lon, z):
    """Współrzędne geograficzne -> piksele „świata” Web Mercator przy danym zoomie."""
    n = TILE * (2 ** z)
    x = (lon + 180.0) / 360.0 * n
    lat_r = math.radians(lat)
    y = (1.0 - math.log(math.tan(lat_r) + 1.0 / math.cos(lat_r)) / math.pi) / 2.0 * n
    return x, y


def to_latlon(x, y, z):
    n = TILE * (2 ** z)
    lon = x / n * 360.0 - 180.0
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lat, lon


def fetch_tile(z, x, y):
    url = TILE_URL.format(z=z, x=x, y=y)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    return Image.open(io.BytesIO(data)).convert("RGB")


def main():
    cw, ch = CROP_SIZE
    pts = [to_world_px(p["lat"], p["lon"], ZOOM) for p in PINS]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]

    # Środek kadru = środek bboxa pinezek.
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2

    # Kontrola: czy pinezki mieszczą się z marginesem.
    span_x, span_y = max(xs) - min(xs), max(ys) - min(ys)
    if span_x > cw * (1 - 2 * MARGIN) or span_y > ch * (1 - 2 * MARGIN):
        print(f"UWAGA: pinezki nie mieszczą się z marginesem {MARGIN:.0%} przy zoomie {ZOOM}. "
              f"Zmniejsz ZOOM albo powiększ CROP_SIZE.", file=sys.stderr)

    left, top = cx - cw / 2, cy - ch / 2
    tx0, ty0 = int(math.floor(left / TILE)), int(math.floor(top / TILE))
    tx1, ty1 = int(math.floor((left + cw) / TILE)), int(math.floor((top + ch) / TILE))

    mosaic = Image.new("RGB", ((tx1 - tx0 + 1) * TILE, (ty1 - ty0 + 1) * TILE))
    count = 0
    for tx in range(tx0, tx1 + 1):
        for ty in range(ty0, ty1 + 1):
            mosaic.paste(fetch_tile(ZOOM, tx, ty), ((tx - tx0) * TILE, (ty - ty0) * TILE))
            count += 1
            time.sleep(0.2)  # grzecznie wobec serwerów OSM
    print(f"Pobrano kafelków: {count} (zoom {ZOOM})", file=sys.stderr)

    ox, oy = left - tx0 * TILE, top - ty0 * TILE
    crop = mosaic.crop((round(ox), round(oy), round(ox) + cw, round(oy) + ch))

    out = crop.resize((cw * OUTPUT_SCALE, ch * OUTPUT_SCALE), Image.LANCZOS)
    out = ImageEnhance.Color(out).enhance(SATURATION)
    out = Image.blend(out, Image.new("RGB", out.size, WARM_OVERLAY), WARM_ALPHA)

    OUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT_IMAGE, "WEBP", quality=WEBP_QUALITY, method=6)

    left_r, top_r = round(ox) + tx0 * TILE, round(oy) + ty0 * TILE
    pins_out = []
    for p, (px, py) in zip(PINS, pts):
        x_pct = (px - left_r) / cw * 100
        y_pct = (py - top_r) / ch * 100
        pins_out.append({**p, "x": round(x_pct, 1), "y": round(y_pct, 1)})

    clat, clon = to_latlon(left_r + cw / 2, top_r + ch / 2, ZOOM)
    meta = {
        "source": "© OpenStreetMap contributors (https://www.openstreetmap.org/copyright)",
        "image": f"img/{OUT_IMAGE.name}",
        "center": {"lat": round(clat, 6), "lon": round(clon, 6)},
        "zoom": ZOOM,
        "crop_px": [cw, ch],
        "size": [cw * OUTPUT_SCALE, ch * OUTPUT_SCALE],
        "color": {"saturation": SATURATION, "overlay": "#%02X%02X%02X" % WARM_OVERLAY, "alpha": WARM_ALPHA},
        "pins": pins_out,
    }
    OUT_JSON.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Zapisano: {OUT_IMAGE.relative_to(ROOT)} ({OUT_IMAGE.stat().st_size // 1024} KB, "
          f"{meta['size'][0]}×{meta['size'][1]} px) i {OUT_JSON.relative_to(ROOT)}", file=sys.stderr)
    print("\nPozycje pinezek do wklejenia w index.html (atrybut style):")
    for p in pins_out:
        print(f'  {p["id"]:<10} ({p["name"]}): style="--x:{p["x"]}%;--y:{p["y"]}%"')


if __name__ == "__main__":
    main()
