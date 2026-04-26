# input number
# process; calculate remainder; num % 2, check remainider = 0
#if 0 even otherwise odd
# print even, odd

number = int(input("enter number: "))
remainder = number % 2

if remainder == 0:
    print(number,"is even")
else:
    print(number,"is odd")


# print(number, decimal)
# print(remainder)