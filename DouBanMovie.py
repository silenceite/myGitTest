# -*- coding:utf-8 -*-  
"""---------------------- 
    author: guzhenjie
    time: 2018/03/28/21/9:05 PM
    Description:
    
    ----------------------"""
import requests
from bs4 import BeautifulSoup
import threading
import time
from queue import Queue


_DATA = []
FILE_LOCK = threading.Lock()
SHARE_Q = Queue.queue()       # 构造一个不限制大小的队列
_WORKING_THREAD_NUM = 3


class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.func = func  # 传入线程函数逻辑

    def run(self):
        self.func()


def get_page(url):
    try:
        my_page = requests.get(url).text
    except Exception as e:
        if hasattr(e, "code"):
            print("The server couldn't fulfill the request.")
            print("Error code: %s" % e.code)
        elif hasattr(e, "reason"):
            print("We failed to reach a server. Please check your url and read the Reason")
            print("Reason: %s" % e.reason)
    return my_page


def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get()                                                # 获得任务
        movie_list = BeautifulSoup.find_all(get_page(url), "html.parser")  # 获得当前页面的电影名
        time.sleep(1)
        SHARE_Q.task_done()
    return movie_list


global SHARE_Q
threads = []
my_url = 'https://movie.douban.com/top250?start={page}&filter='
# 向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
for index in range(10):
    SHARE_Q.put(my_url.format(page=index * 25))
for i in range(_WORKING_THREAD_NUM):
    thread = MyThread(worker)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
SHARE_Q.join()
with open("movie.txt", "w+") as my_file:
    for page in _DATA:
        for movie_name in page:
            my_file.write(movie_name + "\n")
print("Spider Successful!!!")
