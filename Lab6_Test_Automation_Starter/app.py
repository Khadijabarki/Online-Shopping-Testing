
"""Online Shopping System discount logic."""

def calculate_discount(is_member: bool, cart_total: float) -> float:
    """Calculate the discount using sample lab rules."""

    if cart_total < 0:
        raise ValueError("Cart total cannot be negative")

    if is_member and cart_total >= 100:
        return round(cart_total * 0.10, 2)

    if not is_member and cart_total >= 200:
        return round(cart_total * 0.05, 2)

    return 0.0
