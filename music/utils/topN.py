__author__ = 'jjzhu'
__doc__ = '获取平台所有用户的topN歌曲'
from user.models import *

TOP = 10


def top_n():
    all_users = IUser.objects.all()  # 获取所有用户
    data = {}
    for user in all_users:
        history_list = user.play_list.all().get(play_list_name=u'历史记录')

        ten_day = timezone.now() - timezone.timedelta(days=10)
        # 查找出最近10天的听歌记录,并按播放次数降序排序
        musics = history_list.play_time.all().filter(add_date__gt=ten_day, play_time__gt=2).order_by('-play_time')
        if musics.all().count() < TOP:
            data[user.id] = musics
        else:
            data[user.id] = musics[: TOP]
    return data






