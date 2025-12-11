from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    str_number = str(card_number)
    card_mask = f"{str_number[0:5]} {str_number[5:7]}** **** {str_number[12:]}"
    return card_mask


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    account_numbers = str(account_number)
    account_mask = f"** {account_numbers[-4:]}"
    return account_mask
