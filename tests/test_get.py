import requests
from core.api import Api


def test_simple_get():
    response = requests.get('https://httpbin.org/get')
    assert response.status_code == 200


def test_simple_get2():
    response = Api.send_get()
    assert response.status_code == 200
