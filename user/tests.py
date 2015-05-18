from django.test import TestCase

# Create your tests here.
from user.models import *
import hashlib


def add_user():
    fp = open('f:/project/iyinyue/user/data/iuser.txt', encoding='utf-8')
    for line in fp.readlines():
        try:
            user = IUser.objects.get(user_name=line.strip())
        except IUser.DoesNotExist:
            # 用户不存在
            user = IUser()
        else:
            # 用户已经存在
            continue
        default_list = PlayList()  # 创建默认播放列表
        default_list.play_list_name = u'默认列表'  # 默认播放列表名
        default_list.save()

        favorite_list = PlayList()
        favorite_list.play_list_name = u'我喜欢'
        favorite_list.save()

        history_list = PlayList()
        history_list.play_list_name = u'历史记录'
        history_list.save()

        audition_list = PlayList()
        audition_list.play_list_name = u'试听列表'
        audition_list.save()

        user.save()
        user.play_list.add(default_list)
        user.play_list.add(favorite_list)
        user.play_list.add(history_list)
        user.play_list.add(audition_list)
        user.user_name = line.strip()
        user.password = hashlib.sha1('vs7452014'.encode(encoding='utf-8')).hexdigest()

        user.save()