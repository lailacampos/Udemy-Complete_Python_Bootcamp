import random
import os
from hangman_art import *
from hangman_words import word_list

def clear_console():
    if os.name == "nt": # OS is Windows
        os.system("cls")
    else:
        os.system("clear")

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

#Testing code
# print(f'\nPssst, the solution is {chosen_word}.\n')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"\n{' '.join(display)}\n")
print(stages[0])

guesses = []

while not end_of_game:

    #Testing code
    print(f'\nPssst, the solution is {chosen_word}.\n')
    
    guess = input("Guess a letter: \n").lower()
    
    clear_console()

    if guess in guesses:
        print(f"\nYou have already guessed the letter \"{guess}\" before!")
    else: 
        guesses.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Then if user chose a letter that is not in the chosen word, reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"\nThe letter \"{guess}\" is not in the chosen word!")
        lives -= 1

    if lives == 0:
        end_of_game = True
        print("\nYou lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    print(stages[6 - lives])
  