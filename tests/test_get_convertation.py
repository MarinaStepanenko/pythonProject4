from unittest.mock import MagicMock, patch, Mock

from src.external_api import get_convertation


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_rub_only(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    transactions = [
        {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "200.0", "currency": {"code": "RUB"}}},
    ]

    result = get_convertation(transactions)

    assert result == 300.0
    mock_requests_get.assert_not_called()


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_eur_with_api(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    mock_getenv.return_value = "test_api_key"

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "95.5"}
    mock_requests_get.return_value = mock_response

    transactions = [{"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}]

    result = get_convertation(transactions)

    assert result == 95.5
    mock_requests_get.assert_called_once()
    mock_getenv.assert_called_once_with("API_KEY")


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_usd_with_api(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    mock_getenv.return_value = "test_api_key"

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "85.0"}
    mock_requests_get.return_value = mock_response

    transactions = [{"operationAmount": {"amount": "50.0", "currency": {"code": "USD"}}}]

    result = get_convertation(transactions)

    assert result == 85.0


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_mixed_currencies(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    mock_getenv.return_value = "test_api_key"

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "90.0"}
    mock_requests_get.return_value = mock_response

    transactions = [
        {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "1.0", "currency": {"code": "EUR"}}},
    ]

    result = get_convertation(transactions)

    assert result == 190.0


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_api_error(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    """Тест когда API возвращает ошибку"""
    mock_getenv.return_value = "test_api_key"

    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_requests_get.return_value = mock_response

    transactions = [{"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}]

    result = get_convertation(transactions)

    assert result == 500


@patch("requests.get")
@patch("os.getenv")
def test_get_convertation_empty_list(mock_getenv: Mock, mock_requests_get: Mock) -> None:
    result = get_convertation([])

    assert result == 0.0
    mock_requests_get.assert_not_called()
