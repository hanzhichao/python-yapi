
class ResponseNotJSONError(Exception): ...

class ProjectNameExists(Exception): ...


class ServerError(Exception):
    """服务器出错{'errcode': 40011, 'errmsg': '服务器出错...', 'data': None}"""

# requests.exceptions.ConnectionError
# 'errcode': 401, 'errmsg': '该email已经注册', 'data': None


class EnvNotFound(Exception): ...
