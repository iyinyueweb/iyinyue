/**
 * Created by jjzhu on 2015/5/6 0006.
 */

/*
 * 根据播放列表名字获取歌曲
 */
function getSongsByListName(user_name, list_name){
    var play_list = [];
    $.ajax({
        type: 'GET',
        url: url + '/music/getListSongByName/',
        data:{
            user_name: user_name,
            list_name: list_name
        },
        dateType:'json',
        contentType:"application/json",
        async:false,
        success: function(data){
           play_list = data;
        }
    });
    return play_list;
}
