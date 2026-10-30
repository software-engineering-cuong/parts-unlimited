
from main import load_products


def test_products_not_empty():
    products = load_products()
    assert len(products) > 0


def test_product_count():
    products = load_products()
    assert len(products) == 10


def test_prices_are_positive():
    products = load_products()

    for product in products:
        assert float(product["price"]) > 0


def test_stock_is_non_negative():
    products = load_products()

    for product in products:
        assert int(product["stock"]) >= 0


def test_product_names_not_empty():
    products = load_products()

    for product in products:
        assert product["name"].strip() != ""
