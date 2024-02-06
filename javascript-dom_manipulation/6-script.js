/**
 * Insert the data from an API
 * @url the api where we get the request value
 * @res the response after the request from the url
 * @data The json response from the previos request
 */

url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

console.log(url)

fetch(url)
    .then(res => res.json())
    .then(data => {
        document.querySelector('#character').textContent = data.name;
    })
    .catch(err => console.log(err));
