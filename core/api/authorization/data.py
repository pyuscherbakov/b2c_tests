schema_with_success_auth = {
    "type": "object",
    "additionalProperties": False,
    "required": ["data"],
    "properties": {
        "data": {
            "type": "object",
            "additionalProperties": False,
            "required": ["token"],
            "properties": {"token": {"type": "string"}}
        }
    }
}

schema_with_not_success_auth = {
    "type": "object",
    "required": [
        "errors"
    ],
    "additionalProperties": True,
    "properties": {
        "errors": {
            "type": "array",
            "additionalItems": True
        }
    }
}