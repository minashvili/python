import json

#Прочитать файл json 
def read_json(file_path):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        print(news)

read_json('./lesson9/newsafr.json')


#Прочитать файл json и сделать выборку по description и использовать генератор списков с условием что слово больше 6 символов 
def read_json(file_path, max_len_word=6):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
        print(description_words)


read_json('./lesson9/newsafr.json')


















