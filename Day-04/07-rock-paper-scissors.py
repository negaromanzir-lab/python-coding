# rock, paper, scissors game
# This is how it works:
# 1. The user is prompted to choose rock, paper, or scissors by entering 0, 1, or 2 respectively.
# 2. The computer randomly selects rock, paper, or scissors.
# 3. The user's choice and the computer's choice are displayed using ASCII art.
# 4. The winner is determined based on the rules of the game:
#    - Rock (0) beats Scissors (2)
#    - Scissors (2) beats Paper (1)
#    - Paper (1) beats Rock (0)


import random
scissors = '''
    _______
---'   ____)____
            ______)
            __)
           _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__________)
'''
paper = '''
    _______
---'   ____)____    
            ______)
            _______)
           _______) 
---.__________)
'''
game_images = [rock, paper, scissors]

test = True

while(test):
    user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choise = random.randint(0, 2)
    print(f"Computer chose: {computer_choise}")
    print(f"User choise: {user_choise}")
    print("\n")


    if user_choise == 0 and computer_choise == 2:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer chose:")
        print(game_images[computer_choise])
        print("You win!")
    elif computer_choise == 0 and user_choise == 2:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer chose:")
        print(game_images[computer_choise])
        print("You lose!")
    elif computer_choise == 1 and  user_choise == 2:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer chose:")
        print(game_images[computer_choise])
        print("You Win!")
    elif user_choise == 1 and computer_choise == 2:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer chose:")
        print(game_images[computer_choise])
        print("You Lose!")
    elif user_choise == 0 and computer_choise == 1:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer choise:")
        print(game_images[computer_choise])
        print("You Lose")
    elif computer_choise == 0 and user_choise == 1:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer choise:")
        print(game_images[computer_choise])
        print("You Win!")
    elif computer_choise == user_choise:
        print("User choise:")
        print(game_images[user_choise])
        print("Computer chose:")
        print(game_images[computer_choise])
        print("It's a draw!")
    else:
        print("You typed an invalid number, you lose!")
        test = False
