from .base import ApiBase


class ProjectMixIn(ApiBase):
    def get_project_list(self, group_id=11, page=1, limit=10):
        '''
        '''
        url = 'api/project/list'
        params = {
            'group_id': group_id,
            'page': page,
            'limit': limit
        }
        return self.get(url, params=params)

    def get_project(self, project_id: int):
        """
        Get a project
        :param project_id:
        :return:
        """
        url = 'api/project/get'
        params = {'id': project_id}
        return self.get(url, params=params)

    def get_project_by_name(self, name: str):
        """
        Get a project by name
        :param name:
        :return:
        """
        pass

    def search_project(self, keyword: str):
        """
        Search project by keyword
        :param keyword:
        :return:
        """
        url = '/api/project/search'
        params = {'q': keyword}
        return self.get(url, params=params)


    def add_project(self, name: str, basepath='',
                    group_id: int = 11, icon='code-o',
                    color='blue', project_type='private'):
        '''
        Add a project in YApi
        :param name: project name
        :param basepath: project base path
        :param group_id: project group id (default as 11)
        :param icon: project icon (default as code-o)
        :param color: project color (default as blue)
        :param project_type: project type (default as private)
        :return: JSON response body as dictionary  # todo 已存在的项目名
        '''
        url = '/api/project/add'
        payload = {'name': name,
                   'basepath': basepath,
                   'group_id': str(group_id),
                   'icon': icon,
                   'color': color,
                   'project_type': project_type}

        return self.post(url, json=payload)

    def copy_project(self, project_id, name) -> dict:
        url = '/api/project/copy'

        payload = {'switch_notice': True, 'is_mock_open': False, 'strice': False, 'is_json5': False, '_id': 31,
                   'name': '测试项目2', 'basepath': '', 'project_type': 'private', 'uid': 11, 'group_id': 11,
                   'icon': 'code-o', 'color': 'blue', 'add_time': 1687927950, 'up_time': 1687927950, 'env': [
                {'header': [], 'global': [], '_id': '649bbc8ed5f52599e53beadb', 'name': 'local',
                 'domain': 'http://127.0.0.1'}], 'tag': [], 'cat': [
                {'index': 0, '_id': 28, 'name': '公共分类', 'project_id': 31, 'desc': '公共分类', 'uid': 11,
                 'add_time': 1687927950, 'up_time': 1687927950, '__v': 0}], 'role': 'admin', 'preName': '测试项目1'}

        return self.post(url, json=payload)

    def update_project(self, project_id: int, name: str, basepath='', group_id: int = 11, project_type='private',
                       switch_notice=True, strice=False, is_json5=False, env: list[dict] = None,
                       tag: list[dict] = None):
        '''
        Update project
        :param project_id: project id
        :param name: project name
        :param basepath:
        :param group_id:
        :param project_type:
        :param switch_notice:
        :param strice:
        :param is_json5:
        :param env: project environment configurations
            eg: [{'header': [{'name': 'test', 'value': 'abc'}],
                            'global': [{'_id': '6484a903e6b807c906d16a5a', 'name': 'ggg', 'value': 'aaa'}],
                            '_id': '6484a903e6b807c906d16a59', 'name': '环境1', 'domain': 'http://127.0.0.2'},
                           {'header': [], 'global': [], '_id': '64847303e6b807c906d16a52', 'name': 'local',
                            'domain': 'http://127.0.0.1'}],
        :param tag: project tags
            eg: [{'name': 'tag1', 'desc': 'tag1描述'}, {'name': 'tag2', 'desc': ''}]
        :return: JSON response body as dictionary
        '''
        url = 'api/project/up'
        payload = {'id': project_id,
                   'group_id': group_id,
                   'name': name,
                   'project_type': project_type,
                   'basepath': basepath,
                   'switch_notice': switch_notice,
                   'env': env,
                   'strice': strice,
                   'is_json5': is_json5,
                   'tag': tag}

        return self.post(url, json=payload)

    def delete_project(self, project_id: int) -> dict:
        '''
        Delete a project
        :param project_id: project id
        :return: JSON response body as dictionary
        '''
        url = '/api/project/del'
        payload = {'id': project_id}
        return self.post(url, json=payload)

    def get_project_env(self, project_id: int) -> dict:
        '''
        Get project environment configurations
        :param project_id: project id
        :return: JSON response body as dictionary
        '''
        url = '/api/project/get_env'
        params = {'project_id': project_id}
        return self.get(url, params=params)

    def update_project_env(self, project_id: int, env: list[dict]) -> dict:
        '''
        Update project environment configuration
        :param project_id: project id
        :param env: list of environment configurations
            eg: {'name': '环境1', 'domain': 'http://127.0.0.2', 'header': [{'name': 'test', 'value': 'abc'}],
                            'global': [{'name': 'ggg', 'value': 'aaa'}]},
                           {'header': [], 'global': [], '_id': '64847303e6b807c906d16a52', 'name': 'local',
                            'domain': 'http://127.0.0.1'}]
        :return: JSON response body as dictionary
        '''
        url = '/api/project/up_env'
        payload = {'id': project_id, 'env': env}
        return self.post(url, json=payload)
