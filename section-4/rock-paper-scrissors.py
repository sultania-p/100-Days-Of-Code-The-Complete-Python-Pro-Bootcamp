import random
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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    else:
        print("It's a draw!")

# print ("----Second solution---")
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# if user_choice == 0:
#     print(rock)
# elif user_choice == 1:
#     print(paper)
# elif user_choice == 2:
#     print(scissors)
# else:
#     print("Invalid input. Please try again!")
#
# computer_choice = random.randint(0, 2)

# print("Computer chose:")

# if computer_choice == 0:
#     print(rock)
#     if user_choice == 1:
#         print("You won")
#     elif user_choice == 2:
#         print("You lose")
#     else:
#         print("It's a draw")
# elif computer_choice == 1:
#     print(paper)
#     if user_choice == 0:
#         print("You lose")
#     elif user_choice == 2:
#         print("You won")
#     else:
#         print("It's a draw")
# elif computer_choice == 2:
#     print(scissors)
#     if user_choice == 0:
#         print("You won")
#     elif user_choice == 1:
#         print("You lose")
#     else:
#         print("It's a draw")











