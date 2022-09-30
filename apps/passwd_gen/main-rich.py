"""
This script generates a strong password containing letters, symbol and numbers.
Here the user is asked for how many letters, symbol and numbers he/she wants 
in his/her password and then builds a strong password.
"""

import random
import string
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import IntPrompt

console = Console()

console.rule()
console.print(
    ":star2::star2::star2: [bold orange1]Welcome To PyPassword Generator :star2::star2::star2:",
    justify="center",
)
console.rule()

n_letters = IntPrompt.ask("[blue1]How many letters would you like in your password?")
n_symbols = IntPrompt.ask("[blue1]How many symbols would you like?")
n_numbers = IntPrompt.ask("[blue1]How many numbers would you like?")
list_symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# randomly selects letters, symbols and numbers
letters = random.choices(string.ascii_letters, k = n_letters)
symbols = random.choices(list_symbols, k = n_symbols)
numbers = random.choices(string.digits, k = n_numbers)

# then shuffle the whole list
result_list = letters + symbols + numbers
random.shuffle(result_list)  # shuffle inplace

password = "".join(result_list)

print(
    Panel(
        f"[gold1]Here is your password: [/gold1][bold red1]{password}",
        border_style="blue1",
    )
)
