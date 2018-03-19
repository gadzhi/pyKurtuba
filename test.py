from pyKurtuba import Kurtuba

test = Kurtuba('http://localhost:3099',domains=['google', 'yandex'], backup=True, password='12345')


def token():
    return test.new_token()['data']['token']

token()

