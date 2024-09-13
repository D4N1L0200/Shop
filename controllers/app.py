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
                    AppView.message("List products.")
                    self.list_products()
                case 2:
                    AppView.message("Add to cart.")
                case 3:
                    AppView.message("Checkout.")
                case 4:
                    AppView.message("Change password.")
                case 5:
                    message = self.app.logout()
                    AppView.message(message)
                case 6:
                    self.app.running = False
                    break

    def admin_loop(self) -> None:
        while self.app.logged_in:
            op: int = AppView.admin_menu()

            match op:
                case 1:
                    AppView.message("List products.")
                    self.list_products()
                case 2:
                    AppView.message("Add product.")
                case 3:
                    AppView.message("Update product.")
                case 4:
                    AppView.message("Remove product.")
                case 5:
                    AppView.message("List orders.")
                case 6:
                    AppView.message("Create order.")
                case 7:
                    AppView.message("Update order.")
                case 8:
                    AppView.message("Cancel order.")
                case 9:
                    AppView.message("Get report.")
                case 10:
                    message = self.app.logout()
                    AppView.message(message)
                case 11:
                    self.app.running = False
                    break

    def list_products(self) -> None:
        products: list[Product] = self.prod_contr.get_products()

        ProductView.list_products(products)
