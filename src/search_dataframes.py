import re
from collections import Counter, defaultdict
from typing import Dict, List


def sort_dataframes_by_desc(transactions: List[Dict], match: str) -> List[Dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращать список словарей, у которых в описании есть данная строка."""
    result_list = []
    pattern = re.compile(rf'{match}', re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(transaction['description']) is not None:
            result_list.append(transaction)
        else:
            continue
    return result_list


def count_operations_by_category(transactions: List[Dict[str, str]]) -> Dict[str, int]:
    """Считает количество операций по точным категориям на основе поля 'description', определяя категории автоматически."""
    category_counts = Counter()
    descriptions = [transaction.get("description", "").lower() for transaction in transactions]

    # Извлекаем уникальные описания как категории
    unique_categories = set(descriptions)

    # Подсчитываем количество вхождений каждого уникального описания
    for description in unique_categories:
        category_counts[description] = descriptions.count(description)

    return dict(category_counts)
