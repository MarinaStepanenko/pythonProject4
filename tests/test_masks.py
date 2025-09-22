from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card: str) -> None:
    assert get_mask_card_number(card) == "9846 35** **** 4756"
    assert get_mask_card_number("43743583") == "Номер карты должен содержать 16 цифр"


def test_get_mask_account(account: str) -> None:
    assert get_mask_account(account) == "**8926"
    assert get_mask_account("645") == "Номер счёта должен содержать не менее 4 цифр"
