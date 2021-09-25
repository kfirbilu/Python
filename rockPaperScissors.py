import random


def play():
    options = ['r', 'p', 's']
    user = input("write 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    # computer=random.choice(options)
    print(f"computer chose {computer}")
    if user == computer:
        return 'Its a tie'
    if is_win(user, computer):
        return 'You won!'

    return 'You lost'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())
