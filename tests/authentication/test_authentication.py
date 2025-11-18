from http import HTTPStatus
import pytest
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.authentication.authentication_client import AuthenticationClient
from fixtures.users import UserFixture  # Заменяем импорт

from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
class TestAuthentication:
    def test_login(self, function_user: UserFixture,  # Используем фикстуру для создания пользователя
                   authentication_client: AuthenticationClient):
        # Удалили инициализацию API клиентов из теста
        #Удалили запрос на создание пользователя

        # Запрос на логин (login_request -> request)
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        # Выполняем логин (login_response -> response)
        response = authentication_client.login_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        # Валидация ответа (login_response_data -> response_data)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # Используем функцию для проверки статус-кода
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Используем функцию для проверки ответа логина
        assert_login_response(response_data)

        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


