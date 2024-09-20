from models import CartItem, Product, SaleProduct, Sale
from typing import Callable
import json


class SalesManager:
    sales: list[Sale] = []

    @classmethod
    def load_data(cls) -> None:
        with open("data/sales.json", "r") as file:
            data: dict = json.load(file)

        cls.sales = []

        for user_id in data:
            for sale in data[user_id]:
                prods: list[SaleProduct] = []

                for prod in sale["products"]:
                    sale_prod: SaleProduct = SaleProduct(
                        prod["prod_id"], prod["quantity"], prod["price"]
                    )
                    prods.append(sale_prod)

                total: int = sale["total"]
                sale_obj = Sale(user_id, prods, total)
                cls.sales.append(sale_obj)

    @classmethod
    def save_data(cls) -> None:
        out: dict = {}
        for sale in cls.sales:
            user_id: str = sale.get_user_id()
            if user_id not in out:
                out[user_id] = []

            sale_obj = {
                "products": [],
                "total": sale.get_total(),
            }

            for product in sale.get_products():
                sale_obj["products"].append(
                    {
                        "prod_id": product.get_product_id(),
                        "quantity": product.get_quantity(),
                        "price": product.get_price(),
                    }
                )

            out[user_id].append(sale_obj)

        with open("data/sales.json", "w") as file:
            json.dump(out, file, indent=4)

    def get_sales(self) -> list[Sale]:
        return self.sales
    
    def get_sales_by_user(self, user_id: str) -> list[Sale]:
        return [sale for sale in self.sales if sale.get_user_id() == user_id]

    def get_total(self) -> float:
        total: float = 0.0

        for sale in self.sales:
            total += sale.get_total()

        return round(total, 2)

    def get_amount(self) -> int:
        return len(self.sales)

    def sell(self, items: list[CartItem], user_id: str, get_prod: Callable) -> None:
        total: float = 0.0
        prods: list[SaleProduct] = []

        for item in items:
            prod: Product = get_prod(item.get_product_id())
            total += prod.get_price() * item.get_quantity()
            sale_prod: SaleProduct = SaleProduct(
                prod.get_id(), item.get_quantity(), prod.get_price()
            )
            prods.append(sale_prod)

        sale: Sale = Sale(user_id, prods, round(total, 2))

        self.sales.append(sale)
        self.save_data()

    def clear(self) -> None:
        self.sales.clear()
        self.save_data()
