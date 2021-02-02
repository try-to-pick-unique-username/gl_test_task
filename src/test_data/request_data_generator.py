from faker import Faker
from faker.providers import internet
from faker.providers import person

from src.test_data.model import User


class DataGenerator:
    """
    This class uses the Faker package to produce ready test dictionaries that are used in HTTP requests
    """

    def __init__(self):
        self.data = Faker()

    def fake_email(self):
        self.data.add_provider(internet)
        return self.data.email()

    def fake_name(self):
        self.data.add_provider(person)
        return self.data.name_male()

    def user(self):
        name = self.fake_name()
        email = self.fake_email()
        user = User(name, email)
        return user.__dict__
