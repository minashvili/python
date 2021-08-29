#Читать Марк Лутц т1 ст 683
import sys, datetime

from application.people import et_employees
from application.salary import calculate_salary

print()
print(sys.modules)  #Показать все загружаемые модули Python после import, для проверки загружены ли
print()
print(sys.path)     #Показать пути поиска переменной Pythonpath
datetime_object = datetime.date.today()

if __name__ == '__main__':

    print()
    print(f'Вывод текущей даты {datetime_object}')
    print()
    et_employees()
    calculate_salary()
    print()
    

























# import sys, datetime
# sys.path.append("./application/") #Указан относительный путь, где расположены модули, по этому нужно находиться в папке где есть папка application
# from people import et_employees
# from salary import calculate_salary
# print()
# print(sys.modules)  #Показать все загружаемые модули Python после import, для проверки загружены ли
# print()
# print(sys.path)     #Показать пути поиска переменной Pythonpath


# datetime_object = datetime.date.today()


# if __name__ == '__main__':

#     print()
#     print(f'Вывод текущей даты {datetime_object}')
#     print()
#     et_employees()
#     calculate_salary()
#     print()
    





