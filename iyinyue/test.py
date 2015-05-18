__author__ = 'Administrator'
import time
import _thread
import random
from user.models import *


def listen_thread(thread_name, delay):
    print(delay)
    while True:
        print(thread_name+'->:')
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
        t = random.randint(120, 360)
        print(t)
        time.sleep(t)


def list_listen_thread(thread_name, delay):
    print(thread_name, delay)
    while True:
        print(thread_name)
        user_count = IUser.objects.all().count()
        user_index = random.randint(1, user_count)
        curr_user = IUser.objects.all()[user_index-1]
        print(curr_user)
        hist_play_list = curr_user.play_list.get(play_list_name=u'历史记录')
        play_list = curr_user.play_list.get(play_list_name=u'默认列表')
        total = play_list.play_time.all().count()
        play_time_index = random.randint(1, total)
        play_time = play_list.play_time.all()[play_time_index-1]
        print(play_time.id)
        play_time.play_time += 1
        play_time.add_date = timezone.now()
        play_time.save()
        play_list.save()
        try:
            hist_play_list.play_time.get(music=play_time.music)
        except PlayTime.DoesNotExist:
            hist_play_list.play_time.add(play_time)
            hist_play_list.save()
        t = random.randint(120, 360)
        time.sleep(t)
        print(t)


def init_list():
    all_user = IUser.objects.all()
    music_count = Music.objects.all().count()
    for user in all_user:
        play_list = user.play_list.get(play_list_name=u'默认列表')
        try:
            favourite_list = user.play_list.get(play_list_name=u'我喜欢')
        except PlayList.DoesNotExist:
            favourite_list = PlayList()
            favourite_list.play_list_name = u'我喜欢'
            favourite_list.save()
            user.play_list.add(favourite_list)
            user.save()
        repeat_time = random.randint(50, 100)
        print(user.user_name)
        print(repeat_time)
        for i in range(repeat_time):
            music_index = random.randint(1, music_count)
            curr_music = Music.objects.all()[music_index - 1]
            try:
                play_list.play_time.get(music=curr_music)
            except PlayTime.DoesNotExist:
                play_time = PlayTime()
                play_time.music = curr_music
                play_time.play_time += 1
                play_time.add_date = timezone.now()
                play_time.save()
                play_list.play_time.add(play_time)
                play_list.save()
                if i % 5 == 0:
                    favourite_list.play_time.add(play_time)
                    favourite_list.save()


def start_listen_thread():
    # _thread.start_new_thread(listen_thread, ('thread_1', 3 * 60, ))
    # _thread.start_new_thread(listen_thread, ('thread_2', 3 * 60, ))
    # _thread.start_new_thread(listen_thread, ('thread_3', 3 * 60, ))
    # _thread.start_new_thread(listen_thread, ('thread_4', 3 * 60, ))
    # _thread.start_new_thread(listen_thread, ('thread_5', 3 * 60, ))
    _thread.start_new_thread(list_listen_thread, ('thread_6', 3 * 60, ))
    _thread.start_new_thread(list_listen_thread, ('thread_7', 3 * 60, ))
    _thread.start_new_thread(list_listen_thread, ('thread_8', 3 * 60, ))
    _thread.start_new_thread(list_listen_thread, ('thread_9', 3 * 60, ))
    _thread.start_new_thread(list_listen_thread, ('thread_10', 3 * 60, ))



