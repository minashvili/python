# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# Задание 1 
# 1) p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# 2) s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#     Правильно обработайте ситуации, когда пользователь будет вводить не существующий документ.
# 3) l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# 4) a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. -
#     Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# 5) Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

# Задание 2 
# 1) d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;

# 2) m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;

# 3) as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. 
# Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.


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

################# НАЧАЛО БЛОКА Функций работы со списками ####################
def people():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            people()

    print()
    document_number = input('Пожалуйста укажите номер документа:')
    print()
    for document in documents:
        for val in document.values():
            if document_number == val:
                print(f'Владелец документа с номером "{document_number}" {document["name"]}')
                print()
                submenu()
    print()
    print(f'Документ под номером "{document_number}" не найден, проверьте правильность написания ')
    print()
    submenu()


def shelf():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            shelf()
            
    document_number_shelf = input('Пожалуйста укажите номер документа:')
    for key, val in directories.items():
        if document_number_shelf in val:
            print(f'Документ "{document_number_shelf}" на полке №{key}')
            submenu()
    print()
    print(f'Документ под номером "{document_number_shelf}" не найден, проверьте правильность написания ')
    submenu()


def liste():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            liste()

    print(f'Всего документов: {len(documents)} шт')
    print('Список всех документов:')
    for list_document in documents:
        print(f'Документ №{documents.index(list_document) + 1} Тип: {list_document["type"]}, Номер: "{list_document["number"]}", Владелец: "{list_document["name"]}"')
    print()
    print()
    submenu()


def add():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            add()
    
    def check_function():
        test = ''
        for key, val in user_responses.items():
            if val == test:
                print()
                print(f'Значение {key} не заполнено, повторите ввод')
                print()
                submenu()

        if new_number_shelf in directories.keys():
            #Добавление в directories
            directories[new_number_shelf].append(new_number_doc)
            #Добавление в documents
            new_dict = {"type": new_type, "number": new_number_doc, "name": new_owner_name}
            documents.append(new_dict)
            print()
            print(f'Документ {new_number_doc} добавлен на полку номер {new_number_shelf}')
            submenu()  

        elif new_number_shelf not in directories.keys():
            print()
            print(f'Полки c номером {new_number_shelf} нет')    
            print()
            submenu() 

    print()
    print('Добавление нового документа')
    new_number_doc = input('Введите Номер документа:')
    new_type = input('Введите Тип документа:')
    new_owner_name = input('Введите Имя владельца:')
    new_number_shelf = input('Введите Номер полки:')
    user_responses = {"type": new_type, "number": new_number_doc, "name": new_owner_name}
    check_function()


def delete():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            delete()

    def check_function():
        if document_number == '':
                print()
                print(f'Значение не заполнено, повторите ввод')
                print()
                #Вызов саб меню
                submenu()

    document_number = input('Чтобы удалить документ введите его Номер:')
    check_function()

    for document in documents:
        for val in document.values():
            if document_number == val:
                documents.remove(document)
                for key, val in directories.items():
                    if document_number in val:
                        directories[key].remove(document_number)
                print(f'Документ с номером "{document_number}" удален')
                #Вызов саб меню
                submenu()
    if document_number not in document.values():
        print(f'Документ с номером "{document_number}" не найден, повторите ввод')
        #Вызов саб меню
        submenu()


def move():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            move()
    
    print('Чтобы переместить документ на другую полку, введите Номер документа и Номер полки куда хотите переместить')
    document_number = input('Укажите Номер документа:')
    shelf_number = input('Укажите Номер полки:')

    for key, val in directories.items():
        if (document_number in val) and (shelf_number in directories.keys()):
            directories[key].remove(document_number)
            directories[shelf_number].append(document_number)
            #Вызов сабменю
            print()
            print(f'Документ {document_number} перенесен на полку {shelf_number}')
            print()
            submenu()

    print('Номер документа или полки указан не верно')
    #Вызов сабменю
    submenu()


def add_shelf():
    def submenu():
        options = ['[z] - Вернуться в стартовое меню', 
                   '[b] - Повторить ввод', 
                   ] 
        print()
        mainMenu = TerminalMenu(options, title="Пожалуйста выберите дальнейшие действия:")        
        optionsIndex = mainMenu.show() 
        optionsChoice = options[optionsIndex]   
        
        if "[z]" in optionsChoice:              
            print("Вызов меню")
            hardmenu()
        elif "[b]" in optionsChoice:
            print("Вызов функции еще раз")
            add_shelf()

    print()
    print(f'Сейчас доступны полки {list(directories.keys())}')
    print('Чтобы создать новую полку, укажите номер')
    
    
    new_number_shelf = input('Укажите Номер полки:')

    if (new_number_shelf.isnumeric()) and (new_number_shelf not in directories.keys()):
        directories[new_number_shelf] = list()
        print()
        print(f'Полка с номером {new_number_shelf} создана ')
        #Вызов сабменю
        submenu()

    print()
    print(f'Полка {new_number_shelf} существует или не корректно указан номер, полка не может быть создана ')
    #Вызов сабменю
    submenu()



################# КОНЕЦ БЛОКА Функций работы со списками ####################



################# НАЧАЛО БЛОКА Функций менюх #################
def hardmenu():
    options = ['[p] - Узнать имя владельца по номеру документа', 
               '[s] - Узнать номер полки на которой находится документ', 
               '[l] - Посмотреть все документы', 
               '[a] - Добавить новый документ', 
               '[d] - Удаление документа', 
               '[m] - Перенос документа', 
               '[x] - Создание новой полки(as)',  #Пришлось заменить as на с не знаю как обойти
               '[q] - Выход' 
               ]

    mainMenu = TerminalMenu(options, title="Перемещение стрелочками или горячие клавиши в таких [] скобках")        
    optionsIndex = mainMenu.show() 
    optionsChoice = options[optionsIndex]   

    if "[p]" in optionsChoice:                
        people()
    elif "[s]" in optionsChoice:
        shelf()
    elif "[l]" in optionsChoice:
        liste()
    elif "[a]" in optionsChoice:
        add()
    elif "[d]" in optionsChoice:
        delete()
    elif "[m]" in optionsChoice:
        move()
    elif "[x]" in optionsChoice:
        add_shelf()
    elif "[q]" in optionsChoice:
        print('Выход из программы')
        exit(0)
################# КОНЕЦ БЛОКА Функций менюх #################



hardmenu()






















#Создание функции "people" 
#    Запрос данных пользователя (номер документа )
#    Выводт (имя человека которому он пренодлежит)
#
#Создание функции "shelf"
#    Запрос данных пользователя (номер документа)
#    Если документ не сушествует - то сообшить об этом 
#    иначе - Вывод (номерполки на которой он находится)
#    
#Создание функции "listе"
#    выведет список всех документов 
#    в формате passport "2207 876234" "Василий Гупкин";
#
#Создание функции "add"
#    Запрос данных пользователя (номер документа, тип, имя владельца и номер полки, на котором он будет храниться)
#    Если полка не существует - то сообшить об этом
#    
#Создание функции "delete"
#    Запрос данных пользователя (номер документа)
#    Если документ не существует - то сообшить об этом
#    иначе - и удалит его из каталога и из перечня полок
#    
#Создание функции "move"
#    Запрос данных пользователя (номер документа и целевую полку)
#    Если Несуществует документ или полка куда хотят переместить то сообшить об этом 
#    инча - переместит документ с текущей полки на целевую
#
#Создание функции "add shelf"
#    Запрос данных пользователя (номер новой полки)
#    Если полка уже существует то сообшить об этом 
#    иначе - добавит новую полку в перечень










