from .base import ApiBase


class Follow(ApiBase):

    def add_follow(self, uid: int, projectid: int, projectname: str, icod: str, color: str):
        url = '/api/follow/add'

        payload = {"uid": 11, "projectid": 40, "projectname": "测试项目2", "icon": "code-o", "color": "blue"}
        return self.post(url, json=payload)
