import json

from python_yapi.base import ApiBase


class CollectionMixIn(ApiBase):
    def add_collection(self, name: str, desc: str, project_id: int):
        """
        Adds a collection.
        :param name: collection name
        :param desc: collection description
        :param project_id: project id
        :return:
        """
        url = '/api/col/add_col'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
        return self.post(url, json=payload)

    def get_collection_list(self, project_id: int) -> list:
        """
        Get a list of collections.
        :param project_id:
        :return:
            eg: [
                    {
                        "index": 0,
                        "_id": 16,
                        "name": "公共测试集",
                        "project_id": 19,
                        "desc": "公共测试集",
                        "uid": 13,
                        "add_time": 1688525212,
                        "caseList": []
                    },
                    {
                        "index": 0,
                        "_id": 21,
                        "name": "集合1",
                        "project_id": 19,
                        "desc": "集合1描述",
                        "uid": 13,
                        "add_time": 1688525227,
                        "caseList": []
                    }
                ]
        """
        url = '/api/col/list'
        params = {'project_id': project_id}
        return self.get(url, params=params)

    def get_case_list(self, col_id: int) -> dict:
        """
        Get a list of cases.
        :param col_id: test collection id
        :return:
            eg: {
                "checkResponseField": {
                    "name": "code",
                    "value": "0",
                    "enable": false
                },
                "checkScript": {
                    "enable": false
                },
                "index": 0,
                "test_report": "{}",
                "checkHttpCodeIs200": false,
                "checkResponseSchema": false,
                "_id": 26,
                "name": "集合1 copy",
                "project_id": 19,
                "desc": "集合1描述",
                "uid": 13,
                "add_time": 1688525231,
                "up_time": 1688525231,
                "__v": 0
            }
        """
        url = '/api/col/case_list'
        params = {'col_id': col_id}
        return self.request('GET', url, params=params)['colData']

    def get_case_env_list(self, col_id: int):
        """
        Get the test case environment list of a colletion.
        :param col_id: collection id.
        :return:
        """
        url = '/api/col/case_env_list'
        params = {'col_id': col_id}
        return self.get(url, params=params)

    def del_collection(self, col_id: int):
        """
        Delete a collection.
        :param col_id: collection id
        :return:
        """
        url = '/api/col/del_col'
        params = {'col_id': col_id}
        return self.get(url, params=params)

    def clone_case_list(self, new_col_id: int, col_id: int, project_id: int):
        """
        Clone the case list of a collection.
        :param new_col_id: new collection id
        :param col_id: original collection id
        :param project_id: project id of original collection

        :return:
        """
        url = '/api/col/clone_case_list'
        payload = {"new_col_id": new_col_id, "col_id": col_id, "project_id": project_id}
        return self.post(url, json=payload)

    def update_collection(self, col_id: int, name: str, desc: str):
        """
        Update a collection.
        :param col_id:
        :param name:
        :param desc:
        :return:
            eg: {"n":1,"nModified":1,"ok":1}
        """
        url = '/api/col/up_col'
        paylaod = {"name": name, "desc": desc, "col_id": col_id}
        return self.post(url, json=paylaod)

    def add_case_list(self, col_id: int, project_id: int, interface_list: list) -> str:
        """
        Import interfaces form a category to create a list of test cases.
        :param col_id:
        :param project_id:
        :param interface_list:
        :return: "ok"
        """
        url = '/api/col/add_case_list'
        payload = {"interface_list": interface_list, "col_id": col_id, "project_id": project_id}
        return self.post(url, json=payload)

    def update_case(self, case_id: int, casename: str, case_env: str, req_params: list, req_query: list,
                    req_headers: list,
                    req_body_form: list, test_script: str = "", enable_script: bool = False, test_res_body: str = None,
                    test_res_header: str = None):
        """
        Update a case.
        :return: eg: {n: 1, nModified: 1, ok: 1}
        """
        url = 'api/col/up_case'
        paylaod = {"id": case_id, "casename": casename, "case_env": case_env, "req_params": req_params,
                   "req_query": req_query,
                   "req_headers": req_headers, "req_body_form": req_body_form, "test_script": test_script,
                   "enable_script": enable_script,
                   "test_res_body": test_res_body, "test_res_header": test_res_header}

        return self.post(url, json=paylaod)

    def get_case(self, case_id: int):
        """
        Get a test case by id.
        :param case_id: test case id
        :return: eg: {
                        "index": 0,
                        "mock_verify": false,
                        "enable_script": false,
                        "_id": 10,
                        "uid": 13,
                        "add_time": 1688526154,
                        "up_time": 1688526170,
                        "project_id": 19,
                        "col_id": 16,
                        "interface_id": 17,
                        "casename": "示例接口1",
                        "req_params": [],
                        "req_headers": [],
                        "req_query": [],
                        "req_body_form": [],
                        "__v": 0,
                        "case_env": "local",
                        "test_res_body": null,
                        "test_res_header": null,
                        "test_script": "",
                        "path": "/demo/get01",
                        "method": "GET",
                        "res_body_type": "json",
                        "interface_up_time": 1688526091,
                        "req_body_is_json_schema": false,
                        "res_body_is_json_schema": false
                    }
        """
        url = '/api/col/case'
        params = {'caseid': case_id}
        return self.get(url, params=params)

    def update_collection_settings(self, project_id, col_id: int, name, desc, checkHttpCodeIs200: bool,
                                   checkResponseField: bool, checkResponseSchema: bool,
                                   checkScript: bool):
        url = '/api/col/up_col'
        payload = {"col_id": col_id, "checkHttpCodeIs200": checkHttpCodeIs200,
                   "checkResponseField": {"name": "code", "value": "0", "enable": checkResponseField},
                   "checkResponseSchema": checkResponseSchema,
                   "checkScript": {"enable": checkScript}, "index": 0, "test_report": "{}", "_id": 16, "name": name,
                   "project_id": project_id, "desc": desc, "uid": 13, "add_time": 1688525212, "up_time": 1688525212,
                   "__v": 0}
        return self.post(url, json=payload)

    @staticmethod
    def build_test_report_item(caseId: int, method, url, params: dict = {}, headers: dict = {}, status: int = 0,
                               timeout: int = 82400000,
                               res_body: str = '', msg: str = '', validRes: list = [], code: int = None,
                               statusText: str = '') -> dict:
        """
        Build a test report item.
        :param caseId:
        :param method:
        :param url:
        :param params:
        :param headers:
        :param status:
        :param timeout:
        :param res_body:
        :param msg:
        :param validRes:
        :param code:
        :param statusText:
        :return:
        """
        return {
            str(caseId): {
                'caseId': str(caseId),
                'code': code,
                'headers': headers,
                'method': method,
                'msg': msg,
                'params': params,
                'res_body': res_body,
                'status': status,
                'statusText': statusText,
                'timeout': timeout,
                'url': url,
                'validRes': validRes,
            }
        }

    def update_collection_report(self, col_id, test_report: dict):
        """
        Update a collection report.
        :param col_id:
        :param test_report:
            eg: {
                    '10': {'caseId': 10,
                        'code': 400,
                        'headers': {},
                        'method': 'GET',
                        'msg': '数据异常',
                        'params': {},
                        'res_body': '请求异常，请检查 chrome network 错误信息... '
                                    'https://juejin.im/post/5c888a3e5188257dee0322af '
                                    '通过该链接查看教程"）',
                        'status': 0,
                        'statusText': '请求异常，请检查 chrome network 错误信息... '
                                      'https://juejin.im/post/5c888a3e5188257dee0322af '
                                      '通过该链接查看教程"）',
                        'timeout': 82400000,
                        'url': 'http://127.0.0.1/demo/get01',
                        'validRes': [{'message': '请求异常，请检查 chrome network 错误信息... '
                                                 'https://juejin.im/post/5c888a3e5188257dee0322af '
                                                 '通过该链接查看教程"）'}]},
                    '17': {'caseId': 17,
                        'code': 400,
                        'headers': {},
                        'method': 'POST',
                        'msg': '数据异常',
                        'params': {},
                        'res_body': '请求异常，请检查 chrome network 错误信息... '
                                    'https://juejin.im/post/5c888a3e5188257dee0322af '
                                    '通过该链接查看教程"）',
                        'status': 0,
                        'statusText': '请求异常，请检查 chrome network 错误信息... '
                                      'https://juejin.im/post/5c888a3e5188257dee0322af '
                                      '通过该链接查看教程"）',
                        'timeout': 82400000,
                        'url': 'http://127.0.0.1/demo/post01',
                        'validRes': [{'message': '请求异常，请检查 chrome network 错误信息... '
                                                 'https://juejin.im/post/5c888a3e5188257dee0322af '
                                                 '通过该链接查看教程"）'}]}
                }

        :return:
        """
        url = '/api/col/up_col'
        payload = {"col_id": col_id,
                   "test_report": json.dumps(test_report)}

        return self.post(url, json=payload)
