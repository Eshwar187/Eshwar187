import base64
import json
import os
import xml.etree.ElementTree as ET

# Load fonts
with open('assets/fonts/SpaceGrotesk-Bold.woff2', 'rb') as f:
    sg_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('assets/fonts/JetBrainsMono-SemiBold.woff2', 'rb') as f:
    jb_b64 = base64.b64encode(f.read()).decode('utf-8')

# Load images
with open('assets/id.png', 'rb') as f:
    id_png_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('assets/right_pointing.png', 'rb') as f:
    rp_png_b64 = base64.b64encode(f.read()).decode('utf-8')

# Load icons
with open('assets/icons.json', 'r', encoding='utf-8') as f:
    icons = json.load(f)

# AI / ML neural chip icon path
icons['aiml'] = 'M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h2a3 3 0 0 1 3 3v1.27c.6-.34 1-.99 1-1.73a2 2 0 1 1 2 2c0 .74-.4 1.39-1 1.73V15a3 3 0 0 1-3 3h-2v1.27c.6.34 1 .99 1 1.73a2 2 0 1 1-2 2c0-.74-.4-1.39-1-1.73V19h-2a3 3 0 0 1-3-3v-1.27c-.6.34-1 .99-1 1.73a2 2 0 1 1-2-2c0-.74.4-1.39 1-1.73V10a3 3 0 0 1 3-3h2V5.73C9.4 5.39 9 4.74 9 4a2 2 0 0 1 2-2zm-1 7H9a1 1 0 0 0-1 1v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4a1 1 0 0 0-1-1zm4 0h-2v6h2a1 1 0 0 0 1-1v-4a1 1 0 0 0-1-1z'

# Common font face CSS
FONT_CSS = f"""
    @font-face {{
      font-family: 'Space Grotesk';
      font-style: normal;
      font-weight: 700;
      src: url("data:font/woff2;base64,{sg_b64}") format("woff2");
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 600;
      src: url("data:font/woff2;base64,{jb_b64}") format("woff2");
    }}
"""

