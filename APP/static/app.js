const menuBtn = document.querySelector('header nav');
const menu = document.querySelector('header .links');
const form = document.querySelector('body form');
const nameInput = document.getElementById('id_name');
const usernameInput = document.getElementById('id_username');
const emailInput = document.getElementById('id_email');
const passwordInput = document.getElementById('id_password');
const pictureInput = document.getElementById('id_Profile_Picture');
const error_message = document.getElementById('error');

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

const allInputs = [...document.querySelectorAll('form input')];
var timeout;

function Timer(){
    clearTimeout(timeout);

    timeout = setTimeout(() => {
        error_message.style.display = 'none';
    }, 1000);
}

allInputs.forEach(input => {
    input.addEventListener('input', () => {
        Timer();
        error_message.style.display = '';
        error_message.innerHTML = '😎 typing . . .'
        error_message.classList.remove('bad');
        error_message.classList.add('good');
    })
})


form.addEventListener('submit', (e) => {

    if (emailInput){
        error = Signup(usernameInput.value, emailInput.value, passwordInput.value);
        if (error.length > 0){
            error_message.innerText = "";
            e.preventDefault()
            for (i = 0; i < error.length; i++){
                const errorItem = document.createElement('li');
                errorItem.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> ' + error[i];
                error_message.style.display = '';
                error_message.append(errorItem);
            }
            error_message.classList.remove('good');
            error_message.classList.add('bad');
        };
    }
    else{
        error = Login(usernameInput.value, passwordInput.value);
        if (error.length > 0){
            error_message.innerText = "";
            e.preventDefault()
            for (i = 0; i < error.length; i++){
                const errorItem = document.createElement('li');
                errorItem.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> ' + error[i];
                error_message.style.display = '';
                error_message.append(errorItem);
            }
            error_message.classList.remove('good');
            error_message.classList.add('bad');
        }
    }

    function Signup(username, email, password){

        var error = []
        if (username === password){
            error.push("Username and password must not be similar");
        };
        if (String(username).includes('@') == false){
            error.push("Username must contain the '@' symbol")
        };
        if (String(username).includes(' ')){
            error.push("Username must not include space")
        };
        if (String(email).includes('@') == false){
            error.push("Email must contain the '@' symbol")
        };
        if (String(password).includes('@')){
            error.push("Password must not contain the '@' symbol")
        };
        if (String(password).includes(' ')){
            error.push("Password must not include space");
        };
        if (password.length < 8){
            error.push("Password must contain at least 8 characters")
        };
        if (username.length < 10){
            error.push("Username must contain at least 10 characters");
        };
        if (password.length < 10){
            error.push("Password must contain at least 10 characters");
        };
        
        return error;
    };

    function Login(username, password){
        var error = [];
        if (username === password){
            error.push("Username and password must not be similar");
        };
        if (password.length < 8){
            error.push("Password must contain at least 8 characters")
        };
        if (username.length < 10){
            error.push("Username must contain at least 10 characters");
        };
        if (password.length < 10){
            error.push("Password must contain at least 10 characters");
        };
        if (String(password).includes('@')){
            error.push("Password must not contain the '@' symbol")
        };
        if (String(password).includes(' ')){
            error.push("Password must not include space");
        };
        if (String(username).includes('@') == false){
            error.push("Username must contain the '@' symbol")
        };
        if (String(username).includes(' ')){
            error.push("Username must not include space")
        };
        return error;
    };
});