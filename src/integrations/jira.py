import requests
import yaml

def get_jira_data():
    with open('config/api_credentials.yml') as f:
        credentials = yaml.safe_load(f)

    base_url = credentials['jira']['base_url']
    user_email = credentials['jira']['user_email']
    api_key = credentials['jira']['api_key']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {user_email}:{api_key}'
    }

    # Customize this endpoint as needed
    url = f'{base_url}/rest/api/2/search?jql=project=YOUR_PROJECT_KEY'

    response = requests.get(url, headers=headers)
    data = response.json()

    # Process and return the data
    return data
