import json
import subprocess
from typing import Callable


def color_text(color: str, text: str) -> str:
    """
    Make text be a certain color using ANSI color codes.

    Parameters
    color: ANSI escape sequence that goes after '\\033[' (e.g., 36m for cyan)
    text: The text to color

    Returns
    A string object with ANSI escape sequence surrounding the parameter, text.
    """
    return f"\033[{color}{text}\033[0m"


def fzf_menu(
    entries_file: str, prompt: str, activity_loop: Callable, tuple: bool = False
):
    """
    An fzf menu with entries to choose from given ENTRIES_FILE.
    After an entry is selected, it will call the ACTIVITY_LOOP function
    while using the entry chosen as the content provider.
    Optionally, if TUPLE is True, the selected entry's key, value pair
    is passed into the ACTIVITY_LOOP function as a 2-pair tuple.

    Parameters
    entries_file: A JSON file that has the entries (e.g., quizes).
    prompt: The text prompt that fzf shows.
    activity_loop: A function refercence to run an activity (e.g., quiz).
    tuple: Pass a (key, value) pair as a 2-tuple into activity_loop function
    """
    with open(entries_file, "r") as file:
        entries = json.load(file)

    entries_string = ""

    for entry in entries:
        entries_string += f"{entry}\n"

    # Get rid of '\n' for the last entry so the fzf menu does not have a blank listing.
    entries_string = entries_string[:-1]

    while True:
        fzf_process = subprocess.Popen(
            f"fzf --prompt='({prompt})> ' --layout=reverse --height=40",
            shell=True,
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )

        fzf_output = fzf_process.communicate(input=entries_string)[0]

        # Get rid of '\n' so the string can equal one of the keys in quizes.
        fzf_output = fzf_output[:-1]

        if fzf_process.returncode == 130:
            # This happens when the user does ESC or ctrl-C
            break
        elif fzf_output in entries:
            activity_loop(
                (fzf_output, entries[fzf_output])
            ) if tuple else activity_loop((entries[fzf_output]))
        else:
            print(color_text("36m", "That does not exist."))
