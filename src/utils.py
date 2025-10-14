import json
import os.path


def get_operations(directory: str) -> list[dict]:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    if not os.path.exists(directory):
        return []
    with open(directory, "r", encoding="utf-8") as f:
        operations = json.load(f)
        if not isinstance(operations, list):
            return []
    return operations
