"""Standalone pytest exercise for Topic 4.1 (Continuous Integration).

This practice module is independent of main.py and the original CSV dataset.
Run: python -m pytest -v test_lab4_ci.py
"""


def load_sample_products():
    """Return a small, fixed catalog for demonstrating automated tests."""
    return [
        {"id": 1, "name": "Brake Pad", "price": 45.50, "stock": 120},
        {"id": 2, "name": "Oil Filter", "price": 12.00, "stock": 200},
        {"id": 3, "name": "Air Filter", "price": 18.75, "stock": 150},
        {"id": 4, "name": "Spark Plug", "price": 8.90, "stock": 300},
        {"id": 5, "name": "Battery", "price": 115.00, "stock": 40},
    ]


def test_products_not_empty():
    assert len(load_sample_products()) > 0


def test_product_count():
    assert len(load_sample_products()) == 5


def test_prices_are_positive():
    assert all(product["price"] > 0 for product in load_sample_products())


def test_stock_is_non_negative():
    assert all(product["stock"] >= 0 for product in load_sample_products())


def test_product_names_not_empty():
    assert all(product["name"].strip() for product in load_sample_products())
# Verify CI after source code modification
