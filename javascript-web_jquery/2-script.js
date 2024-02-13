/**
 * Change the color of the element header with a click on the element with id #red_header
 * @$ references to the JQuery function
 */
const $ = window.$;

$('#red_header').click(() => {
  $('header').css('color', '#FF0000');
});
