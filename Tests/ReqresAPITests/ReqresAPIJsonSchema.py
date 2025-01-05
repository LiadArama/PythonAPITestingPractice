import jsonschema

users_list_json_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"],
            },
        },
        "support": {
            "support": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "format": "uri"},
                    "text": {"type": "string"}
                },
                "required": ["url", "text"],
                "additionalProperties": False
            }
        },
        "additionalProperties": False
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
    "additionalProperties": False
}

single_user_jsonschema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"],
            "additionalProperties": False
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"],
            "additionalProperties": False
        }
    },
    "required": ["data", "support"],
    "additionalProperties": False
}
