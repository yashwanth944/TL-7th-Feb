function receive(sender, receiver, trail) {
    varmemberCount = document.getElementById("memberCount")
    $.get('/alluser/', function(data) {
        console.log(data);
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                console.log(parseInt(data[i].sender));
                console.log(parseInt(receiver));
                if (parseInt(data[i].sender) == parseInt(receiver)) {
                    box = box.replace('right', 'left blue lighten-5');
                }
                $('#board').append(box);
                scrolltoend();
                if (time < data[i].id) {
                    time = data[i].id;
                }
            }
        }
    })
}

window.onload = function() {
    homeCount();
};

function homeCount() {
    var memberCount = document.getElementById("memberCount");
    memberCount.innerText = "0"
    fetch('http://127.0.0.1:8000/alluser/')
        .then(function(response) {
            return response.json();
        }).then(function(data) {
            memberCount.innerText = data.length
        });
}