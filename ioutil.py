from getpass import getpass
from typing import Callable


def eofcatch(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EOFError:
            exit(0)

    return wrapper


@eofcatch
def input_int_minmax(prompt: str, min: int, max: int) -> int:
    while True:
        inp_str: str = input(prompt)

        trim_inp_str: str = inp_str.strip()

        if len(trim_inp_str) > 1 and trim_inp_str[0] == "-":
            trim_inp_str = trim_inp_str[1:]

        if not trim_inp_str.isnumeric():
            print("Invalid input. Please enter a number.\n")
            continue

        inp: int = int(inp_str)

        if inp < min or inp > max:
            print(
                "Invalid input. Please enter a number between "
                + str(min)
                + " and "
                + str(max)
                + ".\n"
            )
            continue

        return inp


@eofcatch
def input_int_min(prompt: str, min: int) -> int:
    while True:
        inp_str: str = input(prompt)

        trim_inp_str: str = inp_str.strip()

        if len(trim_inp_str) > 1 and trim_inp_str[0] == "-":
            trim_inp_str = trim_inp_str[1:]

        if not trim_inp_str.isnumeric():
            print("Invalid input. Please enter a number.\n")
            continue

        inp: int = int(inp_str)

        if inp < min:
            print(f"Invalid input. Please enter a number above {str(min)}.\n")
            continue

        return inp


@eofcatch
def input_int(prompt: str) -> int:
    while True:
        inp_str: str = input(prompt)

        trim_inp_str: str = inp_str.strip()

        if len(trim_inp_str) > 1 and trim_inp_str[0] == "-":
            trim_inp_str = trim_inp_str[1:]

        if not trim_inp_str.isnumeric():
            print("Invalid input. Please enter a number.\n")
            continue

        inp: int = int(inp_str)

        return inp


@eofcatch
def input_float_min(prompt: str, min: float) -> float:
    while True:
        inp_str: str = input(prompt)

        trim_inp_str: str = inp_str.strip()
        idx: int = inp_str.find(".")

        if idx != -1:
            trim_inp_str = trim_inp_str[:idx] + trim_inp_str[idx + 1 :]

        if len(trim_inp_str) > 1 and trim_inp_str[0] == "-":
            trim_inp_str = trim_inp_str[1:]

        if not trim_inp_str.isnumeric():
            print("Invalid input. Please enter a number.\n")
            continue

        inp: float = float(inp_str)

        if inp < min:
            print(f"Invalid input. Please enter a number above {str(min)}.\n")
            continue

        return inp


@eofcatch
def input_float(prompt: str) -> float:
    while True:
        inp_str: str = input(prompt)

        trim_inp_str: str = inp_str.strip()
        idx: int = inp_str.find(".")

        if idx != -1:
            trim_inp_str = trim_inp_str[:idx] + trim_inp_str[idx + 1 :]

        if len(trim_inp_str) > 1 and trim_inp_str[0] == "-":
            trim_inp_str = trim_inp_str[1:]

        if not trim_inp_str.isnumeric():
            print("Invalid input. Please enter a float.\n")
            continue

        inp: float = float(inp_str)

        return inp


@eofcatch
def input_str(prompt: str, allow_empty: bool = False) -> str:
    while True:
        inp: str = input(prompt).strip()

        if not inp and not allow_empty:
            print("Invalid input. Please enter a string.\n")
            continue

        return inp


@eofcatch
def input_username(prompt: str) -> str:
    while True:
        inp: str = input(prompt).strip()

        if not inp:
            print("Invalid input. Please enter a username.\n")
            continue

        if not inp.isalnum():
            print("Invalid input. Please use alphanumeric characters only.\n")
            continue

        if not inp[0].isalpha():
            print(
                "Invalid input. Please use an alphabetic character as the first character.\n"
            )
            continue

        if len(inp) < 4 or len(inp) > 20:
            print("Invalid input. Please use between 4 and 20 characters.\n")
            continue

        return inp


@eofcatch
def input_password(prompt: str) -> str:
    while True:
        password: str = getpass(prompt).strip()

        if not password:
            print("Invalid input. Please enter a password.\n")
            continue

        if not password.isascii():
            print("Invalid input. Please use ASCII characters only.\n")
            continue

        if " " in password:
            print("Invalid input. Please do not use spaces.\n")
            continue

        if len(password) < 4 or len(password) > 20:
            print("Invalid input. Please use between 4 and 20 characters.\n")
            continue

        return password
