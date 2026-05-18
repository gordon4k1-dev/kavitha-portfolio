import re

with open('index.html', 'r') as f:
    html = f.read()

new_modules = [
    {
        "id": 30,
        "title": "15-Day Internship",
        "subtitle": "Pedagogical Mastery",
        "text": "During this intensive 15-day period, I transitioned from theoretical academic knowledge to active classroom practice. My primary focus was on structured lesson planning using the Panchpadi (Herbartian Five-Step Method): Preparation, Presentation, Association, Generalization, and Application. By shifting from traditional lecturing to student-centric storytelling and visual aids, I maintained high engagement levels among younger learners.",
        "image": "images/internship.jpg",
        "custom_flash": """
                                <!-- Custom Flash: Panchpadi Interactive Diagram -->
                                <div class="mt-4 border border-coral p-4 bg-peach/50 flex flex-col gap-2">
                                    <div class="font-mono text-xs text-coral mb-2 uppercase">System_Routine: Panchpadi_Method</div>
                                    <div class="flex flex-col gap-1 text-sm font-mono text-gray-800">
                                        <div class="panchpadi-step pl-2 border-l-2 border-coral bg-coral/10 py-1">1. Preparation</div>
                                        <div class="panchpadi-step pl-2 py-1">2. Presentation</div>
                                        <div class="panchpadi-step pl-2 py-1">3. Association</div>
                                        <div class="panchpadi-step pl-2 py-1">4. Generalization</div>
                                        <div class="panchpadi-step pl-2 py-1">5. Application</div>
                                    </div>
                                </div>
        """
    },
    {
        "id": 31,
        "title": "Alumni Meet",
        "subtitle": "Institutional Legacy",
        "text": "The Alumni Meet served as a vital bridge between the institution’s history and its future. My role involved organizing the reception and curating a 'Memory Lane' photo gallery that showcased the school’s journey through the years. Observing the interactions between current students and successful alumni provided deep insights into how a school's environment influences long-term career trajectories.",
        "image": "images/alumni.jpg",
        "custom_flash": """
                                <!-- Custom Flash: Memory Lane Ticker -->
                                <div class="mt-4 w-full relative">
                                    <div class="font-mono text-[10px] text-coral absolute -top-4 left-0">ARCHIVE_TIMELINE</div>
                                    <div class="ticker-wrap w-full h-8 flex items-center overflow-hidden">
                                        <div class="ticker font-mono text-sm tracking-widest px-4">
                                            [1998] INITIATION // [2005] EXPANSION // [2012] MILESTONE // [2018] LEGACY // [2023] RENEWAL // [1998] INITIATION // [2005] EXPANSION
                                        </div>
                                    </div>
                                </div>
        """
    },
    {
        "id": 32,
        "title": "Community Outreach",
        "subtitle": "First Aid & Crisis Management",
        "text": "In collaboration with final-year nursing students, I participated in a comprehensive community outreach program focused on emergency response. The demonstration provided practical training on treating minor burns, managing nosebleeds, and executing the recovery position. This experience reinforced the philosophy that an educator’s responsibility extends beyond academics to the physical safety of every student.",
        "image": "images/first_aid.jpg",
        "custom_flash": """
                                <!-- Custom Flash: Safety Icon Pulse -->
                                <div class="mt-6 flex items-center gap-4 border border-red-600/30 p-3 bg-red-50/50">
                                    <div class="w-8 h-8 bg-red-600 rounded-full flex items-center justify-center safety-pulse text-white font-bold text-lg">
                                        +
                                    </div>
                                    <div class="font-mono text-xs text-red-800 uppercase tracking-wide">
                                        NEP 2020: Health & Safety Protocol Active
                                    </div>
                                </div>
        """
    },
    {
        "id": 33,
        "title": "Women’s Day",
        "subtitle": "Empowerment through Expression",
        "text": "To honor the contributions of women in society, I helped organize a vibrant cultural program titled 'Shakti.' The event featured dance and music performances by students that centered on progress and empowerment. I delivered a keynote speech regarding the history of women’s education in India, paying tribute to pioneers like Savitribai Phule and exploring the pedagogical shift toward gender-inclusive classrooms.",
        "image": "images/cultural-events.jpg", 
        "custom_flash": ""
    },
    {
        "id": 34,
        "title": "Science & Creative Arts",
        "subtitle": "Sustainable Future",
        "text": "This dual-purpose event combined analytical thinking with tactile creativity. During Science Day, I guided students through experiments involving air pressure and capillary action to spark curiosity. Simultaneously, the Art and Craft segment focused on 'Best from Waste' projects, encouraging students to repurpose everyday materials into functional art, improving fine motor skills while instilling environmental responsibility.",
        "image": "images/ardandcraft.jpg",
        "custom_flash": """
                                <!-- Custom Flash: Sustainable Badge -->
                                <div class="mt-4 flex justify-end">
                                    <div class="border border-green-600 px-4 py-2 bg-green-50 text-green-800 font-mono text-xs font-bold uppercase tracking-widest flex items-center gap-2">
                                        <div class="w-2 h-2 bg-green-600 rounded-full animate-pulse"></div>
                                        [INIT]: Sustainable Protocol
                                    </div>
                                </div>
        """
    },
    {
        "id": 35,
        "title": "Event Management",
        "subtitle": "Administrative Leadership",
        "text": "Beyond the classroom, I engaged in a specialized module focused on the administrative logistics of schooling. My tasks included drafting event schedules, managing budget allocations, and coordinating communication between school departments. This experience demonstrated that successful teaching is always supported by robust administrative planning and leadership.",
        "image": "images/event_management.jpg",
        "custom_flash": """
                                <!-- Custom Flash: Blueprint Table -->
                                <div class="mt-6 p-4 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiBmaWxsPSJub25lIiBzdHJva2U9IiNmZjdmNTAiIHN0cm9rZS1vcGFjaXR5PSIwLjEiIHN0cm9rZS13aWR0aD0iMSIvPjwvc3ZnPg==')]">
                                    <table class="blueprint-table w-full text-left">
                                        <thead>
                                            <tr>
                                                <th>Phase</th>
                                                <th>Alloc</th>
                                                <th>Status</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>Plan</td>
                                                <td>15%</td>
                                                <td>[DONE]</td>
                                            </tr>
                                            <tr>
                                                <td>Exec</td>
                                                <td>70%</td>
                                                <td>[DONE]</td>
                                            </tr>
                                            <tr>
                                                <td>Rev</td>
                                                <td>15%</td>
                                                <td>[DONE]</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
        """
    },
    {
        "id": 36,
        "title": "Mahatma Phule Day",
        "subtitle": "The Social Reformer’s Vision",
        "text": "We conducted a commemorative lecture to honor the legacy of Mahatma Jyotirao Phule. The discussion focused on his struggle against caste discrimination and his revolutionary role in opening the first school for girls in Pune. This session challenged us as trainees to view education as a tool for social justice and the upliftment of marginalized communities.",
        "image": "images/mahatma_phule.jpg",
        "custom_flash": ""
    },
    {
        "id": 37,
        "title": "Ambedkar Jayanti",
        "subtitle": "Constitutional Values in Education",
        "text": "To celebrate the birth anniversary of Dr. B.R. Ambedkar, I organized a collective reading of the Preamble of the Constitution. The objective was to instill the core values of Liberty, Equality, and Fraternity. We engaged in a discussion centered on Ambedkar’s philosophy of 'Educate, Agitate, and Organize,' linking it to the modern practice of inclusive education.",
        "image": "images/ambedkar_jayanti.jpg",
        "custom_flash": ""
    },
    {
        "id": 38,
        "title": "Educational Technology",
        "subtitle": "Digital Pedagogy & PPT Synthesis",
        "text": "The capstone of my practicum was the development and delivery of a comprehensive Educational PPT Presentation. This project synthesized my internship reflections, student data analysis, and pedagogical growth into a high-impact digital format. I utilized advanced presentation software to create interactive modules that addressed different learning paces. This topic showcases my proficiency in Digital Pedagogy, demonstrating how technology can be used to visualize complex concepts, track student progress, and present academic findings with professional clarity.",
        "image": "images/ppt_presentation.jpg",
        "custom_flash": ""
    }
]

