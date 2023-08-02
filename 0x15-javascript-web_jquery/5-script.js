const $ = window.$;
$('#add_item').click(function () {
  $('<li></li>').text('Item').appendTo('UL.my_list');
});
