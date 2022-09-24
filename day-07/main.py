"""
Ceaser Cipher

This Python Script Encode or Decode A English text message according to ceasar 
cipher for a given shift number.
"""

import string
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import IntPrompt

from art import logo
from clear_screen import clear


def caeser(text: str, shift: int, direction="enocode") -> str:
    """
    Takes a English text to encode or decode, shift number and direction (i.e. encode
    or decode) and returns encoded or decoded text

    parameter
    ---------
    text: str,
    text to encode or decode
    shift: int,
    integer number of how many position you want to shift for each letter in the text
    direction: str, optional
    takes 'encode' or 'decode' as value. It none given, defaults to 'encode'
    """
    alphabet = string.ascii_lowercase
    shifted_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            idx = (alphabet.index(letter) + shift) % 26
            shifted_text += alphabet[idx]
        else:
            shifted_text += letter
    print(f"[blue1]Here is the {direction}d result: [red1]'{shifted_text}'")


console = Console()
response = "yes"

while response == "yes":
    clear()
    console.rule(":star2::star2::star2:", style="gold1")
    print(Panel.fit(f"[gold1]{logo}", border_style="gold1"))

    direction = Prompt.ask(
        "[green1]Type 'encode' to encrypt or 'decode' to decrypt",
        choices=["encode", "decode"],
    )
    text = Prompt.ask("[green1]Type your text")
    shift = IntPrompt.ask("[green1]Type the shift number for caeser cyphering")
    caeser(text, shift, direction)
    response = Prompt.ask(
        "[blue1]Do you want to encrypt/decrypt more text?", choices=["yes", "no"]
    )
    if response == "no":
        console.rule(":star2::star2::star2:", style="gold1")
