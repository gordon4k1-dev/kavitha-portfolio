// SCROLL REVEAL

const modules = document.querySelectorAll(".data-module");

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");
        }
    });

},{
    threshold:0.15
});

modules.forEach(module=>{
    observer.observe(module);
});

// IMAGE AUTO FIX

const images = document.querySelectorAll("img");

images.forEach(img=>{

    img.loading = "lazy";

    img.onerror = () => {

        console.log("Missing image:", img.src);

        const fallback = document.createElement("div");

        fallback.className = "image-error";

        fallback.innerText = "Image Not Found";

        img.parentElement.appendChild(fallback);

        img.remove();
    };
});

// PARALLAX EFFECT

window.addEventListener("scroll",()=>{

    const parallaxImages =
        document.querySelectorAll(".parallax-image");

    parallaxImages.forEach(img=>{

        const speed = 0.05;

        const y =
            window.scrollY * speed;

        img.style.transform =
            `scale(1.1) translateY(${y}px)`;
    });
});
