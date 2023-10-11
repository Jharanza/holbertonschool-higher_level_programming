function toggle_h(){
        let header = document.querySelector('header');
	let header_class = header.getAttribute('class');
	
	if(header_class){
		if (header_class === 'green'){
			header.setAttribute('class', 'red');
		}  
		if(header_class === 'red'){
			header.setAttribute('class', 'green');
		}
	}
}
document.querySelector('#toggle_header').addEventListener('click', toggle_h);
