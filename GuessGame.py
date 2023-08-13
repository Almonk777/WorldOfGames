import random
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number
def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input("Enter a number between 1 and {}: ".format(difficulty)))
            if guess < 1 or guess > difficulty:
                raise ValueError
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(secret_number, difficulty):
    guess = get_guess_from_user(difficulty)
    return guess == secret_number

def play(difficulty):
    print("Guess Game - Guess the Number!")
    print("A random number between 1 and {} has been chosen.".format(difficulty))

    ran_number = generate_number(difficulty)

    if compare_results(ran_number, difficulty):
        print("Congratulations! You guessed the correct number.")
        return True
    else:
        print("Sorry, your guess was incorrect. The secret number was {}.".format(ran_number))
        return False