from unittest import mock

from codigo import hello_world


def test_hello_world():
    request_mock = mock.MagicMock()
    request_mock.get_json.return_value = {"data": "batata"}
    expected_result = ("ok", 200)
    result = hello_world(request_mock)
    assert result == expected_result


def test_not_batata_hello_world():
    request_mock = mock.MagicMock()
    request_mock.get_json.return_value = {"data": "a"}
    expected_result = ("Bad request - Not batata", 400)
    result = hello_world(request_mock)
    assert result == expected_result
