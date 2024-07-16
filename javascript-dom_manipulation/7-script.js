/* fetch  and list the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.
. */

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then((data) => {
    //console.log(data)
    document.getElementById('list_movies');
    let movies = data;

    movies.map(function(title)) {
      let li = document.createElement('li');
      li.appendChild(title);
    ul.appendChild(list_movies)
    }
  })
 .catch(error => Error(), {
})


