def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
name = input("Hello! please enter your name: ")
massage = welcome(name)
# print(welcome(name))

def load_game():
    print('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    while True:
        try:
            game_number = int(input("Enter the game number: "))
            if game_number < 1 or game_number > 3:
                raise ValueError
            break
        except ValueError:
            print("Invalid game number. Please choose a number from 1 to 3.")

    game_number = int(game_number)
    while True:
        try:
            difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty_level < 1 or difficulty_level > 5:
                raise ValueError
            break
        except ValueError:
            print("Invalid difficulty level. Please choose a number from 1 to 5.")

    difficulty = int(difficulty_level)
    # print(f"Game Number: {game_number}")
    # print(f"Difficulty Level: {difficulty_level}")

    return game_number, difficulty
