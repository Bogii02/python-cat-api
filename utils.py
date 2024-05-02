from flask import jsonify


def create_error_message(cause, error):
    payload = {
        "error": {
            "cause": cause,
            "description": str(error)
        }
    }
    payload_string = jsonify(payload)
    return payload_string
