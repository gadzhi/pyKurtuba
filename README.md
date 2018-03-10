# pyKurtuba


Python api-client for [**Kurtuba**](https://github.com/gadzhi/pyKurtuba)

Api клиент для облачного хранилища [**Kurtuba**](https://github.com/gadzhi/pyKurtuba)

### Как начать?:
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
