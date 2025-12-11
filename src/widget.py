def mask_account_card(card_type_and_number: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    subgroups = card_type_and_number.split(" ")
    number_of_elements = len(subgroups)
    card_number = (
        f"{subgroups[-1][0:5]} {subgroups[-1][5:7]}** **** {subgroups[-1][12:]}"
    )
    account_number = (
        f"{subgroups[-1][0:5]} {subgroups[-1][5:7]}** **** {subgroups[-1][12:]}"
    )
    if subgroups[0] == "Счет":
        return f"{subgroups[0]} **{subgroups[1][-4:]}"
    else:
        if number_of_elements <= 2:
            return f"{subgroups[0]} {card_number}"
        else:
            return f"{subgroups[0]} {subgroups[1]} {account_number}"


def get_date(dates: str) -> str:
    """функция изменяет формат даты"""
    date = dates[0:10]
    elements = date.split("-")
    return f"{elements[-1]}.{elements[-2]}.{elements[0]}"
