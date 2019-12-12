$('.ui.dropdown')
    .dropdown()
;
$('select.dropdown')
  .dropdown()
;
$('.category.example .ui.dropdown')
  .dropdown({
    allowCategorySelection: true
  })
;
$('.ui.radio.checkbox')
  .checkbox()
;
$('#progressBar')
  .progress({percent:20})
;
//USE FOR MULTIPLE CHECKBOXES
$('.label.ui.dropdown')
  .dropdown();

$('.no.label.ui.dropdown')
  .dropdown({
  useLabels: false
});

$('.ui.button').on('click', function () {
  $('.ui.dropdown')
    .dropdown('restore defaults')
})
