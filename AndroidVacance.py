# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import json

import requests

import time

import os
def parse(area:int):
        params = {
                'text': 'Android development', # Текст фильтра. В имени должно быть слово "Аналитик"
                'area': area, # Поиск ощуществляется по вакансиям города Москва
                'name': 'Android development',
                'currency': 'KZT',
                'locale': 'KZ',
                'language': 'kz',
                'host': 'hh.kz',
                'page': 0, # Индекс страницы поиска на HH
                'per_page': 30 # Кол-во вакансий на 1 странице

            }

        req = requests.get('https://api.hh.ru/vacancies', params)
        jsonObj = json.loads(req.content.decode())

        nextFileName = 'Android.json'

        f = open(nextFileName, mode='w', encoding='utf8')
        f.write(json.dumps(jsonObj, ensure_ascii=False))
        f.close()
        req.close()
        time.sleep(0.25)
print("Android-dev successfully")


