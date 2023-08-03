# HANGMAN API

# Project Description
he Hangman game is a simple game where one player tries to guess an English word, taking turns suggesting letters. In this implementation, the man being hanged is not drawn. Instead, the player will see the word with the letters appearing as more and more letters are guessed correctly. 

# Installation
To run the project instalations are not needed.

# Usage
The project is hosted at the URL: https://hangman-api-7fcp.onrender.com/. To play the game, you should navigate to: https://hangman-api-7fcp.onrender.com/docs. On the documentation page, click on the "GET" bookmark. Then push the "Try it out" button, followed by the "Execute" button. In the response body, you will see the game description.

To start the game, click on the "POST/hangman/start" bookmark. Then, push the "Try it out" button and the "Execute" button. In the response body, you will see the message "A new Hangman game has started!" and the number of letters in the word.

To continue the game, click on the "POST/hangman/guess/{letter}" bookmark, then push the "Try it out" button. Input a letter into the "letter" field and push the "Execute" button. In the response body, you will see if you guessed the letter correctly. Continue the game until the end.

If you guess the word correctly, you will see a congratulatory message. If not, you will see a message and the word you were supposed to guess.

# Author
The project was made by Junior AI & Data Scientist Mykola Senko [LinkedIn](https://www.linkedin.com/in/mykola-senko-683510a4/) | [GitHub](https://github.com/MykolaSenko)

# License
This project is under GPL License which allows to make modification to the code and use it for commercial purposes.

Vichte, August 3, 2023.