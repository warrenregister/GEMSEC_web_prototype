var button = document.getElementById('enter_button');
var input = document.getElementById('input');
var ul = document.getElementById('results')

function performQuery(){
    if (input.value.length > 0) {
        var li = document.createElement('li');
        li.appendChild(document.createTextNode('3123  ngs_mos1_conv.csv  Warren Register'));
        ul.appendChild(li);
    }
}

button.addEventListener("click", performQuery);
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        button.click();
    }
})