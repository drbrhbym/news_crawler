from datetime import date, timedelta
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')


def crab(class_):
    title = class_.find("h2", class_= "nust clearmen")
    print("------------------------------------------------\n", title.text)
    for content in class_.find_all("a", target="_blank"):
        aurl = content["href"]
        sum = content["title"]
        print(aurl, sum)
        response2 = urlopen(aurl)
        html2 = BeautifulSoup(response2)
        article = html2.find("article", class_="ndArticle_leftColumn")
        view = article.find("div", class_="ndArticle_view").text
        date = article.find("div", class_= "ndArticle_creat").text
        whereP = article.find("div", class_= "ndArticle_margin")
        for pp in whereP.find_all("p"):
            print(pp.text.replace('\r','')) #發現段落有存在\r時, .text會印不出來

        print(view)
        print(date)
        print("------------------------------------------------\n")

start_day = date(2019, 1, 8)
n = 0
while True:
    url = "https://tw.appledaily.com/appledaily/archive/" + str(start_day + timedelta(n)).replace('-', '')
    print("處理頁面:", url)

    response = urlopen(url)
    html = BeautifulSoup(response)

    for headtop in html.find_all("article", class_="nclns eclnms5"):
        crab(headtop)

    '''
    for ent in html.find_all("article", class_= "nclns eclnms9"):
        crab(ent)

    for int in html.find_all("article", class_= "nclns eclnms7"):
        crab(int)

    for spt in html.find_all("article", class_= "nclns eclnms10"):
        crab(spt)

    for eco in html.find_all("article", class_= "nclns eclnms8"):
        crab(eco)

    for house in html.find_all("article", class_= "nclns eclnmsHouse"):
        crab(house)

    for sub in html.find_all("article", class_= "nclns eclnmsHouse"):
        crab(sub)
    '''

    n = n - 1
    if n < -1:
        break