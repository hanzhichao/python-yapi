from python_yapi.base_api import BaseApi


class Interface(BaseApi):
    def add(self, method: str, catid: int, title: str, path: str, project_id: int):
        url = '/api/interface/add'
        payload = {"method": method, "catid": str(catid), "title": title, "path": path, "project_id": project_id}
        res = self.post(url, json=payload)
        return res.json()

    def add_category(self, name: str, desc: str, project_id: int):
        url = '/api/interface/add_cat'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
        res = self.post(url, json=payload)
        return res.json()

    def update(self):
        url = 'api/interface/up'
        payload = {"id":"11","status":"done"}
        res = self.post(url, json=payload)
        return res.json()
