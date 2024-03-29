$(document).ready(function () {
    $('.comments').hide();
    $('.commentForm').hide();
    $('.replies').hide();
    $('.ReplyForm').hide();
    $('.response').hide();
    $('.editCommentForm').hide();

})

$('.comment-button').click(function () {
    $(this).siblings('.comments').show();
    $(this).siblings('.commentForm').show();
})
$('.Reply').click(function () {
    $(this).siblings('.replies').show();
    $(this).siblings('.ReplyForm').show();
})
$('.ResponseReply').click(function () {
    $(this).parent().siblings('.response').show();
})
$('.editCommentbtn').click(function () {
    $(this).siblings('.editCommentForm').show();
})
$('.editReplybtn').click(function () {
    $(this).siblings('.editCommentForm').show();
})
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

$('#ChangeEmail').click(function (e) {
    e.preventDefault();
    var nemail = $('input[name=currentPassword]').val()
    $.ajax({
        method: "POST",
        url: 'updateEmail/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            email: nemail,
        },
        success: function (data) {
            console.log(id + " updated!");
        }
    })
})

$('#ChangePassword').click(function (e) {
    e.preventDefault();
    var cPass = $('input[name=currentPassword]').val()
    var nPass = $('input[name=newPassword]').val()
    console.log("Check check")
    $.ajax({
        method: "POST",
        url: 'updatePassword/',
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            currentPassword: cPass,
            newPassword: nPass,
        },
        success: function (data) {
            if (data.successful == true) {
                alert(data.message);

            }
            else if (data.successful == false) {
                alert(data.message);
            }
        }
    })
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
    var id = $(this).parent().parent().parent().attr("id");
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

            $(this).parent().siblings('.comments').append('<div class="comment" id = "' + obj.id + '" ><p class="commentor-meta">' + obj.author + ' posted</p><p class="comment-meta">' + obj.text + '</p></div>');


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
            $(this).parent().siblings('.replies').append('<div class="reply" id = "' + obj.id + '" ><p class="commentor-meta">' + obj.author + ' replied</p><p class="comment-meta">' + obj.text + '</p></div>');
            $(this).parent().hide();

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

$('.editComment').click(function () {
    var id = $(this).parent().parent().attr("id");
    console.log(id);
    var body = $(this).siblings("textarea").val();
    console.log(body);
    $.ajax({
        method: "PUT",
        url: "updateComment/",
        headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
        data: {
            cid: id,
            text: body
        },
        success: function (data) {
            var obj = data;
            $(this).parent().siblings('.commentText').text(obj.text);
            $(this).parent().hide();

        }.bind(this)
    })
})

$('.ReplyResponse').click(function () {
    var id = $(this).parent().attr("id");
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
            $(this).parent().parent().children().append('<div class="reply" id = "' + obj.id + '" ><p class="commentor-meta">' + obj.author + ' replied</p><p class="comment-meta">' + obj.text + '</p></div>');
            $(this).parent().hide();


        }.bind(this)
    })
})
