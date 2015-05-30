/**
 * Created by JJZHU on 2015/4/22 0022.
 */

$(document).ready(function(){
    var music_list =[];
    $.ajax({
         type: 'GET',
        // TODO
         url: url + '/music/getByGenre/',
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
        list += '<div class="col-xs-6 col-sm-4 col-md-3 col-lg-2">'+
                      '<div class="item">'+
                        '<div class="pos-rlt">'+
                          '<div class="bottom">'+
            //<!-- 时间-->
                            '<span class="badge bg-info m-l-sm m-b-sm"></span>'+
                          '</div>'+
                          '<div class="item-overlay opacity r r-2x bg-black">'+
                            '<div class="text-info padder m-t-sm text-sm">'+
                              '<i class="fa fa-star"></i>'+
                              '<i class="fa fa-star"></i>'+
                              '<i class="fa fa-star"></i>'+
                              '<i class="fa fa-star"></i>'+
                              '<i class="fa fa-star-o text-muted"></i>'+
                            '</div>'+
                            '<div class="center text-center m-t-n">'+
                              '<a href="#"><i class="icon-control-play i-2x"></i></a>'+
                            '</div>'+
                            '<div class="bottom padder m-b-sm">'+
                              '<a href="#" class="pull-right">'+
                                '<i class="fa fa-heart-o"></i>'+
                              '</a>'+
                              '<a href="#">'+
                                '<i class="fa fa-plus-circle"></i>'+
                              '</a>'+
                            '</div>'+
                          '</div>'+
                          '<a href="#"><img src="'+music_list[i]['cover']+'" alt="" class="r r-2x img-full"></a>'+
                        '</div>'+
                        '<div class="padder-v">'+
                          '<a href="'+url+'/detail/?music_id='+music_list[i]['id']+'" target="blank"" class="text-ellipsis">'+music_list[i]['title']+'</a>'+
                          '<a href="#" class="text-ellipsis text-xs text-muted">'+music_list[i]['artist']+'</a>'+
                        '</div>'+
                      '</div>'+
                    '</div>';
        if(i%2 == 0 && i != 0){
            list += '<div class="clearfix visible-xs"></div>';
        }
    }
    $(".row-sm").eq(0).append(
        list
    )
});

function new_song(){
    $.ajax({
         type: 'GET',
        // TODO
         url: url+'/music/getByGenre/',
         dateType:'json',
         contentType:"application/json",
         async:false,
         data:{
           'genres':'Blues'
         },
         success: function(data){

         }
    })
}