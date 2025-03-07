from io import StringIO
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd
import pytest

from src.read_dataframes import read_csv, read_xlsx  # Импортируем функции


@pytest.fixture
def csv_data() -> str:
    return """id;state;date;amount;currency_name;currency_code;from;to;description
1;completed;2024-06-10;1000;USD;840;Alice;Bob;Payment for services
2;pending;2024-06-11;500;EUR;978;Charlie;David;Freelance job
"""


@pytest.fixture
def xlsx_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "id": "1",
                "state": "completed",
                "date": "2024-06-10",
                "amount": "1000",
                "currency_name": "USD",
                "currency_code": "840",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment for services",
            },
            {
                "id": "2",
                "state": "pending",
                "date": "2024-06-11",
                "amount": "500",
                "currency_name": "EUR",
                "currency_code": "978",
                "from": "Charlie",
                "to": "David",
                "description": "Freelance job",
            },
        ]
    )


# Тип возвращаемого значения — List[Dict[str, str]]
@patch("csv.DictReader")
@patch("builtins.open", new_callable=mock_open)
def test_read_csv(mock_open: MagicMock, mock_dict_reader: MagicMock, csv_data: str) -> None:
    # Подменяем результат работы DictReader
    mock_reader = MagicMock()
    mock_reader.__iter__.return_value = iter(
        [
            {
                "id": "1",
                "state": "completed",
                "date": "2024-06-10",
                "amount": "1000",
                "currency_name": "USD",
                "currency_code": "840",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment for services",
            },
            {
                "id": "2",
                "state": "pending",
                "date": "2024-06-11",
                "amount": "500",
                "currency_name": "EUR",
                "currency_code": "978",
                "from": "Charlie",
                "to": "David",
                "description": "Freelance job",
            },
        ]
    )

    mock_dict_reader.return_value = mock_reader

    mock_open.return_value = StringIO(csv_data)  # Подменяем файл-объект

    result = read_csv("fake_path.csv")  # Вызываем функцию
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[0]["state"] == "completed"


# Тип возвращаемого значения — List[Dict[str, str]]
@patch("pandas.read_excel")
def test_read_xlsx(mock_read_excel: MagicMock, xlsx_data: pd.DataFrame) -> None:
    mock_read_excel.return_value = xlsx_data  # Подменяем `pd.read_excel`

    result = read_xlsx("fake_path.xlsx")  # Вызываем функцию
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[0]["state"] == "completed"
