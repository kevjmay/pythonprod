import random

#Update scores
user_wins = 0
computer_wins = 0

#Options
options = ["rock", "paper", "scissors"]

#Logic for if input is valid or exit
while True:
    user_input = input("Type Rock/Paper/Scissors or to exit press Q.\n").lower()
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
    if user_input == "scissors" and computer_pick == "paper":
        print("User win! Congrats!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("User win! Congrats!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "scissors":
        print("User win! Congrats!")
        user_wins += 1
    elif user_input == computer_pick:
        print("You have tied with the computer!")
    else:
        print("Computer win! You lost!")
        computer_wins += 1

#Comments after leaving game
print(f"You have won {user_wins} times.")
print(f"The computer has won {computer_wins} times.")
print("Thank you for playing! Goodbye!")
