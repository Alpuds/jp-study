import json
import subprocess

import utils


def show_material(lesson_path: str):
    subprocess.run(["less", lesson_path])


def add_bookmark(lesson_entry: tuple[str, str]):
    with open("./material/bookmarks.json", "r") as file:
        bookmarks = json.load(file)

    if lesson_entry[0] in bookmarks:
        print(utils.color_text("36m", f"{lesson_entry[0]} is already bookmarked."))
    else:
        bookmarks[lesson_entry[0]] = lesson_entry[1]

        with open("./material/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False, indent=4)


def remove_bookmark(lesson_entry: tuple[str, str]):
    with open("./material/bookmarks.json", "r") as file:
        bookmarks = json.load(file)

    if lesson_entry[0] in bookmarks:
        del bookmarks[lesson_entry[0]]

        with open("./material/bookmarks.json", "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False, indent=4)
    else:
        print(
            utils.color_text(
                "36m", f"Can't remove {lesson_entry[0]}, as it is not bookmarked."
            )
        )
