class SaleProduct:
    def __init__(self, prod_id: str, quantity: int, price: float):
        self.__prod_id: str = ""
        self.__quantity: int = 0
        self.__price: float = 0.0
        
        self.set_product_id(prod_id)
        self.set_quantity(quantity)
        self.set_price(price)
    
    def set_product_id(self, prod_id: str):
        if not isinstance(prod_id, str) or len(prod_id) == 0:
            raise ValueError(f"Invalid value for id: {prod_id}")
        
        self.__prod_id = prod_id
    
    def set_quantity(self, quantity: int):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError(f"Invalid value for quantity: {quantity}")
        
        self.__quantity = quantity
    
    def set_price(self, price: float):
        if not isinstance(price, float) or price < 0:
            raise ValueError(f"Invalid value for price: {price}")
        
        self.__price = price
        
    def get_product_id(self):
        return self.__prod_id
    
    def get_quantity(self):
        return self.__quantity
    
    def get_price(self):
        return self.__price

class Sale:
    def __init__(self, user_id: str, products: list[SaleProduct], total: float):
        self.__user_id: str = ""
        self.__products: list[SaleProduct] = []
        self.__total: float = 0.0
        
        self.set_user_id(user_id)
        self.set_products(products)
        self.set_total(total)
        
    def set_user_id(self, user_id: str):
        if not isinstance(user_id, str) or len(user_id) == 0:
            raise ValueError(f"Invalid value for user_id: {user_id}")
        
        self.__user_id = user_id
    
    def set_products(self, products: list[SaleProduct]):
        if not isinstance(products, list) or len(products) == 0:
            raise ValueError(f"Invalid value for products: {products}")
        
        self.__products = products
    
    def set_total(self, total: float):
        if not isinstance(total, float) or total < 0:
            raise ValueError(f"Invalid value for total: {total}")
        
        self.__total = total
        
    def get_user_id(self):
        return self.__user_id
    
    def get_products(self):
        return self.__products
    
    def get_total(self):
        return self.__total
    
    def get_info(self):
        stock = f"{self.get_stock()}" if self.get_stock() > 1 else "not"
        return f"R${self.get_price()} - {self.get_name()}, {stock} in stock."

