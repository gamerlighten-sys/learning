#1. input 4 numbers
#2. add num 1 and num 2 and add num 3 and num 4 and 
# subtract answer of both by each other
#3. print score
#4. if answer is greater than -1 than print score is positive, 
# otherwise print score is negative

print()

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
num4 = int(input("enter fourth number: "))
answer1 = num1 + num2
answer2 = num3 + num4
final = answer1 - answer2

print()
print("score is",final)

if final < 0:
    print(final, "is negative")
else:
    print(final, "is positive")
 
print()