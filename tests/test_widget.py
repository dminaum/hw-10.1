import pytest
from datetime import datetime
from src.widget import mask_account_card, get_date, format_date


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ],
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


# Тесты для get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", datetime(2024, 3, 11, 0, 0, 0, 0)),
        ("2023-06-21T10:15:30.000000", datetime(2023, 6, 21, 0, 0, 0, 0)),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


# Тесты для format_date
@pytest.mark.parametrize(
    "date_obj, expected",
    [
        (datetime(2024, 3, 11, 0, 0, 0, 0), "11.03.2024"),
        (datetime(2023, 6, 21, 0, 0, 0, 0), "21.06.2023"),
    ],
)
def test_format_date(date_obj, expected):
    assert format_date(date_obj) == expected
