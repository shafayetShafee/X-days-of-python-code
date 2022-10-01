"""
This script simulates a simple auction program in the console
"""

from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

from art import logo
from clear_screen import clear

console = Console()

console.rule(style="gold1")
print(f"[gold1]{logo}")
console.rule(":star2::star2::star2:[gold1]Welcome to the secret auction program.:star2::star2::star2:", 
  style = "gold1")
print("\n")
response = "yes"
bid_dict = {}


while response == "yes":
  name = Prompt.ask("[green4]What's your name? ")
  bid = IntPrompt.ask("[green4]What's your bid? $")
  bid_dict[name] = bid
  response = Prompt.ask("[green4]Are there any other bidders?", choices = ["yes", "no"])
  if response == 'yes':
    clear()


bid_winner = [
  [key, value] for key, value in bid_dict.items() if value == max(bid_dict.values())
]


print("\n")
print(Panel(f"[green1]The winner is [bold]{bid_winner[0][0]} [green1]with a bid of [gold1]${bid_winner[0][1]}", border_style = "purple4"))

