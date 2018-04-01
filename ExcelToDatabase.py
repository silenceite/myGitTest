# -*- coding:utf-8 -*-  
""" 
    @author:rainbow 
    @time: 2018/03/25/21/9:28 PM
    @Description: Excel文件读取入数据库
    
    """
from openpyxl import load_workbook
import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'charset': 'utf8'
}
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
name = 'test_excel'
cursor.execute('create database if not exists %s' % name)
conn.select_db(name)
table_name = 'info'
cursor.execute('create table if not exists %s (id MEDIUMINT NOT NULL AUTO_INCREMENT, name varchar(30), tel varchar(30),'
               'primary key (id)' % table_name)

wb2 = load_workbook('hup.xlsx')
ws = wb2.get_sheet_names()
for row in wb2:
    print("1")
    for cell in row:
        values1 = (cell[0].value, cell[4].value)
        cursor.execute('insert into info(name, tel) values (%s, %s)', values1)

print("over.")
