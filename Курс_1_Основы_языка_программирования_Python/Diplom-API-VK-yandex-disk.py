import requests, time, datetime
import logging
 
#Для простоты понимаю = "Логирование это просто принт" я ничего умней не узнал =D
logging.basicConfig(filename="sample.log",      # Настройка логирования, путь к файлу, установка уровня формиования сообщений лога и тд 
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG)
log = logging.getLogger("log_api_yandex")       # Присвоить тег для лога 

class APIvk:
    def __init__(self, id_user_vk, vk_api_token):
        self.id_user_vk = id_user_vk
        self.vk_api_token = vk_api_token  
        self.vk_api_url = "https://api.vk.com/method/"

    def get_all_fotos_from_vk(self):    
        self.params = {
        'access_token': self.vk_api_token,       
        'v':'5.130', 
        'user_id': self.id_user_vk,
        'extended':'1',
        'album_id': ['wall', 'profile']
        }

        vk_fotos_list = []
        for x in requests.get(f'{self.vk_api_url}/photos.get', params=self.params).json()["response"]["items"]:
            vk_fotos_list.append([x["sizes"][-1]["url"], x["likes"]["count"]]) 
        return vk_fotos_list      
bots_nuke = APIvk('НУЖНО_УКАЗАТЬ_ID_ПОЛЬЗОВАТЕЛЯ_VK','НУЖНО_УКАЗАТЬ_ТОКЕН_ОТ_VK')
#print(bots_nuke.get_all_fotos_from_vk()) # Покажет список [[URL_всех_фото, число_лайков]]

class APIyandex:
    def __init__(self, vk_fotos_list, yandex_api_token):
        self.yandex_api_token = yandex_api_token
        self.vk_fotos_list = vk_fotos_list 
        self.yandex_api_url = "https://cloud-api.yandex.net/v1/disk/" 
        self.my_headers = { 'Authorization': self.yandex_api_token, 'Accept': 'application/json' }
        self.params = {
            "url": "xxxx",
            "path": "Загрузки/xxxx",
            "overwrite": True,
        }

    def vk_raketa_upload_with_for(self):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.params['path'] = f"Загрузки/{timestr}"
        requests.put(f"{self.yandex_api_url}resources", params=self.params, headers=self.my_headers).json()
        
        #Формирует словарик, просто для сортировки и чтобы загружать фотки по возрастанию лайков
        sort_the_list_by_likes = {}
        for x in self.vk_fotos_list():
            sort_the_list_by_likes[x[1]] = x[0]

        #Загрузка картинок в папку Загрузки/дата_в_момент_загрузки
        for x in sorted(sort_the_list_by_likes,reverse=True): 
            self.params['url'] = sort_the_list_by_likes[x]
            self.params['path'] = f"Загрузки/{timestr}/{x}.jpg"
            log.info(requests.post(f"{self.yandex_api_url}resources/upload", params=self.params, headers=self.my_headers).json())
            time.sleep(1)
        
        #Вывод информации по загруженным картинкам 
        total_files = len(sort_the_list_by_likes.keys())
        self.params['limit'] = [total_files]
        for x in requests.get(f"{self.yandex_api_url}resources/last-uploaded", params=self.params, headers=self.my_headers).json()["items"]:
            log.info([{ "file_name":x["name"], "size":x["size"] }])

test_yandex = APIyandex(bots_nuke.get_all_fotos_from_vk,'НУЖНО_УКАЗАТЬ_ТОКЕН_ОТ_YANDEX_DISK')
print(test_yandex.vk_raketa_upload_with_for()) # Ожидает список url фоточек от класса VK, отсортирует его по лайкам и попытается закинуть его в яндек диск 



