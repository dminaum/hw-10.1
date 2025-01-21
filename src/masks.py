def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    """
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_card_number


def get_mask_account(account: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    """
    masked_account = "**" + account[-4:]
    return masked_account
