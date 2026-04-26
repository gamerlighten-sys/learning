number = int(input("enter number: "))
sum = 0
avg = 0

for i in range(1, number + 1):
    sum += i
    avg = sum / number

    if i < number:
        print(i, end = ", ")
    else:
        print(i)
print(f"The Sum of these numbers is {sum}\n")
print(f"The Average of these numbers is {avg}")