import random

randomNum = random.randint(1, 20)
print(f"try to guess the number (between 1 - 20) and see if your correct\n")
guess = 0
num_of_trys = 0

while guess != randomNum:
    guess = int(input("enter guess: "))
    if guess == randomNum:
        print("You got it! Run to play again")
        break
    else:
        print("your guess was wrong, try again!")
    num_of_trys += 1

print(f"number of guesses: {num_of_trys + 1}")