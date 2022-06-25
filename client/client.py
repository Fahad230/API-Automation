from config import SESSION


class RequestClient:
    def get_req(self, url, json=None, headers=None):
        response = SESSION.get(url, json=json, headers=headers)
        return response

    def post_req(self, url, json=None, headers=None):
        response = SESSION.post(url, json=json, headers=headers)
        return response
