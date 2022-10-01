"""
This script simulates a simple auction program in the console
"""

from art import logo
from clear_screen import clear

print(logo)
print("Welcome to the secret auction program.")
response = "yes"
bid_dict = {}

def response_checker(response):
  """
  This function continues to prompting for user response, untill user
  correctly types response as 'yes' or 'no'.
  """
  while response not in {"yes", "no"}:
    response = input("Please type 'yes' or 'no'\n")
  return response


while response == "yes":
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  bid_dict[name] = bid
  response = input("Are there any other bidders? Type 'yes' or 'no'\n")
  response = response_checker(response)
  if response == 'yes':
    clear()


bid_winner = [
  [key, value] for key, value in bid_dict.items() if value == max(bid_dict.values())
]


print(f"The winner is {bid_winner[0][0]} with a bid of ${bid_winner[0][1]}")

