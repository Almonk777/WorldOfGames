import Live
import MainScores
import Score
from GuessGame import play as playGuessGame
from MemoryGame import play as playMemoryGame
from CurrencyRouletteGame import play as playCurrencyRouletteGame
from Tests import play
def play_game():
    while True:
        game_number, difficulty = Live.load_game()
        is_winner = False

        if game_number == 1:
            is_winner = playMemoryGame(difficulty)
        elif game_number == 2:
            is_winner = playGuessGame(difficulty)
        elif game_number == 3:
            is_winner = playCurrencyRouletteGame(difficulty)

        if is_winner:
            Score.add_score(difficulty)

        print(MainScores.score_server(difficulty))

        print("\nDo you want to try our other games???")
        choice = input("Enter 'yes' to play a different game or 'no' to exit: ")
        if choice.lower() != "yes":
            break

message = Live.welcome(Live.name)
print(message)

play_game()

