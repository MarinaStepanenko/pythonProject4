from collections import Counter

from src.utils import filter_data_file, process_bank_operations, process_bank_search


def test_process_bank_search_success(trans_list: list[dict]) -> None:
    assert process_bank_search(trans_list, "счет") == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
    assert process_bank_search(trans_list, "") == []
    assert process_bank_search(trans_list, "вклад") == []


def test_process_bank_operation(trans_list: list[dict]) -> None:
    assert process_bank_operations(trans_list, ["Перевод со счета на счет", "Перевод организации"]) == Counter(
        {"Перевод со счета на счет": 1, "Перевод организации": 1}
    )
    assert process_bank_operations(trans_list, ["Открытие вклада", "Закрытие вклада"]) == Counter()


def test_filter_data_file() -> None:
    data1 = [
        {
            "operationAmount": {"amount": "100.50", "currency": {"code": "USD", "name": "US Dollar"}},
            "date": "2023-10-01",
            "description": "Payment",
            "from": "Card 1234",
            "id": 1,
            "state": "EXECUTED",
            "to": "Account 5678",
        }
    ]

    result1 = filter_data_file(data1)
    assert result1[0]["amount"] == "100.50"
    assert result1[0]["currency_code"] == "USD"
    assert result1[0]["currency_name"] == "US Dollar"
    assert result1[0]["description"] == "Payment"

    data2 = [
        {
            "amount": "200.75",
            "currency": "EUR",
            "currency_name": "Euro",
            "date": "2023-10-02",
            "description": "Transfer",
            "from": "Card 9999",
            "id": 2,
            "state": "PENDING",
            "to": "Account 0000",
        }
    ]

    result2 = filter_data_file(data2)
    assert result2[0]["amount"] == "200.75"
    assert result2[0]["currency_code"] == "EUR"
    assert result2[0]["currency_name"] == "Euro"
    assert result2[0]["description"] == "Transfer"

    data3 = [
        {
            "operationAmount": {"amount": "300.00", "currency": {"code": "GBP", "name": "British Pound"}},
            "currency_name": "Should be ignored",
            "date": "2023-10-03",
            "description": "Mixed format",
            "id": 3,
            "state": "EXECUTED",
        }
    ]

    result3 = filter_data_file(data3)
    assert result3[0]["amount"] == "300.00"
    assert result3[0]["currency_code"] == "GBP"
    assert result3[0]["currency_name"] == "British Pound"

    data4 = [{"amount": "400.25", "date": "2023-10-04", "id": 4, "state": "CANCELED"}]

    result4 = filter_data_file(data4)
    assert result4[0]["amount"] == "400.25"
    assert "currency_code" in result4[0]
    assert "currency_name" in result4[0]
    assert result4[0]["description"] is None
    assert result4[0]["from"] is None
    assert result4[0]["to"] is None
