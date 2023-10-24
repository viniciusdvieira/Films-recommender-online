document.getElementById('scrollLink').addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default behavior of the link

    // Scroll smoothly to the target element
    document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
    });
});
