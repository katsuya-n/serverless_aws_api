import json

def main(event, context):
    input = event["queryStringParameters"]['input']
    if input.isdigit():
        input = int(input)
    else:
        response = {
            "statusCode": 500,
            "body": json.dumps(
                {"result" : "input error"}
            )
        }
        return response

    if input % 15 == 0:
        response = {
            "statusCode": 200,
            "body": json.dumps(
                {"result" : "fizz buzz"}
            )
        }
        return response
    elif input % 3 == 0:
        response = {
            "statusCode": 200,
            "body": json.dumps(
                {"result" : "fizz"}
           )
        }
        return response
    elif input % 5 == 0:
        response = {
            "statusCode": 200,
            "body": json.dumps(
                {"result" : "buzz"}
            )
        }
        return response
    else:
        response = {
            "statusCode": 200,
            "body": json.dumps(
                {"result" : input}
            )
        }
        return response