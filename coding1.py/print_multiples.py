number = float(input("enter number: "))
multiple = int(input(f"how many multiples of {number} do you want to find: "))
print(f"{multiple} of the multiples of {number} are")

for i in range(1, multiple + 1):
    multiply = i
    # multiply += 1
    print(number * multiply)