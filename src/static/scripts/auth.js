const btn = document.querySelector('button')
const login = document.querySelector('.input-login')
const password = document.querySelector('.input-password')

btn.onclick = (event) => {
    event.preventDefault()

    const apiUrl = '/auth/jwt/login'
    const requestBody = new URLSearchParams({
        grant_type: '',
        username: login.value,
        password: password.value,
        scope: '',
        client_id: '',
        client_secret: '',
    });

    fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'accept': 'application/json',
            },
            body: requestBody,
        })
        .then(data => fetch('users/me').then(resp => resp.json()).then(data => {
            if (data.email) {
                // window.location.href = ''
            }
        }))
}