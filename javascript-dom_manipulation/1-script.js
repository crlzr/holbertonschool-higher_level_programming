// if red_header is clicked, the header shall change color
document.getElementById('red_header').onclick = changeColor;

function changeColor() {
  document.querySelector('header').style.color = '#FF0000';
}
