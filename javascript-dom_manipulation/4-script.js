/**
 * Add a li element with a click
 * @li new element to add to the ul element
 * @myList var that get the ul element
 */

document.querySelector('#add_item').addEventListener('click', function() {

    const li = document.createElement('li');
    li.textContent = 'Item';
    
    const myList = document.querySelector('.my_list');
    myList.appendChild(li);

});
