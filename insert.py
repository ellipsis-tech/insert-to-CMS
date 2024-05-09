import contentful_management
import json

client = contentful_management.Client('gzhf2ey3l7ai', 'CT3w5uPMUT-cIwFpqMKq_UtbuCRyXYTPwn23QTybk_k')

space = client.spaces().find('gzhf2ey3l7ai')

content_type_id = 'your_content_type_id'

with open('test.json') as f:
    data = json.load(f)

for item in data:
    fields = {
        'name': {
            'en-US': item['name']
        },
        'position': {
            'en-US': item['Position']
        },
        'department': {
            'en-US': item['department']
        },
        'description': {
            'en-US': item['description']
        },
        'img': {
            'en-US': item['img']
        },
        'linkedin': {
            'en-US': item['linkedin']
        },
        'batch': {
            'en-US': item['batch']
        },
        'order': {
            'en-US': item['order']
        }        
    }

    try:
        entry = space.create_entry(content_type_id, fields)

        entry.publish()

        print("Entry created successfully:", entry.id)

    except contentful_management.errors.NotFoundError as e:
        print("Content Type or Space not found:", e)

    except contentful_management.errors.APIRequestFailedError as e:
        print("API Request Failed:", e)


# client = contentful_management.Client('gzhf2ey3l7ai','CT3w5uPMUT-cIwFpqMKq_UtbuCRyXYTPwn23QTybk_k')

# with open('test.json') as f:
#     data = json.load(f)

# # prints out the existing entries in contentful committee memebers
# # for item in client.entries({'content_type': 'committee'}):
# #     print(getattr(item,'name'))

# # prints out the json file names of committee members
# for item in data:
#     print(item['name'])
