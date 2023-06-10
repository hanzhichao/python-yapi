from .base_api import BaseApi


class Project(BaseApi):

    def add_project(self, name: str, basepath='',
                    group_id: int = 11, icon='code-o',
                    color='blue', project_type='private'):
        """
        添加商品
        :param name:
        :param basepath:
        :param group_id:
        :param icon:
        :param color:
        :param project_type:
        :return:
        """
        url = '/api/project/add'
        payload = {"name": name,
                   "basepath": basepath,
                   "group_id": str(group_id),
                   "icon": icon,
                   "color": color,
                   "project_type": project_type}

        res = self.post(url, json=payload)
        assert 0 == res.json()['errcode'], '添加项目失败'
        return res.json()

    # res = session.get(base_url+'/api/project/get', params={'token':'c3c2a3fb0075592b5e7d833f86a6ac0c1f10214d6b55c0288e7ec0d6cfb10d80'})
    # print(res.text)

    def list_project(self, group_id=11, page=1, limit=10):
        """

        :return:
        """
        url = 'api/project/list'
        params = {
            'group_id': group_id,
            'page': page,
            'limit': limit
        }
        res = self.get(url, params=params)
        return res.json()

    def get_project(self, project_id: int):
        url = 'api/project/get'
        params = {'id': project_id}
        res = self.get(url, params=params)
        return res.json()

    def get_env(self, project_id: int):
        url = 'api/project/get_env'
        params = {'project_id': project_id}
        res = self.get(url, params=params)
        return res.json()

    def update_env(self, name: str, domain: str, header: list[str], global_vars: list[dict]):
        url = 'api/project/up_env'
        payload = {"id": 13,
                   "env": [{"name": "环境1", "domain": "http://127.0.0.2", "header": [{"name": "test", "value": "abc"}],
                            "global": [{"name": "ggg", "value": "aaa"}]},
                           {"header": [], "global": [], "_id": "64847303e6b807c906d16a52", "name": "local",
                            "domain": "http://127.0.0.1"}]}

    def update(self, name: str, basepath='',
                    group_id: int = 11, project_type='private'):
        url = 'api/project/up'
        payload = {"name": name, "project_type": project_type, "basepath": basepath, "switch_notice": True, "id": 13,
                   "env": [{"header": [{"name": "test", "value": "abc"}],
                            "global": [{"_id": "6484a903e6b807c906d16a5a", "name": "ggg", "value": "aaa"}],
                            "_id": "6484a903e6b807c906d16a59", "name": "环境1", "domain": "http://127.0.0.2"},
                           {"header": [], "global": [], "_id": "64847303e6b807c906d16a52", "name": "local",
                            "domain": "http://127.0.0.1"}], "group_id": group_id, "strice": False, "is_json5": False,
                   "tag": [{"name": "tag1", "desc": "tag1描述"}, {"name": "tag2", "desc": ""}]}

        res = self.post(url, json=payload)
        return res.json()

    def delete_project(self, project_id: int):
        url = '/api/project/del'
        payload = {id: project_id}
        res = self.post(url, json=payload)
        return res.json()
