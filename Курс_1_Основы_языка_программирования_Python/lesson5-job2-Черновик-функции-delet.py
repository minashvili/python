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

#Создание функции "delete"
#    Запрос данных пользователя (номер документа)
#    Если документ не существует - то сообшить об этом
#    иначе - и удалит его из каталога и из перечня поло

def delete():
    def check_function():
        if document_number == '':
                print()
                print(f'Значение не заполнено, повторите ввод')
                print()
                #Вызов саб меню
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
    if document_number not in document.values():
        print(f'Документ с номером "{document_number}" не найден, повторите ввод')
        #Вызов саб меню


delete()
print(directories)
print(documents)


# document_number = input('Чтобы удалить документ введите его Номер:')
# 
# for key, val in directories.items():
    # if document_number in val:
        # print(key)
        # directories[key].remove(document_number)
        # print(directories)

    

