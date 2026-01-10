from typing import Any, Union


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
    condition: Union[bool] = True,
) -> list[dict[Any, Any]]:
    """Функция возвращает новый список, отсортированный по дате (date)."""
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=condition)


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
))