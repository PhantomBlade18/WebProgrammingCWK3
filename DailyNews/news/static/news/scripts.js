

$('.category').click(function() {
    var id = $(this).val();
    if ($(this).prop('checked') == true) {
        $.ajax({
            method: "PUT",
            url: "updateCategory/",
            headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
            data: {
                catName: id,
            },
            success: function (data) {
                console.log(id + " updated!");
                $('#profileFavCats').append('<li>' + id + '</li>');
            }
        })
    }
    else {
        $.ajax({
            method: "DELETE",
            url: "updateCategory/",
            headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
            data: {
                catName: id,
            },
            success: function (data) {
                console.log(id + " deleted!");
                children = $('#profileFavCats').children()
                for (i = 0; i < children.length; i++) {
                    if (children[i].val == id)
                        children[i].remove();
                }
            }
        })
    }

})
