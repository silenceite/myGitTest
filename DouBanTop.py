# -*- coding:utf-8 -*-  
""" 
    @author:rainbow 
    @time: 2018/03/25/19
    @Description: 豆瓣电影top250
    
    """
import requests
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
dest_filename = 'movie.xlsx'
ws1 = wb.active
ws1.title = 'movietop250'

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    """获取url地址内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_ = 'grid_view')
    name = []   # 名字
    star_con = []  # 评价人数
    score = []   # 评分
    info_list = []    # 短评
    for i in ol.find_all('li'):
        detail = i.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).get_text()    # 电影名字
        level_star = i.find('span', attrs={'class': 'rating_num'}).get_text()    # 评分
        star = i.find('div', attrs={'class': 'star'})
        star_num = star.find(text=re.compile('评价'))    # 评价

        info = i.find('span', attrs={'class': 'inq'})    # 短评
        if info:    # 判断是否有短评
            info_list.append(info.get_test())
        else:
            info_list.append('无')
        score.append(level_star)
    page = soup.find('span', attrs={'class': 'next'}).find('a')    # 下一页
    if page:
        return name, star_con, score, info_list, DOWNLOAD_URL + page['herf']
    return name, star_con, score, info_list, None


def main():
    url = DOWNLOAD_URL
    name = []
    star_con = []
    score = []
    info = []
    while url:
        doc = download_page(url)
        movie, star, level_num, info_list, url = get_li(doc)
        name = name + movie
        star_con = star_con + star
        score = score + level_num
        info = info + info_list
    for(i, m, o, p) in zip(name, star_con, score, info):
        col_a = 'A%s' % (name.index(i) + 1)
        col_b = 'B%s' % (name.index(i) + 1)
        col_c = 'C%s' % (name.index(i) + 1)
        col_d = 'D%s' % (name.index(i) + 1)
    ws1[col_a] = i
    ws1[col_b] = m
    ws1[col_c] = o
    ws1[col_d] = p
    wb.save(filename=dest_filename)


if __name__ == '__main__':
    main()