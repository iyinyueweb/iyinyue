/**
 * Created by Administrator on 2015/5/1 0001.
 */
$(document).ready(function(){
    var music_id = window.location.href.split('?')[1].split('=')[1];
    $.ajax({
         type: 'GET',
         url: 'http://127.0.0.1:8000/music/getDetail/',
         dateType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'music_id':music_id
         },
         success: function(data){
             showMusicInfo(data)
         }
    });
});

$(document).ready(function(){
    $('#comment_submit').bind("click", function(){
        if($('#comment_content').val() == ""){
            alert('内容为空');
        }
        $.ajax({
            url:"http://127.0.0.1:8000/music/addComment/",
            type:"POST",
            data:{
                comment_content: $('#comment_content').val(),
                comment_user: $.cookie("UserName"),
                comment_music_id: $('.col-sm-8 .panel').attr('music_id')
            },
            success: function(data){
                alert(data+'comment successful');
            }
        })
    });
});


function showMusicInfo(music){
    var html_append = '';
    var music_id = music['id'];
    var comments = [] ;
    $.ajax({
        type: 'GET',
         url: 'http://127.0.0.1:8000/music/getComments/',
         dateType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'music_id':music_id
         },
        success: function(data){
            comments = data ;
         }
    });
    html_append += '<div class="panel wrapper-lg" music_id="'+music_id+'">'+
                       '<div class="row">'+
                            '<div class="col-sm-5">'+
                                '<img src="'+music['cover']+'" class="img-full m-b">'+
                            '</div>'+
                            '<div class="col-sm-7">'+
                                '<h2 class="m-t-none text-black">'+music['title']+'</h2>'+
                        '<div class="m-b-lg">'+
                          '<a href="#" class="btn btn-info">播放</a> <a href="#" class="btn btn-default">'+comments.length+'</a>'+
                        '</div>'+
                        '<div>'+
                          '标签: <a href="#" class="badge bg-light">Musik</a>' +
                                '<a href="#" class="badge bg-light">Pashion</a>'+
                        '</div>'+
                      '</div>'+
                    '</div>'+
                    '<div class="m-t">'+
                      '<p>描述</p>'+
                    '</div>'+
                    '<h4 class="m-t-lg m-b">'+comments.length+'条评论</h4>'+
                    '<section class="comment-list block">';
    for(var i = 0; i < comments.length ; i ++){
        html_append += '<article id="comment-id-'+i+'" class="comment-item">'+
                        '<a class="pull-left thumb-sm">'+
                          '<img src="/static/iyinyue/images/a1.png" class="img-circle">'+
                        '</a>'+
                        '<section class="comment-body m-b">'+
                          '<header>'+
                            '<a href="#"><strong>'+comments[i]['user_name']+'</strong></a>'+
                            /*'<label class="label bg-info m-l-xs">Editor</label>'+*/
                            '<span class="text-muted text-xs block m-t-xs">'+
                              comments[i]['comment_time']+
                            '</span>'+
                          '</header>'+
                          '<div class="m-t-sm">'+comments[i]['comment_content']+'</div>'+
                        '</section>'+
                      '</article>';
    }
    $('.col-sm-8').prepend(html_append);
}