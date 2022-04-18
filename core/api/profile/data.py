schema = {
    "type": "object",
    "additionalProperties": False,
    "required": ["email", "insurance_products"],
    "properties": {
        "email": {
            "type": "string"
        },
        "insurance_products": {
            "type": "array",
            "additionalProperties": False,
            "items": {
                "anyOf": [
                    {
                        "type": "object",
                        "additionalItems": False,
                        "required": ["id", "name", "company"],
                        "properties": {
                            "id": {"type": "string"},
                            "name": {"type": "string"},
                            "company": {"type": "string"}
                        }
                    }
                ]
            }
        }
    }
}

