import random, time
from fun_facts import fun_facts

words = list(fun_facts.keys())
number = str(random.randint(5000, 9900))
guessed = False

percent = ""

print("\nWelcome to Wordle!")
time.sleep(1)

for i in range(100):

    if input("\nWould you like to start a new game (y/n)? ") == "y":
        word = words[random.randint(0, len(words))]
        
        for digit in number:
            
            if len(percent) == 5:
                break
            
            if len(percent) == 2:
                percent += "."
            
            percent += digit

        for j in range(6):
            
            time.sleep(1.5)
            print("\nEnter your guess:")
            guess = input("").lower()

            if guess.isalpha() != True:
                print("Please enter a valid alphabetical guess. Restart the program")
                exit(0) # TODO: improve this logic

            if len(guess) != 5:
                print("Please enter the valid guess length of five. Restart the program")
                exit(0) # TODO: improve this logic

            for k in range(5):
                
                if guess[k] == word[k]:
                    print("🟩", end="")

                elif guess[k] in word:
                    print("🟨", end="")

                elif guess[k] not in word:
                    print("⬛", end="")

            if guess == word:
                print(f"\nYou got it in {j+1} guesses! {percent}% people got this word right.")
                guessed = True
                time.sleep(2)
                print(f"Fun fact: {fun_facts[word]}")
                break

        if guessed == False:
            print(f"\nSorry! The word was {word}! {percent}% people got this word right.")
            time.sleep(2)
            print(f"Fun fact: {fun_facts[word]}")

print("See you later!")


# add feature for fun fact abt word ❌
# add more gamemodes with different length words ❔