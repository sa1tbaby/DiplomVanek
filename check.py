from src.database.page_handles import AdminContent
from src.urls import settings

test = AdminContent(settings)
ss = test.get('services')

for i in ss:
    print(i.service_type)