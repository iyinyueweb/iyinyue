__author__ = 'Administrator'


def json4music(music):
    music_json = {
        'id': music.id,
        'title': music.song_name,
        'artist': music.artist,
        'mp3': music.path,
        'poster': "images/m0.jpg"
        }
    return music_json