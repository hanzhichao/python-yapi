class TestProject:

    def test_get_project_list(self, yapi):
        print(yapi.get_project_list())

    def test_get_project(self, yapi):
        print(yapi.get_project(project_id=22))

    def test_add_project(self, yapi):
        print(yapi.add_project(name='测试项目3'))

    def test_delete_project(self, yapi):
        yapi.delete_project(project_id=22)
        print(yapi.get_project(project_id=22))
