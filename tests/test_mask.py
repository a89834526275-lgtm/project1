import pytest

from src.mask import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("6831982476737658", "6831 98** **** 7658"),
    ("8990922113665229", "8990 92** **** 5229"),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

@pytest.fixture
def mask():
    return "**4305"

def test_get_mask_account(mask):
    assert get_mask_account(73654108430135874305) == mask
