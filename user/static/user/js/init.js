/**
 * Created by Administrator on 2015/4/11 0011.
 */
$(function () {
    var userName = $.cookie("UserName");
    var value = userName == undefined ;
    if(value){
        window.location.href = 'http://127.0.0.1:8000/user/login/';
    }else{
        var user_info = '' ;
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/user/getUserInfo/?user_name='+userName,
            dateType:'json',
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
            url: 'http://127.0.0.1:8000/music/getPlaylist/?user_name='+userName,
            dateType:'json',
            contentType:"application/json",
            async:false,
            success: function(data){
                var play_list = '';
                for(var i = 0; i < data.length; i ++){
                    play_list += '<li>'+
                                '<a href="#">'+
                                '<i class="icon-music-tone icon"></i>'+
                                '<b class="badge bg-success dker pull-right">'+data[i]['count']+'</b>'+
                                '<span>'+data[i]['name']+'</span>'+
                                '</a>'+
                                '</li>'
                }

                $('#play_list').append(
                    play_list
                );


            }
        });
}


$('#logout').click(function () {
            alert("1111")
        });