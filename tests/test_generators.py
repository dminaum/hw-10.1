from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_with_valid_data() -> None:
    transactions: list[dict[str, Any]] = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["description"] == "Transaction 1"
    assert result[1]["description"] == "Transaction 3"


def test_filter_by_currency_with_no_matching_currency() -> None:
    transactions: list[dict[str, Any]] = [
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_empty_list() -> None:
    transactions: list[dict[str, Any]] = []
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_missing_keys() -> None:
    transactions: list[dict[str, Any]] = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"description": "Transaction without currency"},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0].get("description") is None


def test_transaction_descriptions_with_valid_data() -> None:
    transactions: list[dict[str, Any]] = [
        {"description": "Description 1"},
        {"description": "Description 2"},
        {"description": "Description 3"},
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 3
    assert result[0] == "Description 1"
    assert result[1] == "Description 2"
    assert result[2] == "Description 3"


def test_transaction_descriptions_with_no_descriptions() -> None:
    transactions: list[dict[str, Any]] = [{"description": "Description 1"}, {}, {"description": "Description 2"}]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 2
    assert result[0] == "Description 1"
    assert result[1] == "Description 2"


def test_transaction_descriptions_with_empty_list() -> None:
    transactions: list[dict[str, Any]] = []
    result = list(transaction_descriptions(transactions))
    assert len(result) == 0


@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (1000000000000000, 1000000000000002, ["1000 0000 0000 0000", "1000 0000 0000 0001", "1000 0000 0000 0002"]),
        (9999999999999999, 1000000000000000, []),  # Ожидаем пустой список
        (5000000000000000, 5000000000000002, ["5000 0000 0000 0000", "5000 0000 0000 0001", "5000 0000 0000 0002"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_output: list[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected_output


def test_card_number_generator_with_single_value() -> None:
    result = list(card_number_generator(1000000000000000, 1000000000000000))
    assert result == ["1000 0000 0000 0000"]


def test_card_number_generator_with_empty_range() -> None:
    result = list(card_number_generator(1000000000000000, 999999999999999))
    assert result == []


def test_card_number_generator_with_invalid_range() -> None:
    result = list(card_number_generator(1000000000000000, 999999999999))
    assert result == []
