# -*- coding:utf-8 -*-  
"""---------------------- 
    author: Zhenjie Gu
    time:  2018/03/28/22/10:00 PM
    Description: 
    
    ----------------------"""
import requests
from bs4 import BeautifulSoup
import re

my_url = "https://movie.douban.com/top250?start=0&filter="
html = requests.get(my_url)

soup_page = BeautifulSoup(html.text, "html.parser")

movie_list = soup_page.find_all("div", attrs={"class": "bd"}, limit=3)
for movie in movie_list:
    print(movie)

src_list = soup_page.find_all("img", alt=True, attrs={"width": "100"})
for src in src_list:
    print(src["src"])
# quote_list = soup_page.find_all("span", attrs={"class": "inq"})
# for quote in quote_list:
#     print(quote.text)

# evaluations = re.compile(".+人评价")
# evaluation_list = soup_page.find_all(text=evaluations)
# for evaluation in evaluation_list:
#     print(evaluation)

# score_list = soup_page.find_all("span", attrs={"class": "rating_num", "property": "v:average"})
# for score in score_list:
#     print(score.text)

# director = re.compile(".+\s+导演:.+\W")
# movies_list = soup_page.find_all(text=director)
# for movie in movies_list:
#     print(movie)

# movie_date = re.compile(".+\s+([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{ 1 }|[0-9]{ 1 }[1-9][0-9]{2}|[1-9][0-9]{3}).+/+\W")
# movie_dates = soup_page.find_all(text=movie_date)
# for movie_date in movie_dates:
#     print(movie_date)

# 通过正则表达式获取href地址
# address = re.compile("https://movie.douban.com/subject/+[^\s]*")
# movies_href = soup_page.find_all("a", attrs={"href": address})
# for movie_href in movies_href:
#     print(movie_href["href"])

# 获取movie_href
# movies = soup_page.find_all("div", attrs={"class": "hd"})
# for movie_href in movies:
#     print(movie_href.a["href"])

# movies_title = soup_page.find_all("div", attrs={"class": "hd"})
# for movie_title in movies_title:
#     print(movie_title.span.text)
# movie_title
# movies_title = soup_page.find_all("div", attrs={"class": "hd"})
# for movie_title in movies_title:
#     print(movie_title.span.text)
# other_title
# other_titles = soup_page.find_all("span", attrs={"class": "other"})
# for other_title in other_titles:
#     print(other_title.text)
