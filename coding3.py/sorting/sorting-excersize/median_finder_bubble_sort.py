"""Write a program using user defined functions that
accepts a List of numbers as an argument and finds its
median. (Hint : Use bubble sort to sort the accepted list.
If there are odd number of terms, the median is the
center term. If there are even number of terms, add the
two middle terms and divide by 2 get median)"""

arr = []
length = int(input("What is the length of the set of numbers: "))

for i in range(length):
    num = float(input("Enter a number: "))
    arr.append(num)

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

if length % 2 == 1:
    median = arr[length//2]
else:
    median1 = arr[length//2 - 1]
    median2 = arr[length//2]
    median = (median1 + median2)/2

print(median)