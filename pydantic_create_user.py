from pydantic import BaseModel, Field, SecretStr, EmailStr
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: SecretStr ="12345678"
    last_name: str = Field(alias="lastName", default="Иванов")
    first_name: str = Field(alias="firstName", default="Иван")
    middle_name: str = Field(alias="middleName", default="Иванович")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


