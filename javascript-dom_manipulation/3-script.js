/** 
 * Toggle the class of a tag with a click
 * @header get the dom element with tag header
 * 
 */ 

const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', () => {
    if (header.getAttribute('class') == 'red'){
        header.setAttribute('class', 'green');
    } else if (header.getAttribute('class') == 'green'){
        header.setAttribute('class', 'red');
    } 
});
