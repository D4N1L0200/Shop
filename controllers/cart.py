from models import CartItem
import json


class Cart:
    items: list[CartItem] = []

    @classmethod
    def load_data(cls, user_id: str) -> None:
        with open("data/users.json", "r") as file:
            data: dict = json.load(file)

        cart_data: dict = data[user_id]["cart"]

        cls.items = []

        for item in cart_data:
            prod_id = item["prod_id"]
            quantity = item["quantity"]

            cls.insert(CartItem(prod_id, quantity), user_id)

    @classmethod
    def save_data(cls, user_id: str) -> None:
        with open("data/users.json", "r") as file:
            data: dict = json.load(file)

        data[user_id]["cart"] = []

        for item in cls.items:
            data[user_id]["cart"].append(
                {"prod_id": item.get_product_id(), "quantity": item.get_quantity()}
            )

        with open("data/users.json", "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def get_items(cls) -> list[CartItem]:
        return cls.items

    @classmethod
    def get_items_len(cls) -> int:
        return len(cls.items)

    @classmethod
    def get_item_by_idx(cls, item_idx: int) -> CartItem:
        if item_idx < 0 or item_idx > len(cls.items) - 1:
            raise IndexError("Index out of range")

        return cls.items[item_idx]

    @classmethod
    def insert(cls, item: CartItem, user_id: str) -> None:
        for cart_item in cls.items:
            if cart_item.get_product_id() == item.get_product_id():
                cart_item.increase_quantity(item.get_quantity())
                break
        else:
            cls.items.append(item)

        cls.save_data(user_id)

    @classmethod
    def remove_by_idx(cls, item_idx: int, user_id: str) -> None:
        if item_idx < 0 or item_idx > len(cls.items) - 1:
            raise IndexError("Index out of range")

        cls.items.pop(item_idx)

        cls.save_data(user_id)

    @classmethod
    def clear(cls, user_id: str) -> None:
        cls.items = []

        cls.save_data(user_id)
