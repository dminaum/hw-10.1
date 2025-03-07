import re
import unittest
from typing import Dict, List


def sort_dataframes_by_desc(transactions: List[Dict], match: str) -> List[Dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    result_list = []
    pattern = re.compile(rf"{match}", re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(transaction["description"]) is not None:
            result_list.append(transaction)
        else:
            continue
    return result_list


class TestSortDataframesByDesc(unittest.TestCase):
    def setUp(self) -> None:
        """Подготовка тестовых данных"""
        self.transactions = [
            {"date": "2024-03-10", "amount": "100", "description": "Перевод на счет"},
            {"date": "2024-03-11", "amount": "200", "description": "Покупка в магазине"},
            {"date": "2024-03-12", "amount": "150", "description": "Оплата за услуги"},
            {"date": "2024-03-13", "amount": "250", "description": "Перевод на карту"},
            {"date": "2024-03-14", "amount": "300", "description": "Покупка в магазине"},
        ]

    def test_sort_dataframes_by_desc_found(self) -> None:
        """Тестируем, что функция возвращает правильный результат при совпадении строки"""
        result = sort_dataframes_by_desc(self.transactions, "Покупка")
        expected_result = [
            {"date": "2024-03-11", "amount": "200", "description": "Покупка в магазине"},
            {"date": "2024-03-14", "amount": "300", "description": "Покупка в магазине"},
        ]
        self.assertEqual(result, expected_result)

    def test_sort_dataframes_by_desc_not_found(self) -> None:
        """Тестируем, что функция возвращает пустой список, если нет совпадений"""
        result = sort_dataframes_by_desc(self.transactions, "Зарплата")
        self.assertEqual(result, [])

    def test_sort_dataframes_by_desc_case_insensitive(self) -> None:
        """Тестируем, что функция игнорирует регистр"""
        result = sort_dataframes_by_desc(self.transactions, "покупка")
        expected_result = [
            {"date": "2024-03-11", "amount": "200", "description": "Покупка в магазине"},
            {"date": "2024-03-14", "amount": "300", "description": "Покупка в магазине"},
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
