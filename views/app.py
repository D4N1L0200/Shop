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
        print()
        print("\tWelcome, admin!")
        print("1. Manage products (Partially implemented)")
        print("2. Manage orders (Not implemented)")
        print("3. Manage finances (Not implemented)")
        print("4. Manage users (Not implemented)")
        print("5. Logout")
        print("6. Exit")
        return input_int_minmax(" > ", 1, 6)

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
        print("8. Exit")
        return input_int_minmax(" > ", 1, 8)

    @classmethod
    def orders_menu(cls) -> int:
        print()
        print("1. List orders (Not implemented)")
        print("2. Create order (Not implemented)")
        print("3. Update order (Not implemented)")
        print("4. Cancel order (Not implemented)")
        print("5. Search order (Not implemented)")
        print("6. Exit")
        return input_int_minmax(" > ", 1, 6)

    @classmethod
    def finances_menu(cls) -> int:
        print()
        print("1. Get report (Not implemented)")
        print("2. Cash out (Not implemented)")
        print("3. Exit")
        return input_int_minmax(" > ", 1, 3)

    @classmethod
    def users_menu(cls) -> int:
        print()
        print("1. List users (Not implemented)")
        print("2. Add user (Not implemented)")
        print("3. Update user (Not implemented)")
        print("4. Remove user (Not implemented)")
        print("5. Search user (Not implemented)")
        print("6. Check user (Not implemented)")
        print("7. Exit")
        return input_int_minmax(" > ", 1, 7)
