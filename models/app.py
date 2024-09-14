import json
import uuid


class App:
    def __init__(self) -> None:
        self.running: bool = True
        self.username: str = ""
        self.user_id: str = ""
        self.password: str = ""
        self.logged_in: bool = False

    def load_data(self) -> None:
        with open("data/settings.json", "r") as file:
            data: dict = json.load(file)

        if data["logged"]:
            self.username = data["username"]
            self.password = data["password"]
            self.user_id = data["user_id"]

        self.login(self.username, self.password)

    def login(self, username: str, password: str) -> str:
        user_id = uuid.uuid5(uuid.NAMESPACE_DNS, username)

        with open("data/users.json", "r") as file:
            data: dict = json.load(file)

        if user_id.hex not in data:
            return "User not found."

        user = data[user_id.hex]

        if user["password"] != password:
            return "Invalid password."

        self.logged_in = True
        self.username = username
        self.password = password
        self.user_id = user_id.hex

        with open("data/settings.json", "w") as file:
            json.dump(
                {
                    "logged": self.logged_in,
                    "username": self.username,
                    "password": self.password,
                    "user_id": self.user_id,
                },
                file,
                indent=4,
            )

        return f"Successfully logged in as {self.username}."

    def register(self, username: str, password: str) -> str:
        user_id = uuid.uuid5(uuid.NAMESPACE_DNS, username)

        with open("data/users.json", "r") as file:
            data: dict = json.load(file)

        if user_id.hex in data:
            return "User already exists."

        data[user_id.hex] = {
            "username": username,
            "password": password,
            "user_id": user_id.hex,
            "cart": [],
        }

        with open("data/users.json", "w") as file:
            json.dump(data, file, indent=4)

        return "Successfully registered, please login."

    def logout(self) -> str:
        self.logged_in = False
        self.username = ""
        self.password = ""
        self.user_id = ""

        with open("data/settings.json", "w") as file:
            json.dump(
                {
                    "logged": self.logged_in,
                    "username": self.username,
                    "password": self.password,
                    "user_id": self.user_id,
                    "cart": [],
                },
                file,
                indent=4,
            )

        return "Successfully logged out."
