import requests


class BaseApi(object):
    def __init__(self, base_url: str):
        """
        :param base_url:
        :param email:
        :param password:
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        if not url.startswith('http'):
            url = f'{self.base_url}/{url}'
        return self.session.request(method, url, **kwargs)

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

    def login(self, email: str, password: str):
        url = '/api/user/login'
        payload = {"email": email, "password": password}
        res = self.post(url, json=payload)
        assert 0 == res.json()['errcode'], '登录失败'
