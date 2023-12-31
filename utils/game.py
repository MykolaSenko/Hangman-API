from wonderwords import RandomWord

class Hangman: # Create Hangman class
    def __init__(self):    # Create class instances
        r = RandomWord()
        self.word_to_find = r.word()
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.lives = 10
        self.turn_count = 0
        self.error_count = 0

    def play(self, players_letter):
        """
        Allows to input letters, checks if the letter is in the word, counts correctly guessed letters, wrongly guessed letters, lives, turns, errors.
        """
        self.turn_count += 1

        if players_letter in self.word_to_find:
            for h in range(len(self.word_to_find)):
                if players_letter == self.word_to_find[h]:
                    self.correctly_guessed_letters[h] = players_letter

            return self.correctly_guessed_letters

        else:
            self.wrongly_guessed_letters.append(players_letter)
            self.error_count += 1
            self.lives -= 1

            return self.wrongly_guessed_letters, self.error_count, self.lives
