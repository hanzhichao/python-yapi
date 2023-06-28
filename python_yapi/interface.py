from python_yapi.base import ApiBase


class InterfaceMixIn(ApiBase):

    def get_interface(self, id: int):
        """

        :return:
            eg: {
                "errcode": 0,
                "errmsg": "成功！",
                "data": {
                    "query_path": {
                        "path": "/path1",
                        "params": []
                    },
                    "edit_uid": 0,
                    "status": "undone",
                    "type": "static",
                    "req_body_is_json_schema": false,
                    "res_body_is_json_schema": false,
                    "api_opened": false,
                    "index": 0,
                    "tag": [],
                    "_id": 28,
                    "method": "POST",
                    "catid": 28,
                    "title": "接口1",
                    "path": "/path1",
                    "project_id": 31,
                    "req_params": [],
                    "res_body_type": "json",
                    "uid": 11,
                    "add_time": 1687943795,
                    "up_time": 1687943795,
                    "req_query": [],
                    "req_headers": [],
                    "req_body_form": [],
                    "__v": 0,
                    "username": "admin"
                }
            }
        """
        url = '/api/interface/get'
        params = {'id': id}
        return self.get(url, params=params)


    def add_interface(self, method: str, catid: int, title: str, path: str, project_id: int):
        url = '/api/interface/add'
        payload = {"method": method, "catid": str(catid), "title": title, "path": path, "project_id": project_id}
        return self.post(url, json=payload)

    def add_category(self, name: str, desc: str, project_id: int):
        url = '/api/interface/add_cat'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
        return self.post(url, json=payload)

    def update_interface(self):
        url = 'api/interface/up'
        payload = {"id": "11", "status": "done"}
        return self.post(url, json=payload)
