# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
#Из строчек в файле ./lesson8/recipes.txt надо собрать словарь как сверху 




#Читая файл, каждую строчку делает элементом списка даже пустую, по пустой строчке можно и отсортировать 
lines = []
for x in open('./lesson8/recipes.txt'):     #for без метода read формирует список из поданного открытого файла по строчно 
   lines.append(x.strip())                 #strip() возвращает копию строки, в которой все символы были удалены с начала и конца строки (символом по умолчанию является пробел)

print(lines)  




























# for x in lines:
#     print(x)


# result = {lines[n-1]: lines[n+1: n+1+int(lines[n])]
#           for n in range(len(lines)) if lines[n].isnumeric()}


#print(lines)



# lines = [line.strip() for line in open('./lesson8/recipes.txt')] #формирует список и почемуто разделяет его по пробелам =D
# print(lines)












# file = open("./lesson8/recipes.txt")
# print(file.read())
# file.close()


# with open("./lesson8/recipes.txt") as file2:
#     print(file2.read()) #Читает файл целиком, при большом файле могут быть проблемы
     

# # with open("./lesson8/recipes.txt") as file2:
# #     print(file2.readline().strip())
# #     print(file2.readline().strip())
# #     print(file2.readline().strip())



# lines = 0
# with open('./lesson8/recipes.txt') as f:
#     for line in f:
#         if line:
#             lines = lines + 1           

# print(lines)