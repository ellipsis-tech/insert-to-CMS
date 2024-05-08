import contentful_management
import json

client = contentful_management.Client('gzhf2ey3l7ai','CT3w5uPMUT-cIwFpqMKq_UtbuCRyXYTPwn23QTybk_k')

with open('test.json') as f:
    data = json.load(f)

# prints out the existing entries in contentful committee memebers
# for item in client.entries({'content_type': 'committee'}):
#     print(getattr(item,'name'))

# prints out the json file names of committee members
for item in data:
    print(item['name'])