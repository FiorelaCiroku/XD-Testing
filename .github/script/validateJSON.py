import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

validation = validateJSON(jsonData)
print(validation)
