/**
 * Change the color of the element when the document is ready
 * @$ call to the jQuery function
 * @header variable that get the header element
 */
const $ = window.$;

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
