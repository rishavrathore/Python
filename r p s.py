import random
user_input = input("Enter a choice : (rock, paper, scissor)")
possible_action = ["rock","paper","scissor"]
computer_action = random.choice(possible_action)
print("Computer chose ", computer_action)
if user_input == computer_action:
    print("both are same" )
elif user_input== "rock" and computer_action=="scissor":
    print("user wins")
elif user_input=="paper" and computer_action=="rock":
    print("user wins")
elif user_input=="scissor" and computer_action=="paper":
    print("user wins")
elif user_input=="scissor" and computer_action=="rock":
    print("computer wins")
elif user_input=="rock" and computer_action=="paper":
    print("computer wins")
elif user_input=="paper" and computer_action=="scissor":
    print("computer wins")            