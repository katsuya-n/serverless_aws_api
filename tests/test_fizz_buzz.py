import fizz_buzz
import json
import pytest

@pytest.mark.parametrize(
    "test_input, expected_result", [
    ("1", 1),
    ("2", 2),
    ("3", "fizz"),
    ("4", 4),
    ("5", "buzz"),
    ("6", "fizz"),
    ("7", 7),
    ("8", 8),
    ("9", "fizz"),
    ("10", "buzz"),
    ("15", "fizz buzz"),
    ("20", "buzz"),
    ("30", "fizz buzz"),
    ("45", "fizz buzz"),
])
def test_main_fizzbuzz_success(test_input, expected_result):
    expect = {
        "statusCode": 200,
        "body": json.dumps(
            {"result" : expected_result}
        )
    }

    api_gateway_event = {
        "queryStringParameters": {"input": test_input},
    }
    response = fizz_buzz.main(api_gateway_event, "")
    assert response == expect

def test_main_fizzbuzz_error():
    expect = {
        "statusCode": 500,
        "body": json.dumps(
            {"result" : "input error"}
        )
    }

    api_gateway_event = {
        "queryStringParameters": {"input": "dummy_string"},
    }
    response = fizz_buzz.main(api_gateway_event, "")
    assert response == expect