from pathlib import Path
from unittest.mock import Mock, mock_open, patch

from src.read_csv import read_csv_trans


def test_read_csv_success() -> None:
    """Полный тест: декоратор + функция чтения"""
    csv_content = "id;name;amount\n1;Alice;100.0\n2;Bob;200.0"
    expected = [{"id": "1", "name": "Alice", "amount": "100.0"}, {"id": "2", "name": "Bob", "amount": "200.0"}]
    with patch("pathlib.Path.rglob") as mock_rglob, patch("builtins.open", mock_open(read_data=csv_content)):
        mock_file = Mock(spec=Path)
        mock_file.is_file.return_value = True
        mock_rglob.return_value = [mock_file]
        result = read_csv_trans("data.csv")
        assert result == expected


def test_read_csv_file_not_found() -> None:
    """Интеграционный тест когда файл не найден"""
    with patch("pathlib.Path.rglob") as mock_rglob:
        mock_rglob.return_value = []
        result = read_csv_trans("ghost.csv")
        assert result is None
