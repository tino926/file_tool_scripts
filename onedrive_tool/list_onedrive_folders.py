import requests
import configparser
import os

# Check if the ./pri directory exists and contains settings.ini
settings_path = './pri/settings.ini'
if os.path.exists(settings_path):
    # Use configparser to read the settings
    config = configparser.ConfigParser()
    config.read(settings_path)
    client_id = config.get('DEFAULT', 'client_id')
    client_secret = config.get('DEFAULT', 'client_secret')
    tenant_id = config.get('DEFAULT', 'tenant_id')
else:
    # Fallback to hardcoded values or prompt the user
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    tenant_id = 'YOUR_TENANT_ID'

# The URL to get an access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# The scope for accessing OneDrive
scope = 'https://graph.microsoft.com/.default'

# The URL to list the first-level folders in OneDrive
drive_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'

# Function to get an access token
def get_access_token(client_id, client_secret, tenant_id, scope):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status() # Raises an exception if the request failed
    return response.json()['access_token']

# Function to list the first-level folders in OneDrive
def list_onedrive_folders(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(drive_url, headers=headers)
        response.raise_for_status() # Raises an exception if the request failed
        return response.json()['value']
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        print(f"Response body: {response.text}")


# Get an access token
access_token = get_access_token(client_id, client_secret, tenant_id, scope)

# List the first-level folders in OneDrive
folders = list_onedrive_folders(access_token)

# Print the folder names
for folder in folders:
    print(folder['name'])
    
