function loginCheck() {
    var email = document.getElementById("email").value
    var pwd = document.getElementById("pwd").value
    fetch('http://127.0.0.1:8000/alluser/')
        .then(function(response) {
            return response.json();
        }).then(function(data) {
            data.map(each => {
                console.log(email, pwd)
                if (each.first_name === email && each.last_name === pwd) {
                    window.location = "/search"
                }
            })
        });
}