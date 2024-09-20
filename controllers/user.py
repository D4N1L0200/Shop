from models import User
import json


class UsersManager: 
    users: list[User] = []

    @classmethod
    def load_dict(cls) -> dict:
        with open("data/users.json", "r") as file:
            data: dict = json.load(file)

        return data

    @classmethod
    def save_dict(cls, data: dict) -> None:
        with open("data/users.json", "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_data(cls) -> None:
        cls.users = []

        data: dict = cls.load_dict()

        for user_id, user_data in data.items():
            user: User = User(user_id, user_data["username"])

            cls.insert(user)

    @classmethod
    def idx_to_id(cls, user_idx: int) -> str:
        return cls.users[user_idx].get_id()

    @classmethod
    def id_exists(cls, user_id: str) -> bool:
        if not isinstance(user_id, str):
            raise ValueError(f"Invalid value for user id: {user_id}")

        for user in cls.users:
            if user.get_id() == user_id:
                return True

        return False

    @classmethod
    def insert(cls, user: User) -> None:
        if not isinstance(user, User):
            raise ValueError(f"Invalid value for user: {user}")

        if cls.id_exists(user.get_id()):
            raise ValueError(f"User already exists: {user}")

        cls.users.append(user)

    @classmethod
    def get_users(cls) -> list[User]:
        return cls.users

    @classmethod
    def get_users_len(cls) -> int:
        return len(cls.users)

    @classmethod
    def get_user_by_id(cls, user_id: str) -> User:
        if not isinstance(user_id, str):
            raise ValueError(f"Invalid value for user id: {user_id}")

        for user in cls.users:
            if user.get_id() == user_id:
                return user

        raise ValueError(f"user not found: {user_id}")

    @classmethod
    def delete_by_id(cls, user_id: str) -> None:
        if not isinstance(user_id, str):
            raise ValueError(f"Invalid value for user id: {user_id}")

        if not cls.id_exists(user_id):
            raise ValueError(f"User not found: {user_id}")

        data: dict = cls.load_dict()

        data.pop(user_id)

        cls.save_dict(data)

        cls.load_data()
