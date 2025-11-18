import pytest

# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
