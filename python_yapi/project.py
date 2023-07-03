import random
from collections import namedtuple
from enum import Enum
from typing import List, Callable, Optional, Tuple

from slugify import slugify

from .base import ApiBase
from .exceptions import EnvNotFound

# Refer to https://github.com/YMFE/yapi/blob/master/client/constants/variable.js
PROJECT_COLORS = ('blue', 'green', 'yellow', 'red', 'pink', 'cyan', 'gray', 'purple')
PROJECT_ICONS = (
    'code-o',
    'swap',
    'clock-circle-o',
    'unlock',
    'calendar',
    'play-circle-o',
    'file-text',
    'desktop',
    'hdd',
    'appstore-o',
    'line-chart',
    'mail',
    'mobile',
    'notification',
    'picture',
    'poweroff',
    'search',
    'setting',
    'share-alt',
    'shopping-cart',
    'tag-o',
    'video-camera',
    'cloud-o',
    'star-o',
    'environment-o',
    'camera-o',
    'team',
    'customer-service',
    'pay-circle-o',
    'rocket',
    'database',
    'tool',
    'wifi',
    'idcard',
    'medicine-box',
    'coffee',
    'safety',
    'global',
    'api',
    'fork',
    'android-o',
    'apple-o'
)

ProjectTag = namedtuple('ProjectTag', 'name, desc')


class ProjectType(Enum):
    Public = 'public'
    Private = 'private'


class Role(Enum):
    Owner = 'owner'
    Dev = 'dev'
    Guest = 'guest'


