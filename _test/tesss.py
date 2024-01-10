import datetime
import os.path
import json
import time
masters_spec = tuple(['Брови','Ногти','Окрашивание','Шугаринг','Стрижка'])
ddir = os.path.join(os.path.abspath(os.path.pardir), 'static/data')
file_name = os.path.join(ddir, 'services.json')
file_name_2 = os.path.join(ddir, 'masters.json')
file_name_3 = os.path.join(ddir, 'masters_service.json')

"""
smena = 3
graphic = str()
for i in range(2, 32):
    d, v = divmod(i,smena)
    if v != 0:
        graphic+='1'
    else:
        graphic+='0'

print(graphic)

ww = datetime.datetime(2024, 1, 10, 16, 30)
www = "2024-01-10 16:30:00"
print(type(datetime.datetime.fromisoformat(www)))
print(type(ww))

with open('../_doc/Ser.txt', 'r', encoding='UTF-8') as file:
    data = file.read().split('\n')
print(data)

name=''
type_=''
cost=''
listing = list()

name_f = name.find('.')
name_s = name.find('-')
for i in data:

    tmp_dict = {}

    if '.' not in i:
        type_ = i
        continue

    name = i
    cost = i

    name_f = name.find('.') + 2
    name_s = name.find('-') - 1

    cost_f = cost.find('-') + 2
    cost_s = cost.rfind('р')

    name = name[name_f:name_s]
    cost = cost[cost_f:cost_s]


    tmp_dict['type'] = type_
    tmp_dict['name'] = name
    tmp_dict['cost'] = cost
    tmp_dict['content_id'] = ''

    listing.append(tmp_dict)


with open('../static/data/services.json', 'r') as file:
    asd = json.loads(file.read())

asd = asd.get('data')

for j, i in enumerate(asd):
    print(j, i.get('type'))


"""

with open(file_name, 'r', encoding='UTF-8') as file:
    services = json.load(file)

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


