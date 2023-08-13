import random
import time
import os

def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence

def get_list_from_user(difficulty):
    user_list = []
    for _ in range(difficulty):
        try:
            number = int(input("Enter a number: "))
            user_list.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return []
    return user_list

def is_list_equal(list1, list2):
    return list1 == list2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play(difficulty):
    print('''Memory Game - Remember the Numbers!
    You will be shown a sequence of numbers for a short time
    Your task is to recall the sequence correctly.''')

    sequence = generate_sequence(difficulty)
    print("Memorize the sequence...")
    print(' '.join(str(num) for num in sequence))
    time.sleep(1.5)
    clear_screen()

    print("Sequence displayed. Now it's your turn.")

    user_sequence = get_list_from_user(difficulty)
    is_valid = len(user_sequence) == difficulty

    while not is_valid:
        print(f"Invalid input length. Expected {difficulty} numbers, try again!")
        user_sequence = get_list_from_user(difficulty)
        is_valid = len(user_sequence) == difficulty

    correct_count = sum(a == b for a, b in zip(sequence, user_sequence))
    print(f"You remembered {correct_count} number(s) correctly from {difficulty}.")

    if is_list_equal(sequence, user_sequence):
        print("Congratulations! You won the Memory Game.")
        return True
    else:
        print("You lost, Game Over :(.")
        return False
