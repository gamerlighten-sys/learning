numbers = int(input("enter a number: "))

print("\nbefore swap:")
for i in range(1, numbers + 1):
    if i < numbers:
        print(i, end = ", ")
    else:
        print(i, end = "")

print("\n")

print("after swap:")
for i in range(numbers, 1 - 1, -1):
    if i < 2:
        print(i, end = "")
    else:
        print(i, end = ", ")
