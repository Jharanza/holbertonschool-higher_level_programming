/**
 * Show the title of many movies in the ul element
 * @res response from the fetch
 * @data response in dict format
 * @ul variable that get the element with the id list_movies
 * @li new element that get the name of the movie
 */

const ul = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    for (const info of data.results) {
      const li = document.createElement('li');
      li.innerText = info.title;
      ul.appendChild(li);
    }
  });
