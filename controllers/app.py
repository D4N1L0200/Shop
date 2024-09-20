from models import App, CartItem, Product, Sale, User  # type: ignore
from views import AppView, CartView, ProductView, SaleView, UserView  # type: ignore
import uuid


class AppController:
    def __init__(self) -> None:
        from controllers import StocksManager, Cart, SalesManager, UsersManager

        self.app: App = App()
        self.stocks_mngr: StocksManager = StocksManager()
        self.cart: Cart = Cart()
        self.sales_mngr: SalesManager = SalesManager()
        self.users_mngr: UsersManager = UsersManager()

    def main(self) -> None:
        self.app.load_data()
        self.stocks_mngr.load_data()
        self.sales_mngr.load_data()
        self.users_mngr.load_data()

        AppView.message("App initialized. Welcome to the shop!")

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
                    self.users_mngr.load_data()
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
                    self.view_history()
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
                    self.manage_finances_loop()
                case 3:
                    self.manage_users_loop()
                case 4:
                    self.logout()
                case 5:
                    self.app.running = False
                    break

    # Admin loops

    def manage_products_loop(self) -> None:
        while True:
            op: int = AppView.products_menu()

            match op:
                case 1:
                    self.list_products_admin()
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

    def manage_finances_loop(self) -> None:
        while True:
            op: int = AppView.finances_menu()

            match op:
                case 1:
                    self.list_sales()
                case 2:
                    self.list_sales_by_user()
                case 3:
                    self.get_report()
                case 4:
                    self.cash_out()
                case 5:
                    break

    def manage_users_loop(self) -> None:
        while True:
            op: int = AppView.users_menu()

            match op:
                case 1:
                    self.list_users()
                case 2:
                    self.remove_user()
                case 3:
                    self.search_user()
                case 5:
                    break

    # User & Admin methods

    def logout(self) -> None:
        message = self.app.logout()
        AppView.message(message)

    ## User methods

    def list_products(self) -> None:
        products: list[Product] = self.stocks_mngr.get_products()
        ProductView.list_products(products)

    def add_to_cart(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.stocks_mngr.get_products_len()) - 1
        )
        prod_id: str = self.stocks_mngr.idx_to_id(prod_idx)

        if not self.stocks_mngr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        prod: Product = self.stocks_mngr.get_product_by_id(prod_id)

        if prod.get_stock() == 0:
            ProductView.out_of_stock(prod)
            return

        amount: int = CartView.input_buy_amount(prod.get_stock())

        self.stocks_mngr.add_to_cart(prod_id, amount)
        item: CartItem = CartItem(prod_id, amount)
        self.cart.insert(item, self.app.user_id)
        AppView.message(f"Added {prod.get_name()} to cart.")

    def view_cart(self) -> None:
        items: list[CartItem] = self.cart.get_items()
        CartView.list_items(items, self.stocks_mngr.get_product_by_id)

    def remove_from_cart(self) -> None:
        item_idx: int = CartView.input_item_index(self.cart.get_items_len()) - 1
        item: CartItem = self.cart.get_item_by_idx(item_idx)

        self.stocks_mngr.remove_from_cart(item.get_product_id(), item.get_quantity())

        self.cart.remove_by_idx(item_idx, self.app.user_id)

    def checkout(self) -> None:
        items: list[CartItem] = self.cart.get_items()
        if not items:
            AppView.message("Cart is empty. Nothing to checkout.")
            return

        CartView.list_items(items, self.stocks_mngr.get_product_by_id)

        if CartView.confirm_purchase():
            CartView.get_payment()
            self.stocks_mngr.checkout(items)
            self.sales_mngr.sell(
                items, self.app.user_id, self.stocks_mngr.get_product_by_id
            )
            self.cart.clear(self.app.user_id)
        else:
            CartView.cancel_purchase()

    def view_history(self) -> None:
        sales: list[Sale] = self.sales_mngr.get_sales_by_user(self.app.user_id)
        SaleView.list_sales_by_user(
            sales,
            self.stocks_mngr.get_product_by_id,
            self.users_mngr.get_user_by_id,
            self.app.user_id,
        )

    ## Admin methods
    # Product manager

    def list_products_admin(self) -> None:
        products: list[Product] = self.stocks_mngr.get_products()
        ProductView.list_products_full(products)

    def add_product(self) -> None:
        prod_name: str = ProductView.input_product_name()
        prod_description: str = ProductView.input_product_description()
        prod_price: float = ProductView.input_product_price()
        prod_stock: int = ProductView.input_product_stock()

        prod_id: uuid.UUID = uuid.uuid5(uuid.NAMESPACE_DNS, prod_name)

        product: Product = Product(
            prod_id.hex, prod_name, prod_description, prod_price, prod_stock, 0, 0
        )

        self.stocks_mngr.insert(product)

    def update_product(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.stocks_mngr.get_products_len()) - 1
        )
        prod_id: str = self.stocks_mngr.idx_to_id(prod_idx)

        old_prod: Product = self.stocks_mngr.get_product_by_id(prod_id)

        prod_name: str = ProductView.update_product_name(old_prod.get_name())
        prod_description: str = ProductView.update_product_description(
            old_prod.get_description()
        )
        prod_price: float = ProductView.update_product_price(old_prod.get_price())
        prod_stock: int = ProductView.update_product_stock(old_prod.get_stock())
        prod_pending: int = ProductView.update_product_pending(old_prod.get_pending())
        prod_sold: int = ProductView.update_product_sold(old_prod.get_sold())

        product: Product = Product(
            prod_id,
            prod_name,
            prod_description,
            prod_price,
            prod_stock,
            prod_pending,
            prod_sold,
        )

        if not self.stocks_mngr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.stocks_mngr.update(prod_id, product)

    def remove_product(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.stocks_mngr.get_products_len()) - 1
        )
        prod_id: str = self.stocks_mngr.idx_to_id(prod_idx)

        if self.stocks_mngr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.stocks_mngr.delete_by_id(prod_id)

    def search_product(self) -> None:
        pass

    def increase_stock(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.stocks_mngr.get_products_len()) - 1
        )
        prod_id: str = self.stocks_mngr.idx_to_id(prod_idx)

        amount: int = ProductView.input_stock_change()

        if not self.stocks_mngr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.stocks_mngr.increase_stock(prod_id, amount)

    def decrease_stock(self) -> None:
        prod_idx: int = (
            ProductView.input_product_index(self.stocks_mngr.get_products_len()) - 1
        )
        prod_id: str = self.stocks_mngr.idx_to_id(prod_idx)

        amount: int = ProductView.input_stock_change()

        if not self.stocks_mngr.id_exists(prod_id):
            raise ValueError(f"Product not found: {prod_id}")

        self.stocks_mngr.decrease_stock(prod_id, amount)

    # Finance manager

    def list_sales(self) -> None:
        sales: list[Sale] = self.sales_mngr.get_sales()
        SaleView.list_sales(
            sales, self.stocks_mngr.get_product_by_id, self.users_mngr.get_user_by_id
        )

    def list_sales_by_user(self) -> None:
        user_idx: int = UserView.input_user_index(self.users_mngr.get_users_len()) - 1
        user_id: str = self.users_mngr.idx_to_id(user_idx)

        if not self.users_mngr.id_exists(user_id):
            raise ValueError(f"User not found: {user_id}")

        sales: list[Sale] = self.sales_mngr.get_sales_by_user(user_id)
        SaleView.list_sales_by_user(
            sales,
            self.stocks_mngr.get_product_by_id,
            self.users_mngr.get_user_by_id,
            user_id,
        )

    def get_report(self) -> None:
        total: float = self.sales_mngr.get_total()
        amount: int = self.sales_mngr.get_amount()
        SaleView.get_report(total, amount)

    def cash_out(self) -> None:
        total: float = self.sales_mngr.get_total()
        amount: int = self.sales_mngr.get_amount()
        self.sales_mngr.clear()
        SaleView.cash_out(total, amount)

    # User manager

    def list_users(self) -> None:
        users: list[User] = self.users_mngr.get_users()
        UserView.list_users(users)

    def remove_user(self) -> None:
        user_idx: int = UserView.input_user_index(self.users_mngr.get_users_len()) - 1
        user_id: str = self.users_mngr.idx_to_id(user_idx)

        if not self.users_mngr.id_exists(user_id):
            raise ValueError(f"User not found: {user_id}")

        self.users_mngr.delete_by_id(user_id)

    def search_user(self) -> None:
        pass
