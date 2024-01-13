from db_test_func import create_table, get_table_where
from database import declarativeModels

test_value = get_table_where(
    declarativeModels.Masters,
    declarativeModels.Masters.service_type == 'haircut'
)


for val in test_value:
    for i in val.content:
        if i.type == 'img':
            print(i.extra)