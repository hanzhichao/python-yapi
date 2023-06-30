from python_yapi.base import ApiBase


class GroupMixIn(ApiBase):
    def get_group(self, group_id: int = 11):
        url = 'api/group/get'
        params = {'id': group_id}
        return self.get(url, params=params)

    def get_my_group(self):
        """
        Get my default group
        :return:
            eg: {
                "errcode": 0,
                "errmsg": "成功！",
                "data": {
                    "custom_field1": {
                        "enable": false
                    },
                    "type": "private",
                    "_id": 11,
                    "group_name": "User-11",
                    "add_time": 1686400822,
                    "up_time": 1686400822
                }
            }
        """
        url = '/api/group/get_mygroup'
        return self.get(url)

    def get_my_group_id(self)->int:
        return self.get_my_group()['_id']

    def add_group(self, group_name: str, group_desc: str, owner_uids: list[str]):
        """
        Adds a new group

        :param group_name: Group name
        :param group_desc: Group description
        :param owner_uids: Group owner IDs
        :return:
        """
        url = '/api/group/add'
        payload = {"group_name": group_name, "group_desc": group_desc, "owner_uids": owner_uids}
        return self.post(url, json=payload)
