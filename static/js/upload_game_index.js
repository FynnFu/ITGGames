$(document).ready(function () {
    $(".sortable").sortable({
        update: function (event, ui) {
            var sortedIDs = $(".sortable-item").map(function() {
                return $(this).data("image-id");
            }).get();
            $.ajax({
                url: updateSequenceURL,
                type: "POST",
                data: {
                    ids: sortedIDs,
                    csrfmiddlewaretoken: csrfToken,
                },
                success: function (data) {
                    console.log("Sequence updated successfully.");
                },
                error: function (data) {
                    console.log("Error updating sequence.");
                },
            });
        },
    });
});