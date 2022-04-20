from core.api.endpoints import AUTH
from core.utils.api_client import *
import settings
import allure


class Token:
    base_url = ApiClient(settings.base_url)

    @staticmethod
    @allure.step("Получить токен")
    def get_token():
        url = settings.base_url + AUTH
        user = settings.default_user
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        return r.json()["data"]["token"]

