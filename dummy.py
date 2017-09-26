import json
from pprint import pprint

with open('dummy.json') as data_file:    
    data = json.load(data_file)

print(data['glossary']['title'])
