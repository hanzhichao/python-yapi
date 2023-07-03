from pprint import pprint


class TestProject:

    def test_get_project_list(self, yapi_login):
        print(yapi_login.get_project_list())

    def test_get_project(self, yapi_login):
        print(yapi_login.get_project(project_id=55))

    def test_add_project(self, yapi_login):
        print(yapi_login.add_project(name='测试项目3'))

    def test_delete_project(self, yapi_login):
        data = yapi_login.delete_project(project_id=56)
        pprint(data)
        # print(yapi_admin.get_project(project_id=33))

    def test_add_project_with_random_name(self, yapi, faker):
        yapi.login('zhangsan@126.com', 'abc123456')
        # data = yapi.get_my_group()
        # group_id = data['_id']
        data = yapi.add_project(faker.name())
        pprint(data)

    def test_get_project_tag(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_project_tag(55)
        pprint(data)

    def test_update_project_tag(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.update_project_tag(55, tag=[{'desc': 'tag1 desc', 'name': 'tag1'},
                                                {'desc': 'tag2 desc', 'name': 'tag2'}
                                                ])
        pprint(data)

    def test_add_project_tag(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.add_project_tag(55, tag=[{'desc': 'tag6 desc', 'name': 'tag6'},
                                             {'desc': 'tag7 desc', 'name': 'tag7'}
                                             ])
        pprint(data)

    def test_get_project_env(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_project_env(55)
        pprint(data)

    def test_update_project_env(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.update_project_env(55, env=[{'name': '环境1',
                                                 'domain': 'http://127.0.0.2',
                                                 'header': [{'name': 'test', 'value': 'abc'}],
                                                 'global': [{'name': 'ggg', 'value': 'aaa'}]}])

        pprint(data)

    def test_add_project_env_headers(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.add_project_env_headers(55, 'hhh',
                                            headers={'Content-Type': 'application/json'})
        pprint(data)

    def test_get_project_token(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_project_token(55)
        pprint(data)
