import requests

# Define your Contentful space ID and access token
SPACE_ID = 'gzhf2ey3l7ai'
ACCESS_TOKEN = 'CFPAT-M7tSmUDH817o03pFmYK8_o_1rA_xKPlHd4avnKc7Y5E'

# Define the content type ID for the entry you want to create
CONTENT_TYPE_ID = 'Committee'

# Define the URL for the Contentful API endpoint
API_URL = f'https://api.contentful.com/spaces/{SPACE_ID}/entries'

# Define the headers for the request
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/vnd.contentful.management.v1+json'
}

# Define the data for the new entry
data = {
    'fields': {
        'name': {
            'en-US': 'Theodore'  # Adjust 'en-US' if you're using a different locale
        }
        # Add more fields as needed
    },
    'content_type': CONTENT_TYPE_ID
}

# Send a POST request to create the entry
response = requests.post(API_URL, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    print('Entry created successfully.')
    entry_id = response.json()['sys']['id']
    print('Entry ID:', entry_id)
else:
    print('Failed to create entry. Status code:', response.status_code)
    print('Error:', response.json())