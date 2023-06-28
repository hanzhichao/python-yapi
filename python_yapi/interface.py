from python_yapi.base import ApiBase


class InterfaceMixIn(ApiBase):
    def add_interface(self, method: str, catid: int, title: str, path: str, project_id: int):
        url = '/api/interface/add'
        payload = {"method": method, "catid": str(catid), "title": title, "path": path, "project_id": project_id}
        return self.post(url, json=payload)

    def add_category(self, name: str, desc: str, project_id: int):
        url = '/api/interface/add_cat'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
        return self.post(url, json=payload)

    def update_interface(self):
        url = 'api/interface/up'
        payload = {"id": "11", "status": "done"}
        return self.post(url, json=payload)
