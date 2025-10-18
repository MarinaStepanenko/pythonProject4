import json
import logging
import os.path


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