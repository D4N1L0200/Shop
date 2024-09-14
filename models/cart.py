class CartItem:
    def __init__(self, prod_id: str, quantity: int) -> None:
        self.__prod_id: str = ""
        self.__quantity: int = 0

        self.set_prod_id(prod_id)
        self.set_quantity(quantity)

    def get_prod_id(self) -> str:
        return self.__prod_id

    def get_quantity(self) -> int:
        return self.__quantity

    def set_prod_id(self, prod_id: str) -> None:
        if not isinstance(prod_id, str) or len(prod_id) == 0:
            raise ValueError(f"Invalid value for id: {prod_id}")

        self.__prod_id = prod_id

    def set_quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError(f"Invalid value for quantity: {quantity}")

        self.__quantity = quantity
