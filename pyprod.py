import random

#Update scores
user_wins = 0
computer_wins = 0

#Options
options = ["rock", "paper", "scissors"]

#Logic for if input is valid or exit
while True:
    user_input = input("Type Rock/Paper/Scissor or to exit press Q.\n").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    #Logic for computers pick
    random_number = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    #Logic to evaluate wins

