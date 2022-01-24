import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
        print("Success!")
    except ValueError as err:
        print("Error!")
