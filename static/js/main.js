$(document).ready(function() {
    $(document).ajaxSend(function(event, jqxhr, settings) {
        var post_id = settings.p_id;
        $("#loading-indicator_" + post_id).show();
    });
    $(document).ajaxComplete(function(event, request, settings) {
        var post_id = settings.p_id;
        $("#loading-indicator_" + post_id).fadeOut(1700);
    });
    $(".tooltip.delete").click(function() {
        var id = $(this).attr('id');
        var request = $.ajax({
            url: "/post/delete",
            type: "POST",
            data: {post_id: id},
            p_id: id, // for send handler ease
            dataType: 'json'
        });
        request.done(function(msg) {
            //$( "#log" ).html( msg );
            window.location.reload();
        });
        request.fail(function(jqXHR, textStatus) {
            alert( "Request failed: " + textStatus );
        });
    });

});
