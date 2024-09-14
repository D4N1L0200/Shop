from models import App, CartItem, Product  # type: ignore
from views import AppView, CartView, ProductView  # type: ignore
import uuid


class AppController:
    def __init__(self) -> None:
        from controllers import StockManager, Cart

        self.app: App = App()
        self.prod_contr: StockManager = StockManager()
        self.cart: Cart = Cart()

    def main(self) -> None:
        self.app.load_data()
        self.prod_contr.load_data()

        AppView.message("App initialized.")

        try:
            while self.app.running:
                if self.app.logged_in:
                    if self.app.username == "admin":
                        self.admin_loop()
                    else:
                        self.user_loop()
                else:
                    self.unlogged_loop()
        except KeyboardInterrupt:
            self.app.running = False

        AppView.message("App finished.")

    def unlogged_loop(self) -> None:
        while not self.app.logged_in:
            op: int = AppView.unlogged_menu()

            match op:
                case 1:
                    AppView.message("Login menu.")
                    username, password = AppView.login_menu()
                    message = self.app.login(username, password)
                    AppView.message(message)
                case 2:
                    AppView.message("Register menu.")
                    username, password = AppView.register_menu()
                    message = self.app.register(username, password)
                    AppView.message(message)
                case 3:
                    self.app.running = False
                    break

    def user_loop(self) -> None:
        if self.app.logged_in:
            self.cart.load_data(self.app.user_id)

        while self.app.logged_in:
            op: int = AppView.user_menu(self.app.username)

            match op:
                case 1:
                    self.list_products()
                case 2:
                    self.add_to_cart()
                case 3:
                    self.view_cart()
                case 4:
                    self.remove_from_cart()
                case 5:
                    self.checkout()
                case 6:
                    self.change_password()
                case 7:
                    self.logout()
                case 8:
                    self.app.running = False
                    break

    def admin_loop(self) -> None:
        while self.app.logged_in:
            op: int = AppView.admin_menu()

            match op:
                case 1:
                    self.manage_products_loop()
                case 2:
                    self.manage_orders_loop()
                case 3:
                    self.manage_finances_loop()
                case 4:
                    self.manage_users_loop()
                case 5:
                    self.logout()
                case 6:
                    self.app.running = False
                    break

    # Admin loops

    def manage_products_loop(self) -> None:
        while True:
            op: int = AppView.products_menu()

            match op:
                case 1:
                    self.list_products()
                case 2:
                    self.add_product()
                case 3:
                    self.update_product()
                case 4:
                    self.remove_product()
                case 5:
                    self.search_product()
                case 6:
                    self.increase_stock()
                case 7:
                    self.decrease_stock()
                case 8:
                    break

    def manage_orders_loop(self) -> None:
        pass

    def manage_finances_loop(self) -> None:
        pass

    def manage_users_loop(self) -> None:
        pass

    # User & Admin methods

    def list_products(self) -> None:
        products: list[Product] = self.prod_contr.get_products()
        ProductView.list_products(products)

    def logout(self) -> None:
        message = self.app.logout()
        AppView.message(message)

    ## User methods

    def add_to_cart(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.prod_contr.get_products_len()) - 1
        )
        prod_id: str = self.prod_contr.idx_to_id(prod_idx)

        if not self.prod_contr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        prod: Product = self.prod_contr.get_product_by_id(prod_id)
        amount: int = CartView.input_buy_amount(prod.get_stock())

        self.prod_contr.decrease_stock(prod_id, amount)
        item: CartItem = CartItem(prod_id, amount)
        self.cart.insert(item, self.app.user_id)
        AppView.message(f"Added {prod.get_name()} to cart.")

    def view_cart(self) -> None:
        items: list[CartItem] = self.cart.get_items()
        CartView.list_items(items, self.prod_contr.get_product_by_id)

    def remove_from_cart(self) -> None:
        item_idx: int = CartView.input_item_index(self.cart.get_items_len()) - 1
        item: CartItem = self.cart.get_item_by_idx(item_idx)
        
        self.prod_contr.increase_stock(item.get_prod_id(), item.get_quantity())

        self.cart.remove_by_idx(item_idx, self.app.user_id)

    def checkout(self) -> None:
        pass

    def change_password(self) -> None:
        pass

    ## Admin methods
    # Product manager

    def add_product(self) -> None:
        prod_name: str = ProductView.input_product_name()
        prod_description: str = ProductView.input_product_description()
        prod_price: float = ProductView.input_product_price()
        prod_stock: int = ProductView.input_product_stock()

        prod_id: uuid.UUID = uuid.uuid5(uuid.NAMESPACE_DNS, prod_name)

        product: Product = Product(
            prod_id.hex, prod_name, prod_description, prod_price, prod_stock
        )

        self.prod_contr.insert(product)

    def update_product(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.prod_contr.get_products_len()) - 1
        )
        prod_id: str = self.prod_contr.idx_to_id(prod_idx)

        old_prod: Product = self.prod_contr.get_product_by_id(prod_id)

        prod_name: str = ProductView.update_product_name(old_prod.get_name())
        prod_description: str = ProductView.update_product_description(
            old_prod.get_description()
        )
        prod_price: float = ProductView.update_product_price(old_prod.get_price())
        prod_stock: int = ProductView.update_product_stock(old_prod.get_stock())

        product: Product = Product(
            prod_id, prod_name, prod_description, prod_price, prod_stock
        )

        if not self.prod_contr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.prod_contr.update(prod_id, product)

    def remove_product(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.prod_contr.get_products_len()) - 1
        )
        prod_id: str = self.prod_contr.idx_to_id(prod_idx)

        if self.prod_contr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.prod_contr.delete_by_id(prod_id)

    def search_product(self) -> None:
        pass

    def increase_stock(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.prod_contr.get_products_len()) - 1
        )
        prod_id: str = self.prod_contr.idx_to_id(prod_idx)

        amount: int = ProductView.input_stock_change()

        if not self.prod_contr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.prod_contr.increase_stock(prod_id, amount)

    def decrease_stock(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.prod_contr.get_products_len()) - 1
        )
        prod_id: str = self.prod_contr.idx_to_id(prod_idx)

        amount: int = ProductView.input_stock_change()

        if not self.prod_contr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.prod_contr.decrease_stock(prod_id, amount)
