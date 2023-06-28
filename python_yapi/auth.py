from python_yapi.base import ApiBase


class LoginMixIn(ApiBase):
    def login(self, email: str, password: str) -> dict:
        """
        Login YApi
        :param email: user email
        :param password: user password
        :return: JSON response body as dictionary
        """
        url = '/api/user/login'
        payload = {"email": email, "password": password}
        return self.post(url, json=payload)
