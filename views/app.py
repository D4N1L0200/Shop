from ioutil import input_int_minmax, input_username, input_password


class AppView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def unlogged_menu(cls) -> int:
        print()
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        return input_int_minmax(" > ", 1, 3)

    @classmethod
    def login_menu(cls) -> tuple[str, str]:
        username: str = input_username("Username: ")
        password: str = input_password("Password: ")
        return username, password

    @classmethod
    def register_menu(cls) -> tuple[str, str]:
        username: str = input_username("Username: ")
        password: str = input_password("Password: ")
        return username, password

    @classmethod
    def main_menu(cls) -> int:
        print()
        # logged admin:
        # list products
        # add product
        # update product
        # remove product
        # list orders
        # logout
        # exit

        # logged user:
        # list products
        # add to cart
        # checkout
        # logout
        # exit
        return input_int_minmax(" > ", 1, 5)
