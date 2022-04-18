from core.api.authorization.data import schema
from core.api.endpoints import AUTH
from jsonschema import validate
import settings
import pytest


class TestAuth:
    def test_get_token(self, test_api):
        user = settings.default_user
        response = test_api.post(AUTH, verify=False, json={"email": user[0], "password": user[1]})
        assert response.status_code == 200

    def test_check_validate_response_json_schema(self, test_api):
        user = settings.default_user
        response = test_api.post(AUTH, verify=False, json={"email": user[0], "password": user[1]})
        validate(response.json(), schema)
