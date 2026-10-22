import os
import math
import xml.etree.ElementTree as ET

BASE_DIR = r"C:\Users\sandy\.gemini\antigravity-ide\scratch\leinhabersv-bit"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def ensure_dirs():
    for sub in ["identity", "projects", "systems", "closing"]:
        os.makedirs(os.path.join(ASSETS_DIR, sub), exist_ok=True)

# ---------------------------------------------------------------------------
# 1. FLAGSHIP HERO: SIGNAL / FORM (1200 x 520)
# ---------------------------------------------------------------------------
def generate_hero():
    # Generate parametric resonant curve points for the computational centerpiece
    curves_svg = []
    # 3 nested harmonic Lissajous-like resonance curves
    for k, (a, b, delta, color, op) in enumerate([
        (3, 2, math.pi / 4, "#C8F75A", 0.45),
        (5, 4, math.pi / 2, "#94A3B8", 0.35),
        (2, 3, math.pi / 3, "#38BDF8", 0.30)
    ]):
        cx, cy, r = 940, 260, 160 - k * 30
        pts = []
        for step in range(181):
            theta = (step / 180) * 2 * math.pi
            x = cx + r * math.sin(a * theta + delta)
            y = cy + (r * 0.85) * math.sin(b * theta)
            pts.append(f"{x:.1f},{y:.1f}")
        curves_svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="1.2" opacity="{op}"/>')

    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" width="100%" height="auto">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#07080B"/>
      <stop offset="50%" stop-color="#0E1117"/>
      <stop offset="100%" stop-color="#090B10"/>
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F1F0EA"/>
      <stop offset="85%" stop-color="#C8F75A"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>

    <linearGradient id="beam-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(200, 247, 90, 0)"/>
      <stop offset="50%" stop-color="#C8F75A"/>
      <stop offset="100%" stop-color="rgba(56, 189, 248, 0)"/>
    </linearGradient>

    <radialGradient id="aura-glow" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(200, 247, 90, 0.12)"/>
      <stop offset="60%" stop-color="rgba(56, 189, 248, 0.04)"/>
      <stop offset="100%" stop-color="rgba(0, 0, 0, 0)"/>
    </radialGradient>

    <pattern id="grid-dots" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="rgba(255, 255, 255, 0.035)"/>
    </pattern>

    <style>
      @keyframes signalSweep {{
        0% {{ transform: translateX(-400px); }}
        65%, 100% {{ transform: translateX(1250px); }}
      }}
      @keyframes pulseNode {{
        0%, 100% {{ opacity: 0.4; transform: scale(0.98); }}
        50% {{ opacity: 0.95; transform: scale(1.02); }}
      }}
      .anim-sweep {{
        animation: signalSweep 6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      }}
      .anim-pulse {{
        animation: pulseNode 4s ease-in-out infinite;
        transform-origin: 940px 260px;
      }}
      @media (prefers-reduced-motion: reduce) {{
        .anim-sweep, .anim-pulse {{
          animation: none !important;
          opacity: 0.7 !important;
        }}
      }}
    </style>
  </defs>

  <!-- Base Structure -->
  <rect width="1200" height="520" rx="18" fill="url(#bg-grad)"/>
  <rect width="1200" height="520" rx="18" fill="url(#grid-dots)"/>
  <rect width="1200" height="520" rx="18" fill="url(#aura-glow)"/>
  <rect width="1198" height="518" x="1" y="1" rx="17" fill="none" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>

  <!-- Top Signal Sweep Bar -->
  <g clip-path="url(#frame-clip)">
    <rect class="anim-sweep" y="0" x="0" width="350" height="2.5" fill="url(#beam-grad)"/>
  </g>

  <!-- Technical Registration Crosshairs -->
  <g stroke="rgba(255, 255, 255, 0.15)" stroke-width="1">
    <path d="M 28 36 L 40 36 M 34 30 L 34 42"/>
    <path d="M 1160 36 L 1172 36 M 1166 30 L 1166 42"/>
    <path d="M 28 484 L 40 484 M 34 478 L 34 490"/>
    <path d="M 1160 484 L 1172 484 M 1166 478 L 1166 490"/>
  </g>

  <!-- Header Metadata Strip -->
  <g transform="translate(56, 42)">
    <text x="0" y="0" font-family="'JetBrains Mono', 'SF Mono', monospace, sans-serif" font-size="11" font-weight="700" fill="#C8F75A" letter-spacing="1.5">
      SIGNAL / FORM // 2026 EXHIBITION
    </text>
    <text x="320" y="0" font-family="'JetBrains Mono', 'SF Mono', monospace, sans-serif" font-size="11" font-weight="500" fill="#64748B" letter-spacing="0.5">
      INDEX: 00_IDENTITY • LOC: IN / BLR • STUDENT SOFTWARE BUILDER
    </text>
    <text x="1088" y="0" font-family="'JetBrains Mono', 'SF Mono', monospace, sans-serif" font-size="11" font-weight="600" fill="#94A3B8" text-anchor="end" letter-spacing="1">
      @leinhabersv-bit
    </text>
  </g>

  <line x1="56" y1="58" x2="1144" y2="58" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>

  <!-- Main Left Narrative: Monumental Typography -->
  <g transform="translate(56, 172)">
    <!-- Subtitle Flag -->
    <text x="2" y="-36" font-family="'JetBrains Mono', monospace, sans-serif" font-size="12" font-weight="600" fill="#C8F75A" letter-spacing="2">
      // CORE_MONOGRAPH
    </text>

    <!-- Monumental Display Name -->
    <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif" font-size="82" font-weight="900" fill="url(#name-grad)" letter-spacing="-3">
      RITHIK SV
    </text>

    <!-- Architectural Subtitle -->
    <text x="4" y="96" font-family="'JetBrains Mono', monospace, sans-serif" font-size="13" font-weight="600" fill="#94A3B8" letter-spacing="1.2">
      INTERACTIVE SYSTEMS • THOUGHTFUL ENGINEERING • UNEXPECTED EXPERIENCES
    </text>

    <!-- Concise Positioning -->
    <text x="4" y="142" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#CBD5E1" letter-spacing="-0.2">
      Engineering ambitious client-side architectures, deterministic 2D/3D visual graphics,
    </text>
    <text x="4" y="168" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#94A3B8" letter-spacing="-0.2">
      and local-first persistent data engines backed by automated verification.
    </text>

    <!-- Disciplines Line -->
    <g transform="translate(4, 218)">
      <rect x="0" y="0" width="138" height="32" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(200, 247, 90, 0.3)" stroke-width="1"/>
      <text x="69" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#C8F75A">TypeScript 5.x</text>

      <rect x="150" y="0" width="168" height="32" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
      <text x="234" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="500" fill="#E2E8F0">Canvas 2D / Three.js</text>

      <rect x="330" y="0" width="176" height="32" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1"/>
      <text x="418" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="500" fill="#38BDF8">Local-First (IndexedDB)</text>

      <rect x="518" y="0" width="160" height="32" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
      <text x="598" y="19" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="500" fill="#E2E8F0">Next.js App Router</text>
    </g>
  </g>

  <!-- Right Computational Centerpiece: Orbital Geometric Matrix -->
  <g class="anim-pulse">
    <!-- Circular Coordinate Tracks -->
    <circle cx="940" cy="260" r="180" fill="none" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1" stroke-dasharray="3, 5"/>
    <circle cx="940" cy="260" r="140" fill="none" stroke="rgba(200, 247, 90, 0.15)" stroke-width="1.2"/>
    <circle cx="940" cy="260" r="100" fill="none" stroke="rgba(56, 189, 248, 0.18)" stroke-width="1" stroke-dasharray="8, 4"/>
    <circle cx="940" cy="260" r="60" fill="none" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>

    <!-- Axis Crosshair -->
    <line x1="740" y1="260" x2="1140" y2="260" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1"/>
    <line x1="940" y1="60" x2="940" y2="460" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1"/>

    <!-- Parametric Curves -->
    {''.join(curves_svg)}

    <!-- Geometric Nucleus -->
    <circle cx="940" cy="260" r="8" fill="#C8F75A"/>
    <circle cx="940" cy="260" r="22" fill="none" stroke="#C8F75A" stroke-width="1.5" stroke-dasharray="4, 4"/>

    <!-- Degree Compass Markers -->
    <text x="940" y="74" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">000°</text>
    <text x="1132" y="263" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">090°</text>
    <text x="940" y="452" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">180°</text>
    <text x="748" y="263" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">270°</text>

    <!-- Vector Annotation -->
    <text x="940" y="380" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#94A3B8" letter-spacing="1">
      HARMONIC_LATTICE // 60Hz
    </text>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "identity", "hero.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(hero_svg)
    ET.fromstring(hero_svg)
    print("[OK] hero.svg verified valid XML")

    # Also keep backward-compatible root assets/hero.svg pointing to same content
    with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(hero_svg)

# ---------------------------------------------------------------------------
# 2. MONOGRAM: S / V INTERLOCKING GEOMETRY (180 x 180)
# ---------------------------------------------------------------------------
def generate_monogram():
    mono_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="100%" height="auto">
  <defs>
    <linearGradient id="mono-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F1219"/>
      <stop offset="100%" stop-color="#08090C"/>
    </linearGradient>
    <linearGradient id="mono-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C8F75A"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <rect width="180" height="180" rx="20" fill="url(#mono-bg)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1.5"/>
  <circle cx="90" cy="90" r="74" fill="none" stroke="rgba(255, 255, 255, 0.05)" stroke-dasharray="2, 4"/>

  <!-- Geometric Interlocking 'S' / 'V' Monogram -->
  <g stroke="url(#mono-accent)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <!-- S path upper -->
    <path d="M 120 54 L 75 54 A 18 18 0 0 0 75 90 L 105 90 A 18 18 0 0 1 105 126 L 60 126"/>
    <!-- V chevron crossing below -->
    <path d="M 68 85 L 90 138 L 112 85" stroke="#FFFFFF" stroke-width="4.5"/>
  </g>

  <!-- Coordinate Nodes -->
  <circle cx="90" cy="138" r="4" fill="#C8F75A"/>
  <circle cx="120" cy="54" r="3" fill="#FFFFFF"/>
  <circle cx="60" cy="126" r="3" fill="#38BDF8"/>
</svg>'''

    target = os.path.join(ASSETS_DIR, "identity", "monogram.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(mono_svg)
    ET.fromstring(mono_svg)
    print("[OK] monogram.svg verified valid XML")

# ---------------------------------------------------------------------------
# 3. PANIC DELIVERY FLAGSHIP ARTWORK (1200 x 540)
# ---------------------------------------------------------------------------
def generate_panic_card():
    panic_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 540" width="100%" height="auto">
  <defs>
    <linearGradient id="p-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#12080A"/>
      <stop offset="45%" stop-color="#1A0D10"/>
      <stop offset="100%" stop-color="#0A0608"/>
    </linearGradient>

    <linearGradient id="p-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF3838"/>
      <stop offset="50%" stop-color="#FF6B00"/>
      <stop offset="100%" stop-color="#C8F75A"/>
    </linearGradient>

    <pattern id="p-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="rgba(255, 56, 56, 0.04)" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1200" height="540" rx="16" fill="url(#p-bg)"/>
  <rect width="1200" height="540" rx="16" fill="url(#p-grid)"/>
  <rect width="1198" height="538" x="1" y="1" rx="15" fill="none" stroke="rgba(255, 56, 56, 0.15)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#p-accent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Side: Kinetic Trajectory Kinematics Diagram -->
  <g transform="translate(48, 52)">
    <!-- Radar / Boundary Box -->
    <rect width="460" height="436" rx="12" fill="rgba(0, 0, 0, 0.45)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
    <text x="24" y="34" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#FF3838" letter-spacing="1">
      SIMULATION // TRAJECTORY &amp; SLIP-ANGLE KINEMATICS
    </text>

    <!-- Coordinate Grid Lines -->
    <line x1="24" y1="218" x2="436" y2="218" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" stroke-dasharray="4, 4"/>
    <line x1="230" y1="48" x2="230" y2="400" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" stroke-dasharray="4, 4"/>

    <!-- Drift Slip-Angle Arc -->
    <path d="M 60 360 C 120 340, 220 280, 260 160 C 290 80, 360 80, 410 120" fill="none" stroke="#FF6B00" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M 60 360 C 120 340, 220 280, 260 160 C 290 80, 360 80, 410 120" fill="none" stroke="#FF3838" stroke-width="1" stroke-dasharray="4, 4"/>

    <!-- Hold-to-Charge Launch Vector -->
    <path d="M 260 160 Q 320 220, 390 280" fill="none" stroke="#C8F75A" stroke-width="2.5" stroke-dasharray="6, 3"/>

    <!-- Vehicle Tangent Marker -->
    <g transform="translate(260, 160)">
      <polygon points="0,-14 10,12 -10,12" fill="#FF3838"/>
      <circle cx="0" cy="0" r="18" fill="none" stroke="#FF6B00" stroke-width="1.5" stroke-dasharray="3, 3"/>
      <text x="22" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#FFFFFF">VELOCITY_VECTOR</text>
    </g>

    <!-- Delivery Target Zone -->
    <g transform="translate(390, 280)">
      <circle cx="0" cy="0" r="28" fill="none" stroke="#C8F75A" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="14" fill="rgba(200, 247, 90, 0.2)"/>
      <circle cx="0" cy="0" r="4" fill="#C8F75A"/>
      <text x="0" y="44" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C8F75A">DROP_TARGET (±0.4s)</text>
    </g>

    <!-- Cargo Telemetry Bar -->
    <g transform="translate(24, 390)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="10" fill="#94A3B8">CARGO MATRIX: [PIZZA: STABLE] • [EXPRESS: RAPID] • [FRAGILE: NO_COLLISION]</text>
    </g>
  </g>

  <!-- Right Side: Project Architecture & Technical Story -->
  <g transform="translate(544, 52)">
    <!-- Index Header -->
    <g transform="translate(0, 18)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#FF3838" letter-spacing="1.5">
        001 // FLAGSHIP ARCADE ENGINE
      </text>
      <rect x="250" y="-12" width="168" height="22" rx="4" fill="rgba(200, 247, 90, 0.1)" stroke="rgba(200, 247, 90, 0.3)" stroke-width="1"/>
      <text x="334" y="3" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C8F75A">● LIVE ON VERCEL (PROD)</text>
    </g>

    <!-- Title -->
    <text x="0" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="42" font-weight="800" fill="#FFFFFF" letter-spacing="-1">
      PANIC DELIVERY
    </text>

    <!-- Subtitle -->
    <text x="0" y="98" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="500" fill="#FF6B00">
      Arcade Driving &amp; Hold-to-Charge Kinetic Delivery Engine
    </text>

    <!-- Narrative Paragraph -->
    <text x="0" y="136" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      Engineered from scratch using pure TypeScript, HTML5 Canvas 2D, Three.js spatial spikes,
    </text>
    <text x="0" y="158" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      and real-time procedural Web Audio synthesis. Delivers high-velocity vehicle drift physics,
    </text>
    <text x="0" y="180" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      precision package projectile kinematics, dynamic traffic, and zero external sound samples.
    </text>

    <!-- Architectural Differentiators (3 Boxes) -->
    <g transform="translate(0, 214)">
      <!-- Box 1 -->
      <rect x="0" y="0" width="186" height="88" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#FF6B00">DRIFT PHYSICS</text>
      <text x="14" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Custom slip-angle</text>
      <text x="14" y="60" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">simulation &amp; traction</text>
      <text x="14" y="76" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">6-Key Input Loop</text>

      <!-- Box 2 -->
      <rect x="200" y="0" width="186" height="88" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="214" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#C8F75A">PROCEDURAL AUDIO</text>
      <text x="214" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Web Audio API synth</text>
      <text x="214" y="60" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Engine revs &amp; fanfares</text>
      <text x="214" y="76" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Zero Asset Bloat</text>

      <!-- Box 3 -->
      <rect x="400" y="0" width="186" height="88" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="414" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38BDF8">VERIFIED QUALITY</text>
      <text x="414" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">10/10 Vitest Suites</text>
      <text x="414" y="60" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Passing in CI Pipeline</text>
      <text x="414" y="76" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Zero Flaky States</text>
    </g>

    <!-- Stack Footprint & Verified CTAs -->
    <g transform="translate(0, 332)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B">
        STACK: TypeScript • Canvas 2D • Three.js • Web Audio API • Vitest • Vite
      </text>

      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="180" height="36" rx="6" fill="#FF3838"/>
        <text x="90" y="22" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#FFFFFF">
          PLAY LIVE GAME →
        </text>

        <rect x="194" y="0" width="180" height="36" rx="6" fill="rgba(255, 255, 255, 0.05)" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
        <text x="284" y="22" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="#E2E8F0">
          VIEW SOURCE CODE
        </text>
      </g>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "projects", "panic-delivery.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(panic_svg)
    ET.fromstring(panic_svg)
    print("[OK] panic-delivery.svg verified valid XML")

    with open(os.path.join(ASSETS_DIR, "panic-card.svg"), "w", encoding="utf-8") as f:
        f.write(panic_svg)

# ---------------------------------------------------------------------------
# 4. CLIENTLAUNCH COMMERCIAL CASE STUDY (1200 x 480)
# ---------------------------------------------------------------------------
def generate_clientlaunch_card():
    claunch_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="auto">
  <defs>
    <linearGradient id="c-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080E18"/>
      <stop offset="50%" stop-color="#0E1626"/>
      <stop offset="100%" stop-color="#060A12"/>
    </linearGradient>

    <linearGradient id="c-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="60%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>

    <pattern id="c-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="rgba(56, 189, 248, 0.04)"/>
    </pattern>
  </defs>

  <rect width="1200" height="480" rx="16" fill="url(#c-bg)"/>
  <rect width="1200" height="480" rx="16" fill="url(#c-dots)"/>
  <rect width="1198" height="478" x="1" y="1" rx="15" fill="none" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#c-accent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Side: Local-First Architectural Vault Diagram -->
  <g transform="translate(48, 48)">
    <rect width="460" height="384" rx="12" fill="rgba(0, 0, 0, 0.45)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>

    <text x="24" y="32" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1">
      ARCHITECTURE // LOCAL-FIRST CLIENT VAULT
    </text>

    <!-- Top UI Mockup Frame -->
    <g transform="translate(24, 52)">
      <rect width="412" height="150" rx="8" fill="#0C1422" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1"/>
      <circle cx="16" cy="16" r="4" fill="#EF4444"/>
      <circle cx="30" cy="16" r="4" fill="#F59E0B"/>
      <circle cx="44" cy="16" r="4" fill="#10B981"/>
      <text x="64" y="20" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B">ClientLaunch // Proposal &amp; Onboarding Workbench</text>

      <!-- Mockup data rows -->
      <rect x="16" y="36" width="380" height="26" rx="4" fill="rgba(255, 255, 255, 0.03)"/>
      <text x="28" y="53" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#E2E8F0">Tier 3 Growth Retainer • Scope: 12 Assets/mo • $4,200</text>

      <rect x="16" y="68" width="380" height="26" rx="4" fill="rgba(255, 255, 255, 0.02)"/>
      <text x="28" y="85" font-family="-apple-system, sans-serif" font-size="11" font-weight="500" fill="#94A3B8">Contract Status: Executed via Client-Side Agreement Generator</text>

      <rect x="16" y="100" width="380" height="26" rx="4" fill="rgba(56, 189, 248, 0.05)"/>
      <text x="28" y="117" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#38BDF8">IndexedDB Vault: 0ms Latency • Encrypted On-Device</text>
    </g>

    <!-- Lower Diagram: Storage Boundary -->
    <g transform="translate(24, 226)">
      <rect width="194" height="126" rx="6" fill="rgba(56, 189, 248, 0.04)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1"/>
      <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38BDF8">ON-DEVICE VAULT</text>
      <text x="14" y="46" font-family="-apple-system, sans-serif" font-size="11" fill="#CBD5E1">IndexedDB Persistence</text>
      <text x="14" y="64" font-family="-apple-system, sans-serif" font-size="11" fill="#94A3B8">JSON Snapshot Backup</text>
      <text x="14" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#94A3B8">Zero Telemetry Leaks</text>
      <text x="14" y="104" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#10B981">● 100% OFFLINE</text>

      <rect x="218" y="0" width="194" height="126" rx="6" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="232" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#A855F7">COMMERCIAL SUITE</text>
      <text x="232" y="46" font-family="-apple-system, sans-serif" font-size="11" fill="#CBD5E1">Tiered Pricing Matrix</text>
      <text x="232" y="64" font-family="-apple-system, sans-serif" font-size="11" fill="#94A3B8">Scope Enforcer</text>
      <text x="232" y="82" font-family="-apple-system, sans-serif" font-size="11" fill="#94A3B8">Playwright E2E Verified</text>
      <text x="232" y="104" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#C8F75A">● ZERO SUBSCRIPTION</text>
    </g>
  </g>

  <!-- Right Side: Project Architecture & Description -->
  <g transform="translate(544, 48)">
    <g transform="translate(0, 18)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#38BDF8" letter-spacing="1.5">
        002 // COMMERCIAL WEB APPLICATION
      </text>
      <rect x="270" y="-12" width="196" height="22" rx="4" fill="rgba(168, 85, 247, 0.1)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <text x="368" y="3" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C084FC">◆ PRIVATE REPO (COMMERCIAL)</text>
    </g>

    <text x="0" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="40" font-weight="800" fill="#FFFFFF" letter-spacing="-1">
      ClientLaunch
    </text>

    <text x="0" y="96" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="500" fill="#38BDF8">
      Offline-First Operations &amp; Client Agreement Suite for Freelancers
    </text>

    <text x="0" y="132" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      A 100% local-first commercial operations application built for social media managers and independent
    </text>
    <text x="0" y="154" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      consultants. Eliminates monthly SaaS fees by handling client proposal generation, scope enforcement,
    </text>
    <text x="0" y="176" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      electronic agreements, and milestone tracking directly on-device with zero server dependencies.
    </text>

    <!-- Technical Badges -->
    <g transform="translate(0, 212)">
      <rect x="0" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38BDF8">ZERO-CLOUD PRIVACY</text>
      <text x="14" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">IndexedDB local vault</text>
      <text x="14" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">No database subscriptions</text>

      <rect x="200" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="214" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#818CF8">COMMERCIAL TOOLS</text>
      <text x="214" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Tiered scope calculator</text>
      <text x="214" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Agreement generator</text>

      <rect x="400" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="414" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#C8F75A">E2E TEST HARNESS</text>
      <text x="414" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Playwright browser suites</text>
      <text x="414" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Vitest + Oxlint CI</text>
    </g>

    <g transform="translate(0, 318)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B">
        STACK: React 18 • TypeScript • IndexedDB • Playwright E2E • Vitest • TailwindCSS
      </text>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "projects", "clientlaunch.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(claunch_svg)
    ET.fromstring(claunch_svg)
    print("[OK] clientlaunch.svg verified valid XML")

    with open(os.path.join(ASSETS_DIR, "clientlaunch-card.svg"), "w", encoding="utf-8") as f:
        f.write(claunch_svg)

# ---------------------------------------------------------------------------
# 5. EVENTHUB-CC TELEMETRY PLATFORM (1200 x 440)
# ---------------------------------------------------------------------------
def generate_eventhub_card():
    ehub_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="100%" height="auto">
  <defs>
    <linearGradient id="e-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0A18"/>
      <stop offset="50%" stop-color="#140E24"/>
      <stop offset="100%" stop-color="#08060F"/>
    </linearGradient>

    <linearGradient id="e-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="440" rx="16" fill="url(#e-bg)"/>
  <rect width="1198" height="438" x="1" y="1" rx="15" fill="none" stroke="rgba(168, 85, 247, 0.15)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#e-accent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Side: Constellation Network & Ingestion Flow -->
  <g transform="translate(48, 48)">
    <rect width="460" height="344" rx="12" fill="rgba(0, 0, 0, 0.45)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
    <text x="24" y="32" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#A855F7" letter-spacing="1">
      INGESTION PIPELINE // CHEERIO TELEMETRY HARVESTER
    </text>

    <!-- Flow Diagram: Source -> Scraper -> Normalizer -> Dashboard -->
    <g transform="translate(24, 64)">
      <!-- Stage 1 -->
      <rect x="0" y="0" width="120" height="60" rx="6" fill="rgba(168, 85, 247, 0.08)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <text x="60" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C084FC">CAMPUS HUBS</text>
      <text x="60" y="42" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8">Raw HTML Feeds</text>

      <path d="M 120 30 L 146 30" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3, 3"/>

      <!-- Stage 2 -->
      <rect x="146" y="0" width="120" height="60" rx="6" fill="rgba(56, 189, 248, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
      <text x="206" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#38BDF8">CHEERIO INGEST</text>
      <text x="206" y="42" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8">Parser &amp; Sanitizer</text>

      <path d="M 266 30 L 292 30" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3, 3"/>

      <!-- Stage 3 -->
      <rect x="292" y="0" width="120" height="60" rx="6" fill="rgba(200, 247, 90, 0.08)" stroke="rgba(200, 247, 90, 0.3)" stroke-width="1"/>
      <text x="352" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C8F75A">LIVE PORTAL</text>
      <text x="352" y="42" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8">Next.js App Router</text>
    </g>

    <!-- Constellation Visual Nodes -->
    <g transform="translate(24, 150)">
      <circle cx="50" cy="80" r="14" fill="rgba(168, 85, 247, 0.2)" stroke="#A855F7" stroke-width="1.5"/>
      <circle cx="160" cy="40" r="18" fill="rgba(56, 189, 248, 0.2)" stroke="#38BDF8" stroke-width="1.5"/>
      <circle cx="280" cy="90" r="16" fill="rgba(200, 247, 90, 0.2)" stroke="#C8F75A" stroke-width="1.5"/>
      <circle cx="360" cy="30" r="12" fill="rgba(129, 140, 248, 0.2)" stroke="#818CF8" stroke-width="1.5"/>

      <!-- Connecting constellation lines -->
      <line x1="50" y1="80" x2="160" y2="40" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
      <line x1="160" y1="40" x2="280" y2="90" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
      <line x1="280" y1="90" x2="360" y2="30" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1"/>
      <line x1="50" y1="80" x2="280" y2="90" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" stroke-dasharray="4, 4"/>

      <text x="50" y="112" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#C084FC">HACKATHONS</text>
      <text x="160" y="76" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#38BDF8">SYMPOSIA</text>
      <text x="280" y="122" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#C8F75A">WORKSHOPS</text>
      <text x="360" y="58" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#818CF8">COMMUNITIES</text>
    </g>

    <text x="24" y="320" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B">SECURITY: Strict HTTP Security Headers • Vitest CI Verified</text>
  </g>

  <!-- Right Side: Narrative -->
  <g transform="translate(544, 48)">
    <g transform="translate(0, 18)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#A855F7" letter-spacing="1.5">
        003 // CAMPUS TELEMETRY &amp; DISCOVERY
      </text>
      <rect x="280" y="-12" width="186" height="22" rx="4" fill="rgba(168, 85, 247, 0.1)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <text x="373" y="3" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C084FC">◆ PRIVATE REPO (PLATFORM)</text>
    </g>

    <text x="0" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="40" font-weight="800" fill="#FFFFFF" letter-spacing="-1">
      EventHub-CC
    </text>

    <text x="0" y="94" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="500" fill="#C084FC">
      Campus Event Intelligence Portal &amp; Automated Ingestion System
    </text>

    <text x="0" y="130" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      An interactive event discovery platform engineered for university student communities. Consolidates
    </text>
    <text x="0" y="152" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      fragmented campus announcements via an automated server-side Cheerio scraping and normalization pipeline,
    </text>
    <text x="0" y="174" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      featuring an organizer workbench, telemetry charts, and fluid Framer Motion transitions.
    </text>

    <!-- Technical Badges -->
    <g transform="translate(0, 210)">
      <rect x="0" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#A855F7">APP ROUTER (NEXT 15)</text>
      <text x="14" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Obsidian Lumina UI layout</text>
      <text x="14" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">TypeScript + Motion</text>

      <rect x="200" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="214" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38BDF8">DATA INGESTION</text>
      <text x="214" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Cheerio Web Scraper</text>
      <text x="214" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Organizer Workbench</text>

      <rect x="400" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="414" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#C8F75A">SECURITY HEADERS</text>
      <text x="414" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Strict CSP &amp; HSTS</text>
      <text x="414" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Automated Vitest Suite</text>
    </g>

    <g transform="translate(0, 314)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B">
        STACK: Next.js 15 • TypeScript • Node.js 22 • Cheerio • Framer Motion • TailwindCSS
      </text>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "projects", "eventhub.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(ehub_svg)
    ET.fromstring(ehub_svg)
    print("[OK] eventhub.svg verified valid XML")

# ---------------------------------------------------------------------------
# 6. MIC LEARNPATH DAG TRACKER (1200 x 440)
# ---------------------------------------------------------------------------
def generate_mic_card():
    mic_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="100%" height="auto">
  <defs>
    <linearGradient id="m-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06120E"/>
      <stop offset="50%" stop-color="#091A14"/>
      <stop offset="100%" stop-color="#040D09"/>
    </linearGradient>

    <linearGradient id="m-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="50%" stop-color="#00F5D4"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="440" rx="16" fill="url(#m-bg)"/>
  <rect width="1198" height="438" x="1" y="1" rx="15" fill="none" stroke="rgba(16, 185, 129, 0.15)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#m-accent)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Left Side: Directed Acyclic Graph (DAG) Visualization -->
  <g transform="translate(48, 48)">
    <rect width="460" height="344" rx="12" fill="rgba(0, 0, 0, 0.45)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
    <text x="24" y="32" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#10B981" letter-spacing="1">
      DEPENDENCY GRAPH // DIRECTED ACYCLIC PREREQUISITES
    </text>

    <!-- DAG Nodes & Directed Arrows -->
    <g transform="translate(36, 68)">
      <!-- Root Node (Unlocked) -->
      <rect x="0" y="80" width="110" height="46" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="#10B981" stroke-width="1.5"/>
      <text x="55" y="102" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#10B981">AZ-900</text>
      <text x="55" y="116" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8">[PASS] MASTERED</text>

      <!-- Arrows to Tier 2 -->
      <path d="M 110 95 L 148 50" stroke="#10B981" stroke-width="1.5" stroke-dasharray="3, 3"/>
      <path d="M 110 110 L 148 155" stroke="#10B981" stroke-width="1.5" stroke-dasharray="3, 3"/>

      <!-- Tier 2: Cloud Architect (Active) -->
      <rect x="148" y="24" width="110" height="46" rx="6" fill="rgba(0, 245, 212, 0.12)" stroke="#00F5D4" stroke-width="1.5"/>
      <text x="203" y="46" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#00F5D4">AZ-104</text>
      <text x="203" y="60" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#E2E8F0">● IN PROGRESS</text>

      <!-- Tier 2: AI Fundamentals (Unlocked) -->
      <rect x="148" y="132" width="110" height="46" rx="6" fill="rgba(168, 85, 247, 0.12)" stroke="#A855F7" stroke-width="1.5"/>
      <text x="203" y="154" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#A855F7">AI-900</text>
      <text x="203" y="168" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8">[PASS] MASTERED</text>

      <!-- Arrows to Tier 3 -->
      <path d="M 258 47 L 296 47" stroke="rgba(255, 255, 255, 0.2)" stroke-width="1.5"/>
      <path d="M 258 155 L 296 155" stroke="rgba(255, 255, 255, 0.2)" stroke-width="1.5"/>

      <!-- Tier 3: Solutions Architect (Locked) -->
      <rect x="296" y="24" width="110" height="46" rx="6" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <text x="351" y="46" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#64748B">AZ-305</text>
      <text x="351" y="60" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#475569">🔒 PREREQ LOCK</text>

      <!-- Tier 3: AI Engineer (Locked) -->
      <rect x="296" y="132" width="110" height="46" rx="6" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <text x="351" y="154" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#64748B">AI-102</text>
      <text x="351" y="168" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#475569">🔒 PREREQ LOCK</text>
    </g>

    <text x="24" y="320" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B">VALIDATION: Topological Sort • Cycle Detection • Offline AI Fallback</text>
  </g>

  <!-- Right Side: Narrative -->
  <g transform="translate(544, 48)">
    <g transform="translate(0, 18)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#10B981" letter-spacing="1.5">
        004 // KNOWLEDGE GRAPH &amp; DAG
      </text>
      <rect x="250" y="-12" width="176" height="22" rx="4" fill="rgba(168, 85, 247, 0.1)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1"/>
      <text x="338" y="3" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#10B981">● PUBLIC OPEN SOURCE</text>
    </g>

    <text x="0" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="40" font-weight="800" fill="#FFFFFF" letter-spacing="-1">
      MIC LearnPath
    </text>

    <text x="0" y="94" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="500" fill="#00F5D4">
      Prerequisite Directed Acyclic Graph &amp; Curriculum Navigation Engine
    </text>

    <text x="0" y="130" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      A structured technical curriculum progression tool designed to navigate Microsoft learning paths.
    </text>
    <text x="0" y="152" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      Validates knowledge requirements using a Directed Acyclic Graph (DAG) state engine to ensure modules
    </text>
    <text x="0" y="174" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#CBD5E1">
      unlock strictly when dependencies are satisfied, with resilient AI topic explanation fallbacks.
    </text>

    <!-- Technical Badges -->
    <g transform="translate(0, 210)">
      <rect x="0" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#10B981">DAG CONSTRAINT SOLVER</text>
      <text x="14" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Topological dependency sort</text>
      <text x="14" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Strict lock-unlock state</text>

      <rect x="200" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="214" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#00F5D4">RESILIENT AI SUMMARY</text>
      <text x="214" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">Contextual AI explanations</text>
      <text x="214" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Automatic offline failover</text>

      <rect x="400" y="0" width="186" height="74" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1"/>
      <text x="414" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#F59E0B">VITE ECOSYSTEM</text>
      <text x="414" y="44" font-family="-apple-system, sans-serif" font-size="12" fill="#94A3B8">React 18 + TypeScript</text>
      <text x="414" y="60" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Lucide + Tailwind styling</text>
    </g>

    <g transform="translate(0, 314)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B">
        STACK: React 18 • TypeScript • Directed Graph Logic • OpenAI API Fallback • Vite
      </text>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "projects", "mic-learnpath.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(mic_svg)
    ET.fromstring(mic_svg)
    print("[OK] mic-learnpath.svg verified valid XML")

# ---------------------------------------------------------------------------
# 7. HOW I BUILD: ENGINEERING PHILOSOPHY & SYSTEMS AXIOMS (1200 x 380)
# ---------------------------------------------------------------------------
def generate_philosophy():
    phil_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="100%" height="auto">
  <defs>
    <linearGradient id="ph-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0C12"/>
      <stop offset="50%" stop-color="#0F131D"/>
      <stop offset="100%" stop-color="#07080C"/>
    </linearGradient>

    <linearGradient id="ph-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C8F75A"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="380" rx="16" fill="url(#ph-bg)"/>
  <rect width="1198" height="378" x="1" y="1" rx="15" fill="none" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#ph-line)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Top Title Strip -->
  <g transform="translate(48, 44)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#C8F75A" letter-spacing="1.5">
      // CHAPTER 02 • ENGINEERING METHODOLOGY
    </text>
    <text x="0" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF" letter-spacing="-0.8">
      HOW I BUILD: THE THREE AXIOMS
    </text>
    <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="14" fill="#94A3B8">
      Software is not merely code; it is a synthesis of interaction physics, resilient architecture, and mathematical discipline.
    </text>
  </g>

  <!-- 3 Pillar Columns -->
  <g transform="translate(48, 144)">
    <!-- Pillar 1 -->
    <g transform="translate(0, 0)">
      <rect width="348" height="190" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(200, 247, 90, 0.25)" stroke-width="1"/>
      <text x="24" y="36" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#C8F75A">AXIOM 01</text>
      <text x="24" y="64" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Zero Latency by Default</text>
      <text x="24" y="94" font-family="-apple-system, sans-serif" font-size="13" fill="#CBD5E1">Prioritize on-device state (IndexedDB)</text>
      <text x="24" y="114" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">over superfluous remote roundtrips.</text>
      <text x="24" y="134" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">Immediate user feedback without spinners</text>
      <text x="24" y="162" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#C8F75A">→ LOCAL-FIRST PERSISTENCE</text>
    </g>

    <!-- Pillar 2 -->
    <g transform="translate(378, 0)">
      <rect width="348" height="190" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(56, 189, 248, 0.25)" stroke-width="1"/>
      <text x="24" y="36" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#38BDF8">AXIOM 02</text>
      <text x="24" y="64" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Mathematical Aesthetics</text>
      <text x="24" y="94" font-family="-apple-system, sans-serif" font-size="13" fill="#CBD5E1">Kinematic physics, drift vectors,</text>
      <text x="24" y="114" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">procedural Web Audio oscillators,</text>
      <text x="24" y="134" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">and responsive parametric 3D lattices.</text>
      <text x="24" y="162" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#38BDF8">→ CANVAS 2D &amp; THREE.JS</text>
    </g>

    <!-- Pillar 3 -->
    <g transform="translate(756, 0)">
      <rect width="348" height="190" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1"/>
      <text x="24" y="36" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#A855F7">AXIOM 03</text>
      <text x="24" y="64" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Evidence Before Claims</text>
      <text x="24" y="94" font-family="-apple-system, sans-serif" font-size="13" fill="#CBD5E1">No hand-wavy claims of performance.</text>
      <text x="24" y="114" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">Every state transition is guarded by</text>
      <text x="24" y="134" font-family="-apple-system, sans-serif" font-size="13" fill="#94A3B8">automated Vitest unit &amp; Playwright tests.</text>
      <text x="24" y="162" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#A855F7">→ 100% VERIFIED SUITES</text>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "systems", "philosophy.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(phil_svg)
    ET.fromstring(phil_svg)
    print("[OK] philosophy.svg verified valid XML")

# ---------------------------------------------------------------------------
# 8. CLOSING FRAME / TRANSMISSION END (1200 x 300)
# ---------------------------------------------------------------------------
def generate_closing_frame():
    closing_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="100%" height="auto">
  <defs>
    <linearGradient id="cl-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08090C"/>
      <stop offset="50%" stop-color="#0F121A"/>
      <stop offset="100%" stop-color="#05070A"/>
    </linearGradient>

    <linearGradient id="cl-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C8F75A"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="300" rx="16" fill="url(#cl-bg)"/>
  <rect width="1198" height="298" x="1" y="1" rx="15" fill="none" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
  <path d="M 20 1 L 1180 1" stroke="url(#cl-accent)" stroke-width="2" stroke-linecap="round"/>

  <!-- Closing Narrative -->
  <g transform="translate(64, 60)">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#C8F75A" letter-spacing="2">
      // CHAPTER 05 • END OF TRANSMISSION
    </text>
    <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="44" font-weight="900" fill="#FFFFFF" letter-spacing="-1.5">
      LET'S BUILD SOMETHING EXTRAORDINARY.
    </text>
    <text x="0" y="80" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">
      Open for ambitious technical collaborations, software engineering internships, and research initiatives.
    </text>

    <!-- Verified Channels -->
    <g transform="translate(0, 118)">
      <rect x="0" y="0" width="220" height="42" rx="8" fill="rgba(200, 247, 90, 0.08)" stroke="rgba(200, 247, 90, 0.3)" stroke-width="1"/>
      <circle cx="20" cy="21" r="5" fill="#C8F75A"/>
      <text x="36" y="26" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#C8F75A">github/leinhabersv-bit</text>

      <rect x="236" y="0" width="310" height="42" rx="8" fill="rgba(56, 189, 248, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
      <circle cx="256" cy="21" r="5" fill="#38BDF8"/>
      <text x="272" y="26" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#38BDF8">developer-portfolio-eta-steel.vercel.app</text>

      <rect x="562" y="0" width="250" height="42" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1"/>
      <circle cx="582" cy="21" r="5" fill="#FFFFFF"/>
      <text x="598" y="26" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="#E2E8F0">leinhabersv@gmail.com</text>
    </g>
  </g>
</svg>'''

    target = os.path.join(ASSETS_DIR, "closing", "frame.svg")
    with open(target, "w", encoding="utf-8") as f:
        f.write(closing_svg)
    ET.fromstring(closing_svg)
    print("[OK] frame.svg verified valid XML")

if __name__ == "__main__":
    ensure_dirs()
    generate_hero()
    generate_monogram()
    generate_panic_card()
    generate_clientlaunch_card()
    generate_eventhub_card()
    generate_mic_card()
    generate_philosophy()
    generate_closing_frame()
    print("\nALL 8 EXHIBITION ASSETS GENERATED AND VALIDATED SUCCESSFULLY!")
