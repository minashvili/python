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

#Создание функции "add shelf"
#    Запрос данных пользователя (номер новой полки)
#    Если полка уже существует то сообшить об этом 
#    иначе - добавит новую полку в перечень

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

    print('Чтобы создать новую полку, введите Номер полки')
    new_number_shelf = input('Укажите Номер полки:')
    
    if new_number_shelf in directories.keys():
        print()
        print(f'Полка {new_number_shelf} существует и не может быть создана')
        #Вызов сабменю
        submenu()
    
    directories[new_number_shelf] = list()
    print()
    print(f'Полка с номером {new_number_shelf} создана ')
    #Вызов сабменю
    submenu()
















