from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где
    валюта операции соответствует заданной.
    """
    for tr in transactions:
        if tr["operationAmount"]["currency"]["code"] == currency:
            yield tr


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    for tr in transactions:
        yield tr.get("description", "Описание отсутствует")


def card_number_generator(start_number: int, end_number: int) -> Generator:
    """
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
    — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от
    0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    for num in range(start_number, end_number + 1):
        yield (
            f"{(str(num).zfill(16))[0:4]} {(str(num).zfill(16))[4:8]} "
            f"{(str(num).zfill(16))[8:12]} {(str(num).zfill(16))[-4:]}"
        )
