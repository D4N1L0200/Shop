from models import Product


class ProductView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def list_products(cls, products: list[Product]) -> None:
        if not products:
            cls.message("No products found.")
            return

        cls.message("\tProducts:")
        for product in products:
            cls.message(str(product))
