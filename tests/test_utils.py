import json
import os
from typing import Generator

import pytest

from src.utils import load_transactions

TEST_FILE = "data/test_operations.json"


@pytest.fixture
def setup_test_file() -> Generator[None, None, None]:
    """Создаёт тестовый JSON-файл перед тестами и удаляет после"""
    data = [
        {
            "id": 1,
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD",
                    "name": "доллар"
                }
            },
            "date": "2025-02-10",
            "state": "completed",
            "to": '1',
            "from": "1",
            'description': 'Перевод'
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": -50,
                "currency": {
                    "code": "EUR",
                    "name": "евро"
                }
            },
            "date": "2025-02-09",
            "state": "pending",
            "to": '1',
            "from": "1",
            'description': 'Перевод'
        }
    ]

    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

    yield  # Запускаем тесты

    os.remove(TEST_FILE)  # Удаляем файл после тестов


def test_load_transactions_valid(setup_test_file: None) -> None:
    transactions = load_transactions(TEST_FILE)
    assert len(transactions) == 2
    assert transactions[0]["amount"] == 100


def test_load_transactions_empty() -> None:
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("")  # Записываем пустой файл

    transactions = load_transactions(TEST_FILE)
    assert transactions == []


def test_load_transactions_invalid() -> None:
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("not a json")  # Некорректный JSON

    transactions = load_transactions(TEST_FILE)
    assert transactions == []


def test_load_transactions_no_file() -> None:
    transactions = load_transactions("data/non_existent.json")
    assert transactions == []


@pytest.fixture(scope="session", autouse=True)
def cleanup() -> Generator[None, None, None]:
    yield  # Выполняем тесты

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
