__author__ = 'Administrator'
import re
import urllib.request
import urllib
import http.cookiejar

from collections import deque

def start_news():
    queue = deque()
    visited = set()

    url = 'http://news.dbanote.net'

    queue.append(url)
    cnt = 0

    while queue:
        url = queue.popleft()
        visited |= {url}

        print('已抓取：'+str(cnt)+'正在抓取：'+url)
        cnt += 1

        urlop = urllib.request.urlopen(url, timeout=2)

        if 'html' not in urlop.getheader('Content-Type'):
            continue

        try:
            data = urlop.read().decode('utf-8')
        except:
            continue
        linkre = re.compile('href=\"(.+?)\"')
        for x in linkre.findall(data):
            if 'http' in x and x not in visited:
                queue.append(x)


def make_my_opener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def save_file(data, save_path):
    fp = open(save_path, 'wb')
    fp.write(data)
    fp.close()

if __name__ == '__main__':
    import time
    oper = make_my_opener()
    urlop = oper.open('http://www.baidu.com', timeout=1000)
    data = urlop.read()
    save_file(data, 'C:/Users/Administrator/Desktop/data/'+str(time.time())+'.txt')
    print(data.decode())



