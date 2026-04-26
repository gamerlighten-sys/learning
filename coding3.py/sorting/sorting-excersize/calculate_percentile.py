"""All the branches of XYZ school conducted an aptitude
test for all the students in the age group 14 - 16. There
were a total of n students. The marks of n students are
stored in a list. Write a program using a user defined
function that accepts a list of marks as an argument
and calculates the 'xth' percentile (where x is any number
between 0 and 100).You are required to perform the
following steps to be able to calculate the 'xth' percentile.
Note: Percentile is a measure of relative performance i.e. It is
calculated based on a candidate's performance with respect
to others. For example : If a candidate's score is in the 90th
percentile, that means she/he scored better than 90% of
people who took the test.
Steps to calculate the xth percentile:

I. Order all the values in the data set from smallest to
largest using Selection Sort. In general any of the
sorting methods can be used.

II. Calculate index by multiplying x percent
by the total number of values, n.
For example: to find 90th percentile for 120 students:
0.90*120 = 108

III. Ensure that the index is a whole number by using
math.round()

VI. Display the value at the index obtained in Step 3.
The corresponding value in the list is the xth percentile."""

import math

arr = []
length = int(input("How many student's marks are you imputting: "))

for i in range(1, length+1):
    num = float(input(f"Enter a percent for student {i}: "))
    arr.append(num)

percent = int(input("Enter percentile: "))

for i in range(len(arr)):
    smallest = arr[i]
    smallest_index = i

    for j in range(i+1, len(arr)): 
        element = arr[j]
        if element < smallest:
            smallest = element
            smallest_index = j
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

index = round((percent/100) * length)
print(f"the {percent}th percentile of all the {length} student's marks is {arr[index]}")