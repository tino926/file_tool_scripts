import requests
import configparser
from requests_oauthlib import OAuth2Session
import os

# Replace these with your actual client ID and secret
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

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


# Set the necessary scopes for accessing OneDrive
scopes = ['https://graph.microsoft.com/Files.ReadWrite.All']

# Create an OAuth2Session instance
auth_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
oauth = OAuth2Session(client_id, scope=scopes, redirect_uri='http://localhost')

# Fetch the authorization URL and prompt the user to grant permissions
authorization_url, state = oauth.authorization_url(auth_url)
print('Please go to this URL and grant permissions: {}'.format(authorization_url))

# Get the redirect response from the user
redirect_response = input('Enter the full redirect URL: ')

# Fetch the access token
token = oauth.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

# Set up the headers for the Microsoft Graph API requests
headers = {'Authorization': 'Bearer {}'.format(token['access_token'])}

# Make a request to list the folders in the user's OneDrive
url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
response = requests.get(url, headers=headers)

# Print the list of folders
if response.status_code == 200:
    folders = [item for item in response.json()['value'] if item['folder']]
    for folder in folders:
        print(folder['name'])
else:
    print('Error:', response.status_code, response.text)