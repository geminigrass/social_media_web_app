alert("1")
window.onload=function(){

var input = document.getElementById('textfield');
var todolist = document.getElementById('todolist');
var addBtn = document.getElementById('addBtn');

addBtn.addEventListener('click',addItem)

function addItem() {
    var li = document.createElement("li");

    li.innerHTML = input.value;

    todolist.appendChild(li)
}


}






