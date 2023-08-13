import random
import requests
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyRates

def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the value in ILS: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return guess

def get_money_interval(difficulty, ran_number):
    c = CurrencyConverter()
    new_amount = c.convert(ran_number, 'USD', 'ILS')

    difficulty_calc = (new_amount - (6 - difficulty), new_amount +(6 - difficulty))

    return difficulty_calc

# def old_get_money_interval(difficulty, ran_number):
#     response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
#     data = response.json()
#     rate = data["rates"]["ILS"]
#
#     money_value = ran_number * rate
#     difficulty_calc = (money_value - (6 - difficulty), money_value +(6 - difficulty))
#
#     return difficulty_calc
def play(difficulty):
    print('''Currency Roulette Game - Guess the Value in ILS!
    You will be given a random amount in USD.
    Your task is to guess the value of that amount in ILS.''')

    ran_number = random.randint(1, 100)
    money_interval = get_money_interval(difficulty, ran_number)
    print(f"Guess the value in ILS for the amount of {ran_number} USD.")

    user_guess = float(get_guess_from_user())

    lower_bound = money_interval[0]
    upper_bound = money_interval[1]

    if lower_bound <= user_guess <= upper_bound:
        print("Congratulations! Your guess is within the correct range.")
        return True
    else:
        print("Sorry, your guess is outside the correct range.")
        return False

