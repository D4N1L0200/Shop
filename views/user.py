from models import User
from ioutil import input_int_minmax


class UserView:
    @classmethod
    def message(cls, message: str) -> None:
        print(message)

    @classmethod
    def list_users(cls, users: list[User]) -> None:
        if not users:
            cls.message("No users found.")
            return

        cls.message("\tUsers:")
        for idx, user in enumerate(users):
            cls.message(f"{idx + 1}. {user.get_username()}")

    @classmethod
    def input_user_index(cls, users_len: int) -> int:
        user_idx: int = input_int_minmax("User index: ", 1, users_len)
        return user_idx
