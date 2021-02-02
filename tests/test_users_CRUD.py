import allure
import pytest

pytestmark = pytest.mark.CRUD


@allure.feature('Users')
@allure.suite('CRUD Users Tests')
@allure.title('Create a user')
@allure.description("""
1. Send request to create a user
2. Validate the status code - should be 201
3. Validate the response body - should correspond to 'user' schema
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_create_user(app):
    app.user.create(payload=app.data.user())
    app.user.validate_status(expected_code=201)
    app.validator.validate_json(schema_name='user', actual_json=app.user.body)


@allure.feature('Users')
@allure.suite('CRUD Users Tests')
@allure.title('Update a user')
@allure.description("""
1. Send request to create a test user
2. Validate the status code - should be 201
3. Send request to update the test user
4. Validate the status code - should be 200
5. Validate the response body - should correspond to 'user' schema
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_update_user(app):
    app.user.create(payload=app.data.user())
    app.user.validate_status(expected_code=201)
    app.user.update(user_id=app.user.body.get('data').get('id'), payload=app.data.user())
    app.user.validate_status(expected_code=200)
    app.validator.validate_json(schema_name='user', actual_json=app.user.body)


@allure.feature('Users')
@allure.suite('CRUD Users Tests')
@allure.title('Delete a user')
@allure.description("""
1. Send request to create a test user
2. Validate the status code - should be 201
3. Send request to delete the test user
4. Validate the status code - should be 204
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_delete_user(app):
    app.user.create(payload=app.data.user())
    app.user.validate_status(expected_code=201)
    app.user.delete(user_id=app.user.body.get('data').get('id'))
    app.user.validate_status(expected_code=204)
