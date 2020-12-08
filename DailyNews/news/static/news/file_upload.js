

$(function () {
$('#img_file').change(function uploadFile() {
   var formdata = new FormData();
   var file = document.getElementById('img_file').files[0];
   formdata.append('img_file', file);
   formdata.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
   $.ajax({
      xhr: function () {
         var xhr = new window.XMLHttpRequest();
         xhr.upload.addEventListener('progress', progressHandler, false);
         xhr.addEventListener('load', completeHandler, false);
         return xhr;
      },
      type : 'POST',
      url  : 'profile/updateImage/',
      data : formdata,
      success: function(data) {
         $('#profile-img').attr("src",data);
      },
      processData : false,
      contentType : false,
   });
});
});
