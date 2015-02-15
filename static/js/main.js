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
        //var page_y = $( document ).scrollTop();
        var id = $(this).attr('post_id');
        var request = $.ajax({
            url: "/post/delete",
            type: "POST",
            data: {post_id: id},
            p_id: id, // for send handler ease
            dataType: 'json'
        });
        request.done(function(msg) {
            location.reload();
            //$(document).scrollTop(page_y);
        });
        request.fail(function(jqXHR, textStatus) {
            alert( "Request failed: " + textStatus );
        });
    });
});
