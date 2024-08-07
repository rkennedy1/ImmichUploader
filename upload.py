import requests
import os
import sys
from datetime import datetime

def upload(api_key, base_url, file):
    stats = os.stat(file)

    headers = {
        'Accept': 'application/json',
        'x-api-key': api_key
    }

    data = {
        'deviceAssetId': f'{file}-{stats.st_mtime}',
        'deviceId': 'python',
        'fileCreatedAt': datetime.fromtimestamp(stats.st_mtime),
        'fileModifiedAt': datetime.fromtimestamp(stats.st_mtime),
        'isFavorite': 'false',
    }

    files = {
        'assetData': open(file, 'rb')
    }

    response = requests.post(
        f'{base_url}/assets', headers=headers, data=data, files=files)

    print(response.json())
    # {'id': 'ef96f635-61c7-4639-9e60-61a11c4bbfba', 'duplicate': False}

def upload_directory(api_key, base_url, directory):
    print(directory)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            upload(api_key, base_url, file_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python upload.py <API_KEY> <BASE_URL> <DIRECTORY>")
        sys.exit(1)

    api_key = sys.argv[1]
    base_url = sys.argv[2]
    directory = sys.argv[3]

    upload_directory(api_key, base_url, directory)