import allure
from jsonschema.validators import validate

from conftest import load_json_schema, api_request

project = 'reqres'
user_id = id = 2


def test_get_single_user():
    id = 2
    request = api_request(project, url=f'/users/{id}')

    with allure.step('Проверка: статус-код 200'):
        assert request.status_code == 200


def test_single_user_schema():
    schema = load_json_schema(project, 'get_single_user_schema.json')

    request = api_request(project, f'/users/{id}')

    with allure.step('Валидация схемы'):
        validate(request.json(), schema=schema)


def test_user_name():
    request = api_request(project, url=f'/users/{id}')

    with allure.step('Проверка id и эмейла пользователя'):
        assert int(request.json()['data']['id']) == id
        assert str(request.json()['data']['email']) == 'janet.weaver@reqres.in'
