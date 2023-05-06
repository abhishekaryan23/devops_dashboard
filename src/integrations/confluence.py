import requests
import yaml

def get_confluence_data():
    with open('config/api_credentials.yml') as f:
        credentials = yaml.safe_load(f)

    base_url = credentials['confluence']['base_url']
    user_email = credentials['confluence']['user_email']
    api_key = credentials['confluence']['api_key']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {user_email}:{api_key}'
    }

    # Customize this endpoint as needed
    url = f'{base_url}/wiki/rest/api/content/search?cql=type=page'

    response = requests.get(url, headers=headers)
    data = response.json()

    # Process and return the data
    return data
