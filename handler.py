import json

def fizz_buzz(event, context):
    if 'input' not in event.keys():
        response = {
            "statusCode": 500,
            "result": "input error"
        }
        return response
    else:
        input = event['input']
        if input == 15:
            response = {
                "statusCode": 200,
                "result": "fizz bizz"
            }
            return response
        elif input == 3:
            response = {
            "statusCode": 200,
            "result": "fizz"
            }
            return response
        elif input == 5:
            response = {
            "statusCode": 200,
            "result": "buzz"
            }
            return response
        else:
            response = {
                "statusCode": 500,
                "result": "input error"
            }
            return response
