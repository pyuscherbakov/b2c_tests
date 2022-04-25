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
        "errors": {"type": "array", "items": {}}
    }
}

schema_get_status = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "errors"],
    "properties": {
        "status": {"type": "string"},
        "errors": {"type": "array", "items": {}}
    }
}

schema_get_agreement = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "premium", "serial", "number", "agreement_date", "terms", "valid_to",
                 "actions", "info", "errors"],
    "properties": {
        "status": {"type": "string"},
        "premium": {"type": "integer"},
        "serial": {"type": "null"},
        "number": {"type": "string"},
        "agreement_date": {"type": "string"},
        "terms": {
            "type": "object",
            "additionalProperties": False,
            "required": ["kasko"],
            "properties": {
                "kasko": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["bank", "end_date", "franchise", "start_date", "purchase_date",
                                 "start_exploitation_date"],
                    "properties": {
                        "bank": {"type": "string"},
                        "end_date": {"type": "string"},
                        "franchise": {"type": "string"},
                        "start_date": {"type": "string"},
                        "purchase_date": {"type": "string"},
                        "start_exploitation_date": {"type": "string"}
                    }
                }
            }
        },
        "valid_to": {"type": "string"},
        "actions": {"type": "array", "items": {}},
        "info": {"type": "array", "items": {}},
        "errors": {"type": "array", "items": {}}
    }
}

schema_documents = {
    "type": "array",
    "additionalItems": False,
    "properties": {
        "success": {"type": "boolean"},
        "messages": {"type": "string"},
        "name": {"type": "string"},
        "ext": {"type": "string"},
        "type": {"type": "string"},
        "content": {"type": "string"}
    }
}

schema_update_agreement = {
    "type": "object",
    "additionalProperties": False,
    "required": ["status", "errors"],
    "properties": {"status": {"type": "string"},
                   "errors": {"type": "array", "items": {}}}
}
