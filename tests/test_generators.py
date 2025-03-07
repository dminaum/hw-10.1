from typing import Any

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency_with_valid_data() -> None:
    transactions: list[dict[str, Any]] = [
        {
            "id": 1,
            "amount": 100,
            "currency_code": "USD",
            "currency_name": "доллар",
            "date": "2025-02-10",
            "state": "completed",
            "to": "1",
            "from": "1",
            "description": "Оплата услуг",
        },
        {
            "id": 2,
            "amount": 200,
            "currency_code": "EUR",
            "currency_name": "евро",
            "date": "2025-02-09",
            "state": "pending",
            "to": "2",
            "from": "1",
            "description": "Перевод средств",
        },
        {
            "id": 3,
            "amount": 150,
            "currency_code": "USD",
            "currency_name": "доллар",
            "date": "2025-02-08",
            "state": "completed",
            "to": "3",
            "from": "1",
            "description": "Покупка товара",
        },
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["description"] == "Оплата услуг"
    assert result[1]["description"] == "Покупка товара"


def test_filter_by_currency_with_no_matching_currency() -> None:
    transactions: list[dict[str, Any]] = [
        {
            "id": 4,
            "amount": 300,
            "currency_code": "EUR",
            "currency_name": "евро",
            "date": "2025-02-07",
            "state": "completed",
            "to": "4",
            "from": "1",
            "description": "Оплата подписки",
        },
        {
            "id": 5,
            "amount": 250,
            "currency_code": "EUR",
            "currency_name": "евро",
            "date": "2025-02-06",
            "state": "pending",
            "to": "5",
            "from": "1",
            "description": "Оплата аренды",
        },
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_empty_list() -> None:
    transactions: list[dict[str, Any]] = []
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_with_missing_keys() -> None:
    transactions: list[dict[str, Any]] = [
        {
            "id": 6,
            "amount": 400,
            "currency_code": "USD",
            "currency_name": "доллар",
            "date": "2025-02-05",
            "state": "completed",
            "to": "6",
            "from": "1",
        },
        {
            "id": 7,
            "amount": 350,
            "currency_code": "EUR",
            "currency_name": "евро",
            "date": "2025-02-04",
            "state": "pending",
            "to": "7",
            "from": "1",
        },
        {
            "id": 8,
            "amount": 500,
            "date": "2025-02-03",
            "state": "completed",
            "to": "8",
            "from": "1",
            "description": "Неизвестная операция",
        },
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0].get("description") is None


def test_transaction_descriptions_with_valid_data() -> None:
    transactions: list[dict[str, Any]] = [
        {"id": 9, "description": "Зачисление зарплаты"},
        {"id": 10, "description": "Оплата интернета"},
        {"id": 11, "description": "Перевод другу"},
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 3
    assert result[0] == "Зачисление зарплаты"
    assert result[1] == "Оплата интернета"
    assert result[2] == "Перевод другу"


def test_transaction_descriptions_with_no_descriptions() -> None:
    transactions: list[dict[str, Any]] = [
        {"id": 12, "description": "Покупка в магазине"},
        {"id": 13},
        {"id": 14, "description": "Оплата коммунальных услуг"},
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 2
    assert result[0] == "Покупка в магазине"
    assert result[1] == "Оплата коммунальных услуг"


def test_transaction_descriptions_with_empty_list() -> None:
    transactions: list[dict[str, Any]] = []
    result = list(transaction_descriptions(transactions))
    assert len(result) == 0
