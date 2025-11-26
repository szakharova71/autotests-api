from functools import lru_cache  # Импортируем функцию для кеширования

from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
# Импортируем модель LoginRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema

from clients.event_hooks import curl_event_hook  # Импортируем event hook


# Добавили суффикс Schema вместо Dict
class AuthenticationUserSchema(BaseModel, frozen=True):  # Наследуем от BaseModel вместо TypedDict
    email: str
    password: str


# Создаем private builder
@lru_cache(maxsize=None)  # Кешируем возвращаемое значение
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    # Используем модель LoginRequestSchema
    # Значения теперь извлекаем не по ключу, а через атрибуты
    login_request = LoginRequestSchema(email=user.email, password=user.password)

    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        # Значения теперь извлекаем не по ключу, а через атрибуты
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}  # Добавляем event hook для запроса
    )