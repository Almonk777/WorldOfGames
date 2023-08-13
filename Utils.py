import os

# SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE - A number representing a bad return code for a function.
BAD_RETURN_CODE = 400
# Screen_cleaner - A function to clear the screen (useful when playing memory game or before a new game starts).
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


