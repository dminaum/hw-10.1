import os
from typing import Generator

import pytest

from src.decorators import log

LOG_FILE: str = "test_log.txt"


# Функции с декоратором
@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> float:
    return a / b


@log(filename=LOG_FILE)
def multiply(a: int, b: int) -> int:
    return a * b


@pytest.fixture(autouse=True)
def cleanup() -> Generator:
    """Удаляем лог-файл после каждого теста"""
    yield
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
        except PermissionError:
            pass  # Иногда Windows блокирует файл, просто пропускаем


def test_log_to_console_success(capsys: pytest.CaptureFixture) -> None:
    add(2, 3)
    captured = capsys.readouterr()
    assert "add ok" in captured.out.strip()


def test_log_to_console_error(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (5, 0), {}" in captured.err.strip()  # stderr!


def test_log_to_file_success() -> None:
    multiply(4, 5)
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()
    assert "multiply ok" in logs


def test_log_to_file_error() -> None:
    @log(filename=LOG_FILE)
    def faulty_func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        faulty_func()

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()

    assert "faulty_func error: ValueError. Inputs: (), {}" in logs
