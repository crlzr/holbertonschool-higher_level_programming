/* fetch  and list the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.
. */

function getTitle() {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then((data) => {
      data.results.forEach((film) => {
      const list = document.getElementById('list_movies');
      const li = document.createElement("li");
      li.textContent = film.title;
      list.appendChild(li);
      });
    });
}

// Call the function to fetch and display the titles
getTitle();
