import json
import os
from typing import Dict, List

from src.external_api import convert_to_rubles


def load_transactions(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, OSError):
        return []  # Ошибка чтения или файл пустой


def get_transaction_amount_in_rubles(transaction: dict) -> float | None:
    """
    Получает сумму транзакции в рублях.
    :param transaction: Словарь с данными о транзакции
    :return: Сумма в рублях или None в случае ошибки
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        return convert_to_rubles(amount, currency)
    except (KeyError, TypeError, ValueError):
        return None  # Если данных нет или они в неверном формате, возвращаем None
