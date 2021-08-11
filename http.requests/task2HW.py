import requests
import os
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + token
            }
        params = {
            'path': os.path.basename(file_path),
            'overwrite': True
            }
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        r = requests.get(url=url, params=params, headers=headers)
        res = r.json()
        print(json.dumps(res, sort_keys=True, indent=4, ensure_ascii=False))
        # Отправляем локальный файл
        upload = requests.put(url=res['href'], data=open(file_path, 'rb'), params=params, headers=headers)
        print(upload.status_code)

if __name__ == '__main__':
    path_to_file = 'C:\\file.txt'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)