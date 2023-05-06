import requests
import yaml

def get_dynatrace_data():
    with open('config/api_credentials.yml') as f:
        credentials = yaml.safe_load(f)

    base_url = credentials['dynatrace']['base_url']
    api_key = credentials['dynatrace']['api_key']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Api-Token {api_key}'
    }

    # Customize this endpoint as needed
    url = f'{base_url}/api/v1/timeseries/com.dynatrace.builtin:app.useractionduration'

    response = requests.get(url, headers=headers)
    data = response.json()

    # Process and return the data
    return data
