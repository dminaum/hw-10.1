import logging

# Настраиваем логирование
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("masks.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    """
    if len(card_number) < 12:
        logger.error(f"Некорректный номер карты: {card_number}")
        return "****"

    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Замаскирован номер карты: {masked_card_number}")
    return masked_card_number


def get_mask_account(account: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    """
    if len(account) < 4:
        logger.error(f"Некорректный номер счета: {account}")
        return "**"

    masked_account = f"**{account[-4:]}"
    logger.info(f"Замаскирован номер счета: {masked_account}")
    return masked_account
