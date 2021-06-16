#Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них. Т. е. 
# поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

# print(f'Список из поисковых запросов равен {quantity} шт')
# for key in frequency_dictionary.keys():
    # print(f'Запросов из {key} слов {frequency_dictionary[key]} шт, \
# это {round(((int(frequency_dictionary[key]) / int(quantity)) * 100), 2)} \
# процентов от всех запросов')
# 



####Завершенная версия#####
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

frequency_dictionary = {}

for query in queries:
    word_count = len(query.split())
    if word_count not in frequency_dictionary.keys():
        frequency_dictionary[word_count] = 1
    else:
        frequency_dictionary[word_count] += 1

print(f'Список из поисковых запросов равен {len(queries)} шт')
for key, val in frequency_dictionary.items():
    print(f'Запросов из {key} слов {val} шт, \
это {round(((int(val) / int(len(queries))) * 100), 2)} \
процентов от всех запросов')








# #####ВЕРСИЯ МУЖЧИНЫ###########

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

quantity = len(queries)  
list_of_length = [] 
frequency_dictionary = {} 

#подсчет количества слов в значении списка и заполнение нового списка  
for query in queries:
    list_of_length.append(len(query.split()))

#Заполняется словарь. 
#Ключ - уникальное значение словаря list_of_length 
#Значение - использую метод count чтобы проверить сколько таких переменных в мое словаре
for length_word in set(list_of_length):
    frequency_dictionary[length_word] = list_of_length.count(length_word)

print(f'Список из поисковых запросов равен {quantity} шт')
for key in frequency_dictionary.keys():
    print(f'Запросов из {key} слов {frequency_dictionary[key]} шт, \
это {round(((int(frequency_dictionary[key]) / int(quantity)) * 100), 2)} \
процентов от всех запросов')

























