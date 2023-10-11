
let parent_text = document.querySelector('#character');

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

const responseData = fetch(url).then( res => res.json());

responseData.then(({name}) => {
	for (const data of name){
		text = document.createTextNode(data);
		parent_text.appendChild(text);
	}	
});


