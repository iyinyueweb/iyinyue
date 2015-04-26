/**
 * Created by Administrator on 2015/4/26 0026.
 */
$(document).ready(function(){
    var value = $.cookie("UserName") == undefined ;
    var recommend_list = [];
    if(value){
        window.location.href = 'http://127.0.0.1:8000/user/login/';
    }else{
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/music/recommend/',
            dateType:'json',
            contentType:"application/json",
            async:false,
            data:{
              'user_name': $.cookie("UserName")
            },
            success: function(data){
                recommend_list = data;
            }
        });
        var append_html = '';
        for(var i = 0 ; i < recommend_list.length ; i ++){
            append_html += '<a href="#" class="list-group-item clearfix">'+
                          '<span class="pull-right h2 text-muted m-l">1</span>'+
                          '<span class="pull-left thumb-sm avatar m-r">'+
                            '<img src="'+recommend_list[i]['cover']+'" alt="...">'+
                          '</span>'+
                          '<span class="clear">'+
                            '<span>'+recommend_list[i]['title']+'</span>'+
                            '<small class="text-muted clear text-ellipsis">'+recommend_list[i]['artist']+'</small>'+
                          '</span>'+
                        '</a>'
        }
        $('.col-md-5 .list-group').append(
            append_html
        )
    }
});