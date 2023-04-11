import json

items = json.loads('[{"id":1,"text":"zhangsan"},{"id":1,"text":"lisi"}]')

for item in items:
    print(item['id'])


