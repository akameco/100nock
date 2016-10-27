# coding=utf-8
import json

for line in open('./jawiki-country.json'):
    data = json.loads(line)
    if data['title'] == 'イギリス':
        with open('./uk.txt', 'w') as of:
            of.write(data['text'])
