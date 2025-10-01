const menuBtn = document.querySelector('header nav');
const menu = document.querySelector('header .links');
menuBtn.onclick = () => {
    menuBtn.classList.toggle('open');
    if (menu.classList.contains('open')){
        menu.classList.remove('open');
        menu.classList.add('close');
    }else{
        menu.classList.remove('close');
        menu.classList.add('open');
    }
}