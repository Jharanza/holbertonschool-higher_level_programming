/**
 * Change the text from the header element
 * @$ call to the function jQuery
 */
const $ = window.$;

$('#update_header').on('click', () => {
  $('header').text('New Header!!!');
});
