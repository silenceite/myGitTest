# -*- coding:utf-8 -*-  
"""---------------------- 
    @author:rainbow 
    @time: 2018/03/27/19/7:58 PM
    @Description: Uses BeautifulSoup to provide live cricket score.
    
    ----------------------"""
import bs4 as bs
from urllib import request


url = "http://www.cricbuzz.com/cricket-match/live-scores"
sauce = request.urlopen(url).read()
# print(sauce)
soup = bs.BeautifulSoup(sauce, "lxml")
# print(soup)
score = []
results = []

for div_tags in soup.find_all('div', attrs={"class": "cb-lv-scrs-col text-black"}):
    score.append(div_tags.text)
for result in soup.find_all('div', attrs={"class": "cb-lv-scrs-col cb-text-complete"}):
    results.append(result.text)

print(score[1], results[1])
print(len(score))
