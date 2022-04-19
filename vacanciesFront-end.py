# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import json

import requests

import time

import os
params = {
        'text': 'Front-end', # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 40, # Поиск ощуществляется по вакансиям города Москва
        'currency': 'KZT',
        'locale': 'KZ',
        'language':'kz',
        'host':'hh.kz',
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 25 # Кол-во вакансий на 1 странице
    }

req = requests.get('https://api.hh.ru/vacancies', params)
jsonObj = json.loads(req.content.decode())

nextFileName = 'Front-end.json'

f = open(nextFileName, mode='w', encoding='utf8')
f.write(json.dumps(jsonObj, ensure_ascii=False))
f.close()
req.close()
time.sleep(0.25)
print("Front-end successfully")


