import pytest

from src.masks import get_mask_account, get_mask_card_number

data_cases: list[tuple[str, str]] = [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210987654", "9876 54** **** 7654"),
]


@pytest.mark.parametrize("card_number, expected", data_cases)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("123456789012", "**9012"),
    ],
)
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected
