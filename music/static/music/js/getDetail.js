/**
 * Created by Administrator on 2015/5/1 0001.
 */
$(document).ready(function(){
    var music_id = window.location.href.split('?')[1].split('=')[1];
    $.ajax({
         type: 'GET',
         url: url + '/music/getDetail/',
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
            url:url+"/music/addComment/",
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
    var similarityMusics = [] ;
    var musicTags = [] ;
    $.ajax({
        type: 'GET',
         url: url+'/music/getComments/',
         dataType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'music_id':music_id
         },
        success: function(data){
            comments = data ;
         }
    });
    $.ajax({
        type: 'GET',
         url: url+'/music/getSimilarity/',
         dataType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'music_id':music_id
         },
        success: function(data){
            similarityMusics = data ;
         }
    });
    $.ajax({
        type: 'GET',
         url: url+'/music/getMusicTags/',
         dataType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'music_id':music_id
         },
        success: function(data){
            musicTags = data ;
         }
    });
    html_append += '<div class="panel wrapper-lg" music_id="'+music_id+'">'+
                       '<div class="row">'+
                            '<div class="col-sm-5">'+
                                '<img src="'+music['cover']+'" class="img-full m-b">'+
                            '</div>'+
                            '<div class="col-sm-7">'+
                                '<h2 class="m-t-none text-black">歌曲名：'+music['title']+'</h2>'+
                                 '<h2 class="m-t-none text-black">歌手：'+music['artist']+'</h2>'+
                        '<div class="m-b-lg">'+
                          '<a href="#" class="btn btn-info">播放</a> <a href="#" class="btn btn-default">'+comments.length+'</a>'+
                        '</div>'+
                        '<div>'+
                          '标签:</div> ';
    for(var t = 0 ; t < musicTags.length ; t ++){
        html_append += ' <a href="#" class="badge bg-light">'+musicTags[t]+'</a>' ;
    }
    html_append += '</div>'+'</div>'+
                    '</div>'+
                    '<div class="m-t">'+
                      '<p>描述</p>'+
                    '</div>'+'<h4 class="m-t-lg m-b">喜欢听"'+music['title']+'"的人还在听...</h4>'+
                    '<ul class="list-group list-group-lg">';
    for(var i = 0; i < similarityMusics.length ; i ++){
        html_append +='<li class="list-group-item">'+
                        '<div class="pull-right m-l">'+
                          '<a href="#" class="m-r-sm"><i class="icon-cloud-download"></i></a>'+
                          '<a href="#" class="m-r-sm"><i class="icon-plus"></i></a>'+
                          '<a class="m-r-sm heart"><i class="icon-heart"></i></a>'+
                        '<a class="m-r-sm share"><i class="icon-share"></i></a>'+
                        '</div>'+
                        '<a href="#" class="jp-play-me m-r-sm pull-left">'+
                          '<i class="icon-control-play text"></i>'+
                          '<i class="icon-control-pause text-active"></i>'+
                        '</a>'+
                        '<div class="clear text-ellipsis">'+
                          '<a href="http://192.168.191.1:8000/detail/?music_id='+similarityMusics[i]['id']+'">'+similarityMusics[i]['title']+'</a>'+
                          //'<span class="text-muted">__'+similarityMusics[i]['artist']+'</span>'+
                        '</div>'+
                      '</li>';
    }
    html_append +=  '<h4 class="m-t-lg m-b">'+comments.length+'条评论</h4>'+
                    '<section class="comment-list block">';
    for(var j = 0; j < comments.length ; j ++){
        html_append += '<article id="comment-id-'+j+'" class="comment-item">'+
                        '<a class="pull-left thumb-sm">'+
                          '<img src="/static/iyinyue/images/a1.png" class="img-circle">'+
                        '</a>'+
                        '<section class="comment-body m-b">'+
                          '<header>'+
                            '<a href="#"><strong>'+comments[j]['user_name']+'</strong></a>'+
                            /*'<label class="label bg-info m-l-xs">Editor</label>'+*/
                            '<span class="text-muted text-xs block m-t-xs">'+
                              comments[j]['comment_time']+
                            '</span>'+
                          '</header>'+
                          '<div class="m-t-sm">'+comments[j]['comment_content']+'</div>'+
                        '</section>'+
                      '</article>';
    }
    $('.col-sm-8').prepend(html_append);
}