$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
  const movies = data.results;
  const list = $('#list_movies');

  for (let i = 0; i < movies.length; i++) {
    let titleM = movies[i].title;
    list.append('<li>' + titleM + '</li>');
  }
});
