/* ===== REVEAL ON SCROLL ===== */

const reveals = document.querySelectorAll('.reveal');

function revealSections() {

    reveals.forEach(section => {

        const windowHeight = window.innerHeight;
        const revealTop = section.getBoundingClientRect().top;
        const revealPoint = 120;

        if(revealTop < windowHeight - revealPoint){
            section.classList.add('active');
        }

    });

}

window.addEventListener('scroll', revealSections);
revealSections();

/* ===== PARALLAX IMAGES ===== */

window.addEventListener('scroll', () => {

    const parallax = document.querySelectorAll('.parallax-image');

    parallax.forEach(img => {

        const speed = 0.08;
        const yPos = -(window.scrollY * speed);

        img.style.transform = `translateY(${yPos}px) scale(1.08)`;

    });

});

/* ===== MODULE ACTIVE GLOW ===== */

const modules = document.querySelectorAll('.data-module');

window.addEventListener('scroll', () => {

    let current = "";

    modules.forEach(module => {

        const sectionTop = module.offsetTop;
        const sectionHeight = module.clientHeight;

        if(pageYOffset >= sectionTop - sectionHeight / 3){
            current = module.getAttribute('data-id');
        }

    });

    modules.forEach(module => {
        module.classList.remove('module-active');

        if(module.getAttribute('data-id') === current){
            module.classList.add('module-active');
        }
    });

});

/* ===== IMAGE LAZY LOADING ===== */

const images = document.querySelectorAll("img");

images.forEach(img => {
    img.setAttribute("loading","lazy");
});

/* ===== SMOOTH HERO FADE ===== */

window.addEventListener('scroll', () => {

    const hero = document.querySelector('.hero-content');

    if(hero){

        let value = 1 - window.scrollY / 700;

        hero.style.opacity = value;

    }

});

/* ===== TYPEWRITER EFFECT ===== */

const title = document.querySelector('.hero-title');

if(title){

    const original = title.innerHTML;

    title.innerHTML = "";

    let i = 0;

    function typeWriter(){

        if(i < original.length){

            title.innerHTML += original.charAt(i);

            i++;

            setTimeout(typeWriter,40);

        }

    }

    typeWriter();

}

/* ===== FLOATING META EFFECT ===== */

const overlays = document.querySelectorAll('.meta-overlay');

window.addEventListener('mousemove', (e) => {

    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;

    overlays.forEach(overlay => {

        overlay.style.transform = `
            translate(
                ${x * 6}px,
                ${y * 6}px
            )
        `;

    });

});

/* ===== TICKER AUTO ===== */

const ticker = document.querySelector('.ticker');

if(ticker){

    let pos = 0;

    function animateTicker(){

        pos--;

        ticker.style.transform = `translateX(${pos}px)`;

        if(Math.abs(pos) > ticker.scrollWidth / 2){
            pos = 0;
        }

        requestAnimationFrame(animateTicker);

    }

    animateTicker();

}

/* ===== SAFETY PULSE ===== */

const pulse = document.querySelectorAll('.safety-pulse');

pulse.forEach(p => {

    setInterval(() => {

        p.classList.toggle('scale');

    },1000);

});

/* ===== CONSOLE SIGNATURE ===== */

console.log(`
====================================
KAVITHA SARMA PORTFOLIO SYSTEM
Interactive Educational Archive
Build Status : ACTIVE
Modules Loaded : 39
====================================
`);
