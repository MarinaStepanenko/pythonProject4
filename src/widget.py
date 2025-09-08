from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card: str) -> str:
    """
    Принимает Название и Номер Карты одним аргументом в формате Название Номер.
    Возвращает название и замаскированные цифры с 7 по 12 включительно, номер разбит по 4 цифры
    """
    parts = card.split()
    if len(parts[-1]) == 16 and parts[-1].isdigit():
        return f"{parts[:-1]} {get_mask_card_number(parts[-1])}"
    elif len(parts[-1]) == 20 and parts[-1].isdigit():
        return f"{parts[:-1]} {get_mask_account(parts[-1])}"
    else:
        return  "Некорректные данные"






