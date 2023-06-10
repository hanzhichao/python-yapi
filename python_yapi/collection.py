from python_yapi.base_api import BaseApi


class Collection(BaseApi):
    def add_collection(self, name: str, desc: str, project_id: int):
        url = '/api/col/add_col'
        payload = {"name": name, "desc": desc, "project_id": str(project_id)}
