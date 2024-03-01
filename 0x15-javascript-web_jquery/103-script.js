$(document).ready(function () {
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { $('#btn_translate').click(); }
  });
  $('#btn_translate').click(function () {
    $.post('https://hellosalut.stefanbohacek.dev', { lang: $('#language_code').val() }, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
});
