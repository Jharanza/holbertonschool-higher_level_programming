/**
 * Fetch the character name from an API
 * @$ call tot he function jQuery
 * @req promise to the given url
 * @url API's url
 * @jsonp Add dinamically a script to the html document of the API
 */
const $ = window.$;

const req = $.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  datatype: 'jsonp'
});
req.done(data => $('#character').text(data.name));
