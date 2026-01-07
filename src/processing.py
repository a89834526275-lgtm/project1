from typing import Any


def filter_by_state(
    list_of_dictionaries: list[dict[Any, Any]], state: str = "EXECUTED"
) -> list[dict[Any, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state
    соответствует указанному значению."""
    filtered_dictionaries = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == state:
            filtered_dictionaries.append(dictionary)
    return filtered_dictionaries


def sort_by_date(
    list_of_dictionaries: list[dict[Any, Any]],
    condition: str = "сортировка по убыванию",
) -> list[dict[Any, Any]]:
    """Функция возвращает новый список, отсортированный по дате (date)."""
    if condition == "сортировка по убыванию":
        return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=False)
