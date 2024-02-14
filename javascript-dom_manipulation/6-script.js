/**
 * Insert the data from an API
 * @res the response after the request from the url
 * @data The json response from the previos request
 */

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => {
    document.querySelector('#character').innerText = data.name;
  })
  .catch(err => console.log(err));
