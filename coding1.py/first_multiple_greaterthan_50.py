# num = int(input("enter number: "))
num = int(input("enter number: "))
multiples_of_num = num

while multiples_of_num <= 50:
    if multiples_of_num <= 0:
        print("please enter a positive integer that isn't zero")
        exit(0)
    elif multiples_of_num > 50:
        break
    multiples_of_num += num

print(f"the first multiple of {num} that is greater than 50 is {multiples_of_num}")
