
function filters(id) {
    $('#brands').val(2);
    $("#pa_ge").val(1);
    console.log(id)
    // document.getElementById('formss').submit();

}


function page(page) {
    $("#pa_ge").val(page);
    document.getElementById('formss').submit();

}