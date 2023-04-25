import os
from art import logo

def clear_console():
    if os.name == "nt": # OS is Windows
        os.system("cls")
    else:
        os.system("clear")
        
bidders = {}

print(logo)
print("Welcome to the secret auction program.")

bidding_finished = False
max_bid = 0
while not bidding_finished:
  
  name = input("\nWhat is your name?: ")
  bid = float(input("\nWhat's your bid?: $"))

  bidders[name] = bid

  if bid > max_bid:
    max_bidder = name
    max_bid = bidders[name]
  
  # max_bidder = max(bidders, key=bidders.get)
  
  should_continue = input("\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()
  
  if should_continue == "no":
    bidding_finished = True
    clear_console()
    # print(bidders)
    print(f"\nThe winner is {max_bidder} with a bid of ${bidders[max_bidder]:.2f}\n")
  else:
    clear_console()