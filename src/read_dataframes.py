import csv
from typing import Dict, List

import pandas as pd


def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as transactions_csv:
        reader = csv.DictReader(transactions_csv, delimiter=";")  # Читаем файл
        return list(reader)  # Преобразуем в список словарей


def read_xlsx(path: str) -> List[Dict]:
    df = pd.read_excel(path)  # Читаем файл как DataFrame
    transactions = df.to_dict(orient="records")  # Преобразуем в список словарей
    return transactions
