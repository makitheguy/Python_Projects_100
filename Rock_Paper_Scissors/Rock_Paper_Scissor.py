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
game_images =[rock, paper, scissors]
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))

print("you choose: ", )
if users_choice>=3 or users_choice<0:
    print("Invalid number bhai")
else:
    print(game_images[users_choice])
    computer_choice = random.randint(0,2)
    print("computer choose: ")
    print(game_images[computer_choice])


    if users_choice==0 and computer_choice==1:
        print("you loose")
    elif users_choice==0 and computer_choice==2:
        print("you win")
    elif users_choice==computer_choice:
        print("Draw")
    elif users_choice==1 and computer_choice==0:
        print("you win")
    elif users_choice==1 and computer_choice==2:
        print("you win")
    elif users_choice==2 and computer_choice==0:
        print("you loose")
    elif users_choice==2 and computer_choice==1:
        print("you win")
