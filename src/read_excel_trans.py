import pandas as pd

from src.read_csv import find_file_decorator


@find_file_decorator
def read_excel_trans(filename: str) -> list[dict]:
    """
    Получает название файла excel и возвращает список словарей транзакций.
    """
    df = pd.read_excel(filename)
    result = df.to_dict("records")
    return result
