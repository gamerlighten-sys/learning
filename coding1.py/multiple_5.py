# input number
# process; calculate remainder; num % 5, check remainider = 0
# if 0 multiple of 5 otherwise not
# print multiple of 5, not multiple of 5

print()

number = int(input("enter number: "))
remainder = number % 5

print()

if remainder == 0:
    print(number,"is a multiple of 5")
else:
    print(number,"isn't a multiple of 5")

print()