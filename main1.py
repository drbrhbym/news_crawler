from datetime import date, timedelta
from urllib.request import urlopen
#from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')
import pymongo

#MongoDB client
myclient = pymongo.MongoClient("mongodb://192.168.31.195:27017/")
#create Database
mydb = myclient["newsdatabase"]


def crab(class_):
    title = class_.find("h2", class_= "nust clearmen")
    print("------------------------------------------------\n", title.text)

    for content in class_.find_all("a", target="_blank"): #取出網頁內容
        aurl = content["href"]                            #取出新聞內容網址
        sum = content["title"]                            #取出新聞標題
        print(aurl, sum)
        #再送一次request到新聞內容網址, 用美麗湯再解析出網頁內容
        response2 = urlopen(aurl)
        html2 = BeautifulSoup(response2)
        article = html2.find("article", class_="ndArticle_leftColumn") #取出新聞文章主要block，包含觀看人氣、發布日期及文章內容
        view = article.find("div", class_="ndArticle_view").text       #取出觀看人氣
        date = article.find("div", class_= "ndArticle_creat").text     #取出發布日期
        whereP = article.find("div", class_= "ndArticle_margin")       #取出文章段落
        s = []
        for pp in whereP.find_all("p"): #走過所有文章段落，再append起來
            s.append(pp.text.replace('\r',''))#發現段落有存在\r時, .text會印不出來
            #print(pp.text.replace('\r',''))

        print(s)
        print(view)
        print(date)
        print("------------------------------------------------\n")

        #建立新章文章內容(dict)
        mydict = {"class": title.text, "content": { "date": date.replace("出版時間:", " "),
                                                    "viewers":view, "article":s}}
        #插入文章內容至collection
        mycol.insert_one(mydict)

#設定時間日期開始爬, n 用來計算日期(timedelta)
start_day = date(2019, 1, 10)
n = 0

while True:
    url = "https://tw.appledaily.com/appledaily/archive/" + str(start_day + timedelta(n)).replace('-', '')
    mycol = mydb[str(start_day + timedelta(n)).replace('-', '')] #建立collection(在MongoDB等同於建立table)
    print("處理頁面:", url)

    response = urlopen(url)
    html = BeautifulSoup(response)

    #每個分類需各自執行一次crab function, 因為各欄位擷取之class不同
    for headtop in html.find_all("article", class_="nclns eclnms5"):
        crab(headtop)
    for ent in html.find_all("article", class_= "nclns eclnms9"):
        crab(ent)
    for inter in html.find_all("article", class_= "nclns eclnms7"):
        crab(inter)
    for spt in html.find_all("article", class_= "nclns eclnms10"):
        crab(spt)
    for eco in html.find_all("article", class_= "nclns eclnms8"):
        crab(eco)
    for house in html.find_all("article", class_= "nclns eclnmsHouse"):
        crab(house)
    for sub in html.find_all("article", class_= "nclns eclnmsHouse"):
        crab(sub)


    #計算timedelta, 負的表示日期往前推, n < -365 表示抓一整年的新聞
    n = n - 1
    if n < -1:
        break