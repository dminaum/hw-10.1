from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    :param data: Строка, содержащая тип и номер карты или счета.
                 Например, "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".
    :return: Строка с замаскированным номером. Например:
             - Для карты: "Visa Platinum 7000 **** **** 6361"
             - Для счета: "Счет 7365************4305"
    """
    if data.startswith("Счет"):
        number = data.split(" ")[1]
        return f"Счет {get_mask_account(number)}"
    else:
        card_number, card_name = data.rsplit(" ", 1)
        return f"{card_name} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата "2024-03-11T02:26:18.671407"
    в формат "ДД.ММ.ГГГГ".

    :param date_str: Дата в формате ISO (например, "2024-03-11T02:26:18.671407").
    :return: Дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024").
    """

    # Разбираем дату из строки
    date_obj = datetime.fromisoformat(date_str)
    # Преобразуем дату в нужный формат
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
