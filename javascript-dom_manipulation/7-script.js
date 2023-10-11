const parent_t = document.querySelector('#list_movies');

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

const responseData = fetch(url).then( response => response.json());

console.log(responseData);

responseData.then( data => {
	const movies = data.results;
	console.log(movies);
	movies.forEach( movie => {
		const li_el = document.createElement('li');
		li_el.textContent = movie.title;
		parent_t.appendChild(li_el);
	});
});
	
