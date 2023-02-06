#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint
import datetime
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth1 = {'user': 'ЛОГИН', 'pass': 'ПАРОЛЬ'}
api_url = 'https://31-31-202-41.cloudvps.regruhosting.ru/api/report_templates/173/generate'

json = {
    "report_format": "json",
    "input_values": {'packages': 'ngx'}
    #"input_values": {'hosts':'facts.processorcount >= 4 and not os_title ~ "OracleLinux%"', 'packages':'Название_пакета'}
    #"input_values": {'hosts':'facts.processorcount >= 4', 'packages':'Название_пакета'}
    #"input_values": {'hosts':'smart_proxy = "Любая_капсула"', 'packages':'Название_пакета'}
}

api_respone = requests.post(api_url, auth=(auth1['user'], auth1['pass']), json=json, verify=False)
pprint(api_respone.json())
