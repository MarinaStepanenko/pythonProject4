from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_operations

if __name__ == "__main__":
    get_operations("data/operations.json")
    get_mask_account("172846")
    get_mask_card_number("16253425164736253")
