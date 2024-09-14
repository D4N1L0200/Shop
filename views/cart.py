from models import CartItem, Product
from ioutil import input_int_minmax
from typing import Callable
from time import sleep  # simulate payment


class CartView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def input_buy_amount(cls, stock: int) -> int:
        amount: int = input_int_minmax(f"Amount ({stock} in stock): ", 1, stock)
        return amount

    @classmethod
    def list_items(cls, items: list[CartItem], get_prod: Callable) -> None:
        if not items:
            cls.message("No items on cart.")
            return

        total: float = 0.0

        cls.message("\tCart items:")
        for idx, item in enumerate(items):
            prod: Product = get_prod(item.get_prod_id())
            cls.message(
                f"{idx + 1}. {item.get_quantity()}x {prod.get_name()} for R${prod.get_price() * item.get_quantity():.2f} (R${prod.get_price()} each)"
            )

            total += item.get_quantity() * prod.get_price()

        cls.message(f"\nTotal: R${total:.2f}")

    @classmethod
    def input_item_index(cls, items_len: int) -> int:
        item_idx: int = input_int_minmax("Item index: ", 1, items_len)
        return item_idx

    @classmethod
    def confirm_purchase(cls) -> bool:
        cls.message("The available payment method is pix.")
        return input_int_minmax("Confirm purchase? (1 = Yes, 2 = No): ", 1, 2) == 1

    @classmethod
    def get_payment(cls) -> None:
        cls.message("Please send your payment to this key: veryvalidkey@pix.com")
        sleep(5)  # simulate payment
        cls.message("Payment confirmed. Thank you for shopping with us!")

    @classmethod
    def cancel_purchase(cls) -> None:
        cls.message("Purchase canceled.")