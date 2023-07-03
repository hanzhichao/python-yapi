# python-yapi
Python Client for [YApi](https://github.com/YMFE/yapi) based on HTTP Api.


![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/python-yapi)
![PyPI](https://img.shields.io/pypi/v/python-yapi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/python-yapi)


## Install
```shell
pip install python-yapi
```

## Simple Use
> Document: <https://python-yapi.readthedocs.io/en/latest/index.html>


### Register and Login
```python
from python_yapi import YApi
yapi = YApi(base_url='http://localhost:3000')

username, email, password = 'Kevin', 'kevin@126.com', 'abc123'

yapi.register(username, email, password)  # return a dict
yapi.login( email, password) # return a dict
```


### Simple Use
#### Register and Login
```python
import json

from python_yapi import YApi

yapi = YApi(base_url='http://localhost:3000')
email, password = 'kevin@126.com', 'abc123'
yapi.login(email, password)
```

#### Create a project

```python
# Create a private project in user default group, with auto basepath, random color and random icon.
project = yapi.add_project('Demo Project')
project_id = project['_id']
```

#### Create a "GET" interface
```python
# Create a private "GET" interface in project default category with a sample json response.
yapi.add_interface(project_id=project_id,
                   title='Calc Add',
                   method='GET',
                   path='/add',
                   req_query=[
                       {"name": "a", "required": "1", "example": "1", "desc": "var a"},
                       {"name": "b", "required": "1", "example": "2", "desc": "var b"},
                   ],
                   res_body={"code": 0, "message": "success", "data": {"result": "3"}})  # dict as json
```
#### Create a "POST" interface
```python
# Create a private "POST" interface in project default category with a sample json data and a sample json response.
yapi.add_interface(project_id=project_id,
                   title='Calc Sub',
                   method='POST',
                   path='/sub',
                   req_headers=[{"name": "Content-Type", "value": "application/json"}],
                   req_body_other={"a": "5", "b": "1"},  # dict as json
                   res_body={"code": 0, "message": "success", "data": {"result": "4"}})  # dict as json
```
