import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the hero section as we did before
old_hero = """            <header id="hero">
                <div class="hero-bg"></div>
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <div class="hero-badge">Portfolio 2026</div>
                    <h1 class="hero-title">KAVITHA SARMA</h1>
                    <p class="hero-subtitle">B.Ed Scholar & Educator | Jai Ganesh College of Education</p>
                </div>
                <div class="scroll-indicator">
                    <span>Begin Journey</span>
                    <div class="arrow"></div>
                </div>
            </header>"""

new_hero = """            <!-- Jules Sidebar Tracker -->
            <div class="jules-sidebar">
                <div class="jules-label">DATA_TRANSFER</div>
                <div class="jules-progress" id="jules-progress"></div>
            </div>

            <!-- Section A: The Hero -->
            <header id="hero" class="relative w-full h-screen flex items-center justify-center overflow-hidden">
                <!-- System Boot Text Animation Container -->
                <div id="boot-text-container" class="absolute inset-0 flex flex-col justify-center items-center opacity-20 pointer-events-none font-mono text-coral text-sm leading-none whitespace-nowrap z-0 overflow-hidden" style="transform: rotate(-5deg) scale(1.5);">
                    <!-- Populated by JS -->
                </div>

                <!-- Central 3D Glass Pane -->
                <div class="glass-pane relative z-10 w-[90%] max-w-4xl p-8 md:p-16 flex flex-col md:flex-row items-center justify-between">
                    <div class="flex items-center gap-4 mb-6 md:mb-0">
                        <div class="pulsing-core"></div>
                        <div>
                            <div class="font-mono text-[10px] tracking-widest text-coral uppercase">Jules Core Active</div>
                            <div class="font-mono text-sm font-bold text-gray-800 tracking-wider">PROJECT_REF: B.ED_PRACTICUM_2026</div>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="font-mono text-[10px] tracking-widest text-coral uppercase mb-1">Author</div>
                        <div class="font-serif text-xl font-bold text-gray-800">Kavitha Sarma</div>
                        <div class="font-mono text-xs text-gray-600 mt-1">Jai Ganesh College of Education</div>
                    </div>
                </div>

                <!-- Massive Bleeding Title -->
                <h1 class="hero-title absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 font-integral text-[10vw] leading-none whitespace-nowrap text-outline-coral z-20 pointer-events-none mix-blend-difference">
                    PRACTICUM ARCHIVE
                </h1>

                <!-- Scroll Indicator -->
                <div class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center z-20">
                    <span class="font-mono text-xs text-coral tracking-widest uppercase mb-2">Initialize Scroll</span>
                    <div class="w-px h-12 bg-coral relative overflow-hidden">
                        <div class="absolute top-0 left-0 w-full h-full bg-peach transform -translate-y-full scroll-line-anim"></div>
                    </div>
                </div>
            </header>"""

if old_hero in html:
    html = html.replace(old_hero, new_hero)

# Convert section tags
pattern = r'<section class="stream-section" data-id="(\d+)">(.*?)</section>'
sections = re.findall(pattern, html, re.DOTALL)
new_sections_html = ""

for id_str, content in sections:
    img_match = re.search(r'<img src="(.*?)"', content)
    img_src = img_match.group(1) if img_match else ""
    title_match = re.search(r'<h2 class="section-title">(.*?)</h2>', content)
    title = title_match.group(1) if title_match else ""
    subtitle_match = re.search(r'<h3 class="section-subtitle">(.*?)</h3>', content)
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    text_match = re.search(r'<p class="section-text">(.*?)</p>', content)
    text = text_match.group(1) if text_match else ""
    
    new_html = f"""
                <!-- MODULE {id_str}: {title} -->
                <section class="data-module w-full min-h-screen flex flex-col md:flex-row items-center justify-center p-8 md:p-16 gap-8 relative" data-id="{id_str}">
                    <div class="hidden md:flex flex-col items-center justify-center w-1/12 h-full absolute left-0 top-0 border-r border-coral opacity-50 z-10">
                        <div class="vertical-text font-integral text-2xl text-coral tracking-widest uppercase">
                            {title}
                        </div>
                    </div>
                    <div class="w-full md:w-10/12 md:ml-[8%] flex flex-col md:flex-row gap-8 items-center z-10">
                        <div class="w-full md:w-1/2 relative section-visual">
                            <div class="tech-viewport w-full aspect-video md:aspect-[4/3] relative overflow-hidden">
                                <div class="wipe-mask"></div>
                                <img src="{img_src}" alt="{title}" class="parallax-image transform scale-110">
                                <div class="meta-overlay meta-tl">SYS.ID: {int(id_str):03d}</div>
                                <div class="meta-overlay meta-tr">LAT: 18.4485°N</div>
                                <div class="meta-overlay meta-bl">LON: 73.8340°E</div>
                                <div class="meta-overlay meta-br">STATUS: OK</div>
                            </div>
                        </div>
                        <div class="w-full md:w-1/2 flex flex-col gap-4 section-text-content">
                            <div class="font-mono text-xs text-coral tracking-widest uppercase mb-2 border-b border-coral pb-2">
                                [MODULE_{int(id_str):02d}] // {subtitle}
                            </div>
                            <h2 class="font-serif text-3xl md:text-5xl font-bold text-gray-800 mb-4">{title}</h2>
                            <div class="font-mono text-sm leading-relaxed text-gray-700 bg-white/50 p-6 border border-coral/30 relative">
                                <div class="absolute top-0 left-0 w-2 h-2 bg-coral"></div>
                                <span class="text-coral font-bold">[REPORT]:</span> {text}
                            </div>
                        </div>
                    </div>
                </section>
"""
    new_sections_html += new_html

# Apply new sections
start_idx = html.find('<main class="stream-container">')
if start_idx != -1:
    end_idx = html.find('</main>', start_idx)
    if end_idx != -1:
        new_main = '<main class="stream-container relative w-full">\n' + new_sections_html + '\n            </main>'
        html = html[:start_idx] + new_main + html[end_idx + 7:]

# Header fixes (tailwind etc)
if "tailwindcss.com" not in html:
    html = html.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">',
        """<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Integral+CF:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              peach: '#FADADD',
              coral: '#FF7F50',
              'coral-dark': '#e06b40',
            },
            fontFamily: {
              mono: ['"JetBrains Mono"', 'monospace'],
              serif: ['"Playfair Display"', 'serif'],
              integral: ['"Integral CF"', 'sans-serif', 'Arial'],
            }
          }
        }
      }
    </script>"""
    )

with open('index.html', 'w') as f:
    f.write(html)
