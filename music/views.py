from django.http import *
import json
import mutagen.mp3
import datetime

from iyinyue.utils import filedir, mp3reader, json4music
from iyinyue import constant
from user.models import *
from music.recommend import coldStart, UserCF, ItemCF
import os


def get_detail_by_music_id(request):
    if request.method == 'GET':
        music_id = request.GET.get('music_id', None)
        try:
            music = Music.objects.get(pk=music_id)
        except Music.DoesNotExist:
            HttpResponse('error')  # TODO
        else:
            cover = constant.PROJECT_PATH + '/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
            if os.path.exists(cover):
                cover = 'http://127.0.0.1:8000/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
            else:
                cover = 'http://127.0.0.1:8000/static/iyinyue/mp3/cover/default.jpg'
            music_json = {
                'id': music.id,
                'title': music.song_name,
                'artist': music.artist,
                'mp3': music.path,
                'poster': "images/m0.jpg",
                'cover': cover
            }
            return HttpResponse(json.dumps(music_json), content_type='application/json')


# 获取登录用户的歌曲列表
def get_play_list(request):
    user = IUser.objects.get(user_name=request.GET.get('user_name', None))
    play_lists = user.play_list.all()
    play_list_json = []
    for play_list in play_lists:
        list_json = {
            'id': play_list.id,
            'name': play_list.play_list_name,
            'count': play_list.play_time.count()
        }
        play_list_json.append(list_json)
    return HttpResponse(json.dumps(play_list_json), content_type='application/json')


# 获取数据库中所有歌曲
def get_all(request):
    play_list = Music.objects.all()
    play_list_json = []
    for music in play_list:
        music_json = {
            'id': music.id,
            'title': music.song_name,
            'artist': music.artist,
            'mp3': music.path,
            'poster': "images/m0.jpg"
        }
        play_list_json.append(music_json)
    return HttpResponse(json.dumps(play_list_json), content_type='application/json')


# 添加音樂到播放列表
def add_to_playlist(request):
    music_id = request.POST.get('music_id', None)
    play_list_id = request.POST.get('list_id', None)
    # play_list = PlayList.objects.get(pk=1)  # TODO 获取播放列表
    play_list = PlayList.objects.filter(pk=play_list_id, play_time__music__id=music_id)
    # user = IUser.objects.filter(play_list__id=1,
    #                             play_list__play_time__music__id=music_id)\
    #     .filter(user_name=user_name)  # 查找个用户是否已经添加了该歌曲
    if not play_list.exists():  # 用户不存在，则添加该歌曲到用户的播放列表
        # user = IUser.objects.get(user_name=user_name)  # 获取用户
        try:
            music = Music.objects.get(pk=music_id)  # 获取音乐
            play_list = PlayList.objects.get(pk=play_list_id)  # 获取播放列表
            play_time = PlayTime()
            play_time.music = music
            play_time.save()
            play_list.play_time.add(play_time)
            play_list.save()
            music.popular += 1  # 播放次数+1
            music.save()
            return HttpResponse('successful')
        except Music.DoesNotExist:
            HttpResponse('音乐不存在')
        except PlayList.DoesNotExist:
            HttpResponse('播放列表不存在')

    return HttpResponse('already added to you list')


# 用户下载操作
def download(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'download'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()

        def file_iterator(file_name, chunk_size=512):
            with open(file_name, encoding='utf-8') as file_stream:
                while True:
                    c = file_stream.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        file_name = constant.PROJECT_PATH + '/music/recommend/data/testSet.txt'
        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response


# 用户标记红心操作
def heart_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'heart'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        user.favorite_songs.add(music)
        operation.save()
        user.save()
        return HttpResponse('successful')


# 用户分享音乐操作
def share_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'heart'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()
        return HttpResponse('successful')


# 用户踩操作
def dislike_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))
    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'dislike'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()
        music.unpopular += 1  # 踩一下
        music.save()  # 保存
        return HttpResponse('successful')


# 用户对歌曲打标签操作
def tag_music(request):
    if request.method == 'POST':  # 方法为POST
        try:
            music = Music.objects.get(pk=request.POST.get('music_id', None))
            user = IUser.objects.get(user_name=request.POST.get('user_name', None))
            tag_content = request.POST.get('tag', None)  # 获取tag信息
        except(Music.DoesNotExist, IUser.DoesNotExist):
            return HttpResponse('failed')
        else:
            music_tag = MusicTag()
            music_tag.tag_content = tag_content
            music_tag.tag_music = music
            music_tag.tag_user = user
            music_tag.save()
            return HttpResponse('successful')


# 评论歌曲
def comment_music(request):
    if request.method == 'POST':  # 方法为POST
        try:
            music = Music.objects.get(pk=request.POST.get('music_id', None))
            user = IUser.objects.get(user_name=request.POST.get('user_name', None))
            comment_content = request.POST.get('tag', None)  # 获取评论内容
        except(Music.DoesNotExist, IUser.DoesNotExist):
            return HttpResponse('failed')
        else:
            music_comment = Comment()
            music_comment.comment_content = comment_content
            music_comment.comment_music = music
            music_comment.comment_user = user
            music_comment.save()
            return HttpResponse('successful')


