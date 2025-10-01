const menuBtn = document.querySelector('header nav');
const menu = document.querySelector('header .links');
menuBtn.onclick = () => {
    menuBtn.classList.toggle('open');
    menu.classList.toggle('open')
}