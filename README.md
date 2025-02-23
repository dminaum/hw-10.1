# Описание проекта

Этот проект предназначен для обработки финансовых данных. Он включает функции для маскирования номеров карт и счетов, форматирования дат, фильтрации операций по статусу и работы с генераторами.

## Структура проекта

- `masks.py` – содержит функции для маскирования номеров карт и счетов.
- `widget.py` – предоставляет функции для форматирования дат и маскирования данных.
- `processing.py` – отвечает за обработку списка операций: фильтрацию по статусу и сортировку по дате.
- `generators.py` – содержит генераторы для фильтрации транзакций по валюте, получения описаний транзакций и генерации номеров карт.
- `tests/` – содержит тесты для проверки функциональности проекта.

## Установка

Для работы проекта требуется Python 3.8+

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/your-repo/project-name.git
   cd project-name
   ```
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

## Использование

### Маскирование данных

Пример использования функций из `masks.py`:

```python
from masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("7000792289606361"))  # Вывод: "7000 79** **** 6361"
print(get_mask_account("73654108430135874305"))  # Вывод: "**4305"
```

### Обработка строк с номерами карт и счетов

Пример работы `mask_account_card`:

```python
from widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))  # Вывод: "Visa Platinum 7000 **** **** 6361"
print(mask_account_card("Счет 73654108430135874305"))  # Вывод: "Счет **4305"
```

### Форматирование дат

```python
from widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))  # Вывод: "11.03.2024"
```

### Фильтрация операций по статусу

```python
from processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED", "date": "2024-01-01T12:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-01-02T12:00:00"},
]

filtered = filter_by_state(data)
print(filtered)  # Оставит только операции со статусом "EXECUTED"
```

### Сортировка операций по дате

```python
from processing import sort_by_date

sorted_data = sort_by_date(data)
print(sorted_data)  # Отсортирует операции по дате (по убыванию)
```

## Работа с генераторами

### Фильтрация транзакций по валюте

```python
from generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
    {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"}
]

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
```

### Получение описаний транзакций

```python
from generators import transaction_descriptions

transactions = [
    {"description": "Payment for order #1234"},
    {"description": "Refund from store"},
    {"description": "Salary payment"}
]

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)
```

### Генерация номеров карт

```python
from generators import card_number_generator

for card_number in card_number_generator(1000000000000000, 1000000000000005):
    print(card_number)
```

## Тестирование

Проект содержит тесты, проверяющие основные функции, включая генераторы.

### Запуск тестов

```sh
pytest
```

### Проверка покрытия кода тестами

```sh
pytest --cov=.
```

После выполнения команды в репозитории появится папка с отчетом покрытия тестами в формате HTML. Чтобы открыть отчет в браузере, используйте команду:

```sh
pytest --cov=. --cov-report=html
start htmlcov/index.html
```

### Использование фикстур и параметризации

В тестах применяются фикстуры для генерации данных и параметризация для проверки различных сценариев работы функций.

