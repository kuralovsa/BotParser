# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import json

import requests

import time

import os
def parse(area:int):
    params = {
            'area': area, # Поиск ощуществляется по вакансиям города Москва
            'specialization':'1',
            'currency': 'KZT',
            'locale': 'KZ',
            'language':'kz',
            'host':'hh.kz',
            'page': 0, # Индекс страницы поиска на HH
            'per_page': 10 # Кол-во вакансий на 1 странице

        }

    req = requests.get('https://api.hh.ru/vacancies', params)
    jsonObj = json.loads(req.content.decode())

    nextFileName = 'Top10.json'

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsonObj, ensure_ascii=False))
    f.close()
    req.close()
    time.sleep(0.25)
if __name__ == "__main__":
    parse(159)
    print("IOS-dev successfully")


