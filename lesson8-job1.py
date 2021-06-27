

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

print(cook_book)
