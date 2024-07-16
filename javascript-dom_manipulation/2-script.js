// adds the class red to the header element when the user
//clicks on the tag with id red_header
document.getElementById('red_header').onclick = addClass;

function addClass() {
  document.querySelector('header').classList.add('red');
}
