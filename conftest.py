import pytest
import yaml

from src.logging.logger import logger, log_to_remote_server
from src.application import Application


def pytest_addoption(parser):
    parser.addoption("--env", default="qa")


@pytest.fixture(autouse=True)
def pretty_test_info(request):
    test_name = str(request.node.name)
    f_len = len(test_name) + 10
    logger.info('-' * f_len)
    logger.info(f'Started: {test_name}')
    logger.info('-' * f_len)
    yield
    logger.info('-' * f_len)
    logger.info(f'Finished: {test_name}')
    logger.info('-' * f_len)


@pytest.fixture(scope="session")
def env(request):
    environment = request.config.getoption("--env")
    logger.debug(f'The environment is {environment}')
    with open('config.yaml', 'r') as stream:
        return yaml.safe_load(stream).get(environment)


@pytest.fixture(scope="session")
def app(env):
    app = Application(env)
    yield app
    log_to_remote_server(env)
