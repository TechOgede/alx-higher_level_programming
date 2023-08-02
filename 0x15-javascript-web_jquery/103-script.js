const $ = window.$;
$(document).ready(loadAfterContent);

function loadAfterContent () {
  $('INPUT#btn_translate').click(fetchTranslation);

  $('INPUT#btn_translate').keypress(function (e) {
    if (e.keyCode === 13 || e.which === 13 || e.charCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';

    const param = $('INPUT#language_code').val();

    $.get(url + param, function (data) {
      $('DIV#hello').text(data.name);
    });
  }
}
