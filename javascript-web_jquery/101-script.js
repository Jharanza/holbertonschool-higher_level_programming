$(document).ready(function() {
  $('#add_item').click(function() {
    const item = $('<li>Item</li>');
    $('UL.my_list').append(item);
  });
  $('#remove_item').click(function() {
    const list = $('UL.my_list');
    list.find('li:last').remove();
  });
  $('#clear_list').click(function() {
    $('UL.my_list').empty();
  });
});
