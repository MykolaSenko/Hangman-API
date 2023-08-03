from fastapi import FastAPI
from utils.game import Hangman


app = FastAPI()  # Create an instance of the FastAPI class


hangman = Hangman()  # Create an instance of the Hangman class


@app.get('/')
def get_description():
    """
    Create an get request with information about game
    """
    return {
        "description": "The Hangman game is a simple game where one player tries to guess an English word, "
                       "taking turns suggesting letters. In this implementation, the man being hanged is not drawn. "
                       "Instead, the player will see the word with the letters appearing as more and more letters are guessed correctly. "
                       "Words are chosen randomly. The game was made by Mykola Senko (Junior, BeCode)[https://github.com/MykolaSenko]. "
                       "This project is under GPL License which allows making modifications to the code and use it for commercial purposes. "
                       "Vichte, 03.08.2023"
    }


@app.post('/hangman/start')
async def start_new_game():
    """
    Creat a post request which reset the Hangman instance to start a new game

    """
    hangman.__init__()

    game_state = {
        "message": "A new Hangman game has started!",
        "correctly_guessed_letters": hangman.correctly_guessed_letters,
        "wrongly_guessed_letters": hangman.wrongly_guessed_letters,
        "lives": hangman.lives,
        "turn_count": hangman.turn_count,
        "error_count": hangman.error_count,
    }

    return game_state


@app.post('/hangman/guess/{letter}')
async def make_move(letter: str):
    """
    Create a post request which allows to input letters, checks if the letter is in the word, post information about the guessed letters and letters which were not guessed, shows information about the end of a game 
    """

    # Ensure the letter is a single lowercase alphabet
    if not letter.isalpha() or len(letter) > 1:
        return {"error": "Please enter a single letter."}

    # Play the guessed letter in the Hangman game
    hangman.play(letter.lower())

    if '_' not in hangman.correctly_guessed_letters:
        result = {
            "message": "Well done! You won!",
            "correct_word": hangman.word_to_find
        }

    elif hangman.lives <= 0:
        result = {
            "message": "Game over! You have no more lives!",
            "correct_word": hangman.word_to_find
        }

    else:
        result = {
            "correctly_guessed_letters": hangman.correctly_guessed_letters,
            "wrongly_guessed_letters": hangman.wrongly_guessed_letters,
            "lives": hangman.lives,
            "turn_count": hangman.turn_count,
            "error_count": hangman.error_count,
        }

    return result
