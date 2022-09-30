"""
This program creates a bandname by getting user's city and petname and joining
them.
"""

from rich.console import Console
from rich.prompt import Prompt

# creating the Console instance
console = Console()

# creating a styled header
console.rule("")
console.print(
    ":star2::star2::star2: [bold blue_violet]Welcome to the Band Name Generator.[/bold blue_violet] :blue_heart: :star2::star2::star2:",
    justify="center",
)
console.rule("")

city = Prompt.ask("What's name of the city :city_sunrise: you grew up in?")
pet = Prompt.ask("What's your pet's :cat: name?")

console.print(f'Your band name could be [bold red1]"{city}-{pet}"[/bold red1]')
console.rule("")
