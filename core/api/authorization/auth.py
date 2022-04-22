from core.api.endpoints import AUTH
import settings
import allure
import requests


class Token:
    token = None

    @staticmethod
    @allure.step("Получить токен")
    def _get_token():
        url = settings.base_url + AUTH
        user = settings.default_user
        r = requests.post(url, verify=False, json={"email": user[0], "password": user[1]})
        return r.json()["data"]["token"]

    @staticmethod
    def get_token():
        if not Token.token:
            Token.token = Token._get_token()
        return Token.token