def generate_module_html(m):
    
    extra_visual_classes = ""
    extra_text_classes = ""
    bg_quote_html = ""
    mandala_html = ""
    split_screen_html = ""
    
    if m["title"] == "Women’s Day":
        extra_text_classes = "font-serif italic text-lg"
        mandala_html = "<img src=\"data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='50' cy='50' r='45' fill='none' stroke='%23FF7F50' stroke-width='2' stroke-dasharray='5,5'/%3E%3Cpath d='M50 5 L50 95 M5 50 L95 50 M18 18 L82 82 M18 82 L82 18' stroke='%23FF7F50' stroke-width='1'/%3E%3C/svg%3E\" class=\"mandala-bg\">"

    if "Phule" in m["title"] or "Ambedkar" in m["title"]:
        bg_quote_html = "<div class=\"bg-quote select-none\">\"WE, THE PEOPLE\"</div>"
        extra_text_classes = "text-center relative z-10"
        
    if "Science" in m["title"] and "Arts" in m["title"]:
        split_screen_html = """
                        <div class="absolute inset-0 flex">
                            <div class="w-1/2 h-full bg-blue-50/30 border-r border-coral/20"></div>
                            <div class="w-1/2 h-full bg-orange-50/30"></div>
                        </div>
        """

    container_additions = split_screen_html + mandala_html + bg_quote_html

    html = f"""
                <!-- MODULE {m["id"]}: {m["title"]} -->
                <section class="data-module w-full min-h-screen flex flex-col md:flex-row items-center justify-center p-8 md:p-16 gap-8 relative overflow-hidden" data-id="{m["id"]}">
                    {container_additions}
                    <!-- Topic Left -->
                    <div class="hidden md:flex flex-col items-center justify-center w-1/12 h-full absolute left-0 top-0 border-r border-coral opacity-50 z-10">
                        <div class="vertical-text font-integral text-2xl text-coral tracking-widest uppercase">
                            {m["title"]}
                        </div>
                    </div>

                    <!-- Main Content Wrapper -->
                    <div class="w-full md:w-10/12 md:ml-[8%] flex flex-col md:flex-row gap-8 items-center z-10">
                        
                        <!-- Visual / Technical Viewport -->
                        <div class="w-full md:w-1/2 relative section-visual">
                            <div class="tech-viewport w-full aspect-video md:aspect-[4/3] relative overflow-hidden">
                                <div class="wipe-mask"></div>
                                <img src="{m["image"]}" alt="{m["title"]}" class="parallax-image transform scale-110">
                                
                                <!-- Metadata Overlays -->
                                <div class="meta-overlay meta-tl">SYS.ID: {m["id"]:03d}</div>
                                <div class="meta-overlay meta-tr">LAT: 18.4485°N</div>
                                <div class="meta-overlay meta-bl">LON: 73.8340°E</div>
                                <div class="meta-overlay meta-br">STATUS: OK</div>
                            </div>
                        </div>

                        <!-- Text / Report -->
                        <div class="w-full md:w-1/2 flex flex-col gap-4 section-text-content">
                            <div class="font-mono text-xs text-coral tracking-widest uppercase mb-2 border-b border-coral pb-2">
                                [MODULE_{m["id"]:02d}] // {m["subtitle"]}
                            </div>
                            <h2 class="font-serif text-3xl md:text-5xl font-bold text-gray-800 mb-4">{m["title"]}</h2>
                            <div class="font-mono text-sm leading-relaxed text-gray-700 bg-white/50 p-6 border border-coral/30 relative {extra_text_classes}">
                                <div class="absolute top-0 left-0 w-2 h-2 bg-coral"></div>
                                <span class="text-coral font-bold">[REPORT]:</span> {m["text"]}
                            </div>
                            {m["custom_flash"]}
                        </div>

                    </div>
                </section>
"""
    return html

pattern_sec30 = r'<!-- MODULE 30: About the Educator -->.*?</section>'
match_sec30 = re.search(pattern_sec30, html, re.DOTALL)
sec30_content = ""
if match_sec30:
    sec30_content = match_sec30.group(0)
    html = html.replace(sec30_content, "")
    sec30_content = sec30_content.replace('MODULE 30', 'MODULE 39')
    sec30_content = sec30_content.replace('data-id="30"', 'data-id="39"')
    sec30_content = sec30_content.replace('SYS.ID: 030', 'SYS.ID: 039')
    sec30_content = sec30_content.replace('[MODULE_30]', '[MODULE_39]')

new_modules_html = ""
for m in new_modules:
    new_modules_html += generate_module_html(m)

pattern_sec29 = r'<!-- MODULE 29: Peer Community -->.*?</section>'
match_sec29 = re.search(pattern_sec29, html, re.DOTALL)
if match_sec29:
    sec29_content = match_sec29.group(0)
    insertion = sec29_content + "\n" + new_modules_html + "\n" + sec30_content
    html = html.replace(sec29_content, insertion)

with open('index.html', 'w') as f:
    f.write(html)

print("Added 9 new modules and moved section 30 to 39.")
