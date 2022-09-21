"""Rock-Paper-Scissor game

This script contains simple rock-paper-scissor game which runs the game only 
once (without any loop)
"""

import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import IntPrompt
import rps_ascii as rps

console = Console()

console.rule()
console.print(
    ":star2::star2::star2: [bold green3]Welcome to Rock, Paper Scissor game.:star2::star2::star2:",
    justify="center",
)
console.rule()

# 0 for rock , 1 for paper, 2 for scissors
print("\n")
player = IntPrompt.ask(
    "[bold blue1]What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors",
    choices=["0", "1", "2"],
)
print("\n")

# choosing a computer choice randomly
computer = random.randint(0, 2)
ascii_rps = [rps.rock, rps.paper, rps.scissors]

# 1st indices for player and nested indices for computer choice.
decision = [["d", "l", "w"], ["w", "d", "l"], ["l", "w", "d"]]

# output_dict contains the game output according to the result key
output_dict = {
    "d": "[gold1]It's a draw",
    "l": "[red3]You have lost",
    "w": "[green4]You have won!",
}

result = decision[player][computer]  # game result

# styled printing
print(
    Panel(
        f"[bold orange1]{ascii_rps[player]}",
        title="[bold orange1] Player choosed",
        border_style="blue1",
    )
)

print(
    Panel(
        f"[bold red1]{ascii_rps[computer]}",
        title="[bold red1] Computer choosed",
        border_style="blue1",
    )
)

print(Panel((output_dict[result]), title="[gold1]Result", border_style="blue1"))
