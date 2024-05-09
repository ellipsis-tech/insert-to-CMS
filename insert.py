import contentful_management
import json

client = contentful_management.Client('CFPAT-M7tSmUDH817o03pFmYK8_o_1rA_xKPlHd4avnKc7Y5E')

with open('test.json') as f:
    data = json.load(f)

entry_id = None
asset_id = None

for item in data:

    file = item['img']
    upload = client.uploads('gzhf2ey3l7ai').create('C:/Users/ernes/Documents/GitHub/insert-to-CMS/'+file)

    asset = client.assets('gzhf2ey3l7ai', 'master').create(asset_id, {
    'fields': {
        'title': {
            'en-US': item['name']
        },
        'file': {
            'en-US': {
                'fileName': file,
                'contentType': 'image/'+file.split(".")[1],
                'uploadFrom': upload.to_link().to_json()
                }
            }
        }
    })
    asset = asset.process()
    print(upload.to_link().to_json())
    
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
            'en-US': asset.to_link().to_json()
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

