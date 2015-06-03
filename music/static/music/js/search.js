/**
 * Created by jjzhu on 2015/5/18 0018.
 */
$(document).ready(function(){
    $('#search_music').bind('click', function(){
        var search_content = $("#music_or_album").val();
        if(search_content == ""){
            alert("请输入要搜索的音乐或专辑....")
        }else{
            $.ajax({
                type: 'GET',
                url: url+'/music/searchMusic/',
                dataType:'json',
                contentType:"application/json",
                async:false,
                data:{
                    'search_content':search_content
                },
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
                        +data[i]['album']+"</td></tr>";
                    }
                    content+=tbodyContent+"</tbody></table></div>";
                    $("#content").html(content);
                }
            })
        }
    })
});