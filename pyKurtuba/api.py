import requests


class Kurtuba:

    def __init__(self, url):
        self.url = url

    def new_token(self):
        try:

            request = requests.post(self.url + '/create').json()
            
            return request['data']['token']
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")
    
    def set_data(self, token, data):

        try:

            request = requests.post(self.url + token + '/set', data).content

            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def remove(self, token, name):

        try:

            request = requests.delete(self.url + token + '/remove/' + name).content

            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")
            
    def delete(self, token):
        
        try:
            request = requests.delete(self.url + token + '/delete').content

            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def get_all(self, token):
        
        try:
            request = requests.delete(self.url + token + '/getAll').json()

            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def get(self, token, name):

        try:
            request = requests.get(self.url + token + '/get/' + name).json()

            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

