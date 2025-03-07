import json
import os
from typing import Generator
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_to_rubles
from src.utils import get_transaction_amount_in_rubles, load_transactions

TEST_FILE = "test_operations.json"


@pytest.fixture
def setup_test_file() -> Generator[None, None, None]:
    """Создаёт тестовый JSON-файл перед тестами и удаляет после"""
    data = [
        {
            "id": 1,
            "operationAmount": {"amount": 100, "currency": {"code": "USD", "name": "доллар"}},
            "date": "2025-02-10",
            "state": "completed",
            "to": "1",
            "from": "1",
            "description": "Перевод",
        },
        {
            "id": 2,
            "operationAmount": {"amount": -50, "currency": {"code": "EUR", "name": "евро"}},
            "date": "2025-02-09",
            "state": "pending",
            "to": "1",
            "from": "1",
            "description": "Перевод",
        },
    ]

    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

    yield  # Запускаем тесты

    os.remove(TEST_FILE)  # Удаляем файл после тестов


def test_load_transactions(setup_test_file: None) -> None:
    transactions = load_transactions(TEST_FILE)
    assert isinstance(transactions, list)
    assert len(transactions) == 2
    assert transactions[0]["amount"] == 100
    assert transactions[1]["currency_code"] == "EUR"


def test_load_transactions_file_not_found() -> None:
    assert load_transactions("nonexistent.json") == []


def test_load_transactions_invalid_file() -> None:
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("INVALID JSON")

    assert load_transactions(TEST_FILE) == []


@pytest.mark.parametrize(
    "amount, currency, expected",
    [
        (100, "USD", 7500.0),  # 1 USD = 75 RUB
        (50, "EUR", 5000.0),  # 1 EUR = 100 RUB
        (1000, "RUB", 1000.0),  # RUB остаётся RUB
    ],
)
@patch("src.external_api.requests.get")
def test_convert_to_rubles(mock_get: MagicMock, amount: int, currency: str, expected: float) -> None:
    mock_get.return_value.json.return_value = {"result": expected}
    mock_get.return_value.raise_for_status = lambda: None  # Подавляем ошибки

    result = convert_to_rubles(amount, currency)
    assert result == expected


@patch("src.utils.convert_to_rubles", return_value=7500.0)
def test_get_transaction_amount_in_rubles(mock_convert: MagicMock) -> None:
    transaction = {"id": 2, "amount": 100, "currency_code": "USD", "date": "2025-02-09", "state": "pending"}
    assert get_transaction_amount_in_rubles(transaction) == 7500.0
