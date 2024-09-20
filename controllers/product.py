from models import CartItem, Product
import json


class StocksManager:
    products: list[Product] = []

    @classmethod
    def load_data(cls) -> None:
        with open("data/products.json", "r") as file:
            data: dict = json.load(file)

        for prod_id in data:
            prod: Product = Product(prod_id, **data[prod_id])

            cls.insert(prod)

    @classmethod
    def save_data(cls) -> None:
        out = {}
        for product in cls.products:
            out[product.get_id()] = {
                "name": product.get_name(),
                "description": product.get_description(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "pending": product.get_pending(),
                "sold": product.get_sold(),
            }

        with open("data/products.json", "w") as file:
            json.dump(out, file, indent=4)

    def idx_to_id(cls, prod_idx: int) -> str:
        return cls.products[prod_idx].get_id()

    @classmethod
    def id_exists(cls, prod_id: str) -> bool:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                return True

        return False

    @classmethod
    def insert(cls, product: Product) -> None:
        if not isinstance(product, Product):
            raise ValueError(f"Invalid value for product: {product}")

        if cls.id_exists(product.get_id()):
            raise ValueError(f"Product already exists: {product}")

        cls.products.append(product)

        cls.save_data()

    @classmethod
    def get_products(cls) -> list[Product]:
        return cls.products

    @classmethod
    def get_products_len(cls) -> int:
        return len(cls.products)

    @classmethod
    def get_product_by_id(cls, prod_id: str) -> Product:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                return product

        raise ValueError(f"Product not found: {prod_id}")

    @classmethod
    def update(cls, prod_id: str, product: Product) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(product, Product):
            raise ValueError(f"Invalid value for product: {product}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for index, prod in enumerate(cls.products):
            if prod.get_id() == prod_id:
                cls.products[index] = product
                break

        cls.save_data()

    @classmethod
    def delete_by_id(cls, prod_id: str) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        cls.products = [
            product for product in cls.products if product.get_id() != prod_id
        ]

        cls.save_data()

    @classmethod
    def increase_stock(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.increase_stock(amount)
                break

        cls.save_data()

    @classmethod
    def decrease_stock(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.decrease_stock(amount)
                break

        cls.save_data()

    @classmethod
    def increase_pending(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.increase_pending(amount)
                break

        cls.save_data()

    @classmethod
    def decrease_pending(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.decrease_pending(amount)
                break

        cls.save_data()

    @classmethod
    def increase_sold(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.increase_sold(amount)
                break

        cls.save_data()

    @classmethod
    def decrease_sold(cls, prod_id: str, amount: int) -> None:
        if not isinstance(prod_id, str):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(amount, int):
            raise ValueError(f"Invalid value for amount: {amount}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                product.decrease_sold(amount)
                break

        cls.save_data()

    @classmethod
    def add_to_cart(cls, prod_id: str, amount: int) -> None:
        cls.decrease_stock(prod_id, amount)
        cls.increase_pending(prod_id, amount)

        cls.save_data()

    @classmethod
    def remove_from_cart(cls, prod_id: str, amount: int) -> None:
        cls.increase_stock(prod_id, amount)
        cls.decrease_pending(prod_id, amount)

        cls.save_data()

    @classmethod
    def sell_product(cls, prod_id: str, amount: int) -> None:
        cls.increase_sold(prod_id, amount)
        cls.decrease_pending(prod_id, amount)

        cls.save_data()

    @classmethod
    def checkout(cls, items: list[CartItem]) -> None:
        for item in items:
            cls.sell_product(item.get_product_id(), item.get_quantity())

        cls.save_data()
