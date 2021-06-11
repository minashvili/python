from simple_term_menu import TerminalMenu
#Дано по задаче
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
#Конец дано по задаче =D



#Функции "people"
def people(people_sub_menu):
    document_number = input('Пожалуйста укажите номер документа:')
    for document in documents:
        for val in document.values():
            if document_number == val:
                print(f'Владелец документа с номером "{document_number}" {document["name"]}')
                submenu(people_sub_menu)
    print()
    print(f'Документ под номером "{document_number}" не найден, проверьте правильность написания ')
    submenu(people_sub_menu)

#Функция submenu(Подменю) используется в основных функциях
def submenu(name_of_function):
    options = ['[a] - Вернуться в стартовое меню', 
               '[b] - Повторно "Узнать имя владельца по номеру документа"', 
               ] 
    print()
    mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
    optionsIndex = mainMenu.show() 
    optionsChoice = options[optionsIndex]   

    function = {'people_sub_menu': people('people_sub_menu')}
    #Блок условий который в зависимости от ответа пользователя, выполнит функцию
    if "[a]" in optionsChoice:                
        print("Вызов меню")
        hardmenu()

    elif "[b]" in optionsChoice:
        function[name_of_function]

#Словарь функций для подменю
#function = {'people_sub_menu': people('people_sub_menu')}
#function['people_sub_menu']


people('people_sub_menu')







# ##Создание функции "people" 
# #    Запрос данных пользователя (номер документа)
# #    Вывод (имя человека которому он пренодлежит)
# def people():
#     document_number = input('Пожалуйста укажите номер документа:')
#     for list_len in range(len(documents)):
#         for key, val in documents[list_len].items():
#             if document_number == val:
#                 print(f'Владелец документа "{document_number}" {documents[list_len]["name"]}')
#                 return
#     print(f'Документ под номером "{document_number}" не найден, проверьте правильность написания ')
#     people()

# people()






# def people():
    # document_number = input('Пожалуйста укажите номер документа:')
    # for document in documents:
        # for val in document.values():
            # if document_number == val:
                # print(f'Владелец документа с номером "{document_number}" {document["name"]}')
                # return
    # print(f'Документ под номером "{document_number}" не найден, проверьте правильность написания ')
    # people()

#people()