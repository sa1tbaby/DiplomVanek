import datetime
import os.path
import json
import time
masters_spec = tuple(['Брови','Ногти','Окрашивание','Шугаринг','Стрижка'])
ddir = os.path.join(os.path.abspath(os.path.pardir), 'static/data')

file_name_2 = os.path.join(ddir, 'masters.json')
file_name_3 = os.path.join(ddir, 'masters_service.json')


name = 'content'

with open(os.path.join(ddir, f'{name}.json'), 'r', encoding='UTF-8') as file:
    tmp = json.load(file)

str_for_txt = ''
tmp = tmp.get('data')

for row_data in tmp:
    tmp_str = ''

    for key in row_data.keys():
        tmp_str += str(row_data.get(key)) + ','

    tmp_str = tmp_str[:-1] + '\n'
    print(tmp_str)
    str_for_txt += tmp_str

with open(os.path.join(ddir, f'{name}.txt'), 'w', encoding='UTF-8') as file:
    file.write(str_for_txt)


masters = {
    'data': [
        {
            "id": "111",
            "type": "Стрижки"
        },
        {
            "id": "222",
            "type": "Стрижки"
        },
        {
            "id": "333",
            "type": "Стрижки"
        },
        {
            "id": "111",
            "type": "Окрашивание"
        },
        {
            "id": "222",
            "type": "Окрашивание"
        },
        {
            "id": "444",
            "type": "Ногтевой сервис"
        },
        {
            "id": "555",
            "type": "Ногтевой сервис"
        },
        {
            "id": "666",
            "type": "Шугаринг"
        },
        {
            "id": "777",
            "type": "Ресницы и брови"
        },
        {
            "id": "888",
            "type": "Ресницы и брови"
        }
    ]
}
"""


with open(os.path.join(ddir, f'{name}.txt'), 'r', encoding='UTF-8') as file:
    tmp = file.read()

tmp = tmp.replace(',', ';')
tmp = tmp.replace('None', '')

with open(os.path.join(ddir, f'{name}.txt'), 'w', encoding='UTF-8') as file:
    file.write(tmp)

"""