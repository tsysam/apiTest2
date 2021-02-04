import requests

r = requests.get('https://httpbin.org/get')
print(r.status_code)


def test_simple_get():
    response = requests.get('https://httpbin.org/get')
    assert response.status_code == 200
