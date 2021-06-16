from simple_term_menu import TerminalMenu


documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

# #Создание функции "listе"
# #    выведет список всех документов 
# #    в формате passport "2207 876234" "Василий Гупкин";

# def liste(liste_sub_menu):
#     print(f'Всего документов: {len(documents)} шт')
#     print('Список всех документов:')
#     for list_document in documents:
#         print(f'Документ №{documents.index(list_document) + 1} Тип: {list_document["type"]}, Номер: "{list_document["number"]}", Владелец: "{list_document["name"]}"')
    

# liste_sub_menu = 1
# liste(liste_sub_menu)



function = {'people_sub_menu': 'people_sub_menu',
                    'shelf_sub_menu': 'shelf_sub_menu',
                    '3': '3333'
                    }
        
print(function['3'])

