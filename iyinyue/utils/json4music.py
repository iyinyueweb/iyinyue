__author__ = 'Administrator'


# music info 转换json
def json4music(music):
    music_json = {
        'id': music.id,
        'title': music.song_name,
        'artist': music.artist,
        'mp3': music.path,
        'poster': "images/m0.jpg",
        'cover': 'http://127.0.0.1:8000/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
        }
    return music_json