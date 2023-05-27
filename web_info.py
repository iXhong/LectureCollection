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
    data = {}
    info = []

    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser', parse_only=only_class)
    lis = soup.find_all("a")

    for li in lis:
        if 'info' in li['href']:
            # only choose the href with info
            info_text = li.get_text(strip=True)
            info_link = li['href'].replace("..", url[:-num])
            data['info_text'] = info_text
            data['info_link'] = info_link
            info.append(copy.copy(data))
            # add  data dictionary into info list
            # info.append(lambda data: data)

    return info

