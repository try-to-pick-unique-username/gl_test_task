import os
import json
import allure
from jsonschema import validate
from jsonschema import exceptions

from src.logging.logger import logger, log_exception


class SchemaValidator:
    """
        This class reads all schemas in the src/validation/schema folder,
        and then validates the chosen schema against the given JSON
    """
    __schema_path = os.path.join('src', 'validation', 'schema')

    @allure.step('Validating actual response body against the schema {schema_name}')
    def validate_json(self, schema_name, actual_json):
        logger.info(f'Starting to validate actual response body against the schema {schema_name}')
        schema_path = os.path.join(self.__schema_path, schema_name)
        try:
            with open(schema_path, 'r') as f:
                schema = json.loads(f.read())
                validate(actual_json, schema)
            logger.info('Done. The JSON is OK')
        except exceptions.ValidationError as err:
            message = err.args[0]
            log_exception('Failed validating the JSON: ' + message)
            raise AssertionError('JSON schema validation failed. See log for details.')
