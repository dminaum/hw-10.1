import json
import logging
import os
from typing import Dict, List

from src.external_api import convert_to_rubles

# Настраиваем логирование
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден. Возвращаем пустой список.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно загружен. Найдено {len(data)} записей.")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список. Возвращаем пустой список.")
                return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
        return []
    except OSError as e:
        logger.error(f"Ошибка чтения файла {file_path}: {e}")
        return []


def get_transaction_amount_in_rubles(transaction: dict) -> float | None:
    """
    Получает сумму транзакции в рублях.
    :param transaction: Словарь с данными о транзакции
    :return: Сумма в рублях или None в случае ошибки
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        result = convert_to_rubles(amount, currency)
        logger.info(f"Конвертация {amount} {currency} в рубли: {result}")
        return result
    except (KeyError, TypeError, ValueError) as e:
        logger.error(f"Ошибка обработки транзакции {transaction}: {e}")
        return None
