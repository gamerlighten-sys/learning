number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

is_num1_neg = False
is_num2_neg = False

if number1 < 0:
    is_num1_neg = True
    number1 *= -1 # number1 = number1 * -1

if number2 < 0:
    is_num2_neg = True
    number2 *= -1 # number2 = number2 * -1

quotient = number1 // number2
remainder = number1 % number2


if is_num1_neg:
    number1 *= -1

if is_num2_neg:
    number2 *= -1


print()
print("the quotient of", number1, "and", number2, "is", quotient)
print("and the remainder is", remainder)
print()