from contentful_management import Client
import json

client = Client('gzhf2ey3l7ai','CT3w5uPMUT-cIwFpqMKq_UtbuCRyXYTPwn23QTybk_k')

with open('test.json') as f:
    data = json.load(f)

#space = client.spaces().find('gzhf2ey3l7ai')
environment = client.environments('master')
content_type = client.content_types('committee','master')

for item in data:
    entry = content_type.create(item)
    entry.publish()