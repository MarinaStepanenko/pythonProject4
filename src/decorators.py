from functools import wraps
from typing import Any, Callable


def write_file(message: str, filename: str | None = None) -> None:
    if not filename:
        print(message)
    else:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)


def log(filename: str | None = None) -> Callable:
    """
    Логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.Если filename не задан, логи выводятся в консоль.
    """

    def my_decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ок\n"
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
            finally:
                write_file(message, filename)

        return wrapper

    return my_decorator
