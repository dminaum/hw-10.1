import json
import os

import pytest

from src.utils import load_transactions

TEST_FILE = "data/test_operations.json"


@pytest.fixture
def setup_test_file():
    """Создаёт тестовый JSON-файл перед тестами и удаляет после"""
    data = [
        {"id": 1, "amount": 100, "currency": "USD", "date": "2025-02-10"},
        {"id": 2, "amount": -50, "currency": "EUR", "date": "2025-02-09"},
    ]
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

    yield  # Запускаем тесты

    os.remove(TEST_FILE)  # Удаляем файл после тестов


def test_load_transactions_valid(setup_test_file):
    transactions = load_transactions(TEST_FILE)
    assert len(transactions) == 2
    assert transactions[0]["amount"] == 100


def test_load_transactions_empty():
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("")  # Записываем пустой файл

    transactions = load_transactions(TEST_FILE)
    assert transactions == []


def test_load_transactions_invalid():
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("not a json")  # Некорректный JSON

    transactions = load_transactions(TEST_FILE)
    assert transactions == []


def test_load_transactions_no_file():
    transactions = load_transactions("data/non_existent.json")
    assert transactions == []


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    yield  # Выполняем тесты

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
