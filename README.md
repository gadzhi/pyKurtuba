# pyKurtuba
[![PyPI version](https://badge.fury.io/py/pyKurtuba.svg)](https://pypi.python.org/pypi/pyKurtuba)

Python api-client for [**Kurtuba**](https://github.com/hazratgs/kurtuba-storage)

Api клиент для облачного хранилища [**Kurtuba**](https://github.com/hazratgs/kurtuba-storage)

## Как начать?:
Установите библиотеку через 
```python
pip install pyKurtuba
```
Подключите библиотеку

```python
import pyKurtuba
```

Пример использования:
```python

from pyKurtuba import Kurtuba

test = Kurtuba('http://localhost:3199')

test.new_token()
```

## API

### Создание и получение токена:

Токен это ключ к доступу к конкретному хранилищу, а так же своего рода namespace.
Получить новый токен можно с помощью запроса:
    
```python
from pyKurtuba import Kurtuba

test = Kurtuba('http://localhost:3199')

test.new_token()
```

### Добавление данных в хранилище, а так же обновление:
После получения токена, мы можем записать, что-нибудь в наше хранилище, сделать это можно отправив POST запрос по адресу `/set`:

```python
test.set_data(token, data)
```
*token* - ваш токен (можете его предварительно сохранить где нибудь, либо использовать метод получения токена)

*data* - ваши данные в формате ключ-значение(например ```python data = {test:2}```

### Удаление элемента

```python
test.remove(token, key)
```

*token* - токен

*key* - имя элемента

### Удаление храналища

```python
test.delete(token)
```

*token* - токен

### Получение данных

Если вам нужно получить все данные, которые есть в хранилище:

```python
test.get_all(token, name)
```
*token* - токен

*name* - имя коллекции

Если вам нужно получить определенные данные:

```python
test.get(token, key)
```
*token* - токен

*key* - имя ключа


