const login = document.querySelector('button')

login.onclick = async() => {
    const mail = document.querySelector('.mail').value
    const password = document.querySelector('.password').value
    if (mail && password) {
        let resp = await fetch('http://localhost:8000/auth/jwt/login', {
            method: 'POST',
            headers: {
                'accept': 'application/json'
            },
            body: new URLSearchParams({
                'grant_type': '',
                'username': mail,
                'password': password,
                'scope': '',
                'client_id': '',
                'client_secret': ''
            })
        });
        console.log(resp)
    } else console.log('Введите пароль')

}