# Задача №1
# Кто самый умный супергерой? Есть API по информации о супергероях. 
# Нужно определить кто самый умный(intelligence) из трех 
# супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

import requests

# Решение Задача №1
# Функция по циклу for отправляет http запросы в конечную точку /search/XXX, и получает http ответы  
# Заголовок Content-Type в http ответах имеет формат данных json (значит тело ответа сформировано форматом даных json словариками в словариках =В),
# Возможно применить метод .json() который вернет словарь
# Эти словарики(json) "как могу" парсятся и помещается значение в другой словарик dict_json_answer =D


def the_smartest(names_superhero):
    dict_json_answer = {}
    for x in names_superhero:
        dict_json_answer[x] = int(requests.get(f"https://www.superheroapi.com/api.php/2619421814940190/search/{x}").json()["results"][0]["powerstats"]["intelligence"])
    print(f'Самый умный супер герой: {max(dict_json_answer, key=dict_json_answer.get)}')


heroes = [ 'Hulk', 'Captain America', 'Thanos' ]
the_smartest(heroes)
















  