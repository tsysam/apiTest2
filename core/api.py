import configparser
import requests
import os
from allure_commons._allure import step


class Api:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    parser = configparser.ConfigParser()
    parser.read(os.path.join(BASE_DIR, 'config.ini'))
    # parser.read(r'../config.ini')
    # parser.read('config.ini')
    # parser.read('..\\config.ini')

    BASE_URL = parser.get('backend', 'url')
    ENV = "/status"
    GET_URL = BASE_URL + ENV + "/200"

    @staticmethod
    def send_get():
        with step("Send get"):
            url = Api.GET_URL
            result = requests.get(url)
            return result
