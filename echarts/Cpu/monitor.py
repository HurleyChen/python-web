#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
version: python2.7      software: PyCharm
file: monitor.py        time: 2017/3/5 19:56
"""

import psutil
import sqlite3
import time


db_name = 'mydb.db'


def create_db():
    # 连接
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # 创建表
    c.execute('''DROP TABLE IF EXISTS cpu''')  # 删除旧表，如果存在（因为这是临时数据）
    c.execute(
        '''CREATE TABLE cpu (id INTEGER PRIMARY KEY AUTOINCREMENT, insert_time text,cpu1 float, cpu2 float, cpu3 float, cpu4 float)''')

    # 关闭
    conn.close()


def save_to_db(data):
    '''参数data格式：['00:01',3.5, 5.9, 0.7, 29.6]'''
    # 建立连接
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # 插入数据
    c.execute('INSERT INTO cpu(insert_time,cpu1,cpu2,cpu3,cpu4) VALUES (?,?,?,?,?)', data)

    # 提交！！！
    conn.commit()

    # 关闭连接
    conn.close()


# 创建表
create_db()

# 通过循环，对系统进行监控
while True:
    # 获取系统cpu使用率（每隔1秒）
    cpus = psutil.cpu_percent(interval=1, percpu=True)

    # 获取系统时间（只取分:秒）
    t = time.strftime('%M:%S', time.localtime())

    # 保存到数据库
    save_to_db((t, cpus[0], cpus[1], cpus[2], cpus[3]))
    print('save a data')