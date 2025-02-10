import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-06-21T10:15:30.000000", "21.06.2023"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
