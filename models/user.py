class User:
    def __init__(self, user_id: str, username: str) -> None:
        self.__id: str = ""
        self.__username: str = ""

        self.set_id(user_id)
        self.set_username(username)

    def set_id(self, user_id: str):
        if not isinstance(user_id, str) or len(user_id) == 0:
            raise ValueError(f"Invalid value for id: {user_id}")

        self.__id = user_id

    def set_username(self, username: str):
        if not isinstance(username, str) or len(username) == 0:
            raise ValueError(f"Invalid value for username: {username}")

        self.__username = username

    def get_id(self) -> str:
        return self.__id

    def get_username(self) -> str:
        return self.__username
