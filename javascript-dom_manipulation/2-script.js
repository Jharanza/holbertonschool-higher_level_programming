// add a class to a tag

document.querySelector('#red_header').addEventListener('click', () => {
  document.querySelector('header').setAttribute('class', 'red');
});
