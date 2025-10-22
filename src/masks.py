import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: str) -> str:
    """
    Функция получает 16 цифр номер карты и возвращает номер,
    где видны первые 6 цифр и последние четыре. Номер разбит на 4 блока, с пробелами.
    """
    try:
        if len(card) == 16:
            logger.info(f"Номер {card} содержит 16 цифр и будет зашифрован")
            return f"{card[0:4]} {card[4:6]}** **** {card[-4:]}"
        else:
            logger.info("Неверный формат")
            return "Номер карты должен содержать 16 цифр"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return f"Ошибка: {ex}"


def get_mask_account(account_number: str) -> str:
    """Функция заменяет номер счёта на две * и оставляет последние 4 цифры"""
    try:
        if len(account_number) >= 4:
            logger.info(f"Номер {account_number} будет зашифрован")
            return f"**{account_number[-4:]}"
        else:
            logger.info("Неверный формат")
            return "Номер счёта должен содержать не менее 4 цифр"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return f"Ошибка: {ex}"
