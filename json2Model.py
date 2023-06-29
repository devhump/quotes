import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()
from wisesaying.models import Wisesaying

file_path = "./sample.json"

with open(file_path, 'r', encoding="UTF-8") as file:
    data = json.load(file)
    # print(type(data))
    # print(len(data['quotes']))
    for dt in data['quotes']:
        content_ = (dt['content'])
        wisesaying = Wisesaying(content=content_)
        wisesaying.save()

