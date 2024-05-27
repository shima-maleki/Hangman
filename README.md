# Hangman
## AiCore Python Project

### Project Title
Hangman -  A basic command-line game built using Python and Object Oriented Programming.

### Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [License](#license)

### Description
This project is a simple implementation of the classic Hangman game using Python. The aim of the project is to provide a fun and interactive way to practice Python programming, particularly focusing on control flow, loops, and conditionals.

**What it does:**
- Prompts the user to guess a letter in a randomly chosen secret word from a predefined list.
- Checks if the guessed letter is valid (i.e., a single alphabetical character).
- Informs the user if the guess is correct or incorrect.
- Continues to prompt the user until a valid guess is made.

**Aim of the project:**
- To build a basic command-line game in Python.
- To practice using loops and conditional statements.
- To learn how to handle user input and validate it.
- To understand basic string operations and formatting in Python.

**What you learned:**
- How to write python code in modular way.
- How to use `while` loops and `if` statements.
- How to generate random choices from a list.
- How to validate user input.
- Basic string operations and formatting in Python.
- How to write good documentation for a python based application.

### Installation
To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/shima-maleki/Hangman
    ```
2. Navigate to the project directory:
    ```sh
    cd Hangman
    ```

### Usage
To play the game, run the `milestone_5.py` script:

```sh
python milestone_5.py
```

### File Structure

```
hangman/
│
├── README.md
├── milestone_2.py    # basic python pratice
├── milestone_3.py    # basic function practice
├── milestone_4.py    # prepare hangman class
└── milestone_5.py    # final project 
```

**milestone_5.py:** The main Python script for the Hangman game. The script includes the following steps:

- A list of predefined words from which a secret word is randomly chosen.
- A while loop to continuously prompt the user to guess a letter.
- Input validation to ensure the guess is a single alphabetical character.
- Conditional checks to determine if the guessed letter is in the secret word and corresponding messages to the user.


### License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the license terms. See the LICENSE file for more details.


