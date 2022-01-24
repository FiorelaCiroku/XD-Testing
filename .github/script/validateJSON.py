import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
        return "Success!"
    except ValueError as err:
        return "Error!"
