import requests

TOKEN = ''

class YaUploader:
    def __init__(self, token):
        self.token = token

    def headers_list(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
            }

    def get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers_list()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()





    def upload_file(self, file_path,filename):
        response_href = self.get_upload_link(file_path=file_path).get('href', '')
        response = requests.put(response_href, data=open(filename, 'rb'))


if __name__ == '__main__':
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload_file(file_path='ЧЧЧЧЧЧЧЧЧЧЧЧЧЧ', filename='Uploaderdoc.txt')

#не очень понял смысл задания, так как это полная копия того, что было в коде на лекции,
# в результате все-равно не очень ясно, как работать с API Яндекса
# например requests.get(upload_url, headers=headers, params=params) - здесь это стандартная структура запроса GET
# то есть ссылка-заголовки-параметры