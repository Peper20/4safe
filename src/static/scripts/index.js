fetch('/users/me').then(resp => resp.json()).then(data => {
    console.log(data)
    if (data.detail === 'Unauthorized') {
        window.location.href = "login-register"

    }
})