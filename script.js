const portfolioData = [
    },

    {
        title: 'Alumni',
        module: 'MODULE_15',
        image: 'images/alumni.jpg',
        description: `
        Alumni interactions inspired professional growth and networking.
        `
    }
];

const container = document.getElementById('portfolio-container');

portfolioData.forEach(item => {

    const section = document.createElement('section');

    section.className = 'section';

    const card = document.createElement('div');

    card.className = 'card';

    const imageBox = document.createElement('div');

    imageBox.className = 'image-box';

    const image = document.createElement('img');

    image.src = item.image;

    image.alt = item.title;

    const content = document.createElement('div');

    content.className = 'content';

    content.innerHTML = `
        <p class="module-id">${item.module}</p>
        <h2>${item.title}</h2>
        <p>${item.description}</p>
    `;

    image.onerror = () => {

        imageBox.remove();

        section.classList.add('no-image');
    };

    image.onload = () => {
        imageBox.appendChild(image);
    };

    card.appendChild(imageBox);

    card.appendChild(content);

    section.appendChild(card);

    container.appendChild(section);
});
