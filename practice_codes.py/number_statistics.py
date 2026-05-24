arr = []
length = int(input("How long is the array: "))
even_nums = 0
odd_nums = 0

for i in range(length):
    num = int(input("Enter a number to be added to the list: "))
    arr.append(num)

largest, smallest = arr[0], arr[0]

for i in range(1, length):
    num = arr[i]
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

average = sum(arr)/length

for i in range(length):
    num = arr[i]
    if num % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print(arr)
print(f"\nLargest: {largest}")
print(f"Smallest: {smallest}")
# print("Smallest:", smallest)
print(f"Average: {average}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}\n")

print("All numbers greater than the average:")
for i in range(length):
    num = arr[i]
    if num > average:
        print(num, end="|")