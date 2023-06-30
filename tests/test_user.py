import inspect


class TestLogin:
    def test_register(self, yapi):
        data = yapi.register('zhangsan', 'zhangsan@126.com', 'abc123456')
        print(data)

    def test_login(self, yapi):
        data = yapi.login('zhangsan@126.com', 'abc123456')
        print(data)
