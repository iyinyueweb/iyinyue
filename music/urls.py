__author__ = 'Administrator'
from django.conf.urls import patterns, url
from music import views

urlpatterns = patterns('',
                       # 获取用户播放列表url
                       url(r'^getPlaylist/$', views.get_play_list, name='get_play_list'),
                       # 添加音乐到播放列表url
                       url(r'^addToList/$', views.add_to_playlist, name='add_to_playlist'),
                       # 用户下载操作url
                       url(r'^download/$', views.download, name='download'),
                       # 用户标记红心操作url
                       url(r'^heart/$', views.heart_operation, name='heart'),
                       # 用户踩操作url
                       url(r'^dislike/$', views.dislike_operation, name='dislike'),
                       # 初始化音乐（存储数据库）url
                       url(r'^init_music/$', views.init_music, name='initmusic'),
                       # 获取所有音乐列表url
                       url(r'^all/$', views.get_all, name='all'),
                       # 推荐歌曲url
                       url(r'^recommend/$', views.recommend, name='recommend'),
                       # 根据歌曲风格类别来获取音乐
                       url(r'^getByGenre/$', views.get_music_by_genre, name='getByGenre'),
                       # 获取单曲详情
                       url(r'^getDetail/$', views.get_detail_by_music_id, name='getDetail'),
                       # 获取单曲评论
                       url(r'^getComments/$', views.get_comments, name='getComments'),
                       # 添加评论
                       url(r'^addComment/$', views.add_comment, name='addComment'),
                       # 根据播放列表id获取列表歌曲
                       url(r'^getListSongById', views.get_song_by_list_id, name='getListSongById'),
                       # 根据列表名获取列表歌曲
                       url(r'^getListSongByName', views.get_songs_by_list_name, name='getListSongByName'),

                       url(r'^searchMusic', views.search_music, name='searchMusic'),
                       )