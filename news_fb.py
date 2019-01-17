import requests

#udn 範例
url = "https://udn.com/news/story/12783/3596922"
facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()  #['share']['comment_count']
print(facebook_id)

'''
風傳媒 範例
url = "https://www.storm.mg/lifestyle/814618"
facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()  #['share']['comment_count']
print(facebook_id) '''


'''
TVBS 範例
url = "https://news.tvbs.com.tw/local/1067019"
facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()  #['share']['comment_count']
print(facebook_id) '''


'''
Ettoday 範例
url = "https://news.tvbs.com.tw/local/1067019"
facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()  #['share']['comment_count']
print(facebook_id) '''

'''
目前蘋果只能取得share數
url = "https://tw.news.appledaily.com/headline/daily/20190117/38234494/"
facebook_id = requests.get('https://graph.facebook.com/?id={}'.format(url)).json()  #['share']['comment_count']
print(facebook_id) '''