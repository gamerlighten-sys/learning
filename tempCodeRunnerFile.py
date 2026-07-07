import random, time

def gambler(random_list1, random_list2, random_list3, balance):
    for _ in range(0, int(input("For how long do you want your first uninteruppted gambling session to last? (1-30): "))):
        choice1 = random_list1[random.randint(0, 30)]
        choice2 = random_list2[random.randint(0, 30)]
        choice3 = random_list3[random.randint(0, 30)]
        
        time.sleep(1.5)
        print(choice1, end=' | ')
        time.sleep(1.5)
        print(choice2, end=' | ')
        time.sleep(1.5)
        print(choice3, end=' |\n\n')
        time.sleep(1.5)

        balance -= 30
        time.sleep(1.5)

        if choice1 == "50%":
            if choice2 == "50%":
                if choice3 == "50%":
                    print(f"YOU GOT 500%, balance + 150 tokens (and - 30 for your betting price)")
                    balance += 150
                    print(f"balance: {balance}")
                    time.sleep(3.5)

        elif choice1 == "50%" or choice2 == "50%" or choice3 == "50%":
            print("you got 50%, balance + 15 (and - 30 for your betting price)")
            balance += 15
            print(f"Balance: {balance}")
            time.sleep(2.5)
             
        elif choice3 == "Ω":
            print("You got the horshoe, balance + 30 (and - 30 for your betting price)")
            balance += 30
            print(f"Balance: {balance}") 
            time.sleep(2.5)       
        
        elif choice2 == "𓆟":
            print("You got the fish, balance + 40 (and - 30 for your betting price)")
            balance += 40
            print(f"Balance: {balance}")    
            time.sleep(2.5)    
        
        elif choice1 == "¶":
            print("You got the 9, balance + 50 (and - 30 for your betting price)")
            balance += 50
            print(f"Balance: {balance}")  
            time.sleep(2.5)      

        elif choice1 == "250%" or choice2 == "250%" or choice3 == "250%":
            print("YOU GOT 250%, balance + 75 (and - 30 for your betting price)")
            balance += 75
            print(f"Balance: {balance}")
            time.sleep(3)



        elif choice1 == "W":
            if choice2 == "I":
                if choice3 == "N":
                    print(f"YOU WON, balance + 250 tokens (and - 30 for your betting price)")
                    balance += 250
                    print(f"balance: {balance}")
                    time.sleep(3.5)

        elif choice1 == "★":
            if choice2 == "☆":
                if choice3 == "★":
                    print(f"THE STARS BLESS YOU, balance + 400 tokens (and - 30 for your betting price)")
                    balance += 400
                    print(f"balance: {balance}")
                    time.sleep(3.5)

        elif choice1 == "♠":
            if choice2 == "♣":
                if choice3 == "♥":
                    print(f"YOU ARE THE JACK OF ALL TRADES, balance + 500 tokens (and - 30 for your betting price)")
                    balance += 500
                    print(f"balance: {balance}")
                    time.sleep(4)

        elif choice1 == "6":
            if choice2 == "6":
                if choice3 == "6":
                    print(f"YOU HAVE THE DEVIL'S LUCK, balance + 666 tokens (and - 30 for your betting price)")
                    balance += 666
                    print(f"balance: {balance}")
                    time.sleep(4)

        elif choice1 == "7":
            if choice2 == "7":
                if choice3 == "7":
                    print(f"YOU HAVE HIT THE JACKPOT, balance + 1000 tokens (and - 30 for your betting price)")
                    balance += 1000
                    print(f"balance: {balance}")
                    time.sleep(4)

        elif choice1 == "𓆗":
            if choice2 == "𓆗":
                if choice3 == "𓆗":
                    print(f"YOU ENTERED THE COBRAS DEN, balance + 1500 tokens (and - 30 for your betting price)")
                    balance += 1500
                    print(f"balance: {balance}")
                    time.sleep(4)

        else:
            print(f"{balance}\n")
            time.sleep(1.5)
        
    return balance


random_list1 = ['7', '50%', '50%', 'W', 'I', 'N', '6', '250%', 'I', 'I', 'W', 'W', 'N', 'N', '50%', '50%', '¶', '¶', '¶', '𓆟', '𓆟', '𓆟', '★', '★', '☆', '♠', '♠', 'Ω', 'Ω', 'Ω', '𓆗']
random_list2 = ['7', '50%', '50%', 'W', 'I', 'N', '6', '250%', 'I', 'I', 'W', 'W', 'N', 'N', '50%', '50%', '¶', '¶', '¶', '𓆟', '𓆟', '𓆟', '★', '★', '☆', '♣', '♣', 'Ω', 'Ω', 'Ω', '𓆗']
random_list3 = ['7', '50%', '50%', 'W', 'I', 'N', '6', '250%', 'I', 'I', 'W', 'W', 'N', 'N', '50%', '50%', '¶', '¶', '¶', '𓆟', '𓆟', '𓆟', '★', '★', '☆', '♥', '♥', 'Ω', 'Ω', 'Ω', '𓆗']

key = """
𓆗 + 𓆗 + 𓆗 = 1500 tokens        7 + 7 + 7 = 1000 tokens
                            
6 + 6 + 6 = 666 tokens          ♠ + ♣ + ♥ = 500 tokens

★ + ☆ + ★ = 400 tokens         W + I + N = 250 tokens

50% + 50% + 50% = 5x tokens     250% = 2.5x tokens

¶ + _ + _ = 50 tokens           _ + 𓆟 + _ = 40 tokens 

_ + _ + Ω = 30 tokens           50% = .5x tokens
"""

balance = 1000

print("WELCOME TO THE COBRAS DEN GAMBLING 𓆗\n")
time.sleep(1.5)
print(f"Balance: $10/{balance} tokens\n")

if input("Do you want to see the key? (y/n): ") == "y":
    print(f"\nThe Key: {key}")
    time.sleep(3.5)

if input("Are you ready to start gambling (each bet ONLY costs 30 tokens)? (y/n): ") == "y":
    time.sleep(1.5)
    balance = gambler(random_list1, random_list2, random_list3, balance)
    gambler(random_list1, random_list2, random_list3, balance)
    for i in range(30):
        if input("Would you like to have another gambling session (each bet ONLY costs 30 tokens? (y/n): ") == "y":
            balance = gambler(random_list1, random_list2, random_list3, balance)
            gambler(random_list1, random_list2, random_list3, balance)
        else:
            print("See you later")
            break
else:
    print("See you later")