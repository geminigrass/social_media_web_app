//TODO:
//init the page
function populateCommentList() {
    $.get("get-json-posts-followers")
        .done(function (data) {
            console.log(data);
            updatePostData(data);
            //TODO:UNcommon this
            $.get("get-json-comments-followers")
            .done(function(data) {
                updateCommentData(data);
            });
        });
}

function updatePostData(data) {
    var div_post_list = $("#post-list");
    $('#timestamp').val(data['timestamp']);
    for(var i = 0; i< data['posts'].length;i++){
        var html = '';
        var author_name = data['posts'][i]['author_name'];
        var time = data['posts'][i]['time'];
        var content = data['posts'][i]['content'];
        var title = data['posts'][i]['title'];
        var post_id = data['posts'][i]['post_id'];

        html += '<div class="panel panel-primary" id = "panel-' + post_id + '">';
        html += '<div class="panel-heading">'+'<h5 class="panel-title">';
        html += '<a href="/profile/'+ author_name + '">' + title + '</a>';
        html += '</h5>' + '</div>' + '<div class="panel-body">';
        html += content + '</div>' + '<div class="panel-footer text-muted">';
        html += time + ', host by : ' + '<a href="/profile/' + author_name + '">' + author_name + '</a>';

        if (data['posts'][i]['author_pic_url'] != null){
            var author_pic = data['posts'][i]['author_pic_url'];
            html += '<img src="' + author_pic + '" class="img-thumbnail img-responsive" width="40" height="40"> ';
        }

        html += '</div>'+'<ul class="list-group">'+'<li class="list-group-item item-form">';
        html += '<div class="comment-form">';
        html += '<input type="text" class="comment-input">';
        html += '<input type="hidden" class="hidden-input" name="belong_to_post" value="' + title + '">';
        html += '<button class="comment-btn">Comment</button>';
        html += '</div>' + '</li>';
        html += '<li class="list-group-item comments-list" id="post-'+post_id+'">';
        html += '</li>'+'</ul>'+'</div>';
        div_post_list.prepend(html);
        $('.comment-btn').click(function () {
            var new_request = {};
            new_request["content"]= $(this).parent().find('.comment-input').val();
            new_request['belong_to_post']= $(this).parent().find('.hidden-input').val();

            new_request['timestamp'] = $('#timestamp').val();
            console.log("--------I'v manualy change the new_req");
            console.log(new_request);
            $.post("/add-comment", new_request)
              .done(function (data) {
                  console.log("--------The '/add-comment' reseponceText is :");
                  console.log(data);
                  refreshComment();
                  // updateCommentData(data);
              });
        });
    }
}

//handle data response, do the append new data only
//doesn't perform empty()
function updateCommentData(data) {
    $('#timestamp').val(data['timestamp']);
    for(var i = 0; i< data['comments'].length;i++){
        var html = '';
        var author = data['comments'][i]['author'];
        var belong_to_post = data['comments'][i]['belong_to_post'];
        var content = data['comments'][i]['content'];
        var time = data['comments'][i]['time'];
        if (data['comments'][i]['author_pic'] != null){
            var author_pic = data['comments'][i]['author_pic'];
            html += '<img src="' + author_pic + '" class="img-thumbnail img-responsive" width="40" height="40"> ';
        }
        html += '<a href="/profile/' + author + '">' + author + '</a>' + ' comments at ';
        html += time + ' : ';
        $('#post-'+belong_to_post).append(
            '<li>' + html + content + '</li><br>'
        );
    }
}

//refresh
function refreshComment() {
    $.get("get-json-comments-followers", {'timestamp':$('#timestamp').val()})
      .done(function(data) {
          console.log(data);
            updateCommentData(data);
      });
}

function refreshPost() {
    $.get("get-json-posts-followers", {'timestamp':$('#timestamp').val()})
        .done(function (data) {
            updatePostData(data);
        });
}

$(document).ready(function () {
  // CSRF set-up copied from Django docs
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  //TODO:uncommom
  // function csrfSafeMethod(method) {
  //   // these HTTP methods do not require CSRF protection
  //   return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  // }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });

  // Set up to-do list with initial DB items and DOM data
  populateCommentList();
  // Periodically refresh to-do list
    //TODO:uncommon this
  window.setInterval(refreshComment, 5000);
  window.setInterval(refreshPost,5000);
});// End of $(document).ready
