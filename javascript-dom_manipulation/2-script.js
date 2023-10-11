function add_class(){
	document.querySelector('header').setAttribute('class', 'red')
}
document.querySelector('#red_header').addEventListener('click', add_class);
