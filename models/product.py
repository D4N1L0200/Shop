class Product:
    def __init__(
        self,
        prod_id: str,
        name: str,
        description: str,
        price: float,
        stock: int,
        pending: int,
        sold: int,
    ) -> None:
        self.__id: str = ""
        self.__name: str = ""
        self.__description: str = ""
        self.__price: float = 0
        self.__stock: int = 0
        self.__pending: int = 0
        self.__sold: int = 0

        self.set_id(prod_id)
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_stock(stock)
        self.set_pending(pending)
        self.set_sold(sold)

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_price(self) -> float:
        return round(self.__price, 2)

    def get_stock(self) -> int:
        return self.__stock

    def get_pending(self) -> int:
        return self.__pending

    def get_sold(self) -> int:
        return self.__sold

    def set_id(self, prod_id: str) -> None:
        if not isinstance(prod_id, str) or len(prod_id) == 0:
            raise ValueError(f"Invalid value for id: {prod_id}")

        self.__id = prod_id

    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError(f"Invalid value for name: {name}")

        self.__name = name

    def set_description(self, description: str) -> None:
        if not isinstance(description, str) or len(description) == 0:
            raise ValueError(f"Invalid value for description: {description}")

        self.__description = description

    def set_price(self, price: float) -> None:
        if not isinstance(price, float) or price < 0:
            raise ValueError(f"Invalid value for price: {price}")

        self.__price = price

    def set_stock(self, stock: int) -> None:
        if not isinstance(stock, int) or stock < 0:
            raise ValueError(f"Invalid value for stock: {stock}")

        self.__stock = stock

    def set_pending(self, pending: int) -> None:
        if not isinstance(pending, int) or pending < 0:
            raise ValueError(f"Invalid value for pending: {pending}")

        self.__pending = pending

    def set_sold(self, sold: int) -> None:
        if not isinstance(sold, int) or sold < 0:
            raise ValueError(f"Invalid value for sold: {sold}")

        self.__sold = sold

    def increase_stock(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__stock += amount

    def decrease_stock(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__stock -= amount

    def increase_pending(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__pending += amount

    def decrease_pending(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__pending -= amount

    def increase_sold(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__sold += amount

    def decrease_sold(self, amount: int) -> None:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"Invalid value for amount: {amount}")

        self.__sold -= amount

    def get_info(self) -> str:
        stock: str = f"{self.get_stock()}" if self.get_stock() > 1 else "not"
        return f"R${self.get_price()} - {self.get_name()}, {stock} in stock."

    def get_info_full(self) -> str:
        stock: str = f"{self.get_stock()}" if self.get_stock() > 1 else "not"
        return f"R${self.get_price()} - {self.get_name()}, {stock} in stock. {self.get_pending()} pending. {self.get_sold()} sold.\n  - {self.get_description()}"

    def __str__(self) -> str:
        stock: str = f"{self.get_stock()}" if self.get_stock() > 1 else "not"
        return f"R${self.get_price()} - {self.get_name()}, {stock} in stock. {self.get_pending()} pending. {self.get_sold()} sold.\n  - {self.get_description()}"
