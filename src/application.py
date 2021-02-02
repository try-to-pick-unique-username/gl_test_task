from src.test_data.request_data_generator import DataGenerator
from src.validation.schema_validator import SchemaValidator
from src.http_requests.user_request import UserRequest


class Application:

    def __init__(self, env):
        self.env = env
        self.validator = SchemaValidator()
        self.data = DataGenerator()
        self.user = UserRequest(self)
