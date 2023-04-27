import random

banner = '''
                                                                                                          ▄▄                                        
▀███▀▀▀██▄                 ▀███          ▀███▀▀▀██▄                                       ▄█▀▀▀█▄█        ██                                        
  ██   ▀██▄                  ██            ██   ▀██▄                                     ▄██    ▀█                                                  
  ██   ▄██   ▄██▀██▄ ▄██▀██  ██  ▄██▀      ██   ▄██ ▄█▀██▄ ▀████████▄  ▄▄█▀██▀███▄███    ▀███▄    ▄██▀██▀███  ▄██▀███▄██▀███ ▄██▀██▄▀███▄███ ▄██▀███
  ███████   ██▀   ▀███▀  ██  ██ ▄█         ███████ ██   ██   ██   ▀██ ▄█▀   ██ ██▀ ▀▀      ▀█████▄█▀  ██  ██  ██   ▀▀██   ▀▀██▀   ▀██ ██▀ ▀▀ ██   ▀▀
  ██  ██▄   ██     ███       ██▄██         ██       ▄█████   ██    ██ ██▀▀▀▀▀▀ ██        ▄     ▀███       ██  ▀█████▄▀█████▄██     ██ ██     ▀█████▄
  ██   ▀██▄ ██▄   ▄███▄    ▄ ██ ▀██▄       ██      ██   ██   ██   ▄██ ██▄    ▄ ██        ██     ███▄    ▄ ██  █▄   ███▄   ████▄   ▄██ ██     █▄   ██
▄████▄ ▄███▄ ▀█████▀ █████▀▄████▄ ██▄▄   ▄████▄    ▀████▀██▄ ██████▀   ▀█████▀████▄      █▀█████▀ █████▀▄████▄██████▀██████▀ ▀█████▀▄████▄   ██████▀
                                                             ██                                                                                     
                                                           ▄████▄     
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
print(banner)
print("\nAt any point, type \"exit\" to exit the programm.\n")
choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

while choice.lower() != "exit":
    
    if choice.lower() != "exit" and not choice.isnumeric():
        print("\nPlease chose a valid option!")
        choice = (input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    else:        
        if int(choice) < 0 or int(choice) > 2:
            print("\nInvalid choice!")
            choice = (input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        else:
            print(game_images[int(choice)])  

            print("\nComputer chose:")
            print(game_images[computer_choice])
        
            if int(choice) == computer_choice:
                print("It's a draw!")
            elif int(choice) == 0:
                if computer_choice == 1:
                    print("You lose.")
                elif computer_choice == 2:
                    print("You win!")
            elif int(choice) == 1:
                if computer_choice == 0:
                    print("You win!")
                elif computer_choice == 2:
                    print("You lose.")
            elif int(choice) == 2:
                if computer_choice == 0:
                    print("You lose.")
                elif computer_choice == 1:
                    print("You win!")
                    
            choice = (input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            
print("\nEnd of game!\nGoodbye!")
  