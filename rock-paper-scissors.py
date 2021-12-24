import random

def play():
    user = input("What is your choice? \n 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You win!"
    
    else:
        return "You lose!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())
    