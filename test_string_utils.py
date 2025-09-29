import pytest
import os
from string_utils import get_string_length, save_string_to_file, DatabaseManager

# Тесты для метода получения длины строки
class TestGetStringLength:
    def test_empty_string(self):
        assert get_string_length("") == 0

    def test_multiline_string(self):
        text = """Line 1
        Line 2
        Line 3"""
        assert get_string_length(text) == 33

    def test_spaces_string(self):
        assert get_string_length("   ") == 3

    def test_unicode_string(self):
        assert get_string_length("Привет") == 6

# Тесты для метода сохранения в файл
class TestSaveToFile:
    def test_save_string(self, tmp_path):
        test_file = tmp_path / "test.txt"
        save_string_to_file("Hello World", str(test_file))
        with open(test_file, 'r') as f:
            assert f.read() == "Hello World"

    def test_save_empty_string(self, tmp_path):
        test_file = tmp_path / "test.txt"
        save_string_to_file("", str(test_file))
        with open(test_file, 'r') as f:
            assert f.read() == ""

# Фикстура для работы с БД
@pytest.fixture
def db_manager():
    manager = DatabaseManager()
    connection = manager.connect()
    yield connection
    manager.disconnect()
    if os.path.exists("test.db"):
        os.remove("test.db")

# Тесты для работы с БД
class TestDatabase:
    def test_create_table(self, db_manager):
        cursor = db_manager.cursor()
        cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
        cursor.execute("INSERT INTO test VALUES (1, 'John')")
        db_manager.commit()
        
        cursor.execute("SELECT * FROM test")
        results = cursor.fetchall()
        assert len(results) == 1
        assert results[0] == (1, 'John')

    def test_empty_database(self, db_manager):
        cursor = db_manager.cursor()
        cursor.execute("CREATE TABLE test (id INTEGER)")
        cursor.execute("SELECT * FROM test")
        assert len(cursor.fetchall()) == 0