from mask import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    subgroups = card_type_and_number.split(" ")
    number_of_elements = len(subgroups)
    if subgroups[0] == "Счет":
        return f"{subgroups[0]} {get_mask_account(subgroups[-1])}"
    else:
        if number_of_elements <= 2:
            return f"{subgroups[0]} {get_mask_card_number(subgroups[-1])}"
        else:
            return (
                f"{subgroups[0]} {subgroups[1]} {get_mask_card_number(subgroups[-1])}"
            )


def get_date(dates: str) -> str:
    """функция изменяет формат даты"""
    date = dates[0:10]
    elements = date.split("-")
    return f"{elements[-1]}.{elements[-2]}.{elements[0]}"
