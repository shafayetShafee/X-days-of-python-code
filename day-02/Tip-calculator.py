"""
It calculates a certain amount of tips (10%, 12%, 15%) of total bill
"""

from rich.console import Console
from rich.prompt import IntPrompt, FloatPrompt

console = Console()
console.rule("")
console.print(
    ":star2::star2::star2: [bold green3]Welcome to the Tip Calculator[/bold green3] :blue_heart: :star2::star2::star2:",
    justify="center",
)
console.rule("")

# getting user input
total_bill = FloatPrompt.ask("What was the total bill :dollar:? $")
tip = IntPrompt.ask(
    "What percentage tip would you like to give?",
    choices=["10", "12", "15"],
    default=10,
)
people = IntPrompt.ask("How many people :boy::girl: to split the bill?")

# calculate the percentage tips
pay_per_person = (total_bill / people) * (1 + (tip / 100))
console.print(
    f"Each person should pay :dollar:: [bold red1]${pay_per_person:.2f}[/bold red1]"
)

console.rule("")
