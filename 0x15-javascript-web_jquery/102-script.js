$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.post('https://hellosalut.stefanbohacek.dev', { lang: $('#language_code').val() }, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
});
