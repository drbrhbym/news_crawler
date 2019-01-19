from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import random

def refresh():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver.exe")
    driver.get("http://www.cybersyndrome.net/search.cgi?q=JP&a=ABCD&f=s&s=new&n=500")

    s = []
    i = 1
    while True:
        try:
            content = driver.find_element_by_id("n" + str(i)).text
            s.append(content)
        except NoSuchElementException:
            break

        i = i + 1

    random.shuffle(s)

    with open('proxy_IPs.txt', 'w', encoding="utf-8") as f:
        for item in s:
            f.write("%s\n" % item)


    driver.quit()


'''
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') # 允許在無GPU的環境下運行
options.add_argument('--window-size=1920x1080') # 建議設置
browser = Chrome("./chromedriver.exe", chrome_options=options)

browser.get("http://www.cybersyndrome.net/search.cgi?q=JP&a=ABCD&f=s&s=new&n=500")

content = browser.find_element_by_id("n1")
print(content.text)

driver.quit()'''