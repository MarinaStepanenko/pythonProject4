from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(trans_list: list[dict]) -> None:
    currency = "USD"
    expected = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    result = next(filter_by_currency(trans_list, currency))
    assert expected == result


def test_filter_by_currency_no_currency(trans_list: list[dict]) -> None:
    currency = "RUB"
    expected: list = []
    result = list(filter_by_currency(trans_list, currency))
    assert expected == result


def test_filter_by_currency_empty() -> None:
    transaction: list = []
    currency = "USD"
    expected: list = []
    result = list(filter_by_currency(transaction, currency))
    assert expected == result


def test_transaction_descriptions(trans_list: list[dict]) -> None:
    expected = ["Перевод организации", "Перевод со счета на счет"]
    result = list(transaction_descriptions(trans_list))
    assert result == expected
    assert list(transaction_descriptions([])) == []


def test_card_number_generator() -> None:
    expected = ["0000 0000 0000 0003", "0000 0000 0000 0004"]
    result = list(card_number_generator(3, 4))
    assert expected == result
    assert list(card_number_generator(9999999999999998, 9999999999999999)) == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
