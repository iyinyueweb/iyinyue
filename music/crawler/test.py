__author__ = 'Administrator'
# encoding:utf-8
import urllib
import urllib.request

query_args = {}
query_args['word'] = 'Jecvay notes'

url_values = urllib.parse.urlencode(query_args)
url = 'http://www.baidu.com/s?'
full_url = url+url_values
data = urllib.request.urlopen(full_url).read()
data = data.decode('utf-8')
print(data)


def queue_use():
    from collections import deque
    queue = deque(['1', '2', '3'])
    queue.append('4')
    queue.append('5')
    queue.popleft()

