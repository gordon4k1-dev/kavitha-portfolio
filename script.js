// Lenis Smooth Scroll Setup
const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
});

// Integrate Lenis with GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

// ==========================================
// SYSTEM BOOT ANIMATION (HERO)
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
    
    const bootContainer = document.getElementById('boot-text-container');
    const topics = [
        "15-DAY INTERNSHIP", "ALUMNI MEET", "COMMUNITY OUTREACH", 
        "WOMEN'S DAY", "SCIENCE DAY", "EVENT MANAGEMENT", 
        "MAHATMA PHULE DAY", "AMBEDKAR JAYANTI", "EDUCATIONAL TECH"
    ];

    // Populate boot text rows
    if(bootContainer) {
        for(let i=0; i<30; i++) {
            const textRow = document.createElement('div');
            textRow.textContent = topics.join(" // ") + " // " + topics.join(" // ");
            textRow.style.opacity = Math.random() * 0.5 + 0.1;
            bootContainer.appendChild(textRow);
        }
    }

   // Boot Sequence Animation
    const tl = gsap.timeline();

    // 1. Flash the boot text rows smoothly
    tl.to(bootContainer, {
        y: "-50%",
        duration: 3,
        ease: "power4.inOut"
    }, 0);

    // 2. Reveal the Central Glass Info Pane
    tl.from(".glass-pane", {
        y: 50,
        opacity: 0,
        duration: 1.5,
        ease: "power3.out"
    }, 1);

    // ==========================================
    // KINETIC SCROLL & PROGRESS BAR
    // ==========================================
    gsap.to("body", {
        backgroundColor: "#fcd1d6", 
        scrollTrigger: {
            trigger: "body",
            start: "top top",
            end: "bottom bottom",
            scrub: true
        }
    });

    gsap.to("#jules-progress", {
        height: "100%",
        ease: "none",
        scrollTrigger: {
            trigger: "body",
            start: "top top",
            end: "bottom bottom",
            scrub: true
        }
    });

    // ==========================================
    // DATA MODULE REVEALS
    // ==========================================
    const modules = document.querySelectorAll(".data-module");

    modules.forEach((mod) => {
        const wipeMask = mod.querySelector(".wipe-mask");
        const img = mod.querySelector(".parallax-image");
        const textContent = mod.querySelector(".section-text-content");
        const verticalText = mod.querySelector(".vertical-text");

        const modTl = gsap.timeline({
            scrollTrigger: {
                trigger: mod,
                start: "top 75%", 
                toggleActions: "play none none reverse"
            }
        });

        if(wipeMask) {
            modTl.to(wipeMask, {
                scaleY: 0,
                duration: 1.2,
                ease: "power4.inOut"
            }, 0);
        }

        if(img) {
            modTl.from(img, {
                scale: 1.2,
                duration: 1.5,
                ease: "power3.out"
            }, 0);
            
            gsap.to(img, {
                yPercent: 10,
                ease: "none",
                scrollTrigger: {
                    trigger: mod,
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                }
            });
        }

        if(textContent) {
            modTl.from(textContent.children, {
                y: 30,
                opacity: 0,
                duration: 0.8,
                stagger: 0.1,
                ease: "power2.out"
            }, 0.5);
        }

        if(verticalText) {
            modTl.from(verticalText, {
                x: -20,
                opacity: 0,
                duration: 1,
                ease: "power3.out"
            }, 0.2);
        }
    });

    // ==========================================
    // INTERACTIVE PANCHPADI ANIMATION (MODULE 30)
    // ==========================================
    const panchpadiSteps = document.querySelectorAll('.panchpadi-step');
    if(panchpadiSteps.length > 0) {
        ScrollTrigger.create({
            trigger: panchpadiSteps[0].closest('.data-module'),
            start: "top center",
            onEnter: () => {
                panchpadiSteps.forEach((step, index) => {
                    setTimeout(() => {
                        panchpadiSteps.forEach(s => {
                            s.style.borderLeft = "none";
                            s.style.backgroundColor = "transparent";
                            s.style.transform = "translateX(0px)";
                            s.style.color = "#1f2937";
                        });
                        step.style.borderLeft = "4px solid #FF7F50";
                        step.style.backgroundColor = "rgba(255, 127, 80, 0.1)";
                        step.style.transform = "translateX(8px)";
                        step.style.color = "#FF7F50";
                        step.style.transition = "all 0.4s ease";
                    }, index * 1000); 
                });
            }
        });
    }
});