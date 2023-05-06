import random
import os
from art import logo

def clear_console():
    if os.name == "nt": # OS is Windows
        os.system("cls")
    else:
        os.system("clear")

def deal_card(number_of_cards=1):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_dealt = []
    for i in range(0, number_of_cards):
        cards_dealt.append(random.choice(cards))
        
    return cards_dealt

def calculate_score(card_list):
    """
    Takes a list of cards and returns the score calculated from the cards.
    """
    if len(card_list) == 2:
        if 11 in card_list and 10 in card_list:
            return 0
    
    if 11 in card_list and sum(card_list) > 21:
        card_list[card_list.index(11)] = 1
    
    return sum(card_list)
    
def compare_scores(user_score, computer_score):
    
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    elif user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Computer has a blackjack. You lose."
    elif user_score == 0:
        return "You have a blackjack. You win!"
    elif user_score > 21:
        "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        "You lose."

def blackjack():
    print(logo)
    
    user_cards = []
    computer_cards = []
    user_cards += deal_card(2)
    computer_cards += deal_card(2)
    is_game_over = False
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        
        # DEBUG
        print(f"\tComputer's cards: {computer_cards}, computer's score: {computer_score}")
        
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            get_another_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            print()
            
            if get_another_card == "y":
                user_cards += deal_card()                    
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards += deal_card()
        computer_score = calculate_score(computer_cards)
        
    print(f"\nYour final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

clear_console()
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear_console()
    blackjack()
    

    
