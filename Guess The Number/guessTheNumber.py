import random as r


def guess(x):
    random_number = r.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, too low")
        elif guess > random_number:
            print("Sorry, guess again, too high")

    print(f"Great! You have huessed the number! {random_number}")


# guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!=high:
            guess=r.randint(low,high)
        else:
            guess=low
        guess = r.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay, the computer guessed your number - {guess} - correctly")


computer_guess(10)
