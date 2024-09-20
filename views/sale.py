from models import Product, Sale, User
from typing import Callable


class SaleView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def list_sales(
        cls, sales: list[Sale], get_prod: Callable, get_user: Callable
    ) -> None:
        if not sales:
            cls.message("No sales found.")
            return

        cls.message("\tSales:")
        for sale_idx, sale in enumerate(sales):
            user: User = get_user(sale.get_user_id())
            cls.message(f"\n{sale_idx + 1}. {user.get_username()}")

            for sale_prod in sale.get_products():
                prod: Product = get_prod(sale_prod.get_product_id())
                cls.message(
                    f" - {sale_prod.get_quantity()}x {prod.get_name()} for R${sale_prod.get_price()}"
                )
            cls.message(f"Total: R${sale.get_total()}")

    @classmethod
    def list_sales_by_user(
        cls, sales: list[Sale], get_prod: Callable, get_user: Callable, user_id: str
    ) -> None:
        if not sales:
            cls.message("No sales found for this user.")
            return

        user: User = get_user(user_id)

        cls.message(f"\tSales for {user.get_username()}:")
        for sale_idx, sale in enumerate(sales):
            cls.message(f"\n{sale_idx + 1}. Total: R${sale.get_total()}")

            for sale_prod in sale.get_products():
                prod: Product = get_prod(sale_prod.get_product_id())
                cls.message(
                    f" - {sale_prod.get_quantity()}x {prod.get_name()} for R${sale_prod.get_price()}"
                )

    @classmethod
    def get_report(cls, total: float, amount: int) -> None:
        if not total or not amount:
            cls.message("No sales found.")
            return

        cls.message(
            f"Earned R${total} for a total of {amount} sale{"s" if amount > 1 else ''}."
        )

    @classmethod
    def cash_out(cls, total: float, amount: int) -> None:
        if not total or not amount:
            cls.message("No sales found.")
            return

        cls.message(
            f"Cashed out R${total} for a total of {amount} sale{'s' if amount > 1 else ''}."
        )
