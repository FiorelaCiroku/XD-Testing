import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
        validation = validateJSON(jsonData)
        return validation
    except ValueError as err:
        return False