# ==============================================================================
# 1. HERO SVG (HIGH POLISH & KINETIC ANIMATIONS)
# ==============================================================================
def build_hero():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 850 420" width="100%" height="100%">
  <defs>
    <style><![CDATA[
{FONT_CSS}
      .hero-font-display {{
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
      }}
      .hero-font-mono {{
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-weight: 600;
      }}
      
      /* Sweeping Cyber Laser Beam */
      @keyframes heroScanSweep {{
        0% {{ transform: translateY(15px); opacity: 0; }}
        15% {{ opacity: 0.55; }}
        85% {{ opacity: 0.55; }}
        100% {{ transform: translateY(405px); opacity: 0; }}
      }}
      .hero-scan-line {{
        animation: heroScanSweep 6s ease-in-out infinite;
      }}

      /* Monospace Terminal Cursor Blink */
      @keyframes heroCursorBlink {{
        0%, 45% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      .hero-cursor {{
        animation: heroCursorBlink 0.85s infinite;
      }}
      
      /* Rising-Mask Name Reveal */
      @keyframes heroNameReveal {{
        0% {{
          transform: translateY(75px);
          opacity: 0;
        }}
        100% {{
          transform: translateY(0);
          opacity: 1;
        }}
      }}
      .hero-name-target {{
        animation: heroNameReveal 1.3s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both;
      }}

      /* Shimmering Text Gradient Across Name */
      @keyframes heroShimmer {{
        0% {{ stop-color: #ffffff; }}
        50% {{ stop-color: #38bdf8; }}
        100% {{ stop-color: #ffffff; }}
      }}
      
      /* Cycling Roles Animation (12s total loop, 3s per role) */
      @keyframes heroRole1 {{
        0%, 3% {{ opacity: 0; transform: translateY(14px); }}
        6%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes heroRole2 {{
        0%, 25% {{ opacity: 0; transform: translateY(14px); }}
        28%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes heroRole3 {{
        0%, 50% {{ opacity: 0; transform: translateY(14px); }}
        53%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes heroRole4 {{
        0%, 75% {{ opacity: 0; transform: translateY(14px); }}
        78%, 97% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      
      .hero-role-1 {{ animation: heroRole1 12s infinite; }}
      .hero-role-2 {{ animation: heroRole2 12s infinite; opacity: 0; }}
      .hero-role-3 {{ animation: heroRole3 12s infinite; opacity: 0; }}
      .hero-role-4 {{ animation: heroRole4 12s infinite; opacity: 0; }}
      
      /* Radar Beacon Pulse */
      @keyframes heroBeaconPulse {{
        0% {{ r: 3.5px; opacity: 0.95; }}
        70% {{ r: 11px; opacity: 0; }}
        100% {{ r: 11px; opacity: 0; }}
      }}
      .hero-radar-ring {{
        animation: heroBeaconPulse 2s cubic-bezier(0, 0.2, 0.8, 1) infinite;
      }}
      
      /* Portrait Float and Aura Breathing */
      @keyframes heroFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-5px); }}
      }}
      .hero-portrait-card {{
        animation: heroFloat 5s ease-in-out infinite;
      }}

      /* Rotating Reticle / Corner brackets */
      @keyframes heroCornerSpin {{
        0% {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: 40; }}
      }}
      .hero-reticle-anim {{
        animation: heroCornerSpin 4s linear infinite;
      }}

      /* Reduced Motion Override */
      @media (prefers-reduced-motion: reduce) {{
        .hero-scan-line {{ display: none !important; }}
        .hero-name-target {{ animation: none !important; transform: none !important; opacity: 1 !important; }}
        .hero-role-1 {{ animation: none !important; opacity: 1 !important; transform: none !important; }}
        .hero-role-2, .hero-role-3, .hero-role-4 {{ display: none !important; }}
        .hero-cursor {{ animation: none !important; opacity: 1 !important; }}
        .hero-radar-ring {{ animation: none !important; opacity: 0 !important; }}
        .hero-portrait-card {{ animation: none !important; transform: none !important; }}
      }}
    ]]></style>

    <pattern id="hero-dots" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.14" />
    </pattern>

    <linearGradient id="hero-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="70%" stop-color="#a855f7" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.75" />
    </linearGradient>

    <linearGradient id="hero-name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="45%" stop-color="#f0f6ff" />
      <stop offset="85%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#247bff" />
    </linearGradient>

    <linearGradient id="hero-scan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0" />
      <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.7" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.9" />
      <stop offset="75%" stop-color="#38bdf8" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="hero-avatar-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.85" />
    </linearGradient>

    <radialGradient id="hero-glow-1" cx="20%" cy="25%" r="48%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.22" />
      <stop offset="100%" stop-color="#247bff" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="hero-glow-2" cx="85%" cy="80%" r="45%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.18" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0" />
    </radialGradient>

    <clipPath id="hero-name-clip">
      <rect x="40" y="98" width="530" height="78" />
    </clipPath>

    <clipPath id="hero-portrait-clip">
      <rect x="585" y="42" width="225" height="336" rx="20" />
    </clipPath>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="850" height="420" rx="22" fill="#070b16" />
  <rect width="850" height="420" rx="22" fill="url(#hero-dots)" />
  <rect width="850" height="420" rx="22" fill="url(#hero-glow-1)" />
  <rect width="850" height="420" rx="22" fill="url(#hero-glow-2)" />

  <!-- Animated Cybernetic Scanning Laser Beam -->
  <line class="hero-scan-line" x1="20" y1="0" x2="830" y2="0" stroke="url(#hero-scan-grad)" stroke-width="1.6" filter="drop-shadow(0 0 6px #38bdf8)" />

  <!-- Hairline Gradient Outer Border -->
  <rect width="850" height="420" rx="22" fill="none" stroke="url(#hero-border-grad)" stroke-width="1.3" />

  <!-- LEFT CONTENT COLUMN -->
  <g transform="translate(42, 0)">
    <!-- Top Status Badge -->
    <g transform="translate(0, 36)">
      <rect x="0" y="0" width="295" height="28" rx="14" fill="#0c162e" stroke="#247bff" stroke-opacity="0.4" stroke-width="1" />
      <!-- Pulsing Beacon -->
      <circle cx="16" cy="14" r="3.5" fill="#10b981" />
      <circle class="hero-radar-ring" cx="16" cy="14" r="3.5" fill="none" stroke="#10b981" stroke-width="1.6" opacity="0.85" />
      <text x="28" y="18" class="hero-font-mono" font-size="10.5" fill="#94a3b8" letter-spacing="0.5">SYSTEM::ONLINE • OCT 2026 AUDIT</text>
    </g>

    <!-- Typed Greeting with Terminal Prompt -->
    <g transform="translate(0, 88)">
      <text x="0" y="0" class="hero-font-mono" font-size="14.5" fill="#38bdf8" letter-spacing="0.2">
        <tspan fill="#64748b">&gt;</tspan> console.log("Hello, World! I am")<tspan class="hero-cursor" fill="#ff354f">_</tspan>
      </text>
    </g>

    <!-- Rising-Mask Name Reveal -->
    <g clip-path="url(#hero-name-clip)">
      <g class="hero-name-target">
        <text x="40" y="160" class="hero-font-display" font-size="58" fill="url(#hero-name-grad)" letter-spacing="-1">ESHWAR J</text>
      </g>
    </g>

    <!-- Cycling Roles Showcase -->
    <g transform="translate(0, 196)">
      <!-- Role Container Badge -->
      <rect x="0" y="0" width="370" height="36" rx="18" fill="#0b1630" stroke="#247bff" stroke-opacity="0.5" stroke-width="1.2" />
      <!-- Pulsing role indicator -->
      <circle cx="18" cy="18" r="4.5" fill="#ff354f" />
      <circle cx="18" cy="18" r="7.5" fill="none" stroke="#ff354f" stroke-width="1" opacity="0.4" />
      <text x="32" y="22.5" class="hero-font-mono" font-size="10.5" fill="#64748b" letter-spacing="1">ROLE :</text>
      
      <!-- Role 1: Full Stack Developer -->
      <g class="hero-role-1">
        <text x="84" y="23" class="hero-font-mono" font-size="13" fill="#ffffff" font-weight="700">Full Stack Developer</text>
      </g>
      <!-- Role 2: AI/ML Developer -->
      <g class="hero-role-2">
        <text x="84" y="23" class="hero-font-mono" font-size="13" fill="#38bdf8" font-weight="700">AI/ML Developer</text>
      </g>
      <!-- Role 3: Backend Developer -->
      <g class="hero-role-3">
        <text x="84" y="23" class="hero-font-mono" font-size="13" fill="#ff354f" font-weight="700">Backend Developer</text>
      </g>
      <!-- Role 4: DevOps & Cloud Enthusiast -->
      <g class="hero-role-4">
        <text x="84" y="23" class="hero-font-mono" font-size="13" fill="#c084fc" font-weight="700">DevOps &amp; Cloud Enthusiast</text>
      </g>
    </g>

    <!-- One-Line Pitch -->
    <g transform="translate(0, 262)">
      <text class="hero-font-display" font-size="15" fill="#cbd5e1" letter-spacing="-0.1">
        <tspan x="0" y="0">I build scalable full-stack applications and AI-powered</tspan>
        <tspan x="0" y="24">systems that solve real-world problems.</tspan>
      </text>
    </g>

    <!-- Location & Status Row -->
    <g transform="translate(0, 335)">
      <!-- Location Pill -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="180" height="32" rx="8" fill="#091224" stroke="#1e293b" stroke-width="1" />
        <!-- Map Pin Icon -->
        <path d="M12 4a5 5 0 0 0-5 5c0 4 5 9 5 9s5-5 5-9a5 5 0 0 0-5-5zm0 7a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" transform="translate(8, 7) scale(0.85)" fill="#38bdf8" />
        <text x="32" y="20" class="hero-font-mono" font-size="10.5" fill="#94a3b8">Chennai, Tamil Nadu</text>
      </g>

      <!-- Repo Stat Pill -->
      <g transform="translate(190, 0)">
        <rect x="0" y="0" width="170" height="32" rx="8" fill="#091224" stroke="#1e293b" stroke-width="1" />
        <!-- Code Branch Icon -->
        <path d="M17 12a3 3 0 0 0-2.82 2H9.82A3 3 0 0 0 7 12a3 3 0 0 0-2.82 2H3v2h1.18A3 3 0 0 0 7 18a3 3 0 0 0 2.82-2h4.36A3 3 0 0 0 17 18a3 3 0 0 0 3-3 3 3 0 0 0-3-3z" transform="translate(8, 7) scale(0.8)" fill="#ff354f" />
        <text x="30" y="20" class="hero-font-mono" font-size="10.5" fill="#94a3b8">139 Public Repos</text>
      </g>

      <!-- Available Pill -->
      <g transform="translate(370, 0)">
        <rect x="0" y="0" width="160" height="32" rx="8" fill="#091224" stroke="#247bff" stroke-opacity="0.4" stroke-width="1" />
        <circle cx="16" cy="16" r="3.5" fill="#10b981" />
        <text x="28" y="20" class="hero-font-mono" font-size="10" fill="#38bdf8">High-Impact Roles</text>
      </g>
    </g>
  </g>

  <!-- RIGHT PORTRAIT SHOWCASE -->
  <g class="hero-portrait-card">
    <!-- Ambient Aura Glow Behind Portrait -->
    <rect x="578" y="35" width="239" height="350" rx="26" fill="#247bff" fill-opacity="0.18" filter="blur(14px)" />
    <!-- Outer Card Frame -->
    <rect x="585" y="42" width="225" height="336" rx="20" fill="#080e1d" />
    
    <!-- Inlined PNG Portrait (Exact Image & Alpha Preserved) -->
    <g clip-path="url(#hero-portrait-clip)">
      <image href="data:image/png;base64,{id_png_b64}" x="585" y="42" width="225" height="336" preserveAspectRatio="xMidYMid meet" />
      <!-- Subtle internal bottom gradient vignette -->
      <rect x="585" y="260" width="225" height="120" fill="url(#hero-vignette)" />
    </g>
    
    <!-- Hairline Gradient Border on Top of Image -->
    <rect x="585" y="42" width="225" height="336" rx="20" fill="none" stroke="url(#hero-avatar-border)" stroke-width="1.6" />
    
    <!-- Corner Tech Reticle Marks -->
    <path class="hero-reticle-anim" d="M595 56 L612 56 M595 56 L595 73" stroke="#38bdf8" stroke-width="2" fill="none" stroke-linecap="round" />
    <path class="hero-reticle-anim" d="M800 56 L783 56 M800 56 L800 73" stroke="#38bdf8" stroke-width="2" fill="none" stroke-linecap="round" />
    <path class="hero-reticle-anim" d="M595 364 L612 364 M595 364 L595 347" stroke="#ff354f" stroke-width="2" fill="none" stroke-linecap="round" />
    <path class="hero-reticle-anim" d="M800 364 L783 364 M800 364 L800 347" stroke="#ff354f" stroke-width="2" fill="none" stroke-linecap="round" />

    <!-- Portrait Verified Footer Tab -->
    <g transform="translate(600, 336)">
      <rect x="0" y="0" width="195" height="28" rx="8" fill="#070b16" fill-opacity="0.9" stroke="#247bff" stroke-opacity="0.6" stroke-width="1" />
      <!-- Shield / Check Icon -->
      <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" transform="translate(8, 5) scale(0.75)" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      <text x="30" y="18" class="hero-font-mono" font-size="10.5" fill="#f1f5f9" font-weight="700">VERIFIED DEV // OCT 2026</text>
    </g>
  </g>

  <!-- Defs: Vignette Gradient -->
  <defs>
    <linearGradient id="hero-vignette" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#070b16" stop-opacity="0" />
      <stop offset="100%" stop-color="#070b16" stop-opacity="0.9" />
    </linearGradient>
  </defs>
</svg>"""
    return svg

# ==============================================================================
# 2. ABOUT-LIFE SVG (HUD TELEMETRY & 3-SLIDE CAROUSEL)
# ==============================================================================
def build_about_life():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 850 410" width="100%" height="100%">
  <defs>
    <style><![CDATA[
{FONT_CSS}
      .about-font-display {{
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
      }}
      .about-font-mono {{
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-weight: 600;
      }}

      /* 3-Slide Carousel cycling every 4s (12s total loop) */
      @keyframes aboutSlide1 {{
        0%, 30% {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
        33.3%, 97% {{ opacity: 0; transform: translateY(12px); pointer-events: none; }}
        100% {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
      }}
      @keyframes aboutSlide2 {{
        0%, 30% {{ opacity: 0; transform: translateY(12px); pointer-events: none; }}
        33.3%, 63% {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
        66.6%, 100% {{ opacity: 0; transform: translateY(12px); pointer-events: none; }}
      }}
      @keyframes aboutSlide3 {{
        0%, 63% {{ opacity: 0; transform: translateY(12px); pointer-events: none; }}
        66.6%, 97% {{ opacity: 1; transform: translateY(0); pointer-events: auto; }}
        100% {{ opacity: 0; transform: translateY(12px); pointer-events: none; }}
      }}

      .about-slide-1 {{ animation: aboutSlide1 12s cubic-bezier(0.2, 0.8, 0.2, 1) infinite; }}
      .about-slide-2 {{ animation: aboutSlide2 12s cubic-bezier(0.2, 0.8, 0.2, 1) infinite; opacity: 0; }}
      .about-slide-3 {{ animation: aboutSlide3 12s cubic-bezier(0.2, 0.8, 0.2, 1) infinite; opacity: 0; }}

      /* Segment Progress Bar Fills */
      @keyframes aboutProgressSeg1 {{
        0% {{ width: 0px; }}
        33.3% {{ width: 110px; }}
        98% {{ width: 110px; }}
        100% {{ width: 0px; }}
      }}
      @keyframes aboutProgressSeg2 {{
        0%, 33.3% {{ width: 0px; }}
        66.6% {{ width: 110px; }}
        98% {{ width: 110px; }}
        100% {{ width: 0px; }}
      }}
      @keyframes aboutProgressSeg3 {{
        0%, 66.6% {{ width: 0px; }}
        98% {{ width: 110px; }}
        100% {{ width: 0px; }}
      }}

      .about-bar-fill-1 {{ animation: aboutProgressSeg1 12s linear infinite; }}
      .about-bar-fill-2 {{ animation: aboutProgressSeg2 12s linear infinite; width: 0px; }}
      .about-bar-fill-3 {{ animation: aboutProgressSeg3 12s linear infinite; width: 0px; }}

      /* Active Pulse on Capability Cards */
      @keyframes aboutTelemetryPulse {{
        0%, 100% {{ opacity: 0.8; }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 5px #38bdf8); }}
      }}
      .about-pulse-tag {{
        animation: aboutTelemetryPulse 3s ease-in-out infinite;
      }}

      /* Reduced Motion Override */
      @media (prefers-reduced-motion: reduce) {{
        .about-slide-1 {{ animation: none !important; opacity: 1 !important; transform: none !important; }}
        .about-slide-2, .about-slide-3 {{ display: none !important; }}
        .about-bar-fill-1 {{ animation: none !important; width: 110px !important; }}
        .about-bar-fill-2, .about-bar-fill-3 {{ animation: none !important; width: 0px !important; }}
        .about-pulse-tag {{ animation: none !important; }}
      }}
    ]]></style>

    <pattern id="about-dots" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12" />
    </pattern>

    <linearGradient id="about-card-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.6" />
    </linearGradient>

    <linearGradient id="about-seg-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff" />
      <stop offset="60%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>
  </defs>

  <!-- Base Canvas -->
  <rect width="850" height="410" rx="22" fill="#070b16" />
  <rect width="850" height="410" rx="22" fill="url(#about-dots)" />
  <rect width="850" height="410" rx="22" fill="none" stroke="url(#about-card-stroke)" stroke-width="1.3" />

  <!-- LEFT PANEL: Core Architectural Capabilities -->
  <g transform="translate(25, 24)">
    <rect width="385" height="362" rx="18" fill="#090f20" stroke="#1e293b" stroke-width="1" />
    
    <!-- Left Header -->
    <g transform="translate(24, 26)">
      <text x="0" y="0" class="about-font-mono" font-size="10.5" fill="#38bdf8" letter-spacing="1">// SYSTEM LANDSCAPE</text>
      <text x="0" y="24" class="about-font-display" font-size="20" fill="#ffffff">Architectural Capabilities</text>
      <text x="0" y="42" class="about-font-mono" font-size="11" fill="#64748b">Production-grade competencies across the stack</text>
    </g>

    <!-- Capabilities List -->
    <g transform="translate(24, 88)">
      <!-- Capability 1: Full-Stack Architecture -->
      <g transform="translate(0, 0)">
        <rect width="337" height="58" rx="10" fill="#0c162e" stroke="#247bff" stroke-opacity="0.3" stroke-width="1" />
        <circle cx="20" cy="22" r="10" fill="#247bff" fill-opacity="0.2" />
        <!-- Layers Icon -->
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" transform="translate(13, 15) scale(0.6)" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <text x="38" y="20" class="about-font-display" font-size="13" fill="#f8fafc">Full-Stack Architecture</text>
        <text x="38" y="34" class="about-font-mono" font-size="9.5" fill="#94a3b8">Reactive frontends, REST &amp; WebSocket microservices</text>
        <text x="38" y="47" class="about-font-mono" font-size="9" fill="#38bdf8">SvelteKit • TypeScript • Node.js • ASP.NET Core</text>
        <!-- Telemetry Status Tag -->
        <g class="about-pulse-tag" transform="translate(242, 10)">
          <rect width="84" height="15" rx="4" fill="#172554" />
          <text x="6" y="11" class="about-font-mono" font-size="7.5" fill="#93c5fd">THROUGHPUT // HI</text>
        </g>
      </g>

      <!-- Capability 2: AI/ML & Intelligent Systems -->
      <g transform="translate(0, 66)">
        <rect width="337" height="58" rx="10" fill="#0c162e" stroke="#ff354f" stroke-opacity="0.3" stroke-width="1" />
        <circle cx="20" cy="22" r="10" fill="#ff354f" fill-opacity="0.2" />
        <!-- Brain / Neural Icon -->
        <path d="{icons['aiml']}" transform="translate(12, 14) scale(0.65)" fill="#ff354f" />
        <text x="38" y="20" class="about-font-display" font-size="13" fill="#f8fafc">AI/ML &amp; Intelligent Systems</text>
        <text x="38" y="34" class="about-font-mono" font-size="9.5" fill="#94a3b8">Sybil fraud detection, entity graphs &amp; risk engines</text>
        <text x="38" y="47" class="about-font-mono" font-size="9" fill="#ff7686">Python • Graph Analysis • Behavioral ML • Scoring</text>
        <!-- Telemetry Status Tag -->
        <g class="about-pulse-tag" transform="translate(242, 10)">
          <rect width="84" height="15" rx="4" fill="#331018" />
          <text x="6" y="11" class="about-font-mono" font-size="7.5" fill="#fca5a5">GRAPH INFERENCE</text>
        </g>
      </g>

      <!-- Capability 3: Zero-Trust Security & Systems -->
      <g transform="translate(0, 132)">
        <rect width="337" height="58" rx="10" fill="#0c162e" stroke="#10b981" stroke-opacity="0.3" stroke-width="1" />
        <circle cx="20" cy="22" r="10" fill="#10b981" fill-opacity="0.2" />
        <!-- Lock Icon -->
        <path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" transform="translate(13, 14) scale(0.6)" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <text x="38" y="20" class="about-font-display" font-size="13" fill="#f8fafc">Zero-Trust &amp; Runtime Security</text>
        <text x="38" y="34" class="about-font-mono" font-size="9.5" fill="#94a3b8">AES-256 encryption, RBAC &amp; sandboxed execution</text>
        <text x="38" y="47" class="about-font-mono" font-size="9" fill="#34d399">Zero-Trust • Roslyn API • Session Hardening • Redis</text>
        <!-- Telemetry Status Tag -->
        <g class="about-pulse-tag" transform="translate(242, 10)">
          <rect width="84" height="15" rx="4" fill="#062e20" />
          <text x="6" y="11" class="about-font-mono" font-size="7.5" fill="#86efac">AES-256 ENCRYPT</text>
        </g>
      </g>

      <!-- Capability 4: Cloud & DevOps Infrastructure -->
      <g transform="translate(0, 198)">
        <rect width="337" height="58" rx="10" fill="#0c162e" stroke="#a78bfa" stroke-opacity="0.3" stroke-width="1" />
        <circle cx="20" cy="22" r="10" fill="#a78bfa" fill-opacity="0.2" />
        <!-- Cloud / Terminal Icon -->
        <path d="M4 17l6-6-6-6m8 14h8" transform="translate(13, 15) scale(0.6)" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <text x="38" y="20" class="about-font-display" font-size="13" fill="#f8fafc">Cloud &amp; DevOps Engineering</text>
        <text x="38" y="34" class="about-font-mono" font-size="9.5" fill="#94a3b8">Automated CI/CD pipelines &amp; container runtimes</text>
        <text x="38" y="47" class="about-font-mono" font-size="9" fill="#c4b5fd">Docker • GitHub Actions • Google Cloud • PostgreSQL</text>
        <!-- Telemetry Status Tag -->
        <g class="about-pulse-tag" transform="translate(242, 10)">
          <rect width="84" height="15" rx="4" fill="#241038" />
          <text x="6" y="11" class="about-font-mono" font-size="7.5" fill="#d8b4fe">CI/CD AUTOMATED</text>
        </g>
      </g>
    </g>
  </g>

  <!-- RIGHT PANEL: 3-Slide Interests Carousel (4s per slide) -->
  <g transform="translate(435, 24)">
    <rect width="390" height="362" rx="18" fill="#090f20" stroke="#1e293b" stroke-width="1" />

    <!-- Right Header & Progress Indicator -->
    <g transform="translate(24, 26)">
      <text x="0" y="0" class="about-font-mono" font-size="10.5" fill="#ff354f" letter-spacing="1">// PASSIONS &amp; FOCUS</text>
      <text x="0" y="24" class="about-font-display" font-size="20" fill="#ffffff">Interests Carousel</text>
      <text x="240" y="22" class="about-font-mono" font-size="11" fill="#64748b">4s INTERVALS</text>
    </g>

    <!-- Segment Progress Bars (3 Segments with Glowing Head) -->
    <g transform="translate(24, 68)">
      <!-- Seg 1 Track & Fill -->
      <g transform="translate(0, 0)">
        <rect width="110" height="4" rx="2" fill="#182238" />
        <rect class="about-bar-fill-1" height="4" rx="2" fill="url(#about-seg-grad)" />
      </g>
      <!-- Seg 2 Track & Fill -->
      <g transform="translate(116, 0)">
        <rect width="110" height="4" rx="2" fill="#182238" />
        <rect class="about-bar-fill-2" height="4" rx="2" fill="url(#about-seg-grad)" />
      </g>
      <!-- Seg 3 Track & Fill -->
      <g transform="translate(232, 0)">
        <rect width="110" height="4" rx="2" fill="#182238" />
        <rect class="about-bar-fill-3" height="4" rx="2" fill="url(#about-seg-grad)" />
      </g>
    </g>

    <!-- Carousel Container -->
    <g transform="translate(24, 92)">
      <!-- SLIDE 1: Coding -->
      <g class="about-slide-1">
        <rect width="342" height="248" rx="14" fill="#0b1428" stroke="#247bff" stroke-opacity="0.35" stroke-width="1.2" />
        <!-- Badge -->
        <g transform="translate(20, 20)">
          <rect width="110" height="24" rx="12" fill="#247bff" fill-opacity="0.18" stroke="#247bff" stroke-opacity="0.4" stroke-width="1" />
          <text x="14" y="16" class="about-font-mono" font-size="10" fill="#38bdf8" font-weight="700">01 / CODING</text>
        </g>
        <!-- Title -->
        <text x="20" y="74" class="about-font-display" font-size="19" fill="#ffffff">Architecture &amp; Clean Code</text>
        <!-- Body -->
        <text class="about-font-mono" font-size="11.5" fill="#94a3b8" letter-spacing="-0.1">
          <tspan x="20" y="104">Crafting high-throughput async backends,</tspan>
          <tspan x="20" y="124">event loops, and modular domain architectures.</tspan>
          <tspan x="20" y="144">Obsessed with type-safety, maintainability,</tspan>
          <tspan x="20" y="164">and zero-bloat reactive frontends.</tspan>
        </text>
        <!-- Key Points -->
        <g transform="translate(20, 192)">
          <rect width="90" height="24" rx="6" fill="#132347" />
          <text x="10" y="16" class="about-font-mono" font-size="9.5" fill="#cbd5e1">Async I/O</text>

          <rect x="98" y="0" width="105" height="24" rx="6" fill="#132347" />
          <text x="108" y="16" class="about-font-mono" font-size="9.5" fill="#cbd5e1">Clean Patterns</text>

          <rect x="211" y="0" width="85" height="24" rx="6" fill="#132347" />
          <text x="221" y="16" class="about-font-mono" font-size="9.5" fill="#cbd5e1">Type Safety</text>
        </g>
      </g>

      <!-- SLIDE 2: DSA & Problem Solving -->
      <g class="about-slide-2">
        <rect width="342" height="248" rx="14" fill="#0b1428" stroke="#ff354f" stroke-opacity="0.35" stroke-width="1.2" />
        <!-- Badge -->
        <g transform="translate(20, 20)">
          <rect width="135" height="24" rx="12" fill="#ff354f" fill-opacity="0.18" stroke="#ff354f" stroke-opacity="0.4" stroke-width="1" />
          <text x="14" y="16" class="about-font-mono" font-size="10" fill="#ff6b81" font-weight="700">02 / DSA &amp; THEORY</text>
        </g>
        <!-- Title -->
        <text x="20" y="74" class="about-font-display" font-size="19" fill="#ffffff">Algorithmic Problem Solving</text>
        <!-- Body -->
        <text class="about-font-mono" font-size="11.5" fill="#94a3b8" letter-spacing="-0.1">
          <tspan x="20" y="104">Deep rigor in data structures, graph traversal,</tspan>
          <tspan x="20" y="124">and sandboxed execution engines.</tspan>
          <tspan x="20" y="144">Architect of PrepArena — executing student</tspan>
          <tspan x="20" y="164">code safely via Roslyn Scripting &amp; Redis.</tspan>
        </text>
        <!-- Key Points -->
        <g transform="translate(20, 192)">
          <rect width="100" height="24" rx="6" fill="#2d1420" />
          <text x="10" y="16" class="about-font-mono" font-size="9.5" fill="#fca5a5">Graph Theory</text>

          <rect x="108" y="0" width="95" height="24" rx="6" fill="#2d1420" />
          <text x="118" y="16" class="about-font-mono" font-size="9.5" fill="#fca5a5">Code Sandbox</text>

          <rect x="211" y="0" width="85" height="24" rx="6" fill="#2d1420" />
          <text x="221" y="16" class="about-font-mono" font-size="9.5" fill="#fca5a5">Complexity</text>
        </g>
      </g>

      <!-- SLIDE 3: Building Side Projects -->
      <g class="about-slide-3">
        <rect width="342" height="248" rx="14" fill="#0b1428" stroke="#10b981" stroke-opacity="0.35" stroke-width="1.2" />
        <!-- Badge -->
        <g transform="translate(20, 20)">
          <rect width="145" height="24" rx="12" fill="#10b981" fill-opacity="0.18" stroke="#10b981" stroke-opacity="0.4" stroke-width="1" />
          <text x="14" y="16" class="about-font-mono" font-size="10" fill="#34d399" font-weight="700">03 / SIDE PROJECTS</text>
        </g>
        <!-- Title -->
        <text x="20" y="74" class="about-font-display" font-size="19" fill="#ffffff">Shipping Production MVPs</text>
        <!-- Body -->
        <text class="about-font-mono" font-size="11.5" fill="#94a3b8" letter-spacing="-0.1">
          <tspan x="20" y="104">Building end-to-end production systems:</tspan>
          <tspan x="20" y="124">• Abuse-Ring Sentinel (Sybil fraud graphs)</tspan>
          <tspan x="20" y="144">• AetherVault (Zero-trust AES-256 vault)</tspan>
          <tspan x="20" y="164">• PrepArena (Sandboxed DSA platform)</tspan>
        </text>
        <!-- Key Points -->
        <g transform="translate(20, 192)">
          <rect width="95" height="24" rx="6" fill="#0d291e" />
          <text x="10" y="16" class="about-font-mono" font-size="9.5" fill="#86efac">Vigil AI</text>

          <rect x="103" y="0" width="100" height="24" rx="6" fill="#0d291e" />
          <text x="113" y="16" class="about-font-mono" font-size="9.5" fill="#86efac">AetherVault</text>

          <rect x="211" y="0" width="95" height="24" rx="6" fill="#0d291e" />
          <text x="221" y="16" class="about-font-mono" font-size="9.5" fill="#86efac">PrepArena</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 3. STACK SVG (FLOWING PARTICLE ORBIT ACCELERATOR & HARMONIC OSCILLATIONS)
# ==============================================================================
def build_stack():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 850 510" width="100%" height="100%">
  <defs>
    <style><![CDATA[
{FONT_CSS}
      .stack-font-display {{
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
      }}
      .stack-font-mono {{
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-weight: 600;
      }}

      /* Continuous Flowing Orbital Streams (Particle Accelerator effect) */
      @keyframes stackOrbitDashCW {{
        from {{ stroke-dashoffset: 0; }}
        to {{ stroke-dashoffset: -120; }}
      }}
      @keyframes stackOrbitDashCCW {{
        from {{ stroke-dashoffset: 0; }}
        to {{ stroke-dashoffset: 120; }}
      }}
      
      .stack-orbit-1-stream {{
        animation: stackOrbitDashCW 7s linear infinite;
      }}
      .stack-orbit-2-stream {{
        animation: stackOrbitDashCCW 9s linear infinite;
      }}
      .stack-orbit-3-stream {{
        animation: stackOrbitDashCW 11s linear infinite;
      }}

      /* Harmonic Floating Nodes */
      @keyframes stackFloat1 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, -6px); }}
      }}
      @keyframes stackFloat2 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, 6px); }}
      }}
      @keyframes stackFloat3 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(-4px, -3px); }}
      }}
      @keyframes stackPulseCore {{
        0%, 100% {{ r: 32px; opacity: 0.85; filter: drop-shadow(0 0 8px #247bff); }}
        50% {{ r: 37px; opacity: 1; filter: drop-shadow(0 0 16px #38bdf8); }}
      }}

      .stack-node-f1 {{ animation: stackFloat1 4.5s ease-in-out infinite; }}
      .stack-node-f2 {{ animation: stackFloat2 5s ease-in-out infinite; }}
      .stack-node-f3 {{ animation: stackFloat3 5.5s ease-in-out infinite; }}
      .stack-core-pulse {{ animation: stackPulseCore 3s ease-in-out infinite; }}

      /* Core Gyroscope Spinner */
      @keyframes stackGyroSpin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
      }}
      .stack-gyro {{
        transform-origin: 425px 175px;
        animation: stackGyroSpin 12s linear infinite;
      }}

      /* Reduced motion */
      @media (prefers-reduced-motion: reduce) {{
        .stack-orbit-1-stream, .stack-orbit-2-stream, .stack-orbit-3-stream {{ animation: none !important; }}
        .stack-node-f1, .stack-node-f2, .stack-node-f3 {{ animation: none !important; transform: none !important; }}
        .stack-core-pulse {{ animation: none !important; r: 32px !important; }}
        .stack-gyro {{ animation: none !important; }}
      }}
    ]]></style>

    <pattern id="stack-dots" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12" />
    </pattern>

    <linearGradient id="stack-card-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7" />
    </linearGradient>

    <radialGradient id="stack-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.95" />
      <stop offset="45%" stop-color="#247bff" stop-opacity="0.65" />
      <stop offset="100%" stop-color="#070b16" stop-opacity="0" />
    </radialGradient>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="850" height="510" rx="22" fill="#070b16" />
  <rect width="850" height="510" rx="22" fill="url(#stack-dots)" />
  <rect width="850" height="510" rx="22" fill="none" stroke="url(#stack-card-stroke)" stroke-width="1.3" />

  <!-- Header Row -->
  <g transform="translate(36, 32)">
    <text x="0" y="0" class="stack-font-mono" font-size="10.5" fill="#38bdf8" letter-spacing="1">// SYSTEM TOPOLOGY</text>
    <text x="0" y="22" class="stack-font-display" font-size="20" fill="#ffffff">Orchestrated Technology Matrix</text>
    <text x="540" y="20" class="stack-font-mono" font-size="11" fill="#64748b">3 TILTED ELLIPTICAL ACCELERATORS</text>
  </g>

  <!-- ORBITAL PLANETARY SYSTEM (Center: 425, 175) -->
  <g transform="translate(0, 15)">
    <!-- Tilted Ellipses Container (-14 deg tilt) -->
    <g transform="rotate(-14 425 175)">
      <!-- Outer Orbit 3 (Flowing Stream) -->
      <ellipse class="stack-orbit-3-stream" cx="425" cy="175" rx="355" ry="120" fill="none" stroke="#ff354f" stroke-width="1.3" stroke-dasharray="6 7" stroke-opacity="0.45" />
      <!-- Middle Orbit 2 (Flowing Stream) -->
      <ellipse class="stack-orbit-2-stream" cx="425" cy="175" rx="265" ry="90" fill="none" stroke="#38bdf8" stroke-width="1.3" stroke-dasharray="5 6" stroke-opacity="0.55" />
      <!-- Inner Orbit 1 (Flowing Stream) -->
      <ellipse class="stack-orbit-1-stream" cx="425" cy="175" rx="175" ry="58" fill="none" stroke="#247bff" stroke-width="1.4" stroke-dasharray="4 5" stroke-opacity="0.65" />
    </g>

    <!-- Glowing Central Core with Gyroscope Ring -->
    <g transform="translate(425, 175)">
      <circle class="stack-core-pulse" r="32" fill="url(#stack-core-glow)" />
      <!-- Gyroscope Dash Ring -->
      <circle class="stack-gyro" r="26" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4" opacity="0.75" />
      <circle r="20" fill="#09132b" stroke="#38bdf8" stroke-width="1.5" />
      <!-- Central Spark / Core Icon -->
      <path d="M12 2L15 9L22 12L15 15L12 22L9 15L2 12L9 9Z" transform="translate(-12, -12)" fill="#38bdf8" />
      <text y="38" text-anchor="middle" class="stack-font-mono" font-size="9" fill="#94a3b8" letter-spacing="0.5">CORE ENGINE</text>
    </g>

    <!-- ORBIT 1 (INNER): Python, TypeScript, FastAPI, Node.js -->
    <!-- Node 1: Python -->
    <g class="stack-node-f1" transform="translate(265, 135)">
      <rect x="0" y="0" width="88" height="28" rx="14" fill="#0c1832" stroke="#3776ab" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(55,118,171,0.3))" />
      <path d="{icons['python']}" transform="translate(10, 6) scale(0.65)" fill="#3776ab" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">Python</text>
    </g>
    <!-- Node 2: TypeScript -->
    <g class="stack-node-f2" transform="translate(495, 200)">
      <rect x="0" y="0" width="112" height="28" rx="14" fill="#0c1832" stroke="#3178c6" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(49,120,198,0.3))" />
      <path d="{icons['typescript']}" transform="translate(10, 6) scale(0.65)" fill="#3178c6" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">TypeScript</text>
    </g>
    <!-- Node 3: FastAPI -->
    <g class="stack-node-f3" transform="translate(375, 100)">
      <rect x="0" y="0" width="94" height="28" rx="14" fill="#0c1832" stroke="#009688" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(0,150,136,0.3))" />
      <path d="{icons['fastapi']}" transform="translate(10, 6) scale(0.65)" fill="#009688" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">FastAPI</text>
    </g>
    <!-- Node 4: Node.js -->
    <g class="stack-node-f1" transform="translate(390, 235)">
      <rect x="0" y="0" width="96" height="28" rx="14" fill="#0c1832" stroke="#5fa04e" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(95,160,78,0.3))" />
      <path d="{icons['nodedotjs']}" transform="translate(10, 6) scale(0.65)" fill="#5fa04e" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">Node.js</text>
    </g>

    <!-- ORBIT 2 (MIDDLE): PostgreSQL, MongoDB, Docker, SvelteKit -->
    <!-- Node 5: PostgreSQL -->
    <g class="stack-node-f2" transform="translate(170, 120)">
      <rect x="0" y="0" width="114" height="28" rx="14" fill="#0c1832" stroke="#4169e1" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(65,105,225,0.3))" />
      <path d="{icons['postgresql']}" transform="translate(10, 6) scale(0.65)" fill="#4169e1" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">PostgreSQL</text>
    </g>
    <!-- Node 6: MongoDB -->
    <g class="stack-node-f1" transform="translate(605, 215)">
      <rect x="0" y="0" width="102" height="28" rx="14" fill="#0c1832" stroke="#47a248" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(71,162,72,0.3))" />
      <path d="{icons['mongodb']}" transform="translate(10, 6) scale(0.65)" fill="#47a248" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">MongoDB</text>
    </g>
    <!-- Node 7: Docker -->
    <g class="stack-node-f3" transform="translate(300, 65)">
      <rect x="0" y="0" width="90" height="28" rx="14" fill="#0c1832" stroke="#2496ed" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(36,150,237,0.3))" />
      <path d="{icons['docker']}" transform="translate(10, 6) scale(0.65)" fill="#2496ed" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">Docker</text>
    </g>
    <!-- Node 8: SvelteKit -->
    <g class="stack-node-f2" transform="translate(525, 260)">
      <rect x="0" y="0" width="104" height="28" rx="14" fill="#0c1832" stroke="#ff3e00" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(255,62,0,0.3))" />
      <path d="{icons['svelte']}" transform="translate(10, 6) scale(0.65)" fill="#ff3e00" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">SvelteKit</text>
    </g>

    <!-- ORBIT 3 (OUTER): GitHub Actions, Google Cloud, AI/ML, JavaScript -->
    <!-- Node 9: GitHub Actions -->
    <g class="stack-node-f1" transform="translate(85, 145)">
      <rect x="0" y="0" width="140" height="28" rx="14" fill="#0c1832" stroke="#2088ff" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(32,136,255,0.3))" />
      <path d="{icons['githubactions']}" transform="translate(10, 6) scale(0.65)" fill="#2088ff" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">GitHub Actions</text>
    </g>
    <!-- Node 10: Google Cloud -->
    <g class="stack-node-f2" transform="translate(685, 185)">
      <rect x="0" y="0" width="125" height="28" rx="14" fill="#0c1832" stroke="#4285f4" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(66,133,244,0.3))" />
      <path d="{icons['googlecloud']}" transform="translate(10, 6) scale(0.65)" fill="#4285f4" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">Google Cloud</text>
    </g>
    <!-- Node 11: AI/ML -->
    <g class="stack-node-f3" transform="translate(485, 52)">
      <rect x="0" y="0" width="90" height="28" rx="14" fill="#0c1832" stroke="#ff354f" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(255,53,79,0.3))" />
      <path d="{icons['aiml']}" transform="translate(10, 6) scale(0.65)" fill="#ff354f" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">AI / ML</text>
    </g>
    <!-- Node 12: JavaScript -->
    <g class="stack-node-f1" transform="translate(235, 255)">
      <rect x="0" y="0" width="112" height="28" rx="14" fill="#0c1832" stroke="#f7df1e" stroke-width="1.2" filter="drop-shadow(0 2px 5px rgba(247,223,30,0.3))" />
      <path d="{icons['javascript']}" transform="translate(10, 6) scale(0.65)" fill="#f7df1e" />
      <text x="32" y="18" class="stack-font-mono" font-size="11" fill="#f8fafc">JavaScript</text>
    </g>
  </g>

  <!-- BOTTOM SECTION: GROUPED STACK CHIPS -->
  <g transform="translate(36, 332)">
    <!-- Hairline Separator -->
    <line x1="0" y1="0" x2="778" y2="0" stroke="#1e293b" stroke-width="1" />
    <text x="0" y="20" class="stack-font-mono" font-size="10.5" fill="#38bdf8" letter-spacing="1">// SYSTEM CATEGORIES &amp; TOOLING</text>

    <!-- Group 1: Languages & Core Runtimes -->
    <g transform="translate(0, 36)">
      <text x="0" y="18" class="stack-font-mono" font-size="10" fill="#64748b">LANGUAGES :</text>
      
      <g transform="translate(90, 0)">
        <rect width="84" height="26" rx="6" fill="#0a1224" stroke="#3776ab" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['python']}" transform="translate(8, 5) scale(0.65)" fill="#3776ab" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">Python</text>
      </g>
      <g transform="translate(182, 0)">
        <rect width="108" height="26" rx="6" fill="#0a1224" stroke="#3178c6" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['typescript']}" transform="translate(8, 5) scale(0.65)" fill="#3178c6" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">TypeScript</text>
      </g>
      <g transform="translate(298, 0)">
        <rect width="108" height="26" rx="6" fill="#0a1224" stroke="#f7df1e" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['javascript']}" transform="translate(8, 5) scale(0.65)" fill="#f7df1e" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">JavaScript</text>
      </g>
      <g transform="translate(414, 0)">
        <rect width="90" height="26" rx="6" fill="#0a1224" stroke="#5fa04e" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['nodedotjs']}" transform="translate(8, 5) scale(0.65)" fill="#5fa04e" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">Node.js</text>
      </g>
    </g>

    <!-- Group 2: Frameworks, Databases & Intelligence -->
    <g transform="translate(0, 72)">
      <text x="0" y="18" class="stack-font-mono" font-size="10" fill="#64748b">FRAMEWORKS :</text>
      
      <g transform="translate(90, 0)">
        <rect width="90" height="26" rx="6" fill="#0a1224" stroke="#009688" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['fastapi']}" transform="translate(8, 5) scale(0.65)" fill="#009688" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">FastAPI</text>
      </g>
      <g transform="translate(188, 0)">
        <rect width="98" height="26" rx="6" fill="#0a1224" stroke="#ff3e00" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['svelte']}" transform="translate(8, 5) scale(0.65)" fill="#ff3e00" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">SvelteKit</text>
      </g>
      <g transform="translate(294, 0)">
        <rect width="108" height="26" rx="6" fill="#0a1224" stroke="#4169e1" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['postgresql']}" transform="translate(8, 5) scale(0.65)" fill="#4169e1" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">PostgreSQL</text>
      </g>
      <g transform="translate(410, 0)">
        <rect width="98" height="26" rx="6" fill="#0a1224" stroke="#47a248" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['mongodb']}" transform="translate(8, 5) scale(0.65)" fill="#47a248" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">MongoDB</text>
      </g>
    </g>

    <!-- Group 3: Cloud, DevOps & AI -->
    <g transform="translate(0, 108)">
      <text x="0" y="18" class="stack-font-mono" font-size="10" fill="#64748b">CLOUD &amp; AI :</text>
      
      <g transform="translate(90, 0)">
        <rect width="84" height="26" rx="6" fill="#0a1224" stroke="#2496ed" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['docker']}" transform="translate(8, 5) scale(0.65)" fill="#2496ed" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">Docker</text>
      </g>
      <g transform="translate(182, 0)">
        <rect width="134" height="26" rx="6" fill="#0a1224" stroke="#2088ff" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['githubactions']}" transform="translate(8, 5) scale(0.65)" fill="#2088ff" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">GitHub Actions</text>
      </g>
      <g transform="translate(324, 0)">
        <rect width="120" height="26" rx="6" fill="#0a1224" stroke="#4285f4" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['googlecloud']}" transform="translate(8, 5) scale(0.65)" fill="#4285f4" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">Google Cloud</text>
      </g>
      <g transform="translate(452, 0)">
        <rect width="120" height="26" rx="6" fill="#0a1224" stroke="#ff354f" stroke-opacity="0.6" stroke-width="1" />
        <path d="{icons['aiml']}" transform="translate(8, 5) scale(0.65)" fill="#ff354f" />
        <text x="28" y="17" class="stack-font-mono" font-size="10.5" fill="#cbd5e1">AI/ML Systems</text>
      </g>
    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 4. ID-DASHBOARD SVG (REALISTIC LANYARD, DAMPED SWING & PRISMATIC FOIL)
# ==============================================================================
def build_id_dashboard():
    # Construct authentic barcode vector bars
    bar_patterns = [
        3, 1, 2, 1, 4, 1, 2, 3, 1, 2, 4, 1, 1, 3, 2, 1, 3, 1, 4, 2, 1, 3, 1, 2,
        3, 2, 1, 4, 1, 2, 1, 3, 2, 1, 4, 1, 2, 3, 1, 1, 3, 2, 1, 4, 2, 1, 3, 1,
        2, 1, 4, 1, 2, 3, 1, 2, 4, 1, 1, 3, 2, 1, 3, 1, 4, 2, 1, 3, 1, 2, 3, 1
    ]
    cur_x = 0
    barcode_rects = []
    for i, w in enumerate(bar_patterns):
        if i % 2 == 0:
            barcode_rects.append(f'<rect x="{cur_x}" y="0" width="{w}" height="28" fill="#cbd5e1" />')
        cur_x += w + 1

    barcode_svg_lines = "".join(barcode_rects)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 850 560" width="100%" height="100%">
  <defs>
    <style><![CDATA[
{FONT_CSS}
      .id-font-display {{
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
      }}
      .id-font-mono {{
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-weight: 600;
      }}

      /* Damped drop entrance + perpetual gentle +/-1.7 degree pendulum swing */
      @keyframes idDampedDrop {{
        0% {{
          transform: translateY(-110px) rotate(14deg);
          opacity: 0;
        }}
        20% {{
          transform: translateY(0px) rotate(-10deg);
          opacity: 1;
        }}
        40% {{
          transform: translateY(0px) rotate(6.2deg);
        }}
        60% {{
          transform: translateY(0px) rotate(-3.5deg);
        }}
        80% {{
          transform: translateY(0px) rotate(2.1deg);
        }}
        92% {{
          transform: translateY(0px) rotate(-1.7deg);
        }}
        100% {{
          transform: translateY(0px) rotate(0deg);
        }}
      }}

      @keyframes idHarmonicPendulum {{
        0% {{
          transform: rotate(0deg);
        }}
        25% {{
          transform: rotate(1.7deg);
        }}
        50% {{
          transform: rotate(0deg);
        }}
        75% {{
          transform: rotate(-1.7deg);
        }}
        100% {{
          transform: rotate(0deg);
        }}
      }}

      .id-entrance-rig {{
        transform-origin: 425px 48px;
        animation: idDampedDrop 2.8s cubic-bezier(0.2, 0.8, 0.3, 1) 0.1s both;
      }}

      .id-pendulum-rig {{
        transform-origin: 425px 48px;
        animation: idHarmonicPendulum 4.6s ease-in-out 2.9s infinite;
      }}

      /* Holographic Prismatic Foil Sweep */
      @keyframes idFoilSweep {{
        0% {{
          transform: translateX(-480px) rotate(25deg);
          opacity: 0;
        }}
        25%, 65% {{
          opacity: 0.26;
        }}
        100% {{
          transform: translateX(580px) rotate(25deg);
          opacity: 0;
        }}
      }}
      .id-foil-layer {{
        animation: idFoilSweep 5.8s ease-in-out infinite;
      }}

      /* Pulsing Microchip Status Dot */
      @keyframes idChipPulse {{
        0%, 100% {{ r: 3.5px; opacity: 1; }}
        50% {{ r: 5px; opacity: 0.6; filter: drop-shadow(0 0 4px #10b981); }}
      }}
      .id-chip-dot {{
        animation: idChipPulse 2s ease-in-out infinite;
      }}

      /* Reduced motion */
      @media (prefers-reduced-motion: reduce) {{
        .id-entrance-rig, .id-pendulum-rig {{ animation: none !important; transform: none !important; opacity: 1 !important; }}
        .id-foil-layer {{ animation: none !important; opacity: 0.1 !important; transform: none !important; }}
        .id-chip-dot {{ animation: none !important; r: 3.5px !important; }}
      }}
    ]]></style>

    <pattern id="id-dots" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12" />
    </pattern>

    <linearGradient id="id-foil-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0" />
      <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="45%" stop-color="#ffffff" stop-opacity="0.7" />
      <stop offset="65%" stop-color="#ec4899" stop-opacity="0.4" />
      <stop offset="85%" stop-color="#ff354f" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#247bff" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="id-metal-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8" />
      <stop offset="30%" stop-color="#f8fafc" />
      <stop offset="55%" stop-color="#475569" />
      <stop offset="80%" stop-color="#cbd5e1" />
      <stop offset="100%" stop-color="#64748b" />
    </linearGradient>

    <linearGradient id="id-strap-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff354f" />
      <stop offset="12%" stop-color="#0b1329" />
      <stop offset="88%" stop-color="#0b1329" />
      <stop offset="100%" stop-color="#247bff" />
    </linearGradient>

    <linearGradient id="id-card-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8" />
    </linearGradient>

    <clipPath id="id-photo-clip">
      <rect x="252" y="146" width="124" height="136" rx="12" />
    </clipPath>

    <clipPath id="id-card-clip">
      <rect x="225" y="78" width="400" height="456" rx="22" />
    </clipPath>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="850" height="560" rx="22" fill="#070b16" />
  <rect width="850" height="560" rx="22" fill="url(#id-dots)" />
  <rect width="850" height="560" rx="22" fill="none" stroke="url(#id-card-stroke)" stroke-width="1.3" />

  <!-- Background Title & Annotations -->
  <g transform="translate(36, 32)">
    <text x="0" y="0" class="id-font-mono" font-size="10.5" fill="#38bdf8" letter-spacing="1">// VERIFIED CREDENTIAL</text>
    <text x="0" y="22" class="id-font-display" font-size="20" fill="#ffffff">Physical Lanyard Access Pass</text>
    <text x="540" y="20" class="id-font-mono" font-size="11" fill="#64748b">DAMPED PENDULUM +/-1.7°</text>
  </g>

  <!-- STATIC CEILING ANCHOR (Y = 0 to 48) -->
  <g>
    <!-- Webbed Lanyard Strap extending from ceiling down to clasp -->
    <rect x="410" y="0" width="30" height="48" fill="url(#id-strap-grad)" />
    <!-- Texture stitch lines on strap -->
    <line x1="416" y1="0" x2="416" y2="48" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="2 2" />
    <line x1="434" y1="0" x2="434" y2="48" stroke="#1e293b" stroke-width="1.2" stroke-dasharray="2 2" />
  </g>

  <!-- DYNAMIC PENDULUM RIG (Pivot point: 425, 48) -->
  <g class="id-entrance-rig">
    <g class="id-pendulum-rig">

      <!-- Metal Swivel Clasp Assembly -->
      <g>
        <!-- Top D-Ring -->
        <path d="M414 46 C414 42, 436 42, 436 46 L433 54 L417 54 Z" fill="url(#id-metal-grad)" stroke="#1e293b" stroke-width="0.8" />
        <!-- Swivel Barrel Connector -->
        <rect x="420" y="53" width="10" height="12" rx="3" fill="url(#id-metal-grad)" stroke="#334155" stroke-width="0.8" />
        <!-- Clasp Claw Hook looping through badge hole -->
        <path d="M422 65 C422 76, 428 76, 428 65 C428 78, 418 84, 424 94 C426 96, 429 96, 429 92 L429 65 Z" fill="url(#id-metal-grad)" stroke="#1e293b" stroke-width="0.8" />
      </g>

      <!-- ID BADGE CARD (Positioned 225, 78, 400x456) -->
      <g>
        <!-- Card Drop Shadow & Backing Glow -->
        <rect x="220" y="73" width="410" height="466" rx="24" fill="#247bff" fill-opacity="0.12" filter="blur(12px)" />
        
        <!-- Main Card Body -->
        <rect x="225" y="78" width="400" height="456" rx="22" fill="#090e1f" />
        
        <!-- Card Interior Content with Clip -->
        <g clip-path="url(#id-card-clip)">
          <!-- Dot Grid inside card -->
          <rect x="225" y="78" width="400" height="456" fill="url(#id-dots)" />

          <!-- Prismatic Foil Sweep Highlight -->
          <rect class="id-foil-layer" x="225" y="0" width="140" height="600" fill="url(#id-foil-grad)" />

          <!-- Card Header Banner -->
          <g transform="translate(245, 102)">
            <!-- Microchip Graphic -->
            <g transform="translate(0, 0)">
              <rect x="0" y="0" width="28" height="22" rx="4" fill="#d97706" stroke="#fbbf24" stroke-width="1.2" />
              <line x1="9" y1="0" x2="9" y2="22" stroke="#92400e" stroke-width="1" />
              <line x1="19" y1="0" x2="19" y2="22" stroke="#92400e" stroke-width="1" />
              <line x1="0" y1="11" x2="28" y2="11" stroke="#92400e" stroke-width="1" />
            </g>

            <text x="38" y="10" class="id-font-mono" font-size="9" fill="#38bdf8" letter-spacing="1">ACCESS PASS // LEVEL 4</text>
            <text x="38" y="21" class="id-font-mono" font-size="10.5" fill="#ffffff" font-weight="700">VERIFIED DEVELOPER BADGE</text>

            <g transform="translate(260, 2)">
              <circle class="id-chip-dot" cx="0" cy="8" r="3.5" fill="#10b981" />
              <text x="8" y="11" class="id-font-mono" font-size="9" fill="#10b981" font-weight="700">ACTIVE</text>
            </g>
          </g>

          <!-- Top Badge Slot Cutout (Where clasp attaches) -->
          <rect x="385" y="88" width="80" height="12" rx="6" fill="#070b16" stroke="#334155" stroke-width="1.2" />

          <!-- Portrait Section (Left) -->
          <g transform="translate(0, 0)">
            <!-- Frame Base -->
            <rect x="250" y="144" width="128" height="140" rx="14" fill="#0c162e" stroke="#247bff" stroke-width="1.5" />
            <!-- Inlined Portrait (Exact Image & Alpha Preserved) -->
            <g clip-path="url(#id-photo-clip)">
              <image href="data:image/png;base64,{id_png_b64}" x="250" y="144" width="128" height="140" preserveAspectRatio="xMidYMid meet" />
            </g>
          </g>

          <!-- Bio & Credentials (Right) -->
          <g transform="translate(394, 150)">
            <text x="0" y="18" class="id-font-display" font-size="22" fill="#ffffff">ESHWAR J</text>
            <text x="0" y="36" class="id-font-mono" font-size="12" fill="#38bdf8">@eshwar187</text>
            
            <text x="0" y="58" class="id-font-mono" font-size="10.5" fill="#f8fafc">Full Stack Developer</text>
            <text x="0" y="74" class="id-font-mono" font-size="10" fill="#ff7686">AI/ML &amp; Systems Builder</text>

            <text x="0" y="98" class="id-font-mono" font-size="9.5" fill="#64748b">LOCATION:</text>
            <text x="62" y="98" class="id-font-mono" font-size="9.5" fill="#cbd5e1">Chennai, TN</text>

            <text x="0" y="116" class="id-font-mono" font-size="9.5" fill="#64748b">AUDITED:</text>
            <text x="62" y="116" class="id-font-mono" font-size="9.5" fill="#10b981">OCTOBER 2026</text>
          </g>

          <!-- Verified Metrics Section (Showing ONLY verified, dated metrics) -->
          <g transform="translate(245, 305)">
            <!-- Metric 1: Public Repos -->
            <g transform="translate(0, 0)">
              <rect width="112" height="66" rx="10" fill="#0c1730" stroke="#247bff" stroke-opacity="0.45" stroke-width="1" />
              <text x="14" y="28" class="id-font-display" font-size="22" fill="#38bdf8">139</text>
              <text x="14" y="46" class="id-font-mono" font-size="9" fill="#94a3b8">PUBLIC</text>
              <text x="14" y="57" class="id-font-mono" font-size="9" fill="#94a3b8">REPOSITORIES</text>
            </g>

            <!-- Metric 2: Contributions -->
            <g transform="translate(124, 0)">
              <rect width="112" height="66" rx="10" fill="#1a1122" stroke="#ff354f" stroke-opacity="0.45" stroke-width="1" />
              <text x="14" y="28" class="id-font-display" font-size="22" fill="#ff354f">800+</text>
              <text x="14" y="46" class="id-font-mono" font-size="9" fill="#94a3b8">ANNUAL</text>
              <text x="14" y="57" class="id-font-mono" font-size="9" fill="#94a3b8">CONTRIBUTIONS</text>
            </g>

            <!-- Metric 3: Verified Audit Date -->
            <g transform="translate(248, 0)">
              <rect width="112" height="66" rx="10" fill="#0d1f1e" stroke="#10b981" stroke-opacity="0.45" stroke-width="1" />
              <text x="12" y="28" class="id-font-display" font-size="18" fill="#10b981">OCT 2026</text>
              <text x="12" y="46" class="id-font-mono" font-size="9" fill="#94a3b8">VERIFIED</text>
              <text x="12" y="57" class="id-font-mono" font-size="9" fill="#94a3b8">AUDIT DATE</text>
            </g>
          </g>

          <!-- Authentic Barcode & Security Strip -->
          <g transform="translate(245, 390)">
            <rect width="360" height="58" rx="8" fill="#060913" stroke="#1e293b" stroke-width="1" />
            <!-- Barcode Lines -->
            <g transform="translate(18, 10)">
              {barcode_svg_lines}
            </g>
            <text x="180" y="50" text-anchor="middle" class="id-font-mono" font-size="8.5" fill="#64748b" letter-spacing="2">* ESHWAR-187-OCT-2026-SYS *</text>
          </g>
        </g>

        <!-- Hairline Gradient Outer Border on Card -->
        <rect x="225" y="78" width="400" height="456" rx="22" fill="none" stroke="url(#id-card-stroke)" stroke-width="1.6" />
      </g>

    </g>
  </g>
</svg>"""
    return svg

# ==============================================================================
# 5. CONNECT SVG (CHARACTER POINTER WITH HOLOGRAPHIC ENERGY BEAM)
# ==============================================================================
def build_connect():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 850 370" width="100%" height="100%">
  <defs>
    <style><![CDATA[
{FONT_CSS}
      .conn-font-display {{
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
      }}
      .conn-font-mono {{
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-weight: 600;
      }}

      /* Character Subtle Float */
      @keyframes connCharFloat {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-5px); }}
      }}
      .conn-char-float {{
        animation: connCharFloat 4s ease-in-out infinite;
      }}

      /* Holographic Beam Pulse from Character to Cards */
      @keyframes connBeamPulse {{
        0%, 100% {{ opacity: 0.35; stroke-dashoffset: 0; }}
        50% {{ opacity: 0.8; stroke-dashoffset: -20; filter: drop-shadow(0 0 6px #38bdf8); }}
      }}
      .conn-beam-pulse {{
        animation: connBeamPulse 2.5s ease-in-out infinite;
      }}

      /* Nudging Arrow Animation (Energetic and Smooth) */
      @keyframes connNudgeArrow {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(8px); }}
      }}
      .conn-arrow-1 {{ animation: connNudgeArrow 1.4s ease-in-out infinite; }}
      .conn-arrow-2 {{ animation: connNudgeArrow 1.4s ease-in-out 0.25s infinite; }}
      .conn-arrow-3 {{ animation: connNudgeArrow 1.4s ease-in-out 0.5s infinite; }}

      /* Reduced motion */
      @media (prefers-reduced-motion: reduce) {{
        .conn-char-float {{ animation: none !important; transform: none !important; }}
        .conn-beam-pulse {{ animation: none !important; opacity: 0.4 !important; }}
        .conn-arrow-1, .conn-arrow-2, .conn-arrow-3 {{ animation: none !important; transform: none !important; }}
      }}
    ]]></style>

    <pattern id="conn-dots" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12" />
    </pattern>

    <linearGradient id="conn-card-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8" />
    </linearGradient>

    <linearGradient id="conn-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="60%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#ff354f" />
    </linearGradient>

    <linearGradient id="conn-beam-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0" />
    </linearGradient>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="850" height="370" rx="22" fill="#070b16" />
  <rect width="850" height="370" rx="22" fill="url(#conn-dots)" />
  <rect width="850" height="370" rx="22" fill="none" stroke="url(#conn-card-stroke)" stroke-width="1.3" />

  <!-- Holographic Directional Target Beam from character's pointing hand (around 310, 160) towards cards (355) -->
  <path class="conn-beam-pulse" d="M305 160 C325 140, 335 125, 360 120 M305 160 C330 180, 340 195, 360 210 M305 160 C330 220, 340 260, 360 295" fill="none" stroke="url(#conn-beam-grad)" stroke-width="1.8" stroke-dasharray="4 4" />

  <!-- LEFT: Character Pointing Right (Preserving Exact Image and Alpha) -->
  <g class="conn-char-float" transform="translate(10, 16)">
    <!-- Ambient Character Glow Backdrop -->
    <ellipse cx="160" cy="180" rx="140" ry="140" fill="#247bff" fill-opacity="0.14" filter="blur(16px)" />
    <!-- Character Image -->
    <image href="data:image/png;base64,{rp_png_b64}" x="0" y="0" width="320" height="338" preserveAspectRatio="xMidYMid meet" />
  </g>

  <!-- RIGHT: Connect Header & Social Cards -->
  <g transform="translate(345, 24)">
    <!-- Header -->
    <g transform="translate(0, 14)">
      <text x="0" y="0" class="conn-font-mono" font-size="10.5" fill="#38bdf8" letter-spacing="1">// CONNECT &amp; NETWORK</text>
      <text x="0" y="24" class="conn-font-display" font-size="21" fill="url(#conn-title-grad)">Let's Build Something Extraordinary</text>
      <text x="0" y="42" class="conn-font-mono" font-size="11" fill="#94a3b8">Open to high-impact opportunities, AI systems &amp; tech collaborations.</text>
    </g>

    <!-- Social Cards Stack -->
    <g transform="translate(0, 72)">
      <!-- CARD 1: LinkedIn -->
      <a href="https://www.linkedin.com/in/eshwar-j-7b8854289/" target="_blank">
        <g transform="translate(0, 0)">
          <rect width="475" height="70" rx="14" fill="#091329" stroke="#0a66c2" stroke-opacity="0.5" stroke-width="1.2" />
          <!-- Brand Badge -->
          <g transform="translate(14, 13)">
            <rect width="44" height="44" rx="10" fill="#0a66c2" fill-opacity="0.25" stroke="#0a66c2" stroke-width="1.2" />
            <path d="{icons['linkedin']}" transform="translate(10, 10) scale(1)" fill="#0a66c2" />
          </g>
          <!-- Info -->
          <text x="72" y="28" class="conn-font-display" font-size="15" fill="#ffffff">LinkedIn</text>
          <text x="72" y="48" class="conn-font-mono" font-size="10.5" fill="#94a3b8">in/eshwar-j-7b8854289 • Professional Network &amp; Career</text>
          <!-- Nudging Arrow -->
          <g class="conn-arrow-1" transform="translate(435, 35)">
            <path d="M0 -6 L6 0 L0 6 M6 0 L-8 0" stroke="#0a66c2" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round" />
          </g>
        </g>
      </a>

      <!-- CARD 2: YouTube -->
      <a href="https://www.youtube.com/@DevWithEshwar" target="_blank">
        <g transform="translate(0, 84)">
          <rect width="475" height="70" rx="14" fill="#170c14" stroke="#ff0000" stroke-opacity="0.5" stroke-width="1.2" />
          <!-- Brand Badge -->
          <g transform="translate(14, 13)">
            <rect width="44" height="44" rx="10" fill="#ff0000" fill-opacity="0.25" stroke="#ff0000" stroke-width="1.2" />
            <path d="{icons['youtube']}" transform="translate(10, 10) scale(1)" fill="#ff0000" />
          </g>
          <!-- Info -->
          <text x="72" y="28" class="conn-font-display" font-size="15" fill="#ffffff">YouTube</text>
          <text x="72" y="48" class="conn-font-mono" font-size="10.5" fill="#94a3b8">@DevWithEshwar • Code Breakdowns &amp; Tech Tutorials</text>
          <!-- Nudging Arrow -->
          <g class="conn-arrow-2" transform="translate(435, 35)">
            <path d="M0 -6 L6 0 L0 6 M6 0 L-8 0" stroke="#ff0000" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round" />
          </g>
        </g>
      </a>

      <!-- CARD 3: Instagram -->
      <a href="https://www.instagram.com/eshwar_official/" target="_blank">
        <g transform="translate(0, 168)">
          <rect width="475" height="70" rx="14" fill="#180b18" stroke="#e4405f" stroke-opacity="0.5" stroke-width="1.2" />
          <!-- Brand Badge -->
          <g transform="translate(14, 13)">
            <rect width="44" height="44" rx="10" fill="#e4405f" fill-opacity="0.25" stroke="#e4405f" stroke-width="1.2" />
            <path d="{icons['instagram']}" transform="translate(10, 10) scale(1)" fill="#e4405f" />
          </g>
          <!-- Info -->
          <text x="72" y="28" class="conn-font-display" font-size="15" fill="#ffffff">Instagram</text>
          <text x="72" y="48" class="conn-font-mono" font-size="10.5" fill="#94a3b8">@eshwar_official • Developer Lifestyle, Side Builds &amp; BTS</text>
          <!-- Nudging Arrow -->
          <g class="conn-arrow-3" transform="translate(435, 35)">
            <path d="M0 -6 L6 0 L0 6 M6 0 L-8 0" stroke="#e4405f" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round" />
          </g>
        </g>
      </a>
    </g>
  </g>
</svg>"""
    return svg

# Write files
os.makedirs('assets', exist_ok=True)

files = {
    'assets/hero.svg': build_hero(),
    'assets/about-life.svg': build_about_life(),
    'assets/stack.svg': build_stack(),
    'assets/id-dashboard.svg': build_id_dashboard(),
    'assets/connect.svg': build_connect()
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    # Validate XML
    ET.fromstring(content)
    print(f"Generated & validated valid XML: {path} ({len(content)} bytes)")

print("All 5 upgraded animated SVGs built successfully.")
