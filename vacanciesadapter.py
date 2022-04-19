import json
import time

import requests

f = open('1.json', encoding='utf8')
jsonText = f.read()
f.close()

# Преобразуем полученный текст в объект справочника
jsonObj = json.loads(jsonText)

# Получаем и проходимся по непосредственно списку вакансий
for v in jsonObj['items']:

    # Обращаемся к API и получаем детальную информацию по конкретной вакансии
    req = requests.get(v['url'])
    data = req.content.decode()
    req.close()

    # Создаем файл в формате json с идентификатором вакансии в качестве названия
    # Записываем в него ответ запроса и закрываем файл
    fileName = '{}.json'.format(v['id'])
    f = open(fileName, mode='w', encoding='utf8')
    f.write(data)
    f.close()

    time.sleep(0.25)

print('Вакансии собраны')