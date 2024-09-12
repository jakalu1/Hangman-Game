# Hangman-Game
This is a Python implementation of the classic Hangman game, using the Pygame library for the graphical interface and NLTK for the word list.

1. Prerequisites
* Ensure that you have Python installed on your system. You can download it from here.
* You'll also need to install the following libraries:
  * Pygame – for the graphical interface.
  * NLTK – to use the corpus of English words.
* You can install these using pip:
  * pip install pygame
  * pip install nltk

2. Setup
* Clone the repository: First, clone this repository to your local machine:

git clone https://github.com/your-repo/hangman-game.git
cd hangman-game

* Download NLTK data: After installing the nltk package, you need to download the word corpus. Open a Python shell and run:

import nltk
nltk.download('words')

* Run the game: Once the libraries are installed and the corpus is downloaded, run the game with the following command:

python hangman.py

3. Game Instructions
* A random word will be selected for you to guess.
* You’ll have 6 attempts to guess the word.
* Each wrong guess will reveal a part of the hangman figure.
* Input letters one by one using the keyboard.
* If you guess all the letters correctly, you win. If you make 6 incorrect guesses, the game is over.

**Enjoy the game!**
