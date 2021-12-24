import random
number = random.randrange(1, 10)
guess = int(input("guess a number between 1 and 10: "))
chances = 5

# guess the number from 1 to 10 5 times until correct

while guess != number and chances > 0:
    if guess > number:
        print("too high")
        guess = int(input("guess again: "))
        chances -= 1
    else: 
        print("too low")
        guess = int(input("guess again: "))
        chances -= 1

# while chances > 0:
#     if guess == number - 1:
#         print("you are close")
#     elif guess == number + 1:
#         print("you are close")

if chances == 0:
    print("game over")
    print("the number was", number)

if guess == number:
    print("you guessed it!")

