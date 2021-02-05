import configparser
import requests
from allure_commons._allure import step


class Api:
    parser = configparser.ConfigParser()
    parser.read('../config.ini')
    # parser.read('config.ini')
    # parser.read('..\\config.ini')

    BASE_URL = parser.get('backend', 'url')
    GET_URL = BASE_URL + r'/get'

    @staticmethod
    def send_get():
        with step("Send get"):
            url = Api.GET_URL
            result = requests.get(url)
            return result
