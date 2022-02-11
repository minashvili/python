import imaplib, email
from email.header import decode_header
import codecs
import re
from dateutil.parser import parse
from george_password import get_login_pass

#Функция чтения писем 
def email_reader_gave_dict():
        
    YA_HOST = "ПОЧТОВЫЙ СЕРВЕР"
    YA_PORT = 143
    YA_USER = list(get_login_pass()[1].keys())[0]               #Получение пользователя 
    YA_PASSWORD = list(get_login_pass()[1].values())[0]         #Получение пароля
    connection = imaplib.IMAP4(host=YA_HOST, port=YA_PORT)
    connection.login(user=YA_USER, password=YA_PASSWORD)    
    status, msgs = connection.select('INBOX')

    N = 1
    msgs = int(msgs[0])
    
    for x in range(msgs, msgs-N, -1):
        res, msg = connection.fetch(str(x), "(RFC822)")
        #print(msg)
        for x2 in msg:
            if isinstance(x2, tuple):
                msg = email.message_from_bytes(x2[1])
                #print(msg) 
                #Получить тему
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                #Получить отправителя на русском языке =В
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                #Получить дату
                datylka, encoding = decode_header(msg.get("Date"))[0]
                if isinstance(datylka, bytes):
                    datylka = datylka.decode(encoding)
                #Получить отправителя 
                messag_info, encoding = decode_header(msg.get("Received"))[0]
                if isinstance(messag_info, bytes):
                    messag_info = messag_info.decode(encoding)
                infa = re.search(r'(?<=envelope-from <).*.ru', messag_info).group()
                #Получить всех кто в копии
                email_from_copy = []
                
                try:
                    for x in decode_header(msg["CC"]):
                        if '@magnit.ru' in str(x[0]):
                            x2 = re.findall(r'(?<=<).*.ru', str(x[0]))[0]
                            email_from_copy.append(x2)
                except:
                    email_from_copy = 'Нет получателей в копии'

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True)
                            #print("Body:", codecs.decode(body, part.get_content_charset()))
                            boody = codecs.decode(body, part.get_content_charset())
                            #print("Body:", boody)
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True)
                    if content_type == "text/plain":
                        #print("Body:", codecs.decode(body, msg.get_content_charset()))
                        boody = codecs.decode(body, part.get_content_charset())
                        #print("Body:", boody)
    
    #Выхлоп после прочтения письма, делаю словарь для работы других функций
    dict_emails_body = {
            'sender':infa,
            'received_copy':email_from_copy,
            'date':parse(datylka).strftime('%Y-%m-%d %H:%M:%S'),
            'subject':subject,
            'body_of_letter': boody
            }
    return dict_emails_body
#print(email_reader_gave_dict())


#Получить уникальный списко IP адресов из тела сообщения 
def get_ip_adress(dict_from_email):
    body = dict_from_email['body_of_letter']
    cortege_ip = []
    ip_ad = re.findall(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', body)
    for x in ip_ad:
        ip_x = f'{x[0]}.{x[1]}.{x[2]}.{x[3]}'
        if ip_x not in cortege_ip:
            cortege_ip.append(ip_x)
    return cortege_ip        
#print(get_ip_adress(email_reader_gave_dict()))


#Получить уникальный список УЗ из тела сообщения по шаблону "УЗ: логин,логин,логин" 
def get_login_user(dict_from_email):
    cortege_login = []
    body = dict_from_email['body_of_letter']
    user_login = re.findall(r'(?<=УЗ:|уз:|Уз:).*', body)
    for x in user_login:
        for x2 in re.split(',| |\r', x): 
            y = x2.rstrip('@magnit.ru')
            if y not in cortege_login and y != '':
                cortege_login.append(y)    
    return cortege_login 
#print(get_login_user(email_reader_gave_dict()))    


#Проверка есть ли minashvili в копии, если да то дергать функцию проверки тела сообщения 
def manager_letter(dict_from_email):
    if 'minashvili@magnit.ru' in dict_from_email['received_copy'] or 'minashvili@magnit.ru' in dict_from_email['sender']:
        print('Вызов функции парсинга шаблонов команд')
#manager_letter(email_reader_gave_dict())



#Функция поиска шаблонов в теле письма и их выполнения
def check_body(dict_from_email):
    body = dict_from_email['body_of_letter']
    template_store = {
            'Дать доступ доменной уз':'[Д-д]ать доступ (доменной|доменой) [У-у][З-з]'
            }

    if re.findall(template_store['Дать доступ доменной уз'], body ):
        print(f"Нашел шаблон доступа в письме от {dict_from_email['sender']} с датой {dict_from_email['date']} ")
        print()
        print('Получаю логины')
        print(get_login_user(email_reader_gave_dict())) 
        print()
        print('Получаю IP адреса')
        print(get_ip_adress(email_reader_gave_dict()))
        print()
        print('Запускаю Ansible')


    else:
        print('Не нашел шаблон доступа')

check_body(email_reader_gave_dict())

