from python_yapi.base import ApiBase


class UserMixIn(ApiBase):
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

    def logout(self):
        url = '/api/user/logout'
        return self.get(url)

    def register(self, username: str, email: str, password: str) -> dict:
        url = '/api/user/reg'
        payload = {"username": username, "email": email, "password": password}
        return self.post(url, json=payload)

    def get_user(self, id: int):
        """

        :param id:
        :return:
            eg: {
                "errcode": 0,
                "errmsg": "成功！",
                "data": {
                    "uid": 13,
                    "username": "superhin",
                    "email": "superhin@126.com",
                    "role": "member",
                    "type": "site",
                    "add_time": 1687943141,
                    "up_time": 1687943146
                }
            }
        """
        url = '/api/user/find'
        params = {"id": id}
        return self.get(url, params=params)

    def update_user(self, uid: int, username: str = None, email: str = None):
        url = '/api/user/update'
        payload = {"uid": uid}
        if username is not None:
            payload['username'] = username
        if email is not None:
            payload['email'] = email
        return self.post(url, json=payload)

    def change_password(self, uid: int, old_password: str, password: str):
        url = '/api/user/change_password'
        payload = {"uid": uid, "password": password, "old_password": old_password}
        return self.post(url, json=payload)
