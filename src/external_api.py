import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_convertation(transaction: list[dict]) -> float | int:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции amount в рублях.
    Если транзакция в USD или EUR, обращается к API для получения текущего курса и конвертации в рубли.
    """
    amount = 0.0
    for t in transaction:
        if t["operationAmount"]["currency"].get("code") == "RUB":
            amount += float(t["operationAmount"].get("amount"))
        elif (
            t["operationAmount"]["currency"].get("code") == "EUR"
            or t["operationAmount"]["currency"].get("code") == "USD"
        ):
            url = "https://api.apilayer.com/exchangerates_data/convert"
            apikey = os.getenv("API_KEY")
            payload = {
                "amount": {t["operationAmount"].get("amount")},
                "from": {t["operationAmount"]["currency"].get("code")},
                "to": "RUB",
            }
            headers = {"apikey": apikey}

            response = requests.get(url, headers=headers, params=payload)
            status = response.status_code
            if response.status_code != 200:
                return status
            result = response.json()
            amount += float(result.get("result"))
    return amount


with open("data/operations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(get_convertation(data))
