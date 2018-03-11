pyKurtuba
=========

|PyPI version|

Python api-client for `**Kurtuba**`_

Api клиент для облачного хранилища `**Kurtuba**`_

Как начать?:
------------

Установите библиотеку через

.. code:: python

    pip install pyKurtuba

Подключите библиотеку

.. code:: python

    import pyKurtuba

Пример использования:

.. code:: python


    from pyKurtuba import Kurtuba

    test = Kurtuba('http://localhost:3199')

    test.new_token()

API
---

Создание и получение токена:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Токен это ключ к доступу к конкретному хранилищу, а так же своего рода
namespace. Получить новый токен можно с помощью запроса:

.. code:: python

    from pyKurtuba import Kurtuba

    test = Kurtuba('http://localhost:3199')

    test.new_token()

Добавление данных в хранилище, а так же обновление:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

После получения токена, мы можем записать, что-нибудь в наше хранилище,
сделать это можно отправив POST запрос по адресу ``/set``:

.. code:: python

    test.set_data(token, data)

*token* - ваш токен (можете его предварительно сохранить где нибудь,
либо использовать метод получения токена)

*data* - ваши данные в формате ключ-значение(например
``python data = {test:2}``

Удаление элемента
~~~~~~~~~~~~~~~~~

.. code:: python

    test.remove(token, key)

*token* - токен

*key* - имя элемента

Удаление храналища
~~~~~~~~~~~~~~~~~~

.. code:: python

    test.delete(token)

*token* - токен

Получение данных
~~~~~~~~~~~~~~~~

Если вам нужно получить все данные, которые есть в хранилище:

.. code:: python

    test.get_all(token, name)

*token* - токен

*name* - имя коллекции

Если вам нужно получить определенные данные:

.. code:: python

    test.get(token, key)

*token* - токен

*key* - имя ключа

.. _**Kurtuba**: https://github.com/gadzhi/pyKurtuba

.. |PyPI version| image:: https://badge.fury.io/py/pyKurtuba.svg
   :target: https://pypi.python.org/pypi/pyKurtuba