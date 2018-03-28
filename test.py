from pyKurtuba import Kurtuba

test = Kurtuba('https://storage.hazratgs.com/', domains=['google', 'yandex'], back=True, password='12345')


def token():
    return test.new_token()['data']['token']


print(token())
