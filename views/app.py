from ioutil import input_int_minmax, input_username, input_password
from os import system
import platform


def cls() -> None:
    current_os = platform.system()

    if current_os == "Windows":
        system("cls")
    else:
        system("clear")


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
    def user_menu(cls, username: str) -> int:
        print()
        print(f"\tWelcome, {username}!")
        print("1. List products")
        print("2. Add to cart")
        print("3. View cart")
        print("4. Remove from cart")
        print("5. Checkout")
        print("6. View history")
        print("7. Logout")
        print("8. Exit")
        return input_int_minmax(" > ", 1, 8)

    @classmethod
    def admin_menu(cls) -> int:
        print()
        print("\tWelcome, admin!")
        print("1. Manage products")
        print("2. Manage finances")
        print("3. Manage users")
        print("4. Logout")
        print("5. Exit")
        return input_int_minmax(" > ", 1, 5)

    @classmethod
    def products_menu(cls) -> int:
        print()
        print("1. List products")
        print("2. Add product")
        print("3. Update product")
        print("4. Remove product")
        print("5. Search product (Not implemented)")
        print("6. Add stock")
        print("7. Remove stock")
        print("8. Back")
        return input_int_minmax(" > ", 1, 8)

    @classmethod
    def finances_menu(cls) -> int:
        print()
        print("1. List sales")
        print("2. List sales by user")
        print("3. Get report")
        print("4. Cash out")
        print("5. Back")
        return input_int_minmax(" > ", 1, 5)

    @classmethod
    def users_menu(cls) -> int:
        print()
        print("1. List users")
        print("2. Remove user")
        print("3. Search user (Not implemented)")
        print("4. Back")
        return input_int_minmax(" > ", 1, 4)