# 批量添加音乐
def init_music(request):
    project_path = constant.PROJECT_PATH

    path = project_path + '/static/iyinyue/mp3'
    all_files = filedir.print_path(path)
    for file in all_files:
        flag = True
        if '.mp3' not in file:
            continue
        try:
            music_category = file.split('/')[-2]
            category = MusicCategory.objects.filter(music_category=music_category)
            if not category.exists():
                flag = False
                category = MusicCategory()
                category.music_category = music_category
                category.save()
            info = mp3reader.get_mp3_info(file)
        except mutagen.mp3.HeaderNotFoundError:
            continue
        music = Music()
        print(info)
        for k, v in info.items():
            for va in v:
                value = va + ' '
            if 'title' == k:
                music.song_name = str(value).strip()
            if 'artist' == k:
                music.artist = str(value).strip()
            if 'album' == k:
                music.album = str(value).strip()
            if 'genre' == k:
                music.genre = str(value).strip()
            if 'year' == k:
                music.year = str(value).strip()
            if 'comment' == k:
                music.comment = str(value).strip()
        music.path = file.replace(project_path, 'http://127.0.0.1:8000')
        music.save()
        if flag:
            music.category.add(category[0])
        else:
            music.category.add(category)
        music.save()


# 个性化音乐推荐
# method = GET get请求
# parm : user_name 待推用户名
def recommend(request):
    if request.method == 'GET':
        user_name = request.GET.get('user_name', None)  # 获取当前用户名
        user = IUser.objects.get(user_name=user_name)  # 获取当前用户所有信息
        #  获取当前时间与用户注册时间的时间差
        #  约定用户在注册后的十天内为新用户
        time_delta = timezone.now().date() - user.register_time
        recommend_musics = []  # 待推荐的歌曲
        # recommended_musics = []  # 推荐历史记录
        recommend_json = []  # 返回前台歌曲信息的json数组

        if user.play_recorded.count() < 10:  # 如果播放的歌曲少于10 调用冷启动
            recommend_musics = coldStart.cold_start(user)
        else:
            recommend_musics = []

        for recommend_music in recommend_musics:
            recommend_json.append(json4music.json4music(recommend_music))  # 转换为json串
        return HttpResponse(json.dumps(recommend_json), content_type='application/json')
    return HttpResponse('method error')


# 根据风格类型来获取音乐列表
# GET
def get_music_by_genre(request):
    if request.method == 'GET':
        try:
            musics = Music.objects.filter(genre=request.GET.get('genres', None))[25:45]
        except(Music.DoesNotExist, IUser.DoesNotExist):
            return HttpResponse('failed')
        play_list_json = []

        for music in musics:
            cover = constant.PROJECT_PATH + '/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
            if os.path.exists(cover):
                cover = 'http://127.0.0.1:8000/static/iyinyue/mp3/cover/'+music.artist+'_'+music.song_name+'.jpg'
            else:
                cover = 'http://127.0.0.1:8000/static/iyinyue/mp3/cover/default.jpg'
            music_json = {
                'id': music.id,
                'title': music.song_name,
                'artist': music.artist,
                'mp3': music.path,
                'cover': cover
            }
            play_list_json.append(music_json)
        return HttpResponse(json.dumps(play_list_json), content_type='application/json')
    return None


# 获取歌曲评论
# method GET
# parm: music_id
def get_comments(request):
    if request.method == 'GET':
        music_id = request.GET.get('music_id', None)
        comments_json = []
        try:
            comments = Comment.objects.filter(comment_music__pk=music_id)
        except Comment.DoesNotExist:
            HttpResponse('failed')
        else:
            for comment in comments:
                comment_json = {
                    'user_name': comment.comment_user.user_name,
                    'comment_time': datetime.datetime.strftime(comment.comment_time, '%Y-%m-%d %H:%M:%S'),
                    'comment_content': comment.comment_content
                }
                comments_json.append(comment_json)
            return HttpResponse(json.dumps(comments_json), content_type='application/json')


def add_comment(request):
    if request.method == 'POST':
        comment_user = request.POST.get('comment_user', None)
        comment_music_id = request.POST.get('comment_music_id', None)
        comment_content = request.POST.get('comment_content', None)
        try:
            curr_user = IUser.objects.get(user_name=comment_user)
            curr_music = Music.objects.get(pk=comment_music_id)
        except(IUser.DoesNotExist, Music.DoesNotExist):
            return HttpResponse('false')
        else:
            comment = Comment()
            comment.comment_user = curr_user
            comment.comment_music = curr_music
            comment.comment_content = comment_content
            comment.save()
            return HttpResponse('successful')

if __name__ == '__main__':
    init_music(request=None)