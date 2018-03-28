import requests


class Kurtuba:

    def __init__(self, url, domains=None, back=False, password=None):
        self.url = url
        self.domains = domains
        self.back = back
        self.password = password

    def new_token(self):
        try:
            request = requests.post(self.url + '/create', {"domains": self.domains, "backup": self.back,
                                                           'password': self.password}).json()
            return request
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
            request = requests.delete(self.url + token).json()
            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def get(self, token, name):
        try:
            request = requests.get(self.url + token + '/' + name).json()
            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def backup(self, token):
        try:
            request = requests.get(self.url + token + '/backup/').json()
            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")

    def restore(self, token, backup):
        try:
            request = requests.get(self.url + token + '/backup/' + backup).json()
            return request
        except requests.exceptions.ConnectTimeout:
            print("Не удалось подключиться к серверу")
