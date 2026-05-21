import random

def get_choices():
    player_choice = input("Enter rock, paper, or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "paper":
            return "computer wins"
        if computer == "scissors":
            return "you win"
    elif player == "paper":
        if computer == "rock":
            return "you win"
        else:
            return ("computer wins")
    elif player == "scissors":
        if computer == "paper":
            return "you win"
        else:
            return "computer win"




choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