class ProjectMixIn(ApiBase):
    get_my_group_id: Callable

    def get_project_list(self, group_id=None, page=1, limit=10):
        """
        Get project list of a given group.
        :param group_id: group id
        :param page: page number (default as 1
        :param limit: limit number (default as 10)
        :return:
        """
        if group_id is None:
            group_id = self.get_my_group_id()
        url = 'api/project/list'
        params = {
            'group_id': group_id,
            'page': page,
            'limit': limit
        }
        return self.get(url, params=params)

    def get_project(self, project_id: int) -> dict:
        """
        Get a project.
        :param project_id:
        :return:
            eg: {'_id': 55,
                 'add_time': 1688125162,
                 'basepath': '/leslie-medina',
                 'cat': [{'__v': 0,
                          '_id': 95,
                          'add_time': 1688125162,
                          'desc': '公共分类',
                          'index': 0,
                          'name': '公共分类',
                          'project_id': 55,
                          'uid': 15,
                          'up_time': 1688125162}],
                 'color': 'yellow',
                 'env': [{'_id': '649ebeea5ffe870635b0a18a',
                          'domain': 'http://127.0.0.1',
                          'global': [],
                          'header': [],
                          'name': 'local'}],
                 'group_id': 35,
                 'icon': 'environment-o',
                 'is_json5': False,
                 'is_mock_open': False,
                 'name': 'Leslie Medina',
                 'project_type': 'private',
                 'role': 'admin',
                 'strice': False,
                 'switch_notice': True,
                 'tag': [{'_id': '649ec25a5ffe870635b0a194',
                          'desc': 'tag1 desc',
                          'name': 'tag1'},
                         {'_id': '649ec25a5ffe870635b0a193',
                          'desc': 'tag2 desc',
                          'name': 'tag2'}],
                 'uid': 15,
                 'up_time': 1688126042}
        """
        url = 'api/project/get'
        params = {'id': project_id}
        return self.get(url, params=params)

    def get_project_cat(self, project_id: int) -> list:
        data = self.get_project(project_id)
        return data['cat']

    def get_project_default_category_id(self, project_id: int) -> int:
        data = self.get_project_cat(project_id)
        return data[0]['_id']

    def get_project_tag(self, project_id: int) -> List[dict]:
        return self.get_project(project_id)['tag']

    def search_project(self, keyword: str):
        """
        Search project by keyword
        :param keyword:
        :return:
        """
        url = '/api/project/search'
        params = {'q': keyword}
        return self.get(url, params=params)

    def add_project(self, name: str, basepath: str = None,
                    group_id: int = None, icon=None,
                    color=None, project_type='private'):
        """
        Add a project in YApi
        :param name: project name
        :param basepath: project base path
        :param group_id: project group id
        :param icon: project icon, one of PROJECT_ICONS (default as random icon)
        :param color: project color, one of PROJECT_COLORS (default as random color)
        :param project_type: project type (default as private)
        :return: data of JSON response body  # todo 已存在的项目名
            eg: {'__v': 0,
                  '_id': 41,
                  'add_time': 1687941306,
                  'basepath': '',
                  'color': 'blue',
                  'env': [{'_id': '649bf0ba5ffe870635b0a16c',
                           'domain': 'http://127.0.0.1',
                           'global': [],
                           'header': [],
                           'name': 'local'}],
                  'group_id': 11,
                  'icon': 'code-o',
                  'is_json5': False,
                  'is_mock_open': False,
                  'members': [],
                  'name': '测试项目3',
                  'project_type': 'private',
                  'strice': False,
                  'switch_notice': True,
                  'tag': [],
                  'uid': 11,
                  'up_time': 1687941306}

        """
        if not name:
            raise ValueError('Project name is required')

        if group_id is None:
            group_id = self.get_my_group()['_id']

        # todo check project name exists

        if basepath is None:
            basepath = f'/{slugify(str(name))}'

        if color is None:
            color = random.choice(PROJECT_COLORS)

        if icon is None:
            icon = random.choice(PROJECT_ICONS)

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
                       switch_notice=True, strice=False, is_json5=False, env: List[dict] = None,
                       tag: List[dict] = None):
        """
        Update a project.
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
        :return: data of JSON response body
        """
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
        """
        Delete a project
        :param project_id:  id
        :return: data of JSON response body
            eg:  {'deletedCount': 1, 'n': 1, 'ok': 1}
        """
        url = '/api/project/del'
        payload = {'id': project_id}
        data = self.post(url, json=payload)
        assert data['deletedCount'] == 1, 'Delete nothing'

    def get_project_env(self, project_id: int) -> list:
        """
        Get project environment configurations
        :param project_id: project id
        :return: data of JSON response body
            eg: [{'_id': '649ebeea5ffe870635b0a18a',
                  'domain': 'http://127.0.0.1',
                  'global': [],
                  'header': [],
                  'name': 'local'}]}
        """
        url = '/api/project/get_env'
        params = {'project_id': project_id}
        return self.get(url, params=params)['env']

    def get_project_env_by_env_name(self, project_id: int, env_name: str) -> Optional[Tuple[int, dict]]:
        env_list = self.get_project_env(project_id)
        for index, env in enumerate(env_list):
            if env['name'] == env_name:
                return index, env
        return None, None

    def update_project_env(self, project_id: int, env: List[dict]) -> dict:
        """
        Update project environment configuration
        :param project_id: project id
        :param env: list of environment configurations
            eg: [{'name': '环境1',
                  'domain': 'http://127.0.0.2',
                  'header': [{'name': 'test', 'value': 'abc'}],
                  'global': [{'name': 'ggg', 'value': 'aaa'}]}]
        :return: data of JSON response body
            eg: {"n":1,"nModified":1,"ok":1}}
        """
        url = '/api/project/up_env'
        payload = {'id': project_id, 'env': env}
        return self.post(url, json=payload)

    def add_project_env_headers(self, project_id, env_name: str, headers: dict, cookies: dict = None):
        """
        Add headers in project environment configuration.
        :param project_id: project id
        :param headers:
            eg: [{'name': 'test', 'value': 'abc'}]
        :return:
        """
        if cookies:
            cookie = ';'.join([f'{k}={v}' for k, v in cookies.items()])
            headers.update({'Cookie': cookie})

        env_list = self.get_project_env(project_id)
        for index, env in enumerate(env_list):
            if env['name'] == env_name:
                env['header'].extend([{'name': k, 'value': v} for k, v in headers.items()])

                # todo merge cookies
                return self.update_project_env(project_id, env=env_list)

        raise EnvNotFound(f'Not found project_id={project_id} env.name={env_name}')

    def update_project_tag(self, project_id: int, tag: List[dict]):
        """
        Update project tag list.
        :param project_id: project id
        :param tag:
            eg: [{'desc': 'tag1 desc', 'name': 'tag1'}, {'desc': 'tag2 desc', 'name': 'tag2'}]
        :return:
            eg: {'n': 1, 'nModified': 1, 'ok': 1}
        """
        url = '/api/project/up_tag'
        payload = {"id": project_id, "tag": tag}
        return self.post(url, json=payload)

    def add_project_tag(self, project_id: int, tag: List[dict]):
        """
        Add project tag list.
        :param project_id: project id
        :param tag: tag list
        :return:
            eg: {'n': 1, 'nModified': 1, 'ok': 1}
        """
        tag_list = self.get_project_tag(project_id)
        tag_list.extend(tag)
        return self.update_project_tag(project_id, tag_list)

    def get_project_token(self, project_id: int) -> str:
        """
        Get project token.
        :param project_id: project id
        :return: token
            eg: 51ac2fb9044ea64768ba8f8ba7fcf11b5d5d58733d40458756f58a704f9132b0
        """
        url = '/api/project/token'
        params = {'project_id': project_id}
        return self.get(url, params=params)

    def get_project_wiki(self, project_id: int):
        """
        Get project wiki content.
        :param project_id:
        :param desc: html description
            eg: "<p>nihao ya</p>\n"
        :param markdown: markdown description
            eg: "nihao ya"
        :return: data or JSON responsebody
            eg: {"edit_uid": 15,
                "_id": 11,
                "project_id": 55,
                "desc": "<p>nihao ya****</p>",
                "markdown": "nihao ya\\*\\*\\*\\*",
                "username": "zhangsan",
                "uid": 15,
                "add_time": 1688129575,
                "up_time": 1688129736,
                "__v": 0
            }
        """
        url = '/api/plugin/wiki_desc/get'
        params = {"project_id": project_id}
        return self.post(url, params=params)

    def update_project_wiki(self, project_id: int, desc: str, markdown: str, email_notice: bool = True):
        """
        Edit project wiki
        :param project_id:
        :param desc: html description
            eg: "<p>nihao ya</p>\n"
        :param markdown: markdown description
            eg: "nihao ya"
        :return: data or JSON responsebody
            eg: {"n":1,"nModified":1,"ok":1}
        """
        url = '/api/plugin/wiki_desc/up'
        payload = {"project_id": project_id, "desc": desc, "markdown": markdown, "email_notice": email_notice}
        return self.post(url, json=payload)
