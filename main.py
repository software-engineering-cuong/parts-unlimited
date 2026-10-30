
import csv


def load_products(filename="products.csv"):
    with open(filename, encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def show_products(products):
    for product in products:
        print(
            f"{product['id']} - {product['name']} | "
            f"Price: ${product['price']} | "
            f"Stock: {product['stock']}"
        )


def main():
    products = load_products()
    print("PARTS UNLIMITED - PRODUCT CATALOG")
    show_products(products)


if __name__ == "__main__":
    main()
