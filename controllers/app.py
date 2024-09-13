from models import App, Product  # type: ignore
from views import AppView, ProductView  # type: ignore


class AppController:
    def __init__(self) -> None:
        from controllers import ProductController

        self.app: App = App()
        self.prod_contr: ProductController = ProductController()

    def main(self) -> None:
        self.app.load_data()

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
        while self.app.logged_in:
            op: int = AppView.user_menu(self.app.username)

            match op:
                case 1:
                    self.list_products()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    self.logout()
                case 6:
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

    # User & Admin methods

    def list_products(self) -> None:
        products: list[Product] = self.prod_contr.get_products()
        ProductView.list_products(products)

    def logout(self) -> None:
        message = self.app.logout()
        AppView.message(message)

    # Admin methods

    def manage_products_loop(self) -> None:
        while True:
            op: int = AppView.products_menu()

            match op:
                case 1:
                    self.list_products()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    break
                case 8:
                    break

    def manage_orders_loop(self) -> None:
        pass

    def manage_finances_loop(self) -> None:
        pass

    def manage_users_loop(self) -> None:
        pass
