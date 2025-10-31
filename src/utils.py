import json
import logging
import os.path
import re
from collections import Counter
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(directory: str) -> list[dict] | str:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        if not os.path.exists(directory):
            logger.warning(f"Директория файла {directory} не найдена")
            return []
        with open(directory, "r", encoding="utf-8") as f:
            logger.info(f"Информация о транзакциях была выгружена из json файла {directory}.")
            operations = json.load(f)
            if not isinstance(operations, list):
                logger.warning(f"{directory} не содержит список")
                return []
            return operations
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return f"Ошибка: {ex}"


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска, возвращает список словарей,
    у которых в описании есть данная строка.
    """
    if not data or not search_string:
        return []
    pattern = re.escape(search_string)
    new_dicts = []
    for item in data:
        if "description" in item and item["description"] is not None:
            description = str(item["description"])
            if re.findall(pattern, description, flags=re.IGNORECASE):
                new_dicts.append(item)
    return new_dicts


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории. Категории операций хранятся в поле description
    """
    categories_counter: Counter[Any] = Counter()
    for operation in data:
        description = operation.get("description", "")
        for cat in categories:
            if cat.lower() in description.lower():
                categories_counter[cat] += 1
    return categories_counter


def filter_data_file(data: list[dict]) -> list[dict]:
    """Функция, которая приводит список словарей к единому виду"""
    file = []

    for transaction in data:
        converted_dict = {
            "amount": transaction.get("operationAmount", {}).get("amount") or transaction.get("amount"),
            "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code")
            or transaction.get("currency", {}),
            "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name")
            or transaction.get("currency_name"),
            "date": transaction.get("date"),
            "description": transaction.get("description"),
            "from": transaction.get("from"),
            "id": transaction.get("id"),
            "state": transaction.get("state"),
            "to": transaction.get("to"),
        }
        file.append(converted_dict)
    return file
