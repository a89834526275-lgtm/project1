import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def card():
    return "Maestro 1596 83** **** 5199"


def test_mask_account_card(card):
    assert mask_account_card("Maestro 1596837868705199") == card


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
