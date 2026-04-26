sum = 0
nums_entered = 0
print("\nin this program we keep asking you numbers. Once the sum of those numbers crosses 100 we stop\n")


while sum < 100:
    num = int(input("enter number: "))
    sum += num
    nums_entered += 1

print(f"\nnumbers entered: {nums_entered}")
    