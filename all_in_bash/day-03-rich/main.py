"""Treasure Island Game

This script runs a simple treasure island game, where in each stage, user is 
asked about his decision. The game ends with user choosing a spcific colored door.
"""

from rich.console import Console
from rich.prompt import Prompt
from ascii_art import treasure_ascii

console = Console()

console.print(f"[bold gold1]{treasure_ascii}[/bold gold1]")
console.print(
    ":star2::star2::star2: [bold green3]Welcome to Treasure Island.[/bold green3] :star2::star2::star2:"
)
console.print(
    "[bold green3]Your mission is to find the [gold1]treasure[/gold1].[/bold green3] :moneybag::moneybag::moneybag:"
)

direction = Prompt.ask(
    "\nYou're at a cross road. Where do you want to go?", choices=["Left", "Right"]
)

if direction.lower() != "left":
    console.print("[red1]Fall into a hole.\nGame Over[/red1] :pirate_flag:")
else:
    swim = Prompt.ask(
        '\nYou came to a lake. Ther is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across',
        choices=["wait", "swim"],
    )
    if swim.lower() != "wait":
        console.print("[red1]Attacked by trout.\nGame Over[/red1] :pirate_flag:")
    else:
        door = Prompt.ask(
            "\nYou arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?",
            choices=["red", "yellow", "blue"],
        ).lower()
        if door == "yellow":
            console.print("[gold1]You win![/gold1] :moneybag:")
        elif door == "red":
            console.print("[red1]Burned By Fire\nGame Over[/red1] :pirate_flag:")
        elif door == "blue":
            console.print("[red1]Eaten By Beasts\nGame Over[/red1] :pirate_flag:")
        else:
            console.print("[red1]Game Over[/red1] :pirate_flag:")
