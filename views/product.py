from models import Product
from ioutil import input_str, input_int_min, input_int_minmax, input_float_min


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
        for idx, product in enumerate(products):
            cls.message(f"({idx + 1}) {product.get_info()}")

    @classmethod
    def input_product_name(cls) -> str:
        prod_name: str = input_str("Product name: ")
        return prod_name

    @classmethod
    def input_product_description(cls) -> str:
        prod_description: str = input_str("Product description: ")
        return prod_description

    @classmethod
    def input_product_price(cls) -> float:
        prod_price: float = input_float_min("Product price: ", 0)
        return prod_price

    @classmethod
    def input_product_stock(cls) -> int:
        prod_stock: int = input_int_min("Product stock: ", 0)
        return prod_stock

    @classmethod
    def update_product_name(cls, old_name: str) -> str:
        prod_name: str = input_str(
            f"Product name (leave empty for {old_name}): ", allow_empty=True
        )

        if not prod_name:
            return old_name
        return prod_name

    @classmethod
    def update_product_description(cls, old_description: str) -> str:
        prod_description: str = input_str(
            f"Product description (leave empty for {old_description}): ",
            allow_empty=True,
        )

        if not prod_description:
            return old_description
        return prod_description

    @classmethod
    def update_product_price(cls, old_price: float) -> float:
        prod_price: float = input_float_min(
            f"Product price (use '-1' for '{old_price}'): ", -1
        )

        if prod_price == -1:
            return old_price
        return prod_price

    @classmethod
    def update_product_stock(cls, old_stock: int) -> int:
        prod_stock: int = input_int_min(
            f"Product stock (leave '-1' for '{old_stock}'): ", -1
        )

        if prod_stock == -1:
            return old_stock
        return prod_stock

    @classmethod
    def input_product_index(cls, products_len: int) -> int:
        prod_idx: int = input_int_minmax("Product index: ", 1, products_len)
        return prod_idx

    @classmethod
    def input_stock_change(cls) -> int:
        amount: int = input_int_min("Amount: ", 1)
        return amount
