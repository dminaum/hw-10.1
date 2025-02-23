from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    for transaction in transactions:
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
            if transaction["operationAmount"]["currency"].get("code") == currency:
                yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    card_number = start
    while card_number <= stop:
        card_str = str(card_number).zfill(16)
        formatted_card = " ".join([card_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card
        card_number += 1
