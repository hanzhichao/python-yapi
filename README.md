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

### Register and Login
```python
from python_yapi import YApi
yapi = YApi(base_url='http://localhost:3000')

username, email, password = 'Kevin', 'kevin@126.com', 'abc123'

yapi.register(username, email, password)  # return a dict
yapi.login( email, password) # return a dict
```


### Simple Use

```python
import json

from python_yapi import YApi

yapi = YApi(base_url='http://localhost:3000')
email, password = 'kevin@126.com', 'abc123'
yapi.login(email, password)

# Create a private project in user default group, with auto basepath, random color and random icon.
project = yapi.add_project('Demo Project')
project_id = project['_id']

# Create a private "GET" interface in project default category with a sample json response.
yapi.add_interface(project_id=project_id,
                   title='Calc Add',
                   method='GET',
                   path='/add',
                   req_query=[
                       {"name": "a", "required": "1", "example": "1", "desc": "变量a"},
                       {"name": "b", "required": "1", "example": "2", "desc": "变量b"},
                   ],
                   res_body_type="json",
                   res_body=json.dumps({"code": 0, "message": "success", "data": {"result": "3"}}),
                   res_body_is_json_schema=False,
                   status='done')

# Create a private "POST" interface in project default category with a sample json data and a sample json response.
yapi.add_interface(project_id=project_id,
                   title='Calc Sub',
                   method='POST',
                   path='/sub',
                   req_headers=[{"name": "Content-Type", "value": "application/json"}],
                   req_body_type="json",
                   req_body_other=json.dumps({"a": "5", "b": "1"}),
                   req_body_is_json_schema=False,

                   res_body_type="json",
                   res_body=json.dumps({"code": 0, "message": "success", "data": {"result": "4"}}),
                   res_body_is_json_schema=False,
                   status='done')
```
