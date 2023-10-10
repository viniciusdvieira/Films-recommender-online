document.getElementById('scrollLink').addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default behavior of the link

    // Scroll smoothly to the target element
    document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const titles = [
        "Esta sem ideias de filmes para assistir?",
        "Descubra aqui qual filme se encaixa no seu padrão",
        "Seu Recomendador de filmes online"
    ];

    let currentTitleIndex = 0;
    const titleElement = document.getElementById("movie-title");

    function typeTitle() {
        let text = titles[currentTitleIndex];
        let charIndex = 0;
        const typeInterval = setInterval(function() {
            if (charIndex < text.length) {
                titleElement.textContent += text.charAt(charIndex);
                charIndex++;
            } else {
                clearInterval(typeInterval);
                setTimeout(eraseTitle, 2000);
            }
        }, 100);
    }

    function eraseTitle() {
        const eraseInterval = setInterval(function() {
            if (titleElement.textContent.length > 0) {
                titleElement.textContent = titleElement.textContent.slice(0, -1);
            } else {
                clearInterval(eraseInterval);
                currentTitleIndex = (currentTitleIndex + 1) % titles.length;
                setTimeout(typeTitle, 1000);
            }
        }, 50);
    }

    typeTitle(); // Iniciar a animação
});
