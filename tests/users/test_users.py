from http import HTTPStatus
# Импортируем библиотеку pytest
import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture  # Заменяем импорт
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient): # Используем фикстуру API клиента
        # Удалили инициализацию API клиента из теста
        # Формируем фейковый email с параметризованным доменом
        email=fake.email(domain=domain)
        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(email=email)
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Используем функцию для проверки ответа создания юзера
        assert_create_user_response(request, response_data)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_get_user_me(self, function_user: UserFixture, # Используем фикстуру для создания пользователя
                         private_users_client: PrivateUsersClient):

        # Отправляем get запрос на получение пользователя
        response = private_users_client.get_user_me_api()
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Используем функцию для проверки ответа создания юзера
        assert_get_user_response(response_data, function_user.response)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
