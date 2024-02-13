/**
 * Create a new element and add to the html
 * @$ instance of the jQuery function
 */
const $ = window.$;

$('#add_item').on('click', () => {
  $('.my_list').append('<li>Item</li>');
});
