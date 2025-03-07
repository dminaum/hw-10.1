from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    :param data: Строка, содержащая тип и номер карты или счета.
                 Например, "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".
    :return: Строка с замаскированным номером. Например:
             - Для карты: "Visa Platinum 7000 79** **** 6361"
             - Для счета: "Счет **4305"
    """
    data = str(data).strip()

    if data.startswith("Счет"):
        parts = data.split(" ", 1)
        if len(parts) < 2:
            return "Счет **"

        number = parts[1]
        return f"Счет {get_mask_account(number)}"

    parts = data.rsplit(" ", 1)
    if len(parts) < 2:
        return "****"

    card_name, card_number = parts
    return f"{card_name} {get_mask_card_number(card_number)}"



def get_date(date_str: str) -> datetime:
    """
    Преобразует строку с датой из формата "2024-03-11T02:26:18.671407"
    в объект datetime, игнорируя время (только месяц, день и год).

    :param date_str: Дата в формате ISO (например, "2024-03-11T02:26:18.671407").
    :return: Объект datetime, включающий только день, месяц и год.
    """
    # Разбираем дату из строки в формат datetime
    date_obj = datetime.fromisoformat(date_str)
    # Создаем новый объект datetime с учетом только дня, месяца и года (без времени)
    return date_obj.replace(hour=0, minute=0, second=0, microsecond=0)


def format_date(date_obj: datetime) -> str:
    """
    Форматирует объект datetime в строку формата "ДД.ММ.ГГГГ", игнорируя время и миллисекунды.

    :param date_obj: Объект datetime.
    :return: Отформатированная строка в формате "ДД.ММ.ГГГГ".
    """
    return date_obj.strftime("%d.%m.%Y")
