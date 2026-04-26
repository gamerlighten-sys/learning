print("do you want to register to vote in the coming election?")
print("yes")
print("no")
register = input("enter choice: ")

if register == "yes":
    age = int(input("enter age: "))
    print("are you an american citizen?")
    print("yes")
    print("no")
    citizenship = input("enter whether you're an american citizen or not: ")
    state = input("what state are you from: ")

elif register == "no":
    print("thank you for your time")
    exit(0)

else:
    print("please enter a valid choice or fix spelling")
    exit(0)


if age >= 18 and citizenship == "yes":
    print("Great! You have been registered and now are ready to vote")
    print("who do you want to vote for, enter a number from 1-3")
    print("1. donald duck") # donald trump
    print("2. where are the stairs?") # joe biden
    print("3. cameleon harris") # kamala harris
    vote = int(input("who do you vote for (enter a number): "))

else:
    print("you cannot vote because either you aren't")
    print("old enough or you don't have an american citizenship or both")
    exit(0)


if vote == "1" or "2" or "3":
    print("Awesome! Your vote has been registered, have a nice day!")

else:
    print("please enter a valid number from 1-3")