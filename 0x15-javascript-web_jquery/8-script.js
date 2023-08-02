const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  $.each(data.results, function (index, movie) {
    $('<li></li>').text(movie.title).appendTo('UL#list_movies');
  });
});
