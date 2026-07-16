import random

length = int(input("Enter the length of numbers you want to guess: "))
secret_number = random.randint(1, length)
guess = 0
num_guesses = 0

while guess != secret_number:
    guess = int(input("Enter what your guess of the number is: "))
    num_guesses += 1

    if guess > length or guess < 1:
        print("Guess Out Of Range.")
    elif guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        if num_guesses > 5:
            print("That Took A While! But")
        print("You Got It!")