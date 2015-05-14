__author__ = 'Administrator'
import time
import _thread
import random
from user.models import *


def listen_thread(delay):
    print(delay)
    while True:
        user_count = IUser.objects.all().count()
        music_count = Music.objects.all().count()
        user_index = random.randint(1, user_count)
        music_index = random.randint(1, music_count)
        curr_user = IUser.objects.all()[user_index-1]
        curr_music = Music.objects.all()[music_index - 1]
        print(curr_user)
        print(curr_music)
        play_list = curr_user.play_list.get(play_list_name=u'历史记录')
        try:
            play_time = play_list.play_time.get(music=curr_music)
        except PlayTime.DoesNotExist:
            play_time = PlayTime()
            play_time.music = curr_music
        play_time.play_time += 1
        play_time.add_date = timezone.now()
        play_time.save()
        play_list.play_time.add(play_time)
        play_list.save()
        time.sleep(delay)


def start_listen_thread():
    _thread.start_new_thread(listen_thread, (3 * 60, ))



