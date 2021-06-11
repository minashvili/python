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

def add():
    def check_function():
        test = ''
        for key, val in user_responses.items():
            if val == test:
                print()
                print(f'Значение {key} не заполнено, повторите ввод')
                print()
                add() #Вызов саб меню

        if new_number_shelf in directories.keys():
            #Добавление в directories
            directories[new_number_shelf].append(new_number_doc)
            #Добавление в documents
            new_dict = {"type": new_type, "number": new_number_doc, "name": new_owner_name}
            documents.append(new_dict)
            print()
            add() #Вызов саб меню 

        elif new_number_shelf not in directories.keys():
            print()
            print(f'Полки c номером {new_number_shelf} нет')    
            print()
            add() #Вызов саб мен

    print('Добавление нового документа')
    new_number_doc = input('Введите Номер документа:')
    new_type = input('Введите Тип документа:')
    new_owner_name = input('Введите Имя владельца:')
    new_number_shelf = input('Введите Номер полки:')
    user_responses = {"type": new_type, "number": new_number_doc, "name": new_owner_name}
    check_function()


add()



















#a – add – команда, которая добавит новый документ в каталог и в перечень полок, 
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, 
# когда пользователь будет пытаться добавить документ на несуществующую полку.

#Создание функции "add"
#    Запрос данных пользователя (номер документа, тип, имя владельца и номер полки, на котором он будет храниться)
#    Если полка не существует - то сообшить об этом
