/**
 * Add a class to the element header when clicked the element wiht the #red_header id
 * @$ Reference to the function jQuery
 */
const $ = window.$;

$('#red_header').click(() => {
  if (!$('header').hasClass('red')) {
    $('header').addClass('red');
  }
});
