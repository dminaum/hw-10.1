from widget import get_date


def filter_by_state(data: list[dict[str, str]], state: str = "EXECUTED") -> list[dict[str, str]]:
    """
    Фильтрует список словарей по состоянию. Возвращает только те словари, где значение по ключу 'state'
    совпадает с заданным состоянием.

    :param data: Список словарей, содержащих информацию.
    :param state: Состояние, по которому нужно отфильтровать данные (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    # Фильтруем элементы списка по состоянию
    data = [d for d in data if d["state"] == state]
    return data


def sort_by_date(data: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    """
    Сортирует список словарей по дате. Сортировка выполняется по возрастанию или убыванию
    в зависимости от параметра 'reverse'.

    :param data: Список словарей, содержащих информацию.
    :param reverse: Флаг, указывающий на направление сортировки (по умолчанию True — убывание).
    :return: Отсортированный список словарей.
    """
    # Сортируем данные по дате, используя функцию get_date
    sorted_data = sorted(data, key=lambda x: get_date(x["date"]), reverse=reverse)
    return sorted_data
