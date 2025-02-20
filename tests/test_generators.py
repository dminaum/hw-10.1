import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_with_valid_data():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["description"] == "Transaction 1"
    assert result[1]["description"] == "Transaction 3"


def test_filter_by_currency_with_no_matching_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_empty_list():
    transactions = []
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_missing_keys():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"description": "Transaction without currency"}
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0].get("description") is None


def test_transaction_descriptions_with_valid_data():
    transactions = [
        {"description": "Description 1"},
        {"description": "Description 2"},
        {"description": "Description 3"}
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 3
    assert result[0] == "Description 1"
    assert result[1] == "Description 2"
    assert result[2] == "Description 3"


def test_transaction_descriptions_with_no_descriptions():
    transactions = [
        {"description": "Description 1"},
        {},
        {"description": "Description 2"}
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 2
    assert result[0] == "Description 1"
    assert result[1] == "Description 2"


def test_transaction_descriptions_with_empty_list():
    transactions = []
    result = list(transaction_descriptions(transactions))
    assert len(result) == 0


@pytest.mark.parametrize("start, stop, expected_output", [
    (1000000000000000, 1000000000000002, [
        "1000 0000 0000 0000", "1000 0000 0000 0001", "1000 0000 0000 0002"
    ]),
    (9999999999999999, 1000000000000000, ["1000 0000 0000 0000"]),
    (5000000000000000, 5000000000000002, [
        "5000 0000 0000 0000", "5000 0000 0000 0001", "5000 0000 0000 0002"
    ]),
])
def test_card_number_generator(start, stop, expected_output):
    result = list(card_number_generator(start, stop))
    assert result == expected_output


def test_card_number_generator_with_single_value():
    result = list(card_number_generator(1000000000000000, 1000000000000000))
    assert result == ["1000 0000 0000 0000"]


def test_card_number_generator_with_empty_range():
    result = list(card_number_generator(1000000000000000, 999999999999999))
    assert result == []


def test_card_number_generator_with_invalid_range():
    result = list(card_number_generator(1000000000000000, 999999999999))
    assert result == []
