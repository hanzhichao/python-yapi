import json
from pprint import pprint


class TestInterface:
    def test_add_full_interface_get(self, yapi_login):
        data = yapi_login.add_interface(project_id=62, title='add接口', method='GET', path='/add',
                                  req_query=[
                                      {"name": "a", "required": "1", "example": "1", "desc": "变量a"},
                                      {"name": "b", "required": "1", "example": "2", "desc": "变量b"},
                                  ],
                                  res_body_type="json",
                                  res_body=json.dumps({"code": 0, "message": "success",
                                                       "data": {"result": "3"}}),
                                  res_body_is_json_schema=False,
                                  status='done')

        pprint(data)
        assert data['_id'] is not None

    def test_add_full_interface_post(self, yapi_login):
        data = yapi_login.add_interface(project_id=62, title='POST示例接口09', method='POST', path='/post_demo09',
                                        req_headers=[{"name": "Content-Type", "value": "application/json"}],
                                        req_body_type="json",
                                        req_body_other=json.dumps({"username": "Kevin2", "password": "abc123"}),
                                        req_body_is_json_schema=False,
                                        res_body_type="json",
                                        res_body=json.dumps({"code": 0, "message": "success", "status": "done",
                                                             "data": [{"name": "Kevin", "age": 14}]}),
                                        res_body_is_json_schema=False,
                                        status='done')
        pprint(data)
        assert data['_id'] is not None

    def test_add_interface(self, yapi_login):
        data = yapi_login.add_interface(project_id=62, title='POST示例接口09', method='POST', path='/post_demo09')
        pprint(data)
        assert data['_id'] is not None

    def test_update_interface(self, yapi_login):
        data = yapi_login.update_interface(interface_id=73,
                                           req_query=[
                                               {"name": "name", "required": "0", "example": "Kevin", "desc": ""}],
                                           req_headers=[{"name": "Content-Type", "value": "application/json"}],
                                           req_body_type="json",
                                           req_body_other=json.dumps({"username": "Kevin2", "password": "abc123"}),
                                           req_body_is_json_schema=False,
                                           res_body_type="json",
                                           res_body=json.dumps({"code": 0, "message": "success", "status": "done",
                                                                "data": [{"name": "Kevin", "age": 14}]}),
                                           res_body_is_json_schema=False,
                                           status='done'
                                           )

        pprint(data)
        assert data['_id'] is not None
