__author__ = 'jjzhu'
__doc__ = "冷启动：" \
          "解决新注册用户的初步推荐，根据用户的年龄段粗粒度的推荐歌曲"
from user.models import Music, RecommendItem
from music.utils.check import check_recommended_history


# 冷启动
# parm： user ： 待推用户（IUser）
def cold_start(user):
    recommend_musics = []  # 存储待推歌曲
    recommend_history, recommended_musics = check_recommended_history(user)  # 存储已推歌曲

    musics = Music.objects.filter(
        genre='Blues'  # TODO 要改成按age搜索的
        ).order_by('-popular')  # 热度由高到低排序.获取前两首
    count = 0
    for music in musics:  # 遍历歌曲
        if count == 2:  # 只取两首
            break
        if music not in recommended_musics:  # 如果该歌曲未推荐当前用户
            count += 1
            recommend_musics.append(music)  # 则将该歌曲加到待推荐列表中
    musics = Music.objects.all().order_by('-popular')  # 获取热度最高的歌曲
    count = 0
    for music in musics:
        if count == 3:
            break
        if music not in recommend_musics:  # 是否已经待推
            if music not in recommended_musics:  # 是否已推
                count += 1
                recommend_musics.append(music)
    for recommend_music in recommend_musics:
            recommend_item = RecommendItem(music=recommend_music)  # 新建一个推荐歌曲记录
            recommend_item.save()  # 保存，不保存好像会出错
            recommend_history.recommend_items.add(recommend_item)  # 添加到历史记录中去
    recommend_history.save()  # 保存
    return recommend_musics