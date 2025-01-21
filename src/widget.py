from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    if data.startswith('Счет'):
        number = data.split(' ')[1]
        return f'Счет {get_mask_account(number)}'
    else:
        card_number, card_name = data.rsplit(' ', 1)
        return f'{card_name} {get_mask_card_number(card_number)}'
