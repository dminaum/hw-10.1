import pytest
import os
from src.decorators import log

LOG_FILE = "test_log.txt"


# Функции с декоратором
@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b


@log(filename=LOG_FILE)
def multiply(a, b):
    return a * b


@pytest.fixture(autouse=True)
def cleanup():
    """Удаляем лог-файл после каждого теста"""
    yield
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
        except PermissionError:
            pass  # Иногда Windows блокирует файл, просто пропускаем


def test_log_to_console_success(capsys):
    add(2, 3)
    captured = capsys.readouterr()
    assert "add ok" in captured.out.strip()


def test_log_to_console_error(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (5, 0), {}" in captured.err.strip()  # stderr!


def test_log_to_file_success():
    multiply(4, 5)
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()
    assert "multiply ok" in logs


def test_log_to_file_error():
    @log(filename=LOG_FILE)
    def faulty_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        faulty_func()

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()

    assert "faulty_func error: ValueError. Inputs: (), {}" in logs
