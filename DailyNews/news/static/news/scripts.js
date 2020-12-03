
//updates categories in user profile
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

//likes an article with given id
$('.likeArticle').click(function () {
    var id = $(this).parent().attr("id");
    console.log(id);
    $.ajax({
        method: "POST",
        url: "likeArticle/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            aid: id
        },
        success: function (data) {
            if (data.liked == true) {
                //$(this).css("background-color", "blue");
                $(this).html("Unlike");
            }
            else if (data.liked == false) {
                //$(this).css("background-color", "white")
                $(this).html("Like");
            };
            

        }.bind(this)
    })
})

$('.submitComment').click(function () {
    var id = $(this).parent().parent().attr("id");
    console.log(id);
    var body = $(this).siblings("textarea").val();
    console.log(body);
    $.ajax({
        method: "POST",
        url: "addComment/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            aid: id,
            text:body
        },
        success: function (data) {
            var obj = data;
            $(this).parent().parent().children('.comments').append('<div class="comment" id = "' + obj.id + '" ><p>' + obj.author + ' posted</p><p>' + obj.text + '</p></div>');


        }.bind(this)
    })
})
