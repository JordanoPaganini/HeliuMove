const params = new URLSearchParams(window.location.search)

document.addEventListener('keydown', function(event) {
    if (event.key == 'Enter') {
        event.preventDefault();
        document.getElementById('send').click()
    }
})

function redirect (code, url='/plataforma/') {
    if(code == '200') {
        window.location.href = url
    } else if (code == '401') {
        document.getElementsByName("username")[0].value = '';
        document.getElementsByName("password")[0].value = '';
        window.alert('Usuário ou senha inválido')
    } else {
        console.log('Código HTTP inválido, contate o desenvolvedor')
    }
}

function send () {
    username = document.getElementsByName("username")[0].value;
    password = document.getElementsByName("password")[0].value;

    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    data = new FormData()
    data.append('username', username)
    data.append('password', password)

    fetch('/auth/login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result) {
        return result.json()
    }).then(function(data) {
        urlRedirect = params.get('next')
        if (urlRedirect) {
            redirect(code=data['code'], url=urlRedirect)
        } else {
            redirect(code=data['code'])
        }
    })
}