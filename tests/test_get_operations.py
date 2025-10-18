from unittest.mock import Mock, patch

from src.utils import get_operations


@patch("os.path.exists")
@patch("builtins.open")
@patch("json.load")
def test_get_operations_success(mock_json_load: Mock, mock_open: Mock, mock_exists: Mock) -> None:
    mock_exists.return_value = True
    mock_json_load.return_value = [{"id": 123, "amount": 555}]

    result = get_operations("test1")

    assert result == [{"id": 123, "amount": 555}]
    mock_open.assert_called_once_with("test1", "r", encoding="utf-8")


@patch("os.path.exists")
def test_get_operations_empty(mock_exists: Mock) -> None:
    mock_exists.return_value = False
    result = get_operations("not_existing")
    assert result == []


@patch("os.path.exists")
@patch("builtins.open")
@patch("json.load")
def test_get_operations_not_list(mock_json_load: Mock, mock_open: Mock, mock_exists: Mock) -> None:
    """Тест когда JSON не список"""
    mock_exists.return_value = True
    mock_json_load.return_value = {"not": "list"}

    result = get_operations("test.json")

    assert result == []
