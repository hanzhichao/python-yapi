from enum import Enum
from typing import List

from python_yapi.base import ApiBase


class InterfaceStatus(Enum):
    Done = 'done'
    UnDone = 'undone'


class InterfaceMixIn(ApiBase):

    def get_interface(self, interface_id: int):
        """
        Get interface details.
        :param interface_id: Interface id
        :return:
            eg: {'__v': 0,
                 '_id': 37,
                 'add_time': 1688352373,
                 'api_opened': False,
                 'catid': 153,
                 'desc': '<p>一个通过姓名年级获取学生信息的接口</p>\n',
                 'edit_uid': 0,
                 'index': 0,
                 'markdown': '一个通过姓名年级获取学生信息的接口',
                 'method': 'GET',
                 'path': '/demo_get01',
                 'project_id': 62,
                 'query_path': {'params': [], 'path': '/demo_get01'},
                 'req_body_form': [],
                 'req_body_is_json_schema': True,
                 'req_headers': [],
                 'req_params': [],
                 'req_query': [{'_id': '64a23853a534ee9cf4b713a1',
                                'desc': '姓名',
                                'example': 'Kevin',
                                'name': 'name',
                                'required': '1'},
                               {'_id': '64a23853a534ee9cf4b713a0',
                                'desc': '年级',
                                'example': '3',
                                'name': 'class',
                                'required': '0'}],
                 'res_body': '{"type":"object","title":"empty '
                             'object","properties":{"code":{"type":"number","mock":{"mock":"@integer"},"description":"错误码"},"data":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string","mock":{"mock":"@name"},"description":"姓名"},"gender":{"type":"string","mock":{"mock":"@boolean"},"description":"性别 '
                             'true男 '
                             'false女"},"age":{"type":"number","mock":{"mock":"@integer"},"description":"年龄"},"grade":{"type":"number","mock":{"mock":"@integer"},"description":"年级"}},"required":["name","gender","age","grade"]},"description":"数据"}},"required":["code","data"]}',
                 'res_body_is_json_schema': True,
                 'res_body_type': 'json',
                 'status': 'done',
                 'tag': ['tag1', 'tag2'],
                 'title': 'GET示例接口',
                 'type': 'static',
                 'uid': 16,
                 'up_time': 1688352851,
                 'username': 'Kevin'}
        """
        url = '/api/interface/get'
        params = {'id': interface_id}
        return self.get(url, params=params)

    def add_interface(self, title: str, method: str, path: str, project_id: int, catid: int = None,
                      status: str=None,
                      tag: list = None,
                      desc: str = None,
                      markdown: str = None,
                      req_body_is_json_schema: bool = None,
                      req_params: List[dict] = None,
                      req_query: List[dict] = None,
                      req_headers: List[dict] = None,
                      req_body_form: List[dict] = None,
                      req_body_type: str = None,
                      req_body_other: str = None,

                      res_body_is_json_schema: bool = None,
                      res_body_type: str = None,
                      res_body: str = None,
                      switch_notice: bool = False,
                      api_opened: bool = False):
        """
        Adds a new interface.
        :param status:
        :param api_opened:
        :param switch_notice:
        :param res_body:
        :param res_body_is_json_schema:
        :param req_body_other:
        :param req_body_type:
        :param req_body_form:
        :param req_headers:
        :param req_query:
        :param req_params:
        :param markdown:
        :param req_body_is_json_schema:
        :param desc:
        :param tag:
        :param title: interface title
        :param method: http method
        :param path: interface path
        :param project_id: project id
        :param catid: category id
        :return:
            eg: {'__v': 0,
                 '_id': 37,
                 'add_time': 1688352373,
                 'api_opened': False,
                 'catid': 153,
                 'edit_uid': 0,
                 'index': 0,
                 'method': 'GET',
                 'path': '/demo_get01',
                 'project_id': 62,
                 'query_path': {'params': [], 'path': '/demo_get01'},
                 'req_body_form': [],
                 'req_body_is_json_schema': False,
                 'req_headers': [],
                 'req_params': [],
                 'req_query': [],
                 'res_body_is_json_schema': False,
                 'res_body_type': 'json',
                 'status': 'undone',
                 'tag': [],
                 'title': 'GET示例接口',
                 'type': 'static',
                 'uid': 16,
                 'up_time': 1688352373}
        """
        url = '/api/interface/add'
        if catid is None:
            catid = self.get_project_default_category_id(project_id)

        payload = {
            "method": method,
            "title": title,
            "path": path,
            "project_id": project_id,
            "catid": str(catid),
        }
        for key, value in {'tag': tag, 'desc': desc, 'markdown': markdown,
                           'req_body_is_json_schema': req_body_is_json_schema,
                           'req_params': req_params, 'req_query': req_query, 'req_headers': req_headers,
                           'req_body_form': req_body_form, 'req_body_type': req_body_type,
                           'req_body_other': req_body_other,
                           'res_body_is_json_schema': res_body_is_json_schema, 'res_body_type': res_body_type,
                           'res_body': res_body, 'switch_notice': switch_notice, 'api_opened': api_opened,
                'status': status,
                           }.items():
            if value is not None:
                payload[key] = value

        return self.post(url, json=payload)

    def add_category(self, name: str, desc: str, project_id: int):
        url = '/api/interface/add_cat'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
        return self.post(url, json=payload)

    @staticmethod
    def pack_req_query_item(name, required: bool = True, desc: str = "", example: str = ""):
        required_str = "1" if required else "0"
        return {"name": name, "required": required_str, "desc": desc, example: example}

    def update_interface_status(self, interface_id: int, status: str = None):
        url = 'api/interface/up'
        payload = {"id": interface_id, "status": status}
        return self.post(url, json=payload)

    def update_interface(self, interface_id: int, status: str = None, title: str = None, catid: int = None,
                         method: str = None,
                         path: str = None,
                         tag: list = None,
                         desc: str = None,
                         markdown: str = None,
                         req_body_is_json_schema: bool = None,
                         req_params: List[dict] = None,
                         req_query: List[dict] = None,
                         req_headers: List[dict] = None,
                         req_body_form: List[dict] = None,
                         req_body_type: str = None,
                         req_body_other: str = None,

                         res_body_is_json_schema: bool = None,
                         res_body_type: str = None,
                         res_body: str = None,
                         switch_notice: bool = None,
                         api_opened: bool = None,
                         ):
        """
        Update interface details.
        :param req_body_other:
        :param req_body_type:
        :param interface_id:
        :param status:
        :param title:
        :param catid:
        :param method:
        :param path:
        :param tag:
        :param desc:
        :param markdown:
        :param req_body_is_json_schema:
        :param req_params:
        :param req_query:
        :param req_headers:
        :param req_body_form:
        :param res_body_is_json_schema:
        :param res_body_type:
        :param res_body:
            eg: eg: {'properties': {'code': {'description': '错误码',
                                         'mock': {'mock': '@integer'},
                                         'type': 'number'},
                                'data': {'description': '数据',
                                         'items': {'properties': {'age': {'description': '年龄',
                                                                          'mock': {'mock': '@integer'},
                                                                          'type': 'number'},
                                                                  'gender': {'description': '性别 true男 false女',
                                                                             'mock': {'mock': '@boolean'},
                                                                             'type': 'string'},
                                                                  'grade': {'description': '年级',
                                                                            'mock': {'mock': '@integer'},
                                                                            'type': 'number'},
                                                                  'name': {'description': '姓名',
                                                                           'mock': {'mock': '@name'},
                                                                           'type': 'string'}},
                                                   'required': ['name', 'gender', 'age', 'grade'],
                                                   'type': 'object'},
                                         'type': 'array'}},
                 'required': ['code', 'data'],
                 'title': 'empty object',
                 'type': 'object'}
        :param switch_notice:
        :param api_opened:
        :return:
        """
        url = 'api/interface/up'

        data = self.get_interface(interface_id)

        payload = {
            "id": interface_id,
            "catid": catid if catid is not None else data['catid'],
            "title": title if title is not None else data['title'],
            "path": path if path is not None else data['path'],
            "method": method if method is not None else data['method'],
            "status": status if status is not None else data['method'],
            "tag": tag if tag is not None else data['tag'],

            "req_query": req_query if req_query is not None else data['req_query'],
            "req_params": req_params if req_params is not None else data['req_params'],
            "req_headers": req_headers if req_headers is not None else data['req_headers'],
            "req_body_form": req_body_form if req_body_form is not None else data['req_body_form'],
            "req_body_is_json_schema": req_body_is_json_schema if req_body_is_json_schema is not None else data[
                'req_body_is_json_schema'],

            "res_body_type": res_body_type if res_body_type is not None else data['res_body_type'],
            "res_body_is_json_schema": res_body_is_json_schema if res_body_is_json_schema is not None else data[
                'res_body_is_json_schema'],
            "api_opened": api_opened if api_opened is not None else data['api_opened'],
        }

        if desc is not None:
            payload['desc'] = desc
        if markdown is not None:
            payload['markdown'] = markdown
        if res_body is not None:
            payload['res_body'] = res_body
        if req_body_type is not None:
            payload['req_body_type'] = req_body_type
        if req_body_other is not None:
            payload['req_body_other'] = req_body_other
        if switch_notice is not None:
            payload['switch_notice'] = switch_notice

        return self.post(url, json=payload)
