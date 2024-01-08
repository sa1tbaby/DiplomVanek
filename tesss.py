import datetime
import time
masters_spec = tuple(['Брови','Ногти','Окрашивание','Шугаринг','Стрижка'])

import json

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

with open('ser.txt', 'r', encoding='UTF-8') as file:
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


with open('static/data/services.json', 'r') as file:
    asd = json.loads(file.read())

asd = asd.get('data')

for j, i in enumerate(asd):
    print(j, i.get('type'))

"""

with open('static/data/services.json', 'w') as file:
    tmp = {
        'data': listing
    }
    json.dump(tmp, file)


"""
