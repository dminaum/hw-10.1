import pytest
import os
import json
from unittest.mock import patch
from src.utils import load_transactions, get_transaction_amount_in_rubles
from src.external_api import convert_to_rubles

TEST_FILE = "test_operations.json"


@pytest.fixture
def setup_test_file():
    """Создаёт тестовый JSON-файл перед тестами и удаляет после"""
    data = [
        {"id": 1, "amount": 100, "currency": "USD", "date": "2025-02-10"},
        {"id": 2, "amount": -50, "currency": "EUR", "date": "2025-02-09"}
    ]
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

    yield  # Запускаем тесты

    os.remove(TEST_FILE)  # Удаляем файл после тестов


def test_load_transactions(setup_test_file):
    transactions = load_transactions(TEST_FILE)
    assert isinstance(transactions, list)
    assert len(transactions) == 2
    assert transactions[0]["amount"] == 100
    assert transactions[1]["currency"] == "EUR"


def test_load_transactions_file_not_found():
    assert load_transactions("nonexistent.json") == []


def test_load_transactions_invalid_file():
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write("INVALID JSON")

    assert load_transactions(TEST_FILE) == []


@pytest.mark.parametrize("amount, currency, expected", [
    (100, "USD", 7500.0),  # 1 USD = 75 RUB
    (50, "EUR", 5000.0),  # 1 EUR = 100 RUB
    (1000, "RUB", 1000.0)  # RUB остаётся RUB
])
@patch("src.external_api.requests.get")
def test_convert_to_rubles(mock_get, amount, currency, expected):
    mock_get.return_value.json.return_value = {"result": expected}
    mock_get.return_value.raise_for_status = lambda: None  # Подавляем ошибки

    result = convert_to_rubles(amount, currency)
    assert result == expected


@patch("src.external_api.convert_to_rubles", return_value=7500.0)
def test_get_transaction_amount_in_rubles(mock_convert):
    transaction = {"amount": 100, "currency": "USD"}
    assert get_transaction_amount_in_rubles(transaction) == 7500.0
