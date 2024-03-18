import material
import quizes
import utils

while True:
    action = input("(jp-study)> ")
    match action:
        case "material":
            utils.fzf_menu(
                "./material/material.json", "select lesson", material.show_material
            )
        case "material bookmark":
            utils.fzf_menu(
                "./material/bookmarks.json",
                "select bookmarked lesson",
                material.show_material,
            )
        case "quiz":
            utils.fzf_menu("./quizes/quizes.json", "select quiz", quizes.quiz_loop)
        case "bookmark add":
            utils.fzf_menu(
                "./material/material.json",
                "select lesson to bookmark",
                material.add_bookmark,
                tuple=True,
            )
        case "bookmark remove":
            utils.fzf_menu(
                "./material/bookmarks.json",
                "select lesson to unbookmark",
                material.remove_bookmark,
                tuple=True,
            )
        case "q" | "Q":
            break
