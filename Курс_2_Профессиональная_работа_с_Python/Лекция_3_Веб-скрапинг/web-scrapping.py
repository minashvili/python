from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0'}  #Оказывается нужно передавать user-agent для сайта Хабр ну или не только для него 
ret = requests.get('https://habr.com/ru/all/', headers=headers)
ret = ret.text
soup = BeautifulSoup(ret, features='html.parser')

#По заданию определяем список слов для поиска 
keyworlds = ['дизайн', 'фото', 'web', 'Python']

#Словарик статеек где есть подходящие слова 
arry_article = {}

#Получить все статьи по тегу article, статеек обычно 20 штук
text_for_get_id = soup.find_all('article')
for one_article in text_for_get_id:
    for one_word_from_list in keyworlds:
        if one_word_from_list in one_article.text:
            #Получить <Дату>
            date_from_articles = one_article.find('span', class_="tm-article-snippet__datetime-published").find('time').attrs['title']
            
            #Получить <заголовок> 
            title_from_articles = one_article.find(class_="tm-article-snippet__title-link").text
            
            #Получить <Ссылку> 
            href_from_article = one_article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2").find('a', class_="tm-article-snippet__title-link").attrs['href']
            href_from_article = f'https://habr.com{href_from_article}'
            
            #Составляем словарик по заданию "список подходящих статей в формате: <дата> - <заголовок> - <ссылка>"
            arry_article[date_from_articles] = [title_from_articles, href_from_article]
            
#Вывод и завершение задания             
print(arry_article)

