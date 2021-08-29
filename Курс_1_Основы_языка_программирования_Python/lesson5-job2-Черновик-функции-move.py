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

# 2) m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
# Корректно обработайте кейсы, когда пользователь пытается переместить 
# несуществующий документ или переместить документ на несуществующую полку;






print('Чтобы переместить документ на другую полку, введите Номер документа и Номер полки куда хотите переместить')
document_number = input('Укажите Номер документа:')
shelf_number = input('Укажите Номер полки:')

for key, val in directories.items():
    if (document_number in val) and (shelf_number in directories.keys()):
        directories[key].remove(document_number)
        directories[shelf_number].append(document_number)
        #Вызов сабменю

print('Номер документа или полки указан не верно')
#Вызов сабменю
print(directories.items())        








