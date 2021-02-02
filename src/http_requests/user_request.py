import allure

from src.http_requests.base_request import BaseRequest
from src.logging.logger import logger


class UserRequest(BaseRequest):

    def __init__(self, app):
        super(UserRequest, self).__init__(app)

    @property
    def uri(self):
        return self.baseuri + self.endpoints.get('users')

    @allure.step('Sending the request to create a user')
    def create(self, payload):
        logger.info('Sending the request to create a user')
        self.send_request(method='post', url=self.uri, json=payload)

    @allure.step('Sending request to get the user with ID={user_id}')
    def get(self, user_id):
        logger.info(f'Sending request to get the user with ID={user_id}')
        url = self.uri + f'/{user_id}'
        self.send_request(method='get', url=url)

    @allure.step('Sending request to update the user with ID={user_id}')
    def update(self, user_id, payload):
        logger.info(f'Sending request to update the user with ID={user_id}')
        url = self.uri + f'/{user_id}'
        self.send_request(method='put', url=url, json=payload)

    @allure.step('Sending request to delete the user with ID={user_id}')
    def delete(self, user_id):
        logger.info(f'Sending request to delete the user with ID={user_id}')
        url = self.uri + f'/{user_id}'
        self.send_request(method='delete', url=url)
