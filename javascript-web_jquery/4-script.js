/**
 * Toggle the class of the header element between red and green
 * @$ variable to call the function jQuery
 */
const $ = window.$;

$('#toggle_header').click(() => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
