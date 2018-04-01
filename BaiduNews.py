# -*- coding:utf-8 -*-  
"""---------------------- 
    @author:rainbow 
    @time: 2018/03/27/21/9:00 PM
    @Description: Uses BeautifulSoup to provide Latest News Headline along with news link.
    
    ----------------------"""
from bs4 import BeautifulSoup
import requests
import pymysql
import datetime


conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    db="baidunews",
    charset='utf8'
)
cursor = conn.cursor()

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

my_url = "https://news.baidu.com/"
html = requests.get(my_url)

soup_page = BeautifulSoup(html.text, "lxml")
news_list = soup_page.find_all("a", href=True, attrs={"target": "_blank"}, mon=True)
for news in news_list:
    sql = "insert into hotnews (href, name, create_time) VALUES ('%s', '%s', '%s')" % (news['href'], news.text, now)
    try:
        cursor.execute(sql)
    except Exception as e:
        conn.rollback()
        print(e)
    else:
        conn.commit()

# delete data name is ''
sql = "delete from hotnews where name = ''"
try:
    cursor.execute(sql)
except Exception as e:
    conn.rollback()
    print(e)
else:
    conn.commit()

# print("成功插入", cursor.rowcount, "条数据！")
cursor.close()
conn.close()




