import os
#Задание №1
#Читая файл, каждую строчку делает элементом списка даже пустую, по пустой строчке можно и отсортировать 
lines = []
for x in open('./lesson8/recipes.txt'):     #for без метода read формирует список из поданного открытого файла по строчно 
   lines.append(x.strip())                  #strip() возвращает копию строки, в которой все символы были удалены с начала и конца строки (символом по умолчанию является пробел)


#Полученные строчки из список lines, раздеяет по пробелам и разпихивает по спискам в списке list_with_list
list_with_list = []
lines_dict = []
for x in lines:
   if x != '':
      lines_dict.append(x)
   else:
       list_with_list.append(lines_dict)
       lines_dict = []
list_with_list.append(lines_dict)       

#Составления словаря, где каждый нулевой элемент списка становится ключем а остальные элементы становятся значением 
cook_book = {}
for x in list_with_list:
   cook_book[x[0]] = x[2:len(x)]

#Убирает символ "|" из "Яйцо | 2 | шт" и запихивает Яйцо,2,шт как значение словаря {'ingredient_name': 'Яйцо ', 'quantity': ' 2 ', 'measure': ' шт'}
#Формируем словарь для задания №1
for big_key in cook_book.keys():
    with_split = []
    dict_after_split = {}
    for x in cook_book[big_key]:
        x2 = x.split('|')
        dict_after_split['ingredient_name'] = x2[0]
        dict_after_split['quantity'] = x2[1]
        dict_after_split['measure'] = x2[2]
        with_split.append(dict_after_split)
        dict_after_split = {}
    cook_book[big_key] = with_split    

print(f'Задание №1')
print(cook_book)
print()

#Задание №2 
#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

new_dict_for_menu = {}
def get_shop_list_by_dishes(dishes, person_count):
    for x in dishes:
        for x2 in range(len(cook_book[x])):
            new_dict_for_menu[cook_book[x][x2]['ingredient_name']] = \
{'measure': cook_book[x][x2]['measure'], 'quantity': (int(cook_book[x][x2]['quantity']) * int(person_count))}
    print(new_dict_for_menu)

print(f'Задание №2')
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print()

#Задание №3 
#В папке ./lesson8/ лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны
#Необходимо объединить их в один по следующим правилам:
#1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
#2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

print()
print(f'Задание №3')
#Получение списка заполненого полными путями к файлам (правда тут он относительный потому что задан из исходного каталога ./lesson8/)
directory_for_file = "./lesson8/"
tree = os.walk(directory_for_file)
path_files = []                          # Список с полными относительными путями 
for d, dirs, files in tree:
    for x in files:
        path = os.path.join(d,x)         #Формирование полного пути к файлу
        path_files.append(path)          #Добавление строки полного пути в список 
dir_file = d                             #Сохраняет путь к директории для создания файла 

#Подсчет строчек в файле и создание словаря ключ - путь к фалу, значение - количество строк
data_about_path_files = {}                 
for one_path_file in path_files:
    with open(one_path_file) as file:
        line_count = 0
        for line in file:
            line_count += 1
    data_about_path_files[line_count] = one_path_file

#Создаем файл, сортируем словарик по ключам, после записываем все в созданный файл начиная с файлов где меньше всего ключ(он же и количество строчек в файле)   
with open(f'{dir_file}/test.txt', 'w') as my_file:
    for x in sorted(data_about_path_files.keys()):  
        list_for_file = [f'Название файла: {data_about_path_files[x]} ',\
f'Число строк: {x}', f'Сам текст: \n {open(data_about_path_files[x]).read()}']
        for line in list_for_file:
            my_file.write(line + '\n')

print(f'Создан файл {dir_file}test.txt')
