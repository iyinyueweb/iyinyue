/**
 * Created by Administrator on 2015/4/22 0022.
 */
$(document).ready(function(){
    var music_list =[];
    $.ajax({
         type: 'GET',
         url: 'http://127.0.0.1:8000/music/getByGenre/',
         dateType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'genres':'Blues'
         },
         success: function(data){
             music_list = data ;
         }
    });

    var list = "";
    for(var i = 0; i < music_list.length ; i ++) {
        list += '<div class="col-xs-6 col-sm-4 col-md-3 col-lg-2">' +
        '<div class="item">' +
        '<div class="pos-rlt">' +
        '<div class="item-overlay opacity r r-2x bg-black">' +
        '<div class="center text-center m-t-n">' +
        '<a href="#"><i class="fa fa-play-circle i-2x"></i></a>' +
        '</div>' +
        '</div>' +
        '<a href="track-detail.html"><img src="' + music_list[i]['cover'] + '" alt="" class="r r-2x img-full"></a>' +
        '</div>' +
        '<div class="padder-v">' +
        '<a href="track-detail.html" data-bjax data-target="#bjax-target" data-el="#bjax-el" data-replace="true" class="text-ellipsis">' + music_list[i]['title'] + '</a>' +
        '<a href="track-detail.html" data-bjax data-target="#bjax-target" data-el="#bjax-el" data-replace="true" class="text-ellipsis text-xs text-muted">' + music_list[i]['artist'] + '</a>' +
        '</div>' +
        '</div>' +
        '</div>'
    }
    $(".row-sm").append(
        list
    )
});