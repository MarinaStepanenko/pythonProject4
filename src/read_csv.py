import csv
import functools
from pathlib import Path
from typing import Any, Callable


def find_file_decorator(func: Callable) -> Callable:
    """
    Декоратор для автоматического поиска файлов перед выполнением функции
    """

    @functools.wraps(func)
    def wrapper(filename: str, *args: Any, **kwargs: Any) -> Any:
        project_root = Path(__file__).parent.parent
        for file_path in project_root.rglob(filename):
            if file_path.is_file():
                print(f"Файл найден: {file_path}")
                return func(file_path, *args, **kwargs)
        print(f" Файл '{filename}' не найден в проекте")
        return None

    return wrapper


@find_file_decorator
def read_csv_trans(filename: str) -> list[dict]:
    """
    Прочитать файл csv и выдать список словарей с транзакциями
    """
    list_of_dicts = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts
