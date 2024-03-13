import requests
import configparser
import os
import onedrivesdk

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

# # The URL to get an access token
# token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# # The scope for accessing OneDrive
# scope = 'https://graph.microsoft.com/.default'

# # The URL to list the first-level folders in OneDrive
# drive_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'

# # Function to get an access token
# def get_access_token(client_id, client_secret, tenant_id, scope):
#     data = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'scope': scope
#     }
#     response = requests.post(token_url, data=data)
#     response.raise_for_status() # Raises an exception if the request failed
#     return response.json()['access_token']

# # Function to list the first-level folders in OneDrive
# def list_onedrive_folders(access_token):
#     headers = {'Authorization': f'Bearer {access_token}'}
#     response = requests.get(drive_url, headers=headers)
#     response.raise_for_status() # Raises an exception if the request failed
#     return response.json()['value']

# # Get an access token
# access_token = get_access_token(client_id, client_secret, tenant_id, scope)

# # List the first-level folders in OneDrive
# folders = list_onedrive_folders(access_token)

# # Print the folder names
# for folder in folders:
#     print(folder['name'])
    

redirect_uri = 'http://localhost:8080/'  # 設定您的重導向 URI


# 設定 OneDrive API 的基本 URL
api_base_url = 'https://api.onedrive.com/v1.0/'

# 設定所需的權限範圍
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

# 建立 HttpProvider 和 AuthProvider
http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(http_provider=http_provider,
                                          client_id=client_id,
                                          scopes=scopes)

# 建立 OneDriveClient
client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)

# 取得身份驗證 URL
auth_url = client.auth_provider.get_auth_url(redirect_uri)

# 請使用瀏覽器打開此 URL，授權應用程式的存取權限
print('請在瀏覽器中打開以下網址，並授予應用程式存取權限：')
print(auth_url)

# 複製網址列中 "code=" 後的代碼，並在下方貼上
code = input('請輸入網址列中的代碼：')

# 使用代碼進行身份驗證
client.auth_provider.authenticate(code, redirect_uri, client_secret)

# 列出根目錄的內容
items = client.item(drive='me', id='root').children.get()
for item in items:
    print(item.name)
