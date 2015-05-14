__author__ = 'Administrator'
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3
from mutagen import File


# 获取MP3标签方法
# 用mutagen插件
def get_mp3_info(path):
    id3info = MP3(path, ID3=EasyID3)  # 获取MP3标签信息
    afile = File(path)
    tags = afile.tags
    if 'APIC:' in tags:
        artwork = afile.tags['APIC:'].data  # 获取MP3里的图片信息
        #  专辑封面的存储路径
        path = '../../static/iyinyue/mp3/cover/'+id3info['artist'][0].replace('/', '.')+'_'+id3info['title'][0]+'.jpg'
        print(path)
        with open('F:/project/iyinyue/static/iyinyue/mp3/cover/'
                          + id3info['artist'][0].replace('/', '.') + '_'+id3info['title'][0].replace('/', '.')
                          +'.jpg', 'wb') as img:  # 写入图片数据
            img.write(artwork)
    return id3info


# 测试方法
if __name__ == '__main__':

    info = (get_mp3_info(str(u'F:\project\iyinyue\static\iyinyue\mp3\摇滚\AC_DC - Anything Goes.mp3').replace('\\', '/')))
    for k, v in info.items():
        print(k, v)


