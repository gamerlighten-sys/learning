balance = int(input("enter starting balance: $")) 

# import random
# balance = random.randint(100, 500)
add_or_sub = ""

while(add_or_sub != "stop"):
    add_or_sub = input("Do you want to 1. deposit or 2. withrdraw (enter 1 or 2 or stop): ")
    
    if add_or_sub == "1":
        deposit_value = int(input("Enter how much you want to deposit: $"))
        balance += deposit_value
        print()
        if balance < 0:
            print(f"your current balance is -${balance * -1}\n")
        else:
            print(f"your current balance is ${balance}\n")

   
    elif add_or_sub == "2":
        withdraw_value = int(input("Enter how much you want to withdraw: $"))
        
        if balance < withdraw_value:
            print(f"there will be an over draft of -${(balance - withdraw_value) * (-1)}. Are you sure you want to continue?")
            overdraft_or_not = str(input("(enter yes/no): "))
            
            if overdraft_or_not == "yes":
                balance -= withdraw_value
                print(f"\nyour current balance is -${balance * -1}\n")
            elif overdraft_or_not == "no":
                print(f"\nyour current balance is ${balance}\n")


            else:
                print("please enter either 1 or 2 or 'stop'")

        
        elif balance >= withdraw_value:
            balance -= withdraw_value
            print(f"\nyour current balance is ${balance}\n")


    elif add_or_sub == "stop":
        if balance < 0:
            print(f"\nyour final balance is -${balance * -1}\n")
        else:
            print(f"\nyour final balance is ${balance}\n")

    elif add_or_sub != "1" or add_or_sub != "2":
        print("please enter either 1 or 2 or 'stop'")
        print()

    