__author__ = 'jjzhu'
__doc__ = '获取平台所有用户的topN歌曲'

from user.models import *


def top_n():
    all_users = IUser.objects.all()  # 获取所有用户
    # for user in all_users:




