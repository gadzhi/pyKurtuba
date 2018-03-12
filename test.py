from pyKurtuba import Kurtuba
import requests
test = Kurtuba('http://localhost:3099', True, '12345', ['google', 'yandex'])

print(test.new_token())

