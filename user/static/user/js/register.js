/**
 * Created by Administrator on 2015/4/9 0009.
 */

$(function () {
    $('#register').bind("click",function(){
        $.ajax({
            url:url+"/user/register/",
            type:"POST",
            data:{
                user_name: $('#user_name').val(),
                user_email: $('#user_email').val(),
                user_password: $('#user_password').val()
            },
            success: function(data){
                if(data == 2){
                    alert('阿偶，昵称已被用过啦=，=')
                }
                if(data == 1){
                    $.cookie("UserName", $('#user_name').val(), {path:'/'});
                    window.location.href=url+"/index/";
                }
            }
        })
    });
});