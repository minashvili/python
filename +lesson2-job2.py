
height = int(input('Введите рост призывника: '))
age = int(input('Введите возраст призывника: '))
child = int(input('Введите количество детей призывника: '))
student = input('Является ли призывник студентом "да" или "нет": ').lower()

if child >= 2 or student == 'да':
    print('Освобожден от службы')
else:
    if 18 <= age < 27:
        if height < 170:
            print('В танкисты')
        elif height < 185:
            print('На флот')
        elif height < 200:
            print('В десантники')
        else:
            print('В другие войска')
    else:
        print('Непризывной возраст')
