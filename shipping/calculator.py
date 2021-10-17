from decimal import Decimal


def get_book_shipping_cost(book_quantity=1):

    if book_quantity >= 16:
        shipping_rate = 0
    elif book_quantity in range(11, 16):
        shipping_rate = 1
    elif book_quantity in range(5, 11):
        shipping_rate = 2
    elif book_quantity in range(2, 5):
        shipping_rate = 3
    else:
        shipping_rate = 4

    shipping_cost = book_quantity * shipping_rate

    return Decimal(shipping_cost).quantize(Decimal("0.00"))
