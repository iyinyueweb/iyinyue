__author__ = 'jjzhu'
__doc__ = '音乐模块的工具类，主要是进行一些检查'
from user.models import RecommendHistory
from django.utils import timezone


# 检查用户的推荐记录
def check_recommended_history(user):
    recommended_musics = []
    try:
            # 查找推荐记录是否存在，主要用户新注册用户
        recommend_history = RecommendHistory.objects.get(recommend_user__user_name=user.user_name)
    except RecommendHistory.DoesNotExist:  # 若不存在，则新建一个推荐记录
        recommend_history = RecommendHistory(recommend_user=user, latest_recommend_time=timezone.now())
    for recommended_item in recommend_history.recommend_items.all():  # 获取推荐过的所有歌曲记录
        recommended_musics.append(recommended_item.music)  # 添加
    return recommend_history, recommended_musics