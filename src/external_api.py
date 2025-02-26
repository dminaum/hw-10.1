import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rubles(amount: float, currency_from: str, currency_to: str = "RUB") -> float | None:
    """
    Конвертирует сумму из одной валюты в рубли через API.

    :param amount: Сумма для конвертации
    :param currency_from: Исходная валюта (например, "USD", "EUR")
    :param currency_to: Валюта назначения (по умолчанию "RUB")
    :return: Сумма в рублях или None в случае ошибки
    """
    if currency_from == currency_to:
        return amount  # Если уже в рублях, просто возвращаем

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем HTTP-статус (если 4xx или 5xx, выбросит ошибку)
        data = response.json()
        return data.get("result")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе API: {e}")
        return None  # В случае ошибки возвращаем None

