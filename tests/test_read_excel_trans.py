from pathlib import Path
from unittest.mock import Mock, patch

from src.read_excel_trans import read_excel_trans


def test_read_excel__trans_success() -> None:
    expected = [{"id": "1", "name": "Alice", "amount": "100.0"}, {"id": "2", "name": "Bob", "amount": "200.0"}]
    with patch("pathlib.Path.rglob") as mock_rglob, patch("pandas.read_excel") as mock_read_excel:
        mock_file = Mock(spec=Path)
        mock_file.is_file.return_value = True
        mock_rglob.return_value = [mock_file]

        mock_df = Mock()
        mock_df.to_dict.return_value = expected
        mock_read_excel.return_value = mock_df

        result = read_excel_trans("data.excel")
        assert result == expected
        mock_read_excel.assert_called_once_with(mock_file)


def test_read_excel_file_not_found() -> None:
    with patch("pathlib.Path.rglob") as mock_rglob:
        mock_rglob.return_value = []
        result = read_excel_trans("ghost.excel")
        assert result is None
