import csv
import web_info
import os
import json
import logging


csvpath = '../data/data.csv'

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='crawler.log', encoding='utf-8', level=logging.INFO)


def create(path):
    """
    create the data csv
    :param path: data csv path
    :return: data csv in path
    """
    with open(path, 'w', newline='') as f:
        c = csv.writer(f)
        c.writerow(['college', 'name', 'link'])
        logging.info('%s created successfully', path)


def save(path):
    """
    save the web info into data.csv
    :param path: saved path
    :return: csv with data
    """
    if not os.path.isfile(path):
        create(path)
    else:
        with open('../data/college.json', 'r') as f:
            data = json.load(f)
            logging.info("json load successfully")
            # 读取学院配置文件
        with open(path, 'a+') as f:
            c = csv.writer(f)

            for k, v in data.items():
                url = v.get('url')
                strainer = v.get('strainer')
                num = v.get('num')
                # 读取学院配置文件中的参数
                infos = web_info.getinfo(url, strainer, num)
                # 调用web_info()抓取信息
                if infos:
                    for info in infos:
                        # info为列表嵌套字典
                        info_name = info.get('info_text')
                        info_link = info.get('info_link')
                        info_college = k  # college name
                        info_date = info.get('info_date')
                        # info_id = info.get('info_id')
                        item = [info_college, info_name, info_link]
                        c.writerow(item)

                else:
                    logging.warning("Failed to get web info")


create(csvpath)
save(csvpath)
