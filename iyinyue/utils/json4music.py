__author__ = 'Administrator'
from iyinyue import constant
import os


# music info 转换json
def json4music(music):
    cover = constant.PROJECT_PATH + '/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
    if os.path.exists(cover):
        cover = constant.URL + '/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
    else:
        cover = constant.URL + '/static/iyinyue/mp3/cover/default.jpg'
    music_json = {
        'id': music.id,
        'title': music.song_name,
        'artist': music.artist,
        'album': music.album,
        'mp3': constant.URL + music.path,
        'poster': "images/m0.jpg",
        'cover': cover
        }
    return music_json