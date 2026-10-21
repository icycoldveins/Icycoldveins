from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
GREEN = "#0c3028"
GOLD = "#c5a15b"
CREAM = "#f1e7d0"


def heading(title: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="64" viewBox="0 0 960 64" role="img" aria-label="{escape(title)}">
<rect width="960" height="64" fill="{GREEN}"/>
<path d="M24 32H300 M660 32H936" stroke="{GOLD}" stroke-width="1" opacity=".72"/>
<path d="M310 32l7-7 7 7-7 7z M636 32l7-7 7 7-7 7z" fill="{GOLD}"/>
<text x="480" y="40" text-anchor="middle" fill="{CREAM}" font-family="Georgia,serif" font-size="34" letter-spacing="3">{escape(title.upper())}</text>
</svg>'''


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="260" viewBox="0 0 960 260" role="img" aria-label="Kevin Wijaya, Icycoldveins, currently at Capital One">
<rect width="960" height="260" fill="{GREEN}"/>
<g fill="none" stroke="{GOLD}" stroke-width="1.5">
  <path d="M40 26H920V234H40Z" opacity=".8"/>
  <path d="M58 44H410 M550 44H902V216H750 M210 216H58V44" opacity=".45"/>

</g>
<g transform="translate(480 44)" fill="none" stroke="{GOLD}" stroke-width="1.3">
  <path d="M0 0V32 M-5 30L-20 5 M5 30L20 5 M-10 32L-35 14 M10 32L35 14 M-15 34L-48 25 M15 34L48 25"/>
  <path d="M-4 37l4-4 4 4-4 4z" fill="{GOLD}"/>
</g>
<text x="480" y="125" text-anchor="middle" fill="{CREAM}" font-family="Georgia,serif" font-size="54" letter-spacing="6">KEVIN WIJAYA</text>
<text x="480" y="163" text-anchor="middle" fill="{GOLD}" font-family="Arial,sans-serif" font-size="20" letter-spacing="4">ICYCOLDVEINS</text>
<path d="M390 186h180" stroke="{GOLD}" stroke-width="1" opacity=".75"/>
<text x="480" y="216" text-anchor="middle" fill="{CREAM}" font-family="Arial,sans-serif" font-size="21" letter-spacing="1">Currently at Capital One</text>
</svg>'''
    (ASSETS / "art-deco-header.svg").write_text(header + "\n", encoding="utf-8")
    for title in ("Background", "Toolkit", "Activity", "Connect"):
        (ASSETS / f"heading-{title.lower()}.svg").write_text(heading(title) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
