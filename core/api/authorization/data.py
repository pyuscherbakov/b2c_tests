schema = {
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