from python_yapi.base_api import BaseApi


class Group(BaseApi):
    def get_group(self, group_id: int=11):
        url = 'api/group/get'
        params = {'id': group_id}
        res = self.get(url, params=params)
        return res.json()