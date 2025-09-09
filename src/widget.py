from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """
    Принимает Название и Номер Карты одним аргументом в формате Название Номер.
    Возвращает название и замаскированные цифры с 7 по 12 включительно, номер разбит по 4 цифры
    """
    parts = card.split()
    if len(parts[-1]) == 16 and parts[-1].isdigit():
        return f"{" ".join(parts[:-1])} {get_mask_card_number(parts[-1])}"
    elif len(parts[-1]) == 20 and parts[-1].isdigit():
        return f"{" ".join(parts[:-1])} {get_mask_account(parts[-1])}"
    else:
        return "Некорректные данные"


def get_date(date: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_new = date.split("T")
    new = date_new[0].split("-")
    return f"{'.'.join(new[::-1])}"
