#1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
#2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
#3. объединить все дублирующиеся записи о человеке в одну.

import csv
import re

with open("./text_storage.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

#Созданание словаря feo_plus_index, в каждой строчке файла регуляркой искать ФИО и в конце сделать словавь по примеру  key=ИНДЕКС СТРОЧКИ  val=НАЙДЕННОЕ ФИО
def feo_plus_index(contacts_list1):

    errors = 0
    feo_plus_index = {}                                       #Словарь Ключи = 'Индекс строчки списка где искала регулярка', Значение = 'Найденное регуляркой ФИО'
    for x in contacts_list1:
        u = (','.join(str(z) for z in x))
        name = re.search(r'^([А-я\d]+(?:( |,)[А-я\d]{2,}( |,)[А-я\d]{2,}))|^([А-я\d]+(?:( |,)[А-я\d]{2,}))', u)
        try:                                                       #Убрал в исключения ошибки если регулярка ничего не находит в строчке 
            key_for_dict = re.split(',| ', name.group(0))          #Сохраняю в переменную то что нашла регулярка 
            val_for_dict = contacts_list1.index(x)                 #Сохраняю в переменную индекс строчки где искала регулярка 
            feo_plus_index[val_for_dict] = key_for_dict            #Леплю словарь
        except:
            errors = errors + 1
    return feo_plus_index
# print()
# print(feo_plus_index(contacts_list))
# print()

#Функция получения словаря где key = Фамилия value = Список со всеми номерами строчек где встречается фамилия   
def create_dict_surname(feo_plus_index):

    #Создание словаря с уникальным ФИО и значением объедененных строчек
    double_string = []
    double_string2 = {}
    for x, y in feo_plus_index.items():          #x - номер строк в сроваре contacts_list, y - список с ФИО 
        for x2, y2 in feo_plus_index.items():
            if 100 - (sum(i != j for i, j in zip(y, y2)) / float(len(y))) * 100 == 100.0:  #Cложный не мой алгоритм
                if x != x2:
                    double_string.append(y[0])                                                                                             # получаю словать где одинаковые ФИО но разные строчки в основном файле 
                    double_string2[x] = y

    out_list = {}
    for x in set(double_string): 
        out_list2 = []
        for x2, y2 in double_string2.items():
            if x == y2[0]:
                out_list2.append(x2)
                out_list[x] = out_list2
        out_list2 = []

    #Словарь ключ - фамилия, значение - списко номеров строчек
    surname_for_dict = {}
    for x in feo_plus_index:
        surname_for_dict[feo_plus_index[x][0]] = x


    for x in out_list:
        surname_for_dict[x] = out_list[x]

    return surname_for_dict
# print(create_dict_surname(feo_plus_index(contacts_list)))
# print()

#Функция, объединяет все существующие строчки в которых находит поданную фамилию и делат один большой список
def create_list_str(surname):

    wow_list = []
    for x in [create_dict_surname(feo_plus_index(contacts_list))[surname]]:
        if type(x) == int:
            for x2 in contacts_list[x]:
                wow_list.append(x2)
        else:
            for x2 in x:
                for x3 in contacts_list[x2]:
                    wow_list.append(x3) 

    return wow_list
# print(create_list_str('Мартиняхин'))
# print()

#Достать фио из списка функции create_list_str
def serarc_fio(surname):
    try:
        u = ' '.join(create_list_str(surname)) 
        name = re.search(r'^([А-я\d]+(?:( |,)[А-я\d]{2,}( |,)[А-я\d]{2,}))|^([А-я\d]+(?:( |,)[А-я\d]{2,}))', u)
        return name.group(0)
    except:
        return f'Фио не указано'

#Достать Емаил из списка функции create_list_str 
def serarc_email(surname):
    try:
        u = ' '.join(create_list_str(surname)) 
        name = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}', u)
        return name.group(0)
    except:
        return f'Емал не указан'   

#Достать место работы из списка функции create_list_str 
def serarc_organiza(surname):
    return create_list_str(surname)[3]

#Достать позицию из списка функции create_list_str 
def serarc_position(surname):
    try:
        if create_list_str(surname)[4] == '':
            return create_list_str(surname)[11]
        else:
            return create_list_str(surname)[4] 
    except:
        return f'Позиция не указана'

#Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999; из списка функции create_list_str
def serarc_phone(surname):
    try: 
        u = ','.join(create_list_str(surname))
        name = re.search(r'(\+7|8)[- _]*\(?[- _]*(\d{3}[- _]*\)?([- _]*\d){7}|\d\d[- _]*\d\d[- _]*\)?([- _]*\d){6}).*', u)
        phone = name.group(0).split(',')[0]
        name = re.findall(r'[0-9]', phone)
        if len(name) > 11:
            return f"+7({''.join(name[1:4])}){''.join(name[4:10])} доб.{''.join(name[11:])}"
        else:
            return f"+7({''.join(name[1:4])}){''.join(name[4:10])}"

    except:
        return f'Телефон не найден'

#Функция добавляет поданную строчку в csv файл
def add_str_into_csv(data):
    with open("./text_storage_new.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

#Функция финально заполняет список final_list
def info_aboute_fio(surname): 
    final_list = []
    for x in serarc_fio(surname).split():
        final_list.append(x)
    final_list.append(serarc_organiza(surname))
    if serarc_position(surname) == '':
        final_list.append('Позиция не указана')
    else:    
        final_list.append(serarc_position(surname))
    final_list.append(serarc_phone(surname))
    final_list.append(serarc_email(surname))
    add_str_into_csv(final_list)
    return final_list

#Дергает функцию которая ожидает на вход фамилию и записывает в новый ./text_storage_new.csv файл финальную запись о человеке 
print()
for x in create_dict_surname(feo_plus_index(contacts_list)).keys():
    info_aboute_fio(x)



