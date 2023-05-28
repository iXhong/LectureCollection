# config=utf-8
import copy
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests


def getinfo(url, strainer, num):
    """
    use for getting the current info (included links) on the webpage
    For example,it will return a list of dic which contains the link and the name
    note: url should be ended with /index/tzgg.htm
    """
    only_class = SoupStrainer(class_=strainer)
    # parsing-only-part-of-a-document with the SoupStrainer of bs4
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36'}
    data = {}
    info = []
    info_id = 0

    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=only_class)
    lis = soup.find_all("a")

    for li in lis[:10]:
        if 'info' in li['href']:
            # only choose the href with info
            info_id += 1
            info_text = li.get_text(strip=True)
            info_link = li['href'].replace("..", url[:-num])
            data['info_id'] = info_id
            data['info_text'] = info_text
            data['info_link'] = info_link
            info.append(copy.copy(data))
            # add  data dictionary into info list
            # info.append(lambda data: data)

    return info
