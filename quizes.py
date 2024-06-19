import json
import random

import utils


def quiz_loop(quiz_file: str):
    """
    A loop that consists of presenting questions and the user answering them.
    The loop ends when the last question is answered.
    Everytime the user selects an answer, there will be instant feedback in
    regard to what was the correct answer.

    Parameters
    quiz_file: A string of the path of a JSON file with the questions and answers.
    """
    with open(quiz_file, "r") as file:
        questions = json.load(file)

    prompt = quiz_file.split("/")[3].split("_")[0]

    print(utils.color_text("34m", questions["directions"]))
    # No longer need the key, directions, in the dictionary.
    del questions["directions"]

    for key, value in questions.items():
        # key is the question in the top level of the dictionary (e.g., queston-1).
        # value is the inner dictionary that contains the question and options.
        question_num = key.split("-")[1]
        print(utils.color_text("36m", f"{question_num}: {value['question']}"))
        # Get rid of the key, question, so the options are left in the inner-dictionary.
        del value["question"]
        print("")

        # Randomize the order of the options
        opts = list(value.values())
        random.shuffle(opts)
        correctNum = 0
        for index, option in enumerate(opts):
            print(f"{index + 1}. {option}")
            if option == value["correctOption"]:
                correctNum = index + 1

        print("")

        ans = input(f"({prompt})> ")

        if ans == "q" or ans == "Q":
            break

        if int(ans) == correctNum:
            print(utils.color_text("32m", "✓ Correct\n"))
        else:
            print(utils.color_text("31m", "✕ Incorrect"))
            print(
                f"The {utils.color_text('32m', 'correct answer')} is {utils.color_text('32m', value['correctOption'])}.\n"
            )
