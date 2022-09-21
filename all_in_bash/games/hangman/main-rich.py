"""
This script runs the hangman game in command line where the user asked to guess
a letter of an English word, if he/she successes then he/she has to guess the
next letter of that word. But if he/she fails then lose a life and proceeds to
hang.
"""

import random
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

from clear_screen import clear
from hangman_words import word_list
from hangman_arts import stages, logo


# choose a word from word list randomly.
chosen_word = random.choice(word_list)
dashes = list("_" * len(chosen_word))
lives = 6

print(Panel.fit(f"[bold red1]{logo}", border_style="red1"))
print("[bold red1]Welcome to Hangman Game :pirate_flag:")
print("\n")
print("[blue1]You have total [bold]6 lives")

while dashes.count("_") > 0 and lives > 0:
    guess = Prompt.ask("[blue1]Guess a letter")
    print("\n")

    if guess in dashes:
        clear()
        print(f"[yellow]You have already guessed {guess}")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            dashes[i] = guess

    if guess not in chosen_word:
        print(
            f"[blue1]You guessed {guess}. That's not in the word. [red1]You lose a live."
        )
        lives -= 1
        print(f"[red1]You have [bold]{lives} more lives.")

    print(
        Panel.fit(
            f"[gold1]Guessed so far: [blue1]{' '.join(dashes)}", border_style="blue1"
        )
    )
    print(Panel.fit(f"[red bold]{stages[lives]}", border_style="red1"))
    print("\n")

if lives > 0:
    print(
        f"\n[green1]You have correctly guessed all letters of the word [orange1]'{chosen_word}'"
    )
    print("[gold1]You have won!")
else:
    print(
        f"\n[red1]You couldn't guess all the letters correctly of the word [orange1]'{chosen_word}'"
    )
    print("[red1]You have lost!")
