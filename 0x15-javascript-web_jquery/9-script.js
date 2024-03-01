$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
  $('#hello').text(data.hello);
});
