__author__ = 'jjzhu'
__doc__ = '获取平台所有用户的topN歌曲'
import math
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


def get_score():
    all_users = IUser.objects.all()
    all_score = {}  # 存储评分数据
    for user in all_users:
        this_score = {}  # 存储单个用户的评分数据
        # 获取历史播放记录列表
        history_list = user.play_list.all().get(play_list_name=u'历史记录')
        # 获取
        favourite_list = user.play_list.all().get(play_list_name=u'我喜欢')
        for play_time in history_list.play_time.all():
            last_play_time = play_time.add_date
            time_count = play_time.play_time
            try:
                # 是否在“我喜欢”列表中
                favourite_list.play_time.all().filter(music=play_time.music)
            except PlayTime.DoesNotExist:
                init_count = 1
            else:
                init_count = 2
            # 计算公式 score = init + log(time)/(1+a(T-t))
            score = init_count + math.log(time_count)/\
                                 (1 + 0.5 + (timezone.now() - last_play_time))
            if score > 10:
                score = 10
            this_score[play_time.music.id] = score
        all_score[user.id] = this_score
    return all_score


def data_for_cluster(score_list):
    """
    聚类数据集
    :param score_list:评分列表
    :return:数据集
    """
    data = []
    user_ids = []  # 存储用户id
    all_category = []  # 存储所有类别
    user_category = {}  # 存储用户音乐基因
    for user, scores in score_list:
        user_ids.append(user)  # 存储当前用户
        category_dict = {}  # 存储类别及其各类别的歌曲个数及评分
        for music_id, score in scores.items():  # 遍历当前用户的兴趣列表
            music = Music.objects.get(pk=music_id)  # 获取当前歌曲
            categorys = music.category.all()  # 获取当前歌曲的所属类别
            if categorys.__len__() != 0:
                for c in categorys:
                    if c.music_category not in all_category:
                        all_category.append(c.music_category)
                    if c.music_category not in category_dict.keys():
                        category_dict[c.music_category] = {'count': 0, 'score': 0}
                    category_dict[c.music_category]['count'] += 1
                    category_dict[c.music_category]['score'] += score
            user_category[user] = category_dict
    for user_id in user_ids:
        category_vector = []
        category_dict = user_category[user_id]
        for category in all_category:
            if category not in category_dict.keys():
                category_vector.append(0)
            else:
                category_vector.append(category_dict[category]['score']/category_dict[category]['count'])
        data.append(list(map(float, category_vector)))
    return data


def data_for_rel(score_list):
    """
    关联分析数据集
    :param score_list:
    :return:
    """
    data = []
    for socres in score_list.values():
        data.append(list(socres.keys()))
    return data













