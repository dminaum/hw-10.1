from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2024-01-01T12:00:00"},
        {"id": "2", "state": "CANCELED", "date": "2024-01-02T12:00:00"},
    ]


def test_filter_by_state(sample_data: List[Dict[str, str]]) -> None:
    result = filter_by_state(sample_data)
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


def test_sort_by_date(sample_data: List[Dict[str, str]]) -> None:
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]["date"] == "2024-01-02T12:00:00"
