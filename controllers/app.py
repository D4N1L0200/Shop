from models import App, Product  # type: ignore
from views import AppView, ProductView  # type: ignore


class AppController:
    def __init__(self) -> None:
        from controllers import ProductController

        self.app: App = App()
        self.prod_contr: ProductController = ProductController()

    def main(self) -> None:
        """
        logged admin:
        list products
        add product
        update product
        remove product
        list orders
        logout
        exit

        logged user:
        list products
        add to cart
        checkout
        logout
        exit
        """

        self.app.load_data()

        AppView.message("App initialized.")

        while not self.app.logged:
            op: int = AppView.unlogged_menu()

            match op:
                case 1:
                    AppView.message("Login menu.")
                    username, password = AppView.login_menu()
                    # AppView.message(f"Username: {username} | Password: {password}")
                    message = self.app.login(username, password)
                    AppView.message(message)
                case 2:
                    AppView.message("Register menu.")
                    username, password = AppView.register_menu()
                    # AppView.message(f"Username: {username} | Password: {password}")
                    message = self.app.register(username, password)
                    AppView.message(message)
                case 3:
                    AppView.message("App finished.")
                    break
            # match op:
            #     case 1:
            #         self.add_product()
            #     case 2:
            #         self.update_product()
            #     case 3:
            #         self.remove_product()
            #     case 4:
            #         self.list_products()
            #     case 5:
            #         AppView.message("App finished.")
            #         break

    def add_product(self) -> None:
        pass

    def update_product(self) -> None:
        pass

    def remove_product(self) -> None:
        pass

    def list_products(self) -> None:
        products: list[Product] = self.prod_contr.get_products()

        ProductView.list_products(products)
