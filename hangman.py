import random

def check(guess, secret_word, guessed_letters, mistake, attempts):
    if guess in guessed_letters:
        print("You already guessed this letter!")

    elif guess in secret_word:
        guessed_letters.add(guess)
        print("Correct Guess!")

    else:
        mistake += 1
        guessed_letters.add(guess)
        print("Wrong Guess!")
        print("Mistakes:", mistake, "/", attempts)
        print("Remaining attempts:", attempts - mistake)

    return mistake


def ascii_art(mistake):
    if mistake == 0:
        print('''
        +---+
            |
            |
            |
        ===
        ''')

    elif mistake == 1:
        print('''
        +---+
        O   |
            |
            |
        ===
        ''')

    elif mistake == 2:
        print('''
        +---+
        O   |
        |   |
            |
        ===
        ''')

    elif mistake == 3:
        print('''
        +---+
        O   |
       /|   |
            |
        ===
        ''')

    elif mistake == 4:
        print('''
        +---+
        O   |
       /|\\  |
            |
        ===
        ''')

    elif mistake == 5:
        print('''
        +---+
        O   |
       /|\\  |
       /    |
        ===
        ''')

    elif mistake == 6:
        print('''
        +---+
        O   |
       /|\\  |
       / \\  |
        ===
        ''')


with open("words.txt", "r") as file:
    words = [word.strip().lower() for word in file if word.strip().isalpha()]

if not words:
    print("No words found in file!")
    exit()

secret_word = random.choice(words).strip().lower()

guessed_letters = set()
attempts = 6
mistake = 0

while mistake < attempts:

    ascii_art(mistake)

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    print()

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter only one alphabet.")
        continue


    mistake = check(guess, secret_word, guessed_letters, mistake, attempts)


    if all(letter in guessed_letters for letter in secret_word):
        print("""
        ========================
               YOU WIN!
        ========================
        Congratulations!
        """)
        print("The correct word is:", secret_word)
        break

else:
    ascii_art(mistake)

    print("""
        ========================
            GAME OVER!
        ========================
    """)

    print("The correct word is:", secret_word)
