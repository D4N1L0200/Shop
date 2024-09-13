from models import Product


class ProductController:
    products: list[Product] = []
    logging: bool = False

    @classmethod
    def set_logging(cls, logging: bool) -> None:
        if not isinstance(logging, bool):
            raise ValueError(f"Invalid value for logging: {logging}")

        cls.logging = logging

    @classmethod
    def id_exists(cls, prod_id: int) -> bool:
        if not isinstance(prod_id, int):
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

    @classmethod
    def get_products(cls) -> list[Product]:
        return cls.products

    @classmethod
    def get_product_by_id(cls, prod_id: int) -> Product:
        if not isinstance(prod_id, int):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        for product in cls.products:
            if product.get_id() == prod_id:
                return product

        raise ValueError(f"Product not found: {prod_id}")

    @classmethod
    def update(cls, prod_id: int, product: Product) -> None:
        if not isinstance(prod_id, int):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not isinstance(product, Product):
            raise ValueError(f"Invalid value for product: {product}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        for index, prod in enumerate(cls.products):
            if prod.get_id() == prod_id:
                cls.products[index] = product
                break

    @classmethod
    def delete_by_id(cls, prod_id: int) -> None:
        if not isinstance(prod_id, int):
            raise ValueError(f"Invalid value for product id: {prod_id}")

        if not cls.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        cls.products = [
            product for product in cls.products if product.get_id() != prod_id
        ]
