from pprint import pprint


class TestGroup:

    def test_get_my_group(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_my_group()
        pprint(data)

    def test_get_my_group_id(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_my_group_id()
        pprint(data)

    def test_get_group(self, yapi):
        yapi.login('zhangsan@126.com', 'abc123456')
        data = yapi.get_group(35)
        pprint(data)
