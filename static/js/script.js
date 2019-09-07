$(function() {
    $('button').click(function() {
        var userQuery = $('#txtquery').val();

        $.ajax({
            url: '/serialize',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});