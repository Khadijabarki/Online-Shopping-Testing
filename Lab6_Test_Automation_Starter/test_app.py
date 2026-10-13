
import pytest
from app import calculate_discount

@pytest.mark.parametrize(
    "is_member, cart_total, expected",
    [
        (True, 100, 10.00),
        (True, 50, 0.00),
        (False, 200, 10.00),
        (False, 100, 0.00),
        (True, 250, 25.00),
        (False, 300, 15.00),
        (False, 0, 0.00),
    ],
)
def test_calculate_discount(is_member, cart_total, expected):
    assert calculate_discount(is_member, cart_total) == expected

def test_negative_cart_total_is_rejected():
    with pytest.raises(ValueError):
        calculate_discount(False, -1)
