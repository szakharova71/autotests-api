from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
# Вместо CreateFileRequestDict импортируем CreateFileRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
# Вместо AuthenticationUserDict импортируем AuthenticationUserSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()

# Создаем пользователя
# Больше нет необходимости передавать значения, они будут генерировать автоматически
create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
# Вместо AuthenticationUserDict используем AuthenticationUserSchema
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
# Вместо CreateFileRequestDict используем CreateFileRequestSchema
# Автоматическая генерация данных, кроме необходимых параметров
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
# Используем сгенерированные значения для создания курса
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id, # Используем атрибуты вместо ключей
    created_by_user_id=create_user_response.user.id  # Используем атрибуты вместо ключей
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)