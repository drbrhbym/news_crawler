from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')
import time


def crab(class_):
    news_link = class_.find("a", class_="card_link")["href"]
    artical_number = news_link.split("/")[-1]
    id = "storm-politic-" + artical_number
    news_title = class_.find("h3", class_="card_title").text
    news_create_time = class_.find("span", class_="info_time").text

    response2 = urlopen(news_link)
    html2 = BeautifulSoup(response2)
    artical = html2.find("div", class_="article_content_inner")
    content = []
    for p in artical.find_all("p"):
        content.append(p.text)
    #print("".join(content))

    response3 = urlopen("https://service-pvapi.storm.mg/pvapi/get_pv/" + artical_number)
    html3 = BeautifulSoup(response3)
    news_view = html3.text.split(":")[-1].replace("}", "")
    print(news_view)



while True:
    url = "https://www.storm.mg/category/118/1"
    print("處理頁面:", url)

    response = urlopen(url)
    html = BeautifulSoup(response)

    for politic in html.find_all("div", class_="category_card"):
        crab(politic)
    break