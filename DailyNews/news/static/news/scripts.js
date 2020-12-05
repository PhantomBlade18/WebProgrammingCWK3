
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

$('.email').click(function() {
    var id = $(this).val();
    if ($(this).prop('checked') == true) {
        $.ajax({
            method: "POST",
            url: 'profile/updateEmail/',
            headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
            data: {
                email: id,
            },
            success: function (data) {
                console.log(id + " updated!");
            }
        })
    }
}

$('.password').click(function() {
    var id = $(this).val();
    if ($(this).prop('checked') == true) {
        $.ajax({
            method: "POST",
            url: 'profile/updatePassword/',
            headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
            data: {
                password: id,
            },
            success: function (data) {
                console.log(id + " updated!");
            }
        })
    }
}

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
            $(this).parent().parent().children('.comments').append('<div class="comment" id = "' + obj.id + '" ><p class="commentor-meta">' + obj.author + ' posted</p><p class="comment-meta">' + obj.text + '</p></div>');


        }.bind(this)
    })
})
$('.submitReply').click(function () {
    var id = $(this).parent().parent().attr("id");
    console.log(id);
    var body = $(this).siblings("textarea").val();
    console.log(body);
    $.ajax({
        method: "POST",
        url: "addReply/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            cid: id,
            text: body
        },
        success: function (data) {
            var obj = data;
            $(this).parent().parent().children('.replies').append('<div class="reply" id = "' + obj.id + '" ><p class="commentor-meta">' + obj.author + ' replied</p><p class="comment-meta">' + obj.text + '</p></div>');


        }.bind(this)
    })
})

$('.deleteComment').click(function () {
    var id = $(this).parent().attr("id");
    console.log(id);
    $.ajax({
        method: "DELETE",
        url: "deleteComment/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            cid: id,

        },
        success: function (data) {
            var obj = data;
            $(this).parent().parent().children('.comments').append('<p> Comment Deleted! </p>');
            $(this).parent().remove();


        }.bind(this)
    })
})

$('.deleteReply').click(function () {
    var id = $(this).parent().attr("id");
    console.log(id);
    $.ajax({
        method: "DELETE",
        url: "deleteReply/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            rid: id,

        },
        success: function (data) {
            var obj = data;
            $(this).parent().parent().children('.replies').append('<p> Comment Deleted! </p>');
            $(this).parent().remove();


        }.bind(this)
    })
})
