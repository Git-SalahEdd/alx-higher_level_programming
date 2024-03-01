$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (idx, elmnt) {
    $('#list_movies').append(elmnt.title + '</br>');
  });
});
