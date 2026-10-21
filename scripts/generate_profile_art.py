from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
NAVY = "#030d1a"
CYAN = "#06b6d4"
SKY = "#0ea5e9"
INDIGO = "#6366f1"
ICE = "#e6f7ff"
SECTIONS = ("Background", "Toolkit", "Activity", "Connect")


def heading(title: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="76" viewBox="0 0 960 76" clip-path="url(#section-clip)" role="img" aria-label="{escape(title)}">
<defs>
  <clipPath id="section-clip"><rect width="960" height="76" rx="24"/></clipPath>
  <linearGradient id="section-bg" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="{NAVY}"/>
    <stop offset="1" stop-color="#081c30"/>
  </linearGradient>
  <radialGradient id="section-glow">
    <stop stop-color="{CYAN}" stop-opacity=".48"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="960" height="76" rx="24" fill="url(#section-bg)"/>
<ellipse cx="155" cy="8" rx="250" ry="92" fill="url(#section-glow)" opacity=".52"/>
<ellipse cx="845" cy="78" rx="245" ry="95" fill="url(#section-glow)" opacity=".36"/>
<rect x="16" y="6" width="928" height="64" rx="21" fill="#ffffff" fill-opacity=".09" stroke="#ffffff" stroke-opacity=".18"/>
<path d="M38 7H922" stroke="#ffffff" stroke-opacity=".24" stroke-linecap="round"/>
<text x="480" y="51" text-anchor="middle" fill="{ICE}" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="600" letter-spacing="1.2">{escape(title)}</text>
</svg>'''


def profile_header() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="280" viewBox="0 0 960 280" clip-path="url(#header-clip)" role="img" aria-label="Kevin Wijaya, Icycoldveins, currently at Capital One">
<defs>
  <clipPath id="header-clip"><rect width="960" height="280" rx="30"/></clipPath>
  <linearGradient id="header-bg" x1="0" y1="0" x2="1" y2="1">
    <stop stop-color="{NAVY}"/>
    <stop offset=".54" stop-color="#07172a"/>
    <stop offset="1" stop-color="#091d31"/>
  </linearGradient>
  <radialGradient id="cyan-glow">
    <stop stop-color="{CYAN}" stop-opacity=".72"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="indigo-glow">
    <stop stop-color="{INDIGO}" stop-opacity=".68"/>
    <stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="sky-glow">
    <stop stop-color="{SKY}" stop-opacity=".64"/>
    <stop offset="1" stop-color="{SKY}" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="960" height="280" rx="30" fill="url(#header-bg)"/>
<ellipse cx="132" cy="15" rx="290" ry="190" fill="url(#cyan-glow)" opacity=".56"/>
<ellipse cx="835" cy="268" rx="310" ry="190" fill="url(#indigo-glow)" opacity=".50"/>
<ellipse cx="788" cy="5" rx="190" ry="120" fill="url(#sky-glow)" opacity=".34"/>
<rect x="58" y="30" width="844" height="220" rx="28" fill="#ffffff" fill-opacity=".09" stroke="#ffffff" stroke-opacity=".20"/>
<path d="M84 31H876" stroke="#ffffff" stroke-opacity=".28" stroke-linecap="round"/>
<text x="480" y="106" text-anchor="middle" fill="{ICE}" font-family="Arial, Helvetica, sans-serif" font-size="46" font-weight="700" letter-spacing=".3">Kevin Wijaya</text>
<text x="480" y="148" text-anchor="middle" fill="#67e8f9" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="600" letter-spacing="3">ICYCOLDVEINS</text>
<path d="M393 172H567" stroke="#ffffff" stroke-opacity=".22" stroke-linecap="round"/>
<text x="480" y="211" text-anchor="middle" fill="{ICE}" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="500">Currently at Capital One</text>
</svg>'''


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "glass-header.svg").write_text(profile_header() + "\n", encoding="utf-8")
    for title in SECTIONS:
        (ASSETS / f"heading-{title.lower()}.svg").write_text(heading(title) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
