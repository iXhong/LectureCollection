import csv
import json
import web_info


def csv_save(csvpath):
    """
    use the web_info() to scrapy the urls in college.json
    and save the data to a csv file
    :return: a csv file with data
    """
    with open('./data/college.json', 'r') as f:
        data = json.load(f)
        print('load ok')
        # 读取学院配置文件
    csvfile = open(csvpath, 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow(['college', 'name', 'link'])
    # write the header row for once time

    for k, v in data.items():
        url = v.get('url')
        strainer = v.get('strainer')
        num = v.get('num')
        # 读取学院配置文件中的参数
        infos = web_info.getinfo(url, strainer, num)
        # 调用web_info()抓取信息
        for info in infos:
            # info为列表嵌套字典
            info_name = info.get('info_text')
            info_link = info.get('info_link')
            info_college = k  # college name
            item = [info_college, info_name, info_link]
            c.writerow(item)

    csvfile.close()
