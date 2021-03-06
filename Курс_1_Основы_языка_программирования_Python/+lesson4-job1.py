# Задание 1. Дан список с визитами по городам и странам. Напишите код,
# который возвращает отфильтрованный список geo_logs, содержащий только
# визиты из России.

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# Кривой Вариант
for x in range(len(geo_logs)):
    for x2, x3 in geo_logs[x].items():
        if "Россия" in x3:
            print(x3)

print()

# Храмой Вариант
for x in range(len(geo_logs)):
    for x2, x3 in geo_logs[x].items():
        if "Россия" in x3:
            print(geo_logs[x])
