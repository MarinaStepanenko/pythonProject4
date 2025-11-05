from typing import Dict


def filter_by_state(my_list_info: list[Dict], state: str = "EXECUTED") -> list[Dict]:
    """
    Принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Возвращает новый список словарей, содержащий только те, у которых ключ
    state соответствует указанному значению.
    """
    new_list = []
    for my_list in my_list_info:
        if my_list.get("state") == state:
            new_list.append(my_list)
    return new_list


def sort_by_date(list_info: list[Dict], reverse: bool = True) -> list[Dict]:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате ("date").
    """
    new_list = sorted(list_info, key=lambda x: x["date"], reverse=reverse)
    return new_list
