import requests
from core.api.endpoints import AUTH
import settings


class Token:
    @staticmethod
    def get_token():
        url = settings.base_url + AUTH
        user = settings.default_user
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        return r

