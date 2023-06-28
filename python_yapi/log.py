class LogMixIn:
    def get_log_list(self, typeid: int = 11, type: str = 'group', page: int = 1, limit: int = 10):
        url = '/api/log/list?typeid=11&type=group&page=1&limit=10'
        params = {'typeid': typeid, 'type': type, 'page': page, 'limit': limit}
        return self.post(url, params=params)
