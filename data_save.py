import json
import os
import web_info
import sqlite3

"""
create()用于创建数据库以及info数据表
write()用于将每个院的数据依次添加序号并写入数据库

"""


def create(dbpath):
    """
    create a sqlite database
    only run it when you want to create a database,
    or you might get your current database losed!!
    """
    os.remove(dbpath)
    conn = sqlite3.connect(dbpath)
    print("connect ok")
    c = conn.cursor()
    c.execute("create table info(id integer primary key autoincrement not null, name text not null, link text not null "
              ")")
    # 创建表info,包含id name link
    conn.commit()
    conn.close()
    print("creat ok")


def write(dbpath):
    """
    use web_info to crawl the data and save it
    to the sqlite database
    :return: a db file named dbpath
    """
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    # 连接数据库并设置游标

    with open('./data/college.json', 'r') as f:
        data = json.load(f)
        print('load ok')
        # 读取学院配置文件

    info_id = 0
    for v in data.values():
        url = v.get('url')
        strainer = v.get('strainer')
        num = v.get('num')
        # 读取学院配置文件中的参数
        infos = web_info.getinfo(url, strainer, num)
        # 调用web_info()抓取信息
        for info in infos:
            # info为列表嵌套字典
            info_text = info.get('info_text')
            info_link = info.get('info_link')
            info_id += 1
            # 获取递增id , text and link
            data_to_w = (info_id, info_text, info_link)
            c.execute("insert or ignore into info values (?,?,?)", data_to_w)
            # 写入数据库
            conn.commit()
    c.close()
    conn.close()
    # 关闭数据库
