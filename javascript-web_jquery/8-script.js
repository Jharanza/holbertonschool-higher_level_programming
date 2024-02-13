/**
 * Get the titles of the movies from an given API
 * @$ call to the function jQuery
 * @req request to the API
 * @data response manipulation from the request
 * @info requested info
 * @url API's url
 * @jsonp Add dinamically a script to the html document of the API
 */
const $ = window.$;

const req = $.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  datatype: 'jsonp'
});

req.done(data => {
  for (const info of data.results) {
    $('#list_movies').append(`<li>${info.title}</li>`);
  }
});
