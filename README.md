# pyKurtuba
[![PyPI version](https://badge.fury.io/py/pyKurtuba.svg)](https://pypi.python.org/pypi/pyKurtuba)

Python api-client for [**Kurtuba**](https://github.com/hazratgs/kurtuba-storage)

Api клиент для облачного хранилища [**Kurtuba**](https://github.com/hazratgs/kurtuba-storage)

### Features
 - Create token
 - Refresh token
 - Get value of a property from the storage
 - Get all storage data
 - Set key/value
 - Remove element it storage
 - Delete storage
 - Get backup list
 - Restoring the vault from a backup

## Getting Started

#####Install
```python
pip install pyKurtuba
```

Example:
```python

from pyKurtuba import Kurtuba

test = Kurtuba('http://localhost:3199')

test.new_token()
```

## API

### Create token

All parameters (domains, backup, password) are optional:

    
```python
from pyKurtuba import Kurtuba

test = Kurtuba('http://localhost:3099',domains=['google', 'yandex'], backup=True, password='12345')

test.new_token()
```

 <details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "data":{
    "token": "002cac23-aa8b-4803-a94f-3888020fa0df",
    "refreshToken": "5bf365e0-1fc0-11e8-85d2-3f7a9c4f742e"
  }
}
```
#### Writing data to storage
To write data to the storage, you need to transfer the data object:

```python
test.set_data(token, {test:2})
```
<details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "message": "Successfully added"
}
```
</details>

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

#### Get all storage

Если вам нужно получить все данные, которые есть в хранилище:

```python
test.get_all(token, name)
```
<details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "data": {
    name: 'hazratgs',
    age: 25,
    city: 'Derbent'
    skills: ['javascript', 'react+redux', 'nodejs', 'mongodb']
  }
}
```
</details>

#### Get property

```python
test.get(token, key)
```
 <details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "data": "hazratgs"
}
```
</details>

#### Remove property

```python
test.get(token, key)
```

 <details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "message": "Successfully deleted"
}
```
</details>

#### Get backup list storage
If you passed a parameter `backup` when creating a token, then your repository will have backup copies, which are created every 2 hours and stored during the day.
In order to get a list of active copies of the repository, send the request:

```python
test.backup(token)
```
<details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "data": [
    'Sun Mar 04 2018 19:39:42 GMT+0300 (MSK)', 
    'Sun Mar 04 2018 20:39:42 GMT+0300 (MSK)'
  ]
}
```
</details>

#### Restoring the vault from a backup
To return the store to a specific checkpoint, pass the date of the checkpoint:

```python
test.restore(token, name_backup)
```

 <details>
  <summary>View Response</summary>

```js 		 
{
  "status":  true,
  "message": "Successfully restored"
}
```
</details>

