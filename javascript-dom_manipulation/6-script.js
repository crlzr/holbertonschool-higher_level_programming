/* fetch the character name from this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag with id character.
You must use the Fetch API. */

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then((data) => {
    //console.log(data)
    document.getElementById('character').innerHTML = data.name;
  })
  .catch(error => Error(), {
})


