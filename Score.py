
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
import Utils
import os

def add_score(difficulty):
    filename = Utils.SCORES_FILE_NAME

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            current_score = int(file.read())
    else:
        current_score = 0

    points_of_winning = (difficulty * 3) + 5
    current_score += points_of_winning

    with open(filename, 'w') as file:
        file.write(str(current_score))

    return current_score







    open(Utils.SCORES_FILE_NAME, "")
    file = open(Utils.SCORES_FILE_NAME, "a+")
    points_of_winning = int((difucllty * 3) + 5)
    accumulation = file + points_of_winning
    file

