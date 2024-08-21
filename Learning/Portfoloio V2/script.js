const nav = document.querySelector('nav');
const menuLinks = document.querySelectorAll('.menu-link');
const main = document.querySelector('main');

menuLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const href = link.getAttribute('href');
        const page = href.replace('#', '');
        loadPage(page);
    });
});

function loadPage(page) {
    nav.classList.add('open');
    menuLinks.forEach((link) => {
        link.classList.remove('open');
    });
    document.querySelector(`[href="#${page}"]`).classList.add('open');
    main.innerHTML = '';
    fetch(`${page}.html`)
        .then((response) => response.text())
        .then((html) => {
            main.innerHTML = html;
            nav.classList.remove('open');
        });
}