from controllers import AppController  # type: ignore


def main() -> None:
    controller: AppController = AppController()
    controller.main()


if __name__ == "__main__":
    main()
