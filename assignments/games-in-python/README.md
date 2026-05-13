# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You'll practice string manipulation, conditionals, loops, and random selection while creating an interactive game.

## 📝 Tasks

### 🛠️ Implement Word Selection and Display

#### Description
Create the game setup where a random word is selected and displayed with placeholder underscores. Players should be able to see how many letters they need to guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the word as underscores (e.g., `_ _ _ _`)
- Show the total number of attempts available

### 🛠️ Handle Letter Guesses

#### Description
Implement the core game logic that processes player guesses, updates the word display, and tracks incorrect guesses.

#### Requirements
Completed program should:

- Accept letter input from the player
- Reveal correctly guessed letters in their positions
- Track incorrect guesses and decrease attempts remaining
- Prevent duplicate guesses from being counted

### 🛠️ Determine Win and Lose Conditions

#### Description
Add game-ending logic that determines when the player wins or loses, and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (win)
- End the game when attempts reach zero (lose)
- Display the hidden word when the game ends
- Show a clear win/lose message to the player
