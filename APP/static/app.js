const menuBtn = document.querySelector('header nav');
const menu = document.querySelector('header .links');
const form = document.querySelector('body form');
const nameInput = document.getElementById('id_name');
const usernameInput = document.getElementById('id_username');
if (form){
    // const nameInput = form.
    console.log(nameInput)
    console.log(usernameInput)
}
// const nameInput = document


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