import contentful_management
import json
import requests

client = contentful_management.Client('CFPAT-M7tSmUDH817o03pFmYK8_o_1rA_xKPlHd4avnKc7Y5E')

with open('test.json') as f:
    data = json.load(f)

entry_id = None

for item in data:
    # image_path = item['img']  # Update with the actual path to your image file
    # with open(image_path, 'rb') as image_file:
    # # Upload image to Contentful
    #     upload_response = client.uploads(
    #         image_file
    #     )
    # upload_data = upload_response
    file_or_path = item['img']  # This can also be a file-like object e.g.: `open('my_file', 'rb')`.
    upload = client.uploads('gzhf2ey3l7ai').create(file_or_path)

    entry = client.entries('gzhf2ey3l7ai', 'master').create(entry_id, {
    'content_type_id': 'committee',
    'fields': {
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
        'image': {
            'en-US': {
                    contentType: 'image/jpeg',
                    fileName: 'test.jpg',
                    upload: 'http://www.example.com/test.jpg'
            }
        },
        'linkedIn': {
            'en-US': item['linkedin']
        },
        'batch': {
            'en-US': int(item['batch'])
        },
        'order': {
            'en-US': item['order']
        }        
    }
    })
    try:

        entry.publish()

        print("Entry created successfully:", entry.id)

    except contentful_management.errors.NotFoundError as e:
        print("Content Type or Space not found:", e)

    except contentful_management.errors.APIRequestFailedError as e:
        print("API Request Failed:", e)


# client = contentful_management.Client('gzhf2ey3l7ai','CT3w5uPMUT-cIwFpqMKq_UtbuCRyXYTPwn23QTybk_k')

# with open('test.json') as f:
#     data = json.load(f)

# #prints out the existing entries in contentful committee memebers
# for item in client.entries('gzhf2ey3l7ai', 'master', {'content_type': 'committee'}):
#     print(getattr(item,'name'))

# # prints out the json file names of committee members
# for item in data:
#     print(item['name'])
