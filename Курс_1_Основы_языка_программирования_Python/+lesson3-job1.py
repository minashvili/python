

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
warning = (f'Внимание количество людей в списках не совпадает'
           'кто-то может остаться без пары!')

if len(boys) != len(girls):
    print(warning)

boys2 = sorted(boys)
girls2 = sorted(girls)
zip_boys2_girls2 = zip(boys2, girls2)

print(f'Идеальные пары:')
for x, x2 in zip_boys2_girls2:
    print(f'{x} и {x2}')
