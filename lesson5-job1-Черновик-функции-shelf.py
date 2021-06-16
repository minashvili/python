from simple_term_menu import TerminalMenu

#Дано по задаче
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

#Перечень полок
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}
#Конец дано по задаче =D
# 2) s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#     Правильно обработайте ситуации, когда пользователь будет вводить не существующий документ.
shelf_sub_menu = 1 


#Функция "shelf"
def shelf(shelf_sub_menu):
    document_number_shelf = input('Пожалуйста укажите номер документа:')
    for key, val in directories.items():
        if document_number_shelf in val:
            print(key)
            print('Вызов submenu')
    
    print()
    print(f'Документ под номером "{document_number_shelf}" не найден, проверьте правильность написания ')
    print('Вызов submenu')
    #submenu(people_sub_menu)


shelf(shelf_sub_menu)
























