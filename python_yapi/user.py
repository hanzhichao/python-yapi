from python_yapi.base import ApiBase


class UserMixIn(ApiBase):
    def login(self, email: str, password: str) -> dict:
        """
        Login YApi
        :param email: user email
        :param password: user password
        :return: JSON response body as dictionary
            eg: {'add_time': 1688116008,
                 'email': 'zhangsan@126.com',
                 'role': 'member',
                 'study': False,
                 'type': 'site',
                 'uid': 15,
                 'up_time': 1688116008,
                 'username': 'zhangsan'}
        """
        url = '/api/user/login'
        payload = {"email": email, "password": password}
        return self.post(url, json=payload)

    def logout(self):
        url = '/api/user/logout'
        return self.get(url)

    def register(self, username: str, email: str, password: str) -> dict:
        """

        :param username:
        :param email:
        :param password:
        :return:
            eg: {'add_time': 1688116008,
                 'email': 'zhangsan@126.com',
                 'role': 'member',
                 'study': False,
                 'type': 'site',
                 'uid': 15,
                 'up_time': 1688116008,
                 'username': 'zhangsan'}
        """
        url = '/api/user/reg'
        payload = {"username": username, "email": email, "password": password}
        return self.post(url, json=payload)

    def find_user(self, uid: int):
        """
        Find a user by uid.
        :param uid: user id
        :return: user data
            eg: {"uid": 13,
                "username": "superhin",
                "email": "superhin@126.com",
                "role": "member",
                "type": "site",
                "add_time": 1687943141,
                "up_time": 1687943146}
        """
        url = '/api/user/find'
        params = {"id": uid}
        return self.get(url, params=params)

    def get_user_status(self):
        """
        Get user status.
        :return:
            eg:{ "_id": 15,
                "username": "zhangsan",
                "email": "zhangsan@126.com",
                "up_time": 1688116008,
                "add_time": 1688116008,
                "role": "member",
                "type": "site",
                "study": false}
        """
        url = '/api/user/status'
        return self.get(url)

    def up_study(self):
        url = '/api/user/up_study'
        return self.get(url)

    def update_user(self, uid: int, username: str = None, email: str = None):
        """
        Update user info
        :param uid: user id
        :param username: username
        :param email: user email
        :return:
        """
        url = '/api/user/update'
        payload = {"uid": uid}
        if username is not None:
            payload['username'] = username
        if email is not None:
            payload['email'] = email
        return self.post(url, json=payload)

    def change_password(self, uid: int, old_password: str, password: str):
        """
        Change password.
        :param uid: user id
        :param old_password: user original password
        :param password: user new password
        :return:
        """
        url = '/api/user/change_password'
        payload = {"uid": uid, "password": password, "old_password": old_password}
        return self.post(url, json=payload)
