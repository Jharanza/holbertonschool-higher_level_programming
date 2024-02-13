/**
 * get the data from an API when document is ready
 * @$ call to the jQuery function
 * @req request to the API
 * @data data from the responso to the API
 * @url API's url
 * @jsonp Add dinamically a script to the html document of the API
 */
const $ = window.$;

$(document).ready(() => {
  const req = $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    datatype: 'jsonp'
  });

  req.done(data => {
    $('#hello').text(data.hello);
  });
});
