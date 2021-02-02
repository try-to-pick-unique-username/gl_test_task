import logging.config
import os
import yaml
import datetime

from src.logging.ssh_client import SSHClientLogger

LOGGING_CONFIG_FILE = os.path.join('src', 'logging', 'logging_config.yaml')
LOG_FILE = os.path.join('src', 'logging', 'logs',
                        'log-' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.log')


def settings():
    with open(LOG_FILE, 'a'):
        with open(LOGGING_CONFIG_FILE, 'r') as stream:
            d = yaml.safe_load(stream)
            d['handlers']['file']['filename'] = LOG_FILE
    return d


logger = logging.getLogger()
logging.config.dictConfig(settings())


def log_exception(error_message):
    logger.exception(msg=error_message)
    return error_message


def log_to_remote_server(env):
    with SSHClientLogger(env) as sshclient:
        sshclient.copy_log(LOG_FILE)
