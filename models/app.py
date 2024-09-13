import json


class App:
    def __init__(self) -> None:
        self.username: str = ""
        self.password: str = ""
        self.logged: bool = False

    def load_data(self) -> None:
        with open("data/settings.json", "r") as file:
            data: dict = json.load(file)

        if data["logged"]:
            self.username = data["username"]
            self.password = data["password"]

        self.login(self.username, self.password)

    def login(self, username: str, password: str) -> str:
        return "Failed to login."

    def register(self, username: str, password: str) -> str:
        
        return "Failed to register."
