import allure
import requests
import yaml
import os

from src.logging.logger import logger, log_exception


class BaseRequest:
    __endpoints_path = os.path.join('src', 'http_requests', 'endpoints.yaml')

    def __init__(self, app):
        self.app = app
        self.endpoints = self.endpoints()
        self.status_code = None
        self.body = None

    @property
    def baseuri(self):
        return self.app.env.get('host') + self.endpoints.get('base')

    def endpoints(self):
        with open(self.__endpoints_path, 'r') as stream:
            return yaml.safe_load(stream)

    def headers(self):
        token = self.app.env.get('token')
        return {
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }

    def send_request(self, method, url, status_ok_check=True, **kwargs):
        logger.debug(f'Request data: method={method}, url={url}, headers={self.headers()}')
        r = requests.request(method=method.upper(), url=url, headers=self.headers(), **kwargs)
        if status_ok_check:
            logger.debug('Checking if status code is OK')
            assert r.status_code == requests.codes.ok, \
                log_exception(f'The request failed with {r.status_code} status code')
        self.body = r.json()
        self.status_code = self.body.get('code')
        allure.attach(r.content)

    @allure.step('Validating response status code; expected - {expected_code}')
    def validate_status(self, expected_code: int):
        logger.info(f'Validating response status code; expected - {expected_code}')
        assert expected_code == self.status_code, \
            log_exception(f'Got {self.status_code} status code in response')
