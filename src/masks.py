def get_mask_card_number(card: str) -> str:
    """
    Функция получает 16 цифр номер карты и возвращает номер,
    где видны первые 6 цифр и последние четыре. Номер разбит на 4 блока, с пробелами.
    """
    if len(card) == 16:
        return f"{card[0:4]} {card[4:6]}** **** {card[-4:]}"
    else:
        return "Номер карты должен содержать 16 цифр"


def get_mask_account(account_number: str) -> str:
    """Функция заменяет номер счёта на две * и оставляет последние 4 цифры"""
    if len(account_number) >= 4:
        return f"**{account_number[-4:]}"
    else:
        return "Номер счёта должен содержать не менее 4 цифр"
