$(document).on("click", ".open-modal", function () {
    var id = $(this).data('data-id');
    $.get('/1', {}, function(data) {
    	$(myModal).html(data);
        console.log('itworks');
        console.log(data);
    });
    return false; // prevent default
});
