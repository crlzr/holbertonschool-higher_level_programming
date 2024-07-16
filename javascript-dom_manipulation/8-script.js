/* fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML element with id hello.
The translation of “hello” must be displayed in the HTML element with id hello
Your script must work when it is imported from the <head> tag
. */

fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then((data) => {
    //console.log(data)
    document.getElementById('hello').innerHTML = data.hello;
  })
  .catch(error => Error(), {
})