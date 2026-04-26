#1. input 2 numbers
#2. subtract numbers by each other
#3. if answer is negative than num 2 is bigger, 
# else num 1 is bigger

print()
number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

if number1 > number2:
    print(number1, "is bigger than", number2)
elif number1 < number2:
    print(number2, "is bigger than", number1)
else:
    print(number1,"and", number2, "are equal")