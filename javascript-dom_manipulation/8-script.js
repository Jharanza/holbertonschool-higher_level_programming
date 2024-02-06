/**
 * Fetch and display a value imported in the head
 * @hello const that get the elememt with the 
 */

document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(res => res.json())
    .then(data => {
        const hello = document.querySelector('#hello');
        hello.innerText = data['hello'];
    });
});
