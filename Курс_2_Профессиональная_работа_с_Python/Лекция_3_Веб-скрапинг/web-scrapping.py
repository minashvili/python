import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}  #Оказывается нужно передавать user-agent для сайта Хабр ну или не только для него 

ret = requests.get('https://habr.com/ru/all/', headers=headers)
ret = ret.text
soup = BeautifulSoup(ret, features='html.parser')

#Получить всю статью с, почемуто, не полной вложенностью через web 
articles = soup.find(id='589727')         #(class_="tm-article-snippet__title-link")#('article', id='589727') 
#print(articles) 

#Получить название статьи
title_from_articles = articles.find(class_="tm-article-snippet__title-link")
print(title_from_articles.text)

#Получить ссылка на хабы 
hubs_from_articles = articles.find_all('div', class_='tm-article-snippet__hubs')
for x in hubs_from_articles:
    print(x.text)










# ret = requests.get('https://habr.com/ru/all/')
# ret = ret.text
# soup = BeautifulSoup(ret, features='html.parser')
#print(soup)

#Получить всю статью с, почемуто, не полной вложенностью
#articles = soup.find_all('div',class_='article-formatted-body article-formatted-body_version-2') 
#print(ret) 

# #Получить название статьи
# title_from_articles = articles.find(class_="tm-article-snippet__title-link")
# #print(title_from_articles.text)

# #Получить объект откуда брать ссылку на хабы 
# objeckt_hubs_from_articles = articles.find('div', class_="tm-article-snippet")
# #print(objeckt_hubs_from_articles.prettify())

# #Получить ссылка на хабы 
# hubs_from_articles = articles.find_all('div', class_='tm-article-snippet__hubs')
# #print(hubs_from_articles)




























# soup = BeautifulSoup(ret.text, features='html.parser')
# articles = soup.find() 
# 
# print(articles)











# article_title = articles[0].find_all(class_="tm-articles-subpage")
#print(articles)
# print(article_title[0].prettify())
# print()
# print(article_title[0].text)

# article_hub = articles[0].find_all('div', class_="tm-article-snippet__hubs")
# print(article_hub)
















                                         #.prettify() красивый вывод html в консоль 
#print()
# print(articles[0].find_all('div', class_="article-formatted-body"))































# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # определяем список ключевых слов
# KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL = "https://habr.com/ru/all/"

# driver = webdriver.Firefox()   #Нужно установить geckodriver
# driver.get(URL)

# elem = driver.find_element_by_name("article")
# # elem.send_keys("A")
# # elem.send_keys(Keys.RETURN)
# #assert "No results found." not in driver.page_source

# driver.close()






























#import requests
#from bs4 import BeautifulSoup
#
#ret = requests.get('https://2ip.ru/')
##print(ret.text)
#soup = BeautifulSoup(ret.text, 'html.parser')
#el = soup.find(id='d_clip_button')
#ip = el.text
#print(ip)
#




#import requests
# ret = requests.get('https://2ip.ru/')
# #print(ret.text)

# id_pos = ret.text.find('id="d_clip_button"')
# ip_start_pos = ret.text.find('<span>', id_pos) + 6
# ip_end_pos = ret.text.find('</', ip_start_pos)
# ip = ret.text[ip_start_pos:ip_end_pos]

# print(ip)



