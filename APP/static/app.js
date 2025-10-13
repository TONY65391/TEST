const menuBtn = document.querySelector('header nav');
const menu = document.querySelector('header .links');
const form = document.querySelector('body form');
const nameInput = document.getElementById('id_name');
const usernameInput = document.getElementById('id_username');
const emailInput = document.getElementById('id_email');
const passwordInput = document.getElementById('id_password');
const pictureInput = document.getElementById('id_Profile_Picture');
const error_list = document.querySelector('.bug .cont ol');
const errorBtn = document.querySelector('.bug .cont .options button');

if (errorBtn){
    errorBtn.addEventListener('click', () => {
        document.querySelector('.bug').classList.remove('show');
        document.querySelector('.bug').classList.add('hide');
    })
}

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
if (form){
    form.addEventListener('submit', (e) => {

        if (emailInput){
            error = Signup(usernameInput.value, emailInput.value, passwordInput.value);
            if (error.length > 0){
                e.preventDefault();
                document.querySelector('.bug').classList.add('show');
                document.querySelector('.bug').classList.remove('hide');

                error_list.innerHTML = "";
                for (i = 0; i < error.length; i++){
                    const li = document.createElement('li');
                    li.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> ${error[i]}`;
                    error_list.append(li);
                }
            }
        }
        else{
            error = Login(usernameInput.value, passwordInput.value);
            if (error.length > 0){
                e.preventDefault();
                document.querySelector('.bug').classList.add('show');
                document.querySelector('.bug').classList.remove('hide');

                error_list.innerHTML = "";
                for (i = 0; i < error.length; i++){
                    const li = document.createElement('li');
                    li.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> ${error[i]}`;
                    error_list.append(li);
                }
            }
        }

        function Signup(username, email, password){

            var error = []
            if (username === password){
                error.push("Username and password must not be similar");
            };
            if (username.includes('@') == false){
                error.push("Username must contain the '@' symbol")
            };
            if (username.includes(' ')){
                error.push("Username must not include space")
            };
            if (email.includes('@') == false){
                error.push("Email must contain the '@' symbol")
            };
            if (password.includes('@') == false){
                error.push("Password must not contain the '@' symbol")
            };
            if (password.includes(' ')){
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
            if (password.includes('@') == false){
                error.push("Password must contain the '@' symbol")
            };
            if (password.includes(' ')){
                error.push("Password must not include space");
            };
            if (username.includes('@') == false){
                error.push("Username must contain the '@' symbol")
            };
            if (username.includes(' ')){
                error.push("Username must not include space")
            };
            return error;
        };
    });
}