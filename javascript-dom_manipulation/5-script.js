function change_text(){
	document.querySelector('header').textContent = 'New Header!!!';
}

document.getElementById('update_header').addEventListener('click', change_text)
