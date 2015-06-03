/**
 * Created by jjzhu on 2015/4/11 0011.
 */
$(document).ready(function(){
    var play_list =[];
    $.ajax({
            type: 'GET',
            url: url+'/music/recommend/',
            dateType:'json',
            contentType:"application/json",
            async:false,
            data:{
              'user_name': $.cookie("UserName")
            },
            success: function(data){
                play_list = data;
            }
    });

    var list = "";
    for(var i = 0; i < play_list.length ; i ++){
        list += "<li class=\"list-group-item\" data-orign="+play_list[i]['id']+">"+
                "        <div class=\"pull-right m-l\">"+
                "          <a  class=\"m-r-sm download\"><i class=\"icon-cloud-download\"></i></a>"+
                "          <a  class=\"m-r-sm plus\"><i class=\"icon-plus\"></i></a>"+
                "          <a class=\"m-r-sm heart\"><i class=\"icon-heart\"></i></a>"+
                "          <a class=\"m-r-sm like\"><i class=\"icon-like\"></i></a>"+
                "          <a class=\"m-r-sm dislike\"><i class=\"icon-dislike\"></i></a>"+
                "          <a class=\"m-r-sm share\"><i class=\"icon-share\"></i></a>"+
                "          <i class=\"icon-close\"></i>"+
                "          </div>"+
                "          <a href=\"#\" class=\"jp-play-me m-r-sm pull-left\">"+
                "           <i class=\"icon-control-play text\"></i>"+
                          "<i class=\"icon-control-pause text-active\"></i>"+
                        "</a>"+
                        "<div class=\"clear text-ellipsis\">"+
                          "<a href='"+url+"/detail/?music_id="+play_list[i]['id']+"' target='blank'>"+play_list[i]['title']+"</a>"+
                          "<span class=\"text-muted\">__"+play_list[i]['artist']+"</span>"+
                        "</div>"+
                      "</li>" ;
    }
    $(".no-radius").append(
        list
            );

    $(".m-r-sm").click(function(){
        var id =$(this).parent().parent().attr("data-orign");
        if($(this).hasClass("download")){
            download_music(id);
        } else  if($(this).hasClass("plus")){
            plus_to_list(id)
        }
    });
});

/**
 * 下载音乐操作
 * @param music_id 当前音乐id
 */
function download_music(music_id){
    $.ajax({
        type: 'POST',
        url: url+'/music/download/',
        data:{
            music_id: music_id,
            user_name: $.cookie('UserName')
        },
        async:false,
        success: function(data){
            alert('successful:'+data);
        }
    })
}
/**
 * 将当前音乐添加都收听列表
 * @param music_id
 */
function plus_to_list(music_id){
    $.ajax({
        type: 'POST',
        url: url+'/music/addToList/',
        data:{
            music_id: music_id,
            user_name: $.cookie('UserName'),
            list_name: '默认列表'
        },
        async:false,
        success: function(data){
            alert('successful:'+data);
        }
    })
}

