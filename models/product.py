class Product:
    def __init__(
        self,
        prod_id: int,
        name: str,
        description: str,
        price: float,
        stock: int,
    ) -> None:
        self.__id: int = 0
        self.__name: str = ""
        self.__description: str = ""
        self.__price: float = 0
        self.__stock: int = 0

        self.set_id(prod_id)
        self.set_name(name)
        self.set_description(description)
        self.set_price(price)
        self.set_stock(stock)

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def set_id(self, prod_id: int) -> None:
        if not isinstance(prod_id, int) or prod_id < 0:
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

    def __str__(self) -> str:
        return f"({self.__id}) {self.__name} - {self.__description} - R${self.__price} - {self.__stock} in stock."
