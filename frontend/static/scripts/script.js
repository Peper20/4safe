const btn = document.querySelector('button')
const login = document.querySelector('.input-login')
const password = document.querySelector('.input-password')

btn.onclick = (event) => {
    event.preventDefault(); // Предотвращаем стандартное поведение отправки формы

    const apiUrl = 'http://localhost:8000/auth/jwt/login';
    const requestBody = new URLSearchParams({
        grant_type: '',
        username: login.value,
        password: password.value,
        scope: '',
        client_id: '',
        client_secret: '',
    });

    fetch(apiUrl, {
            // mode: 'no-cors',
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'accept': 'application/json',
            },
            body: requestBody,
        })
        .then(response => response.json())
        .then(data => {
            // Обрабатываем данные ответа здесь
            console.log(data);
        })
        .catch(error => {
            // Обрабатываем ошибки здесь
            console.error('Error:', error);
        });
};