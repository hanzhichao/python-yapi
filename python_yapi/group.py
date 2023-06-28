from python_yapi.base import ApiBase


class GroupMixIn(ApiBase):
    def get_group(self, group_id: int=11):
        url = 'api/group/get'
        params = {'id': group_id}
        return self.get(url, params=params)
