import argparse
import shutil
from pathlib import Path


def get_unique_path(path: Path) -> Path:
    """
    Повертає унікальний шлях, щоб файли з однаковими
    назвами не перезаписували один одного.
    """
    if not path.exists():
        return path

    counter = 1

    while True:
        new_path = (
            path.parent
            / f"{path.stem}_{counter}{path.suffix}"
        )

        if not new_path.exists():
            return new_path

        counter += 1


def copy_file(file_path: Path, destination: Path) -> None:
    """
    Копіює файл у піддиректорію відповідно
    до його розширення.
    """
    extension = file_path.suffix.lower().lstrip(".")

    if not extension:
        extension = "no_extension"

    target_directory = destination / extension
    target_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    target_path = get_unique_path(
        target_directory / file_path.name
    )

    shutil.copy2(
        file_path,
        target_path
    )

    print(
        f"Скопійовано: {file_path} "
        f"-> {target_path}"
    )


def process_directory(
    source: Path,
    destination: Path
) -> None:
    """
    Рекурсивно перебирає всі елементи директорії.
    """
    try:
        for item in source.iterdir():

            # Якщо папка dist знаходиться всередині source,
            # не заходимо в неї повторно
            try:
                if item.resolve() == destination.resolve():
                    continue
            except OSError:
                pass

            if item.is_dir():
                process_directory(
                    item,
                    destination
                )

            elif item.is_file():
                try:
                    copy_file(
                        item,
                        destination
                    )
                except (
                    PermissionError,
                    OSError
                ) as error:
                    print(
                        f"Не вдалося скопіювати "
                        f"{item}: {error}"
                    )

    except PermissionError as error:
        print(
            f"Немає доступу до директорії "
            f"{source}: {error}"
        )

    except OSError as error:
        print(
            f"Помилка при читанні "
            f"{source}: {error}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Рекурсивне копіювання файлів "
            "із сортуванням за розширеннями."
        )
    )

    parser.add_argument(
        "source",
        type=Path,
        help="Шлях до вихідної директорії"
    )

    parser.add_argument(
        "destination",
        nargs="?",
        type=Path,
        default=Path("dist"),
        help=(
            "Шлях до директорії призначення "
            "(за замовчуванням dist)"
        )
    )

    args = parser.parse_args()

    source = args.source
    destination = args.destination

    if not source.exists():
        print(
            f"Помилка: директорія "
            f"{source} не існує."
        )
        return

    if not source.is_dir():
        print(
            f"Помилка: {source} "
            f"не є директорією."
        )
        return

    destination.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"Вихідна директорія: {source}"
    )

    print(
        f"Директорія призначення: "
        f"{destination}"
    )

    process_directory(
        source,
        destination
    )

    print("\nКопіювання завершено.")


if __name__ == "__main__":
    main()