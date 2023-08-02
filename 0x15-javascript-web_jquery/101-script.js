const $ = window.$;
$(document).ready(loadAfterContent);

function loadAfterContent () {
  $('DIV#add_item').click(function () {
    $('<li></li>').text('Item').appendTo('UL.my_list');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list > li:last').remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
}
