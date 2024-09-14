from models import CartItem, Product
from ioutil import input_int_minmax
from typing import Callable


class CartView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def input_buy_amount(cls, stock: int) -> int:
        amount: int = input_int_minmax(f"Amount (max {stock}): ", 1, stock)
        return amount

    @classmethod
    def list_items(cls, items: list[CartItem], get_prod: Callable) -> None:
        if not items:
            cls.message("No items on cart.")
            return

        cls.message("\tCart items:")
        for idx, item in enumerate(items):
            prod: Product = get_prod(item.get_prod_id())
            cls.message(
                f"{idx + 1}. {item.get_quantity()}x {prod.get_name()} for R${prod.get_price() * item.get_quantity():.2f} (R${prod.get_price()} each)"
            )

    @classmethod
    def input_item_index(cls, items_len: int) -> int:
        item_idx: int = input_int_minmax("Item index: ", 1, items_len)
        return item_idx
