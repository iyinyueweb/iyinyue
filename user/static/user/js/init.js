/**
 * Created by Administrator on 2015/4/11 0011.
 */
$(function () {
    var userName = $.cookie("UserName");
    var value = userName == undefined ;
    if(value){
        var arr = window.location.href.split('/');
        var flag = true ;
        if( arr[arr.length - 2] != 'register'){
            flag = false ;
        }
        if( arr[arr.length - 2] != 'login'  ){
            flag = false ;
        }
        if(flag){
            window.location.href = url + '/user/login/';
        }
    }else{
        var user_info = '' ;
        $.ajax({
            type: 'GET',
            url: url + '/user/getUserInfo/?user_name='+userName,
            dataType:'json',
            contentType:"application/json",
            async:false,
            success: function(data){
                user_info = data
            }
        });

        $('.dropdown .bg ').append(
            '<span class="thumb-sm avatar pull-right m-t-n-sm m-b-n-sm m-l-sm">'+
            '                <img src="/static/iyinyue/images/a0.png" alt="...">'+
            '              </span>'+ user_info['user_name']+
            '               <b class="caret"></b>'+
            '            </a>'
        );

        showPlayList(userName);

    }
});

function showPlayList(userName){
    $.ajax({
            type: 'GET',
            url: url+'/music/getPlaylist/?user_name='+userName,
            dataType:'json',
            contentType:"application/json",
            async:false,
            success: function(data){
                var play_list = '';
                var icon = '';
                for(var i = 0; i < data.length; i ++){
                    if(data[i]['name'] == '我喜欢'){
                        icon = 'icon-heart'
                    }else{
                        icon = 'icon-music-tone'
                    }
                    play_list += '<li>'+
                                '<a href="#" class="playlist" list_id='+data[i]['id']+'>'+
                                '<i class="'+icon+' icon"></i>'+
                                '<b class="badge bg-success dker pull-right">'+data[i]['count']+'</b>'+
                                '<span>'+data[i]['name']+'</span>'+
                                '</a>'+
                                '</li>'
                }

                $('#play_list').append(
                    play_list
                );

                getListSong();

            }
        });
}


function getListSong(){


    $('.playlist').click(function(){
         var listId = $(this).attr('list_id');
        $.ajax({
            type: 'GET',
            url: url+'/music/getListSongById/?list_id='+listId,
            dataType:'json',
            contentType:"application/json",
            success: function(data){
                var  content = '<div class="table-responsive"><table class="table table-striped b-t b-light"><thead>' +
                    '<tr><th class="th-sortable">歌曲</th>' +
                    '<td>歌手</td>' +
                    '<td>专辑</td></tr></thead><tbody>';
                var len=data.length;
                var tbodyContent="";
                if(len==0){
                    return;
                }
                for(var i=0;i<len;i++){
                    tbodyContent +="<tr><td>"+"<a href="+url+"/detail/?music_id="+data[i]['id']+" target='blank'>"+data[i]['title']+"</a>" +
                    " <div class=\"pull-right m-l\">"+
                   "<a  class=\"m-r-sm download\"><i class=\"icon-control-play\"></i></a>"+
                "          <a  class=\"m-r-sm download\"><i class=\"icon-cloud-download\"></i></a>"+
                "          <a class=\"m-r-sm heart\"><i class=\"icon-heart\"></i></a>"+
                "          <a class=\"m-r-sm share\"><i class=\"icon-share\"></i></a>"+
                "          <i class=\"icon-close\"></i>"+
                "          </div></td><td>"
                    +data[i]['artist']+"</td><td>"
                    +data[i]['title']+"</td></tr>";
                }
                content+=tbodyContent+"</tbody></table></div>";
                $("#content").html(content);
            }
        })
    });
}

$('#logout').click(function () {
            alert("1111")
        });