import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
        return True
    except ValueError as err:
        return False
