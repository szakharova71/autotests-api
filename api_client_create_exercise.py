from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
# Вместо CreateFileRequestDict импортируем CreateFileRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
# Вместо AuthenticationUserDict импортируем AuthenticationUserSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
# Вместо AuthenticationUserDict используем AuthenticationUserSchema
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client= get_exercises_client(authentication_user)

# Загружаем файл
# Вместо CreateFileRequestDict используем CreateFileRequestSchema
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем задание
create_exercise_request = CreateExerciseRequestSchema(
    title="Новое задание",
    course_id=create_course_response.course.id,
    max_score=50,
    min_score=5,
    order_index=1,
    description= "Описание нового задания",
    estimated_time="2 часа",
)
create_exercise_response=exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)