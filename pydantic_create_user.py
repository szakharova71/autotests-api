from pydantic import BaseModel, Field, SecretStr

from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str  # намеренно аннотируем как str, чтобы тестировать негативные кейсы
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str = Field(default_factory=get_random_email)
    password: SecretStr ="12345678"
    last_name: str = Field(alias="lastName", default="Иванов")
    first_name: str = Field(alias="firstName", default="Иван")
    middle_name: str = Field(alias="middleName", default="Иванович")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


