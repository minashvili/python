person = int(input('Укажите колличество гостей: '))

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

#Метод мужчины 
for x in range(len(cook_book)):
    if cook_book[x][0] == 'салат':
        print(f'Салат:')
        for x2 in range(len(cook_book[x][1])):
            print(f'{cook_book[x][1][x2][0]},\
 {cook_book[x][1][x2][1] * person}{cook_book[x][1][x2][2]}')

    elif cook_book[x][0] == 'пицца':
        print()
        print(f'Пицца:')
        for x3 in range(len(cook_book[x][1])):
            print(f'{cook_book[x][1][x3][0]},\
 {cook_book[x][1][x3][1] * person}{cook_book[x][1][x3][2]}')

    elif cook_book[x][0] == 'фруктовый десерт':
        print()
        print(f'Фруктовый десерт:')
        for x4 in range(len(cook_book[x][1])):
            print(f'{cook_book[x][1][x4][0]},\
 {cook_book[x][1][x4][1] * person}{cook_book[x][1][x4][2]}')


#Метод Кошули <3
for x in range(len(cook_book)):
    print(f'{cook_book[x][0].capitalize()}:')
    for x2 in range(len(cook_book[x][1])):
        print(f'{cook_book[x][1][x2][0]},\
 {cook_book[x][1][x2][1] * person}{cook_book[x][1][x2][2]}')
    print()
    