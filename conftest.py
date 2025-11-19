pytest_plugins = (
    "fixtures.users",
    "fixtures.files",  # Добавляем фикстуры для работы с файлами
    "fixtures.courses",  # Добавляем фикстуры для работы с vbкурсами
    "fixtures.exercises",  # Добавляем фикстуры для работы с заданиями
    "fixtures.authentication"
)