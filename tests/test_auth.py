from core.api.authorization import get_token
from core.api.authorization.data import schema
from jsonschema import validate


class TestAuth:
    def test_get_token(self):
        r = get_token()
        assert r.status_code == 200

    def test_check_validate_response_json_schema(self):
        r = get_token()
        validate(r.json(), schema)
