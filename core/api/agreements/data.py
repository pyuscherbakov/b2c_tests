body_create_agreement = {
    "contract_id": "",
    "product_id": ""
}

schema_with_not_success = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "errors"],
    "properties": {
        "status": {"type": "string"},
        "errors": {"type": "array", "items": {}}
    }
}

schema_with_success = {
    "type": "object",
    "additionalProperties": False,
    "required": ["id"],
    "properties": {"id": {"type": "string"}}
}

schema_issue_agreement = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "errors"],
    "properties": {
        "status": {"type": "string"},
        "errors": {"type": "array","items": {}}
    }
}

schema_get_status = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "errors"],
    "properties": {
        "status": {"type": "string"},
        "errors": {"type": "array","items": {}}
    }
}