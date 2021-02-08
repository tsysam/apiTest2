from core.api_uis import Api


def test_get_ping():
    response = Api.send_get_ping()
    assert response.status_code == 200
