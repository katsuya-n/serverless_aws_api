import json

def main(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps(
            {"status" : "OK"}
        )
    }
    return response