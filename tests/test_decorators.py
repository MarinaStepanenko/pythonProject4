from _pytest.capture import CaptureFixture

from src.decorators import log


@log()
def func_div(a: float, b: float) -> float:
    return a / b


@log("logs/log.txt")
def func_div_2(a: float, b: float) -> float:
    return a / b


def test_log_file_error() -> None:
    func_div_2(4, 0)
    assert "func_div_2 error: ZeroDivisionError. Inputs: (4, 0), {}\n" in open("logs/log.txt", encoding="utf-8")


def test_log_file() -> None:
    func_div_2(4, 2)
    assert "func_div_2 ок\n" in open("logs/log.txt", encoding="utf-8")


def test_log_console(capsys: CaptureFixture) -> None:
    func_div(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "func_div ок\n\n"


def test_log_console_error(capsys: CaptureFixture) -> None:
    func_div(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "func_div error: ZeroDivisionError. Inputs: (4, 0), {}\n\n"
