
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

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 '''

game_image = [rock , paper , scissors]


import random
user_choice = int(input("WELCOME! Choose 0 for rock , 1 for paper and 2 for scissors\n"))
if user_choice > 2 or user_choice < 0 :
    print("You choose invalid")
else:    
    print("You chose :" , game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose: " , game_image[computer_choice])
    if user_choice >=3 or user_choice < 0 :
        print("You Lose. Choose bw 0 ,1 and 2.")
    elif computer_choice == 2 and user_choice == 0:
        print("You WIN!")    
    elif user_choice == computer_choice:
        print("It's a Draw!") 
    elif computer_choice > user_choice:
        print("You Lose!")    
    elif user_choice == 2 and computer_choice == 0 :
        print("You lose!")    
    elif user_choice  > computer_choice :
        print("You won!")