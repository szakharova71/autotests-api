from pydantic import BaseModel, Field


# Добавили суффикс Schema вместо Dict
class TokenSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")  # Использовали alias
    access_token: str = Field(alias="accessToken")  # Использовали alias
    refresh_token: str = Field(alias="refreshToken")  # Использовали alias


# Добавили суффикс Schema вместо Dict
class LoginRequestSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


# Добавили суффикс Schema вместо Dict
class LoginResponseSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


# Добавили суффикс Schema вместо Dict
class RefreshRequestSchema(BaseModel):  # Наследуем от BaseModel вместо TypedDict
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")  # Использовали alias