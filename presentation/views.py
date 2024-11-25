from presentation.utils import clear_screen


def print_line() -> None:
    print("=" * 33)


def print_options(options: dict) -> None:
    clear_screen()
    print_line()
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def print_results(results: list[tuple]) -> None:
    print("Entries:")
    for result in results:
        print(result[1])
        print(result[2])
        print()