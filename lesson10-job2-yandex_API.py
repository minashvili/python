# 2№ Задание
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!


import requests


class YaUploader:
    def __init__(self, file_path: str, token):
        self.file_on_pc = file_path
        self.token = token
        self.list_for_file_on_pc = []

    def Checking_the_Path(self): 
        if '/' in self.file_on_pc:
            self.list_for_file_on_pc = self.file_on_pc.split('/')
            
        elif '\\' in self.file_on_pc:
            self.list_for_file_on_pc = self.file_on_pc.split('\\')

    def upload(self):
        self.Checking_the_Path()
        my_headers = { 'Authorization': self.token, 'Accept': 'application/json' }
        params = {
            'path':f"Загрузки/{self.list_for_file_on_pc[-1]}",
            'overwrite':True
        }
        res = requests.get(f"https://cloud-api.yandex.net/v1/disk/resources/upload",params=params, headers=my_headers).json()
        upload = requests.put(url=res['href'], data=open(self.file_on_pc, 'rb'),params=params, headers=my_headers)
        return upload


testupload = YaUploader('ТВОЙ_ПОЛНЫЙ_ПУТЬ_К_ФАЙЛУ', 'ТВОЙ_ТОКЕН_ОТ_ЯНДЕКСА')

print(testupload.upload())


























#Варинат без ООП
# #Указать путь к файлу на Компе и токен для авторизации в яндексдиске
# file_on_pc = '/home/gia/Документы/Англиский/mine.png'
# token = 'OAuth AQAAAAANpscJAADLWySTyEw_bEsGlx0oHMo3va0'

# #Жалка проверка пути к файлу, Линуксовский или Виндовый? =D
# list_for_file_on_pc = []
# if '/' in file_on_pc:
#     list_for_file_on_pc = file_on_pc.split('/')
# elif '\\' in file_on_pc:
#     list_for_file_on_pc = file_on_pc.split('\\')

# #Хидеры http 
# my_headers = { 'Authorization': token, 'Accept': 'application/json' }

# #Параметры в URL для PUT запроса
# params = {
#     'path':f"Загрузки/{list_for_file_on_pc[-1]}",
#     'overwrite':True
# }
# #Остальная "логика" работы API Яндекс.Диска
# res = requests.get(f"https://cloud-api.yandex.net/v1/disk/resources/upload",params=params, headers=my_headers).json()
# upload = requests.put(url=res['href'], data=open(file_on_pc, 'rb'),params=params, headers=my_headers)

# print(upload)



# #Просмотр всех имен файлов на диске
# def show_names_file():
#     amount_files = len(requests.get("https://cloud-api.yandex.net/v1/disk/resources/files", headers=my_headers).json()['items'])
#     json_files = requests.get("https://cloud-api.yandex.net/v1/disk/resources/files", headers=my_headers).json()['items']
    
#     for x in range(amount_files):
#         print(json_files[x]['name'])

# show_names_file()
