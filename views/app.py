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
    def user_menu(cls, username: str) -> int:
        print()
        print(f"\tWelcome, {username}!")
        print("1. List products")
        print("2. Add to cart (Not implemented)")
        print("3. Checkout (Not implemented)")
        print("4. Change password (Not implemented)")
        print("5. Logout")
        print("6. Exit")
        return input_int_minmax(" > ", 1, 6)

    @classmethod
    def admin_menu(cls) -> int:
        # TODO: edit to have submenus
        print()
        print("\tWelcome, admin!")
        print("1. List products")
        print("2. Add product (Not implemented)")
        print("3. Update product (Not implemented)")
        print("4. Remove product (Not implemented)")
        print("5. List orders (Not implemented)")
        print("6. Create order (Not implemented)")
        print("7. Update order (Not implemented)")
        print("8. Cancel order (Not implemented)")
        print("9. Get report (Not implemented)")
        print("10. Logout")
        print("11. Exit")
        return input_int_minmax(" > ", 1, 11)
