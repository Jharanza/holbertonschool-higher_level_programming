function add_newItem(){
	let new_li = document.createElement('li');
	new_li.textContent = 'Item';
	let ul_class = document.querySelector('ul');
	ul_class.appendChild(new_li);
}

document.querySelector('#add_item').addEventListener('click', add_newItem);
