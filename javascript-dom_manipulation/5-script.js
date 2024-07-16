// updates the text of the header element to New Header!!!
// when the user clicks on the element with id update_header

document.getElementById('update_header').onclick = changeText;

function changeText() {
  document.querySelector("header").innerHTML = "New Header!!!";
}