$('#add_item').on('click', function(){
  var newItem = $('<li>Item</li>');
  $('ul.my_list').append(newItem);
});
