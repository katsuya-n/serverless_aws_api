import health_check
import json

def test_main():
    response = health_check.main("", "")
    expect = {
        "statusCode": 200,
        "body": json.dumps(
            {"status" : "OK"}
        )
    }

    assert response == expect