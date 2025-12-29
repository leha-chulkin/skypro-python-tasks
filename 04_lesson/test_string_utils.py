import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# 1. Тесты для метода capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("", ""),  # пустая строка
])
def test_capitalize_positive(input_str: str, expected: str):
    assert string_utils.capitalize(input_str) == expected

def test_capitalize_none():
    with pytest.raises(TypeError):
        string_utils.capitalize(None)

def test_capitalize_non_string():
    with pytest.raises(TypeError):
        string_utils.capitalize(123)

# 2. Тесты для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   hello world", "hello world"),
    ("no_spaces", "no_spaces"),
    ("   ", ""),  # строка из одних пробелов
    ("", ""),    # пустая строка
])
def test_trim_positive(input_str: str, expected: str):
    assert string_utils.trim(input_str) == expected

def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

def test_trim_non_string():
    with pytest.raises(AttributeError):
        string_utils.trim(456)

# 3. Тесты для метода contains
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "z", False),
])
def test_contains_positive(string: str, symbol: str, expected: bool):
    assert string_utils.contains(string, symbol) == expected

def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")
    with pytest.raises(AttributeError):
        string_utils.contains("hello", None)

def test_contains_non_string():
    with pytest.raises(AttributeError):
        string_utils.contains(12345, "a")
    with pytest.raises(AttributeError):
        string_utils.contains("hello", 5)

# 4. Тесты для метода delete_symbol
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("delete all", "a", "delete ll"),
])
def test_delete_symbol_positive(string: str, symbol: str, expected: str):
    assert string_utils.delete_symbol(string, symbol) == expected

def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "k")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("SkyPro", None)

def test_delete_symbol_non_string():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(123, "k")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("SkyPro", 1)