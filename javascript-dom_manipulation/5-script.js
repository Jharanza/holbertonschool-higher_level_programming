/**
 * Update the text from the element header
 * @header var that get the element header
 * @update var that get the element with id update_header
 */

const header = document.querySelector('header');
const update = document.querySelector('#update_header');

update.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});
