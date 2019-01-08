import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')
from datetime import date, datetime, timedelta
import time
from datetime import date, timedelta
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import warnings
warnings.filterwarnings('ignore')

import threading, queue, time, urllib

start_day = date(2019, 1, 8)
baseUrl = "https://tw.appledaily.com/appledaily/archive/"
urlQueue = queue.Queue()

for n in range(10):
    url = baseUrl + str(start_day + timedelta(n)).replace('-', '')
    urlQueue.put(url)
    #print(url)

def fetchUrl(urlQueue):
    while True:
        try:
            url = urlQueue.get_nowait()
            #i = urlQueue.qsize()
        except Exception as e:
            break
        print('Current Thread Name %s, Url: %s ' % (threading.currentThread().name, url))
        try:
            response = urlopen(url)
            responseCode = response.getcode()
        except Exception as e:
            continue
        if responseCode == 200:
            time.sleep(0.5)


if __name__ == '__main__':
    startTime = time.time()
    threads = []
    threadNum = 4
    for i in range(threadNum):
        t = threading.Thread(target=fetchUrl, args=(urlQueue, ))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    endTime = time.time()
    print('Done, Time cost: %s ' % (endTime - startTime))