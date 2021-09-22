import requests
from pprint import pprint


class YaDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token),
        }

    def get_f_list(self):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(file_url, headers=headers)
        result_respons = response.status_code
        return result_respons



    def upload_file_to_disk(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': disk_file_path}
        response = requests.put(upload_url, headers=headers, params=params)
        res1 = response.json()
        res = response.status_code
        return res


if __name__ == '__main__':

  ya = YaDisk(token='AQAAAAAWLmwGAADLW2CdA2rud0lyl25MavDNGOk')
  pprint(ya.get_f_list())
  pprint(ya.upload_file_to_disk(disk_file_path='1111'))
