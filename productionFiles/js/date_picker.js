document.addEventListener('DOMContentLoaded', function() {
    $('#date_picker_icon').click(function() {
        $('#id_date').datepicker().focus();
    });

    $('#id_date').change(function() {
        $('#date_text').val($(this).val());
    });
});
