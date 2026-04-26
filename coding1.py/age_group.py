print("Do you want to find out your age group? (yes/no)")
choice = input("enter yes or no: ")

if choice == "yes":
    age = float(input("enter your age: "))

elif choice == "no":
    print("thank you for your time")
    exit(0)

if age >= 0 and age < 1:
    print("you are an infa- WAIT HOW ARE YOU TYPING LITTLE BRO")

elif age >= 1 and age < 4:
    print("you are a toddler")

elif age >= 4 and age < 6:
    print("you are a pre-schooler")

elif age >= 6 and age < 13:
    print("you are school-age")

elif age >= 13 and age < 19:
    print("you are a teenager")
    
elif age >= 19 and age < 60:
    print("you are an adult")

elif age > 60:
    print("you are a senior citizen")

else:
    print("please enter a valid number")