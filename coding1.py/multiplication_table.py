number = int(input("which number's multiplication table do you want to see: "))
tables = int(input(f"how many tables of {number} do you want to find: "))
print(f"{tables} of the tables for {number} are")

for i in range(1, tables + 1):
    multiply = i
    # multiply += 1
    print(number * multiply)